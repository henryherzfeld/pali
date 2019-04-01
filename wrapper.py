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

def process_run(palis):
    # declaration
    time_array = np.zeros((len(algorithms), len(palis)), dtype=float)
    result_array = np.zeros((len(algorithms), len(palis)), dtype=object)

    for pali_id, pali in enumerate(palis):
        for alg_id, algorithm in enumerate(algorithms):
            a = "alg." + algorithm + "_pali.pali(" + str(pali) + ")"
            start = time.clock()
            result = eval(a)
            end = time.clock()

            # assignment
            time_array[alg_id][pali_id] = end-start
            result_array[alg_id][pali_id] = result

    return time_array, result_array


def process(n, runs, n_words, np1, np2, interval):

    metrics = np.zeros((runs, n//interval, 2))

    # create the factor for each run here
    n_pali_factors = np.linspace(np1, np2, runs)

    for run, n_pali_factor in enumerate(n_pali_factors):

        p = 0

        while p < n:
            p = p + interval
            n_pali = p * n_pali_factor

            # getting input using seed method
            palis = seed(p, n_pali, n_words)

            # initializing run
            time_array, pali_array = process_run(palis)
