import requests
import pytest
from utils.DataPreparation import convert_to_json


class TetonServer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = self.login(self.username, self.password)

    def login(self, username, password, status=200, error=None):
        data = convert_to_json(username=username, password=password)
        response = requests.post("https://tetonapi.arcserve.com:8443/api/users/login",
                                 json=data, headers={"Content-Type": "application/json"})
        print(response.json())
        if status == 200:
            token = response.json()['data']['token']
            return token
        self.check_response_error(response, status, error)

    def check_response_error(self, response, status, error):
        status_code = response.status_code
        error_code = response.json()['errors'][0]['code']
        if(status != status_code):
            pytest.fail("expected code is: {}, actual code is: {}".format(
                status, status_code))
        if(error != error_code):
            pytest.fail("expected error is: {}, actual error is: {}".format(
                error, error_code))

    def create_rps(self, server_name, server_port, server_protocol, server_username, server_password, organization_id, site_id, status=201, error=None):
        data = convert_to_json(server_name=server_name, server_port=server_port, server_protocol=server_protocol, server_username=server_username,
                               server_password=server_password, organization_id=organization_id, site_id=site_id)

        response = requests.post("https://tetonapi.arcserve.com:8443/api/recoverypointservers", json=data,
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + self.token})
        if response.status_code == 201:
            return response.json()
        print(response.json())
        self.check_response_error(response, status, error)

    def create_lbs(self, server_name, server_port, server_protocol, server_username, server_password, organization_id, site_id, status=201, error=None):
        data = convert_to_json(server_name=server_name, server_port=server_port, server_protocol=server_protocol, server_username=server_username,
                               server_password=server_password, organization_id=organization_id, site_id=site_id)

        response = requests.post("https://tetonapi.arcserve.com:8443/api/linuxbackupservers", json=data,
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + self.token})
        if response.status_code == 201:
            return response.json()
        print(response.json())
        self.check_response_error(response, status, error)

    def connect_windows(self, source_name, source_type, username, password, site_id, status=200, error=None):
        data = convert_to_json(source_name=source_name, source_type=source_type, username=username, password=password, site_id=site_id)
        response = requests.post("https://tetonapi.arcserve.com:8443/api/sources/windows/connect", json=data,
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + self.token})
        if response.status_code == 200:
            return response.json()
        print(response.json())
        self.check_response_error(response, status, error)
