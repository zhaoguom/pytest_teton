import asyncio
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ALL_COMPLETED
import socket
from urllib.parse import urlparse
import time


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path

    if path == "":
        path = "/"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    client.send(
        "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    # print(html_data)
    client.close()
    return html_data


if __name__ == "__main__":
    start_time = time.time()
    
    for url in range(1, 50):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        print(get_url(url))
        
    print("elapsed time %s " % (time.time()-start_time))
