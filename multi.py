from time import sleep, time
from threading import Thread, current_thread

# def slow_func(num):
#     print(f'Slow Func Thread: {current_thread()}')
#     sleep(num)
#
# start = time()
# # slow_func()
# # slow_func()
# # slow_func()
# print(f'Main thread: {current_thread()}')
# threads = []
#
# for i in range(10):
#     # th = Thread(target=slow_func, args=[i])  # slow_func(i)
#     th = Thread(target=slow_func, kwargs={'num': i})  # slow_func(num=i)
#     # th = Thread(target=slow_func, args=[i], kwargs={'num': i})  # slow_func(i, num=i)
#     th.start()
#     threads.append(th)
#
# for thread in threads:
#     thread.join()
#
# end = time()
#
# print(end - start)

# import requests
#
# def get_url(url):
#     response = requests.get(url)
#     print(response.status_code)
#
# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://uk.wikipedia.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B0_%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F',
#     'https://uk.wikipedia.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B0_%D0%BC%D0%BE%D0%B2%D0%B0',
#     'https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0_%D0%BC%D0%BE%D0%B2%D0%B0',
# ] * 40
#
# start = time()
# # 51
# # for url in urls:
# #     get_url(url)
#
# # threads
# # 5.6
# threads = []
# for url in urls:
#     th = Thread(target=get_url, args=[url])
#     th.start()
#     threads.append(th)
#
#
# for th in threads:
#     th.join()
#
# end = time()
#
# print(end - start)

from multiprocessing import Process

def decr(num):
    while num != 0:
        num -= 1

# 3.67, 3.31, 4.02, 3.6 === 3.5
start = time()
N = 500_000_000
# 3.52, 4, 4.08, 3.6
# th1 = Process(target=decr, args=[N / 2])
# th2 = Process(target=decr, args=[N / 2])

th1 = Thread(target=decr, args=[N / 2])
th2 = Thread(target=decr, args=[N / 2])

th1.start()
th2.start()

th1.join()
th2.join()

end = time()

print(end - start)

'''
GIL - Global Interpreter Lock
IO bound - MultiThread, async (sleep, requests.get, call DB)
CPU bound - MultiProcess
'''