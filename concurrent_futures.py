from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ALL_COMPLETED, FIRST_COMPLETED

import time

def get_html(inteval):
    time.sleep(inteval)
    print("get page {} success".format(inteval))
    return inteval

if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=3)

    urls = [3, 2, 4]
    # method 1: 通过future获取线程结果，先执行完成先打印
    # all_tasks = [executor.submit(get_html, url) for url in urls]
    # for future in as_completed(all_tasks):
    #     data = future.result()
    #     print(data)

    # method 2: 通过executor 获取已经完成的task, map返回的顺序和urls的顺序一致
    # for data in executor.map(get_html, urls):
    #     print(data)
    
    # method 3: wait 可以阻塞主线程
    all_tasks = [executor.submit(get_html, url) for url in urls]
    wait(all_tasks, return_when=FIRST_COMPLETED)
    # for task in all_tasks:
    #     print(task.result())
    print("in main")