'''
Multiprocessing

Source:
https://www.youtube.com/watch?v=fKl2JW_qrso&t=592s
'''

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping; slept {seconds}...'

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    # OLD WAY:
    # processes = []

    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     # args must be serializable with Pickle
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    finish = time.perf_counter()

    print(f'Finsihed in {round(finish-start, 2)} second(s)')

if __name__ == "__main__":
    main()
