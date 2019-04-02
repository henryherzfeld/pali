import numpy
from seeder import seed
import numpy as np
import time
import alg.bf_pali
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

algorithms = [
        'bf',
        # 'dp',
        # 'ex',
        # 'ma'
]

def process_algorithms(palis):
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

    # create the factors for each run
    # used as sequences to loop over
    n_factors = np.arange(interval, n+interval, interval)
    n_pali_factors = np.linspace(np1, np2, runs)

    for run, n_pali_factor in enumerate(n_pali_factors):

        plot_array = np.zeros((len(algorithms), len(n_factors)), dtype='float')

        for n_factor in n_factors:

            n_pali = int(n_factor * n_pali_factor)

            # getting input using seed method
            palis = seed(n_factor, n_pali, n_words)

            time_array, pali_array = process_algorithms(palis)

            # adding every algorithms performance to plot_array with average
            # across each word ran
            for i, alg in enumerate(algorithms):
                plot_array[i][(n_factor//interval)-1] = np.mean(time_array[i])

        for i, alg in enumerate(algorithms):
            plt.plot(n_factors, np.ravel(plot_array[i]), label=alg)

        plt.legend()
        plt.show()
