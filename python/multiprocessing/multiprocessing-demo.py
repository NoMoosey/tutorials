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
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something,secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finsihed in {round(finish-start, 2)} second(s)')

if __name__ == "__main__":
    main()
