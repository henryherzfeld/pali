import numpy
from seeder import seed
import numpy as np
import time
import alg.bf_pali
import logging

logger = logging.getLogger(__name__)

algorithms = [
        'bf',
        # 'dp',
        # 'ex',
        # 'ma'
]

def process_run(input):

    # declaration
    time_array = np.zeros((len(algorithms),len(input)), dtype=float)
    result_array = np.zeros((len(algorithms),len(input)), dtype=object)

    for input_id, input in enumerate(input):
        for alg_id, algorithm in enumerate(algorithms):
            a = "alg." + algorithm + "_pali.pali(" + str(input) + ")"
            start = time.clock()
            result = eval(a)
            end = time.clock()

            # assignment
            time_array[alg_id][input_id] = end-start
            result_array[alg_id][input_id] = result

    return time_array, result_array


def process(n, runs, n_words, np1, np2, interval):


    metrics = np.zeros((runs,n//interval,4))

    # create the factor for each run here
    n_pali_factors = np.linspace(np1, np2, runs)

    for run, n_pali_factor in enumerate(n_pali_factors):

        p = 0

        while p < n:
            p = p + interval
            n_pali = p * n_pali_factor

            # getting input using seed method
            input = seed(p, n_pali, n_words)

            # initializing run
            print(process_run(input))
