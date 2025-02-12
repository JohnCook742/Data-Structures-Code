import math
import time

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

algorithm = merge_sort
algorithm_name = str(algorithm.__name__)
for i in range(13):
    start = time.time()
    size = math.floor(math.pow(2, i))
    result = algorithm([item for item in range(size)][::-1])
    end = time.time()
    run_time = end-start
    print(algorithm_name + " " + str(size) + " " + str(run_time))