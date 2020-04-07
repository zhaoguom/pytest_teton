from server.tetonserver import TetonServer
import pytest

teton_server = TetonServer("zhaoguo.ma+0407@gmail.com", "Zetta1234")

testdata_rps = [
    ("10.57.50.74", "8014", "https", "administrator", "cnbjrdqa1@",
     "5bf8e2bf-a1ad-4d17-92ef-4bdc6cd7db9d", "dd820c17-d3bd-45c1-922a-cd4ec27ec3b9", 400, "01200001"),
    ("10.57.50.10", "804", "https", "administrator", "cnbjrdqa1@",
        "5bf8e2bf-a1ad-4d17-92ef-4bdc6cd7db9d", "dd820c17-d3bd-45c1-922a-cd4ec27ec3b9", 400, "00900008")
]


@pytest.mark.parametrize("server_name, server_port, server_protocol, server_username, server_password, organization_id, site_id, status, error", testdata_rps)
def test_create_rps(server_name, server_port, server_protocol, server_username, server_password, organization_id, site_id, status, error):
    teton_server.create_rps(server_name, server_port, server_protocol,
                            server_username, server_password, organization_id, site_id, status, error)


testdata_lbs = [
    ("10.57.50.82", "8014", "https", "root", "cnbjrdqa1@",
     "5bf8e2bf-a1ad-4d17-92ef-4bdc6cd7db9d", "dd820c17-d3bd-45c1-922a-cd4ec27ec3b9", 201, None),
]


@pytest.mark.parametrize("server_name, server_port, server_protocol, server_username, server_password, organization_id, site_id, status, error", testdata_lbs)
def test_create_lbs(server_name, server_port, server_protocol, server_username, server_password, organization_id, site_id, status, error):
    teton_server.create_lbs(server_name, server_port, server_protocol,
                            server_username, server_password, organization_id, site_id, status, error)
