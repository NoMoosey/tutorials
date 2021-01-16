'''
Multiprocessing

Source:
https://www.youtube.com/watch?v=fKl2JW_qrso&t=592s
'''

import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping...')

def main():
    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finsihed in {round(finish-start, 2)} second(s)')

if __name__ == "__main__":
    main()