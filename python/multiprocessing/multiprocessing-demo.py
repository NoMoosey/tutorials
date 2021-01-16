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



finish = time.perf_counter()

print(f'Finsihed in {round(finish-start, 2)} second(s)')

