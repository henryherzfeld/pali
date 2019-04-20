from seeder import seed
import numpy as np
import time
import alg.bf_pali, alg.ex_pali, alg.dp_pali, alg.ma_pali
import logging
import matplotlib.pyplot as plt
import math

logger = logging.getLogger(__name__)

algorithms = {
        'bf': 3,
        'dp': 2,
        'ex': 2,
        'ma': 1
}

SCALE = 1000000000

def calculate_constant(n, exp, time):
    return (time / (n**exp))

def outfile(a, b, c, d, file):
    file.write("{0},{1},{2},{3}\n".format(a,b,c,d))

def process_algorithms(palis):
    # creating two arrays with same dimensionality
    # time contains list of times, result stores list of solution for each word
    time_array = np.zeros((len(algorithms), len(palis)), dtype=float)
    result_array = np.zeros((len(algorithms), len(palis)), dtype=object)

    for pali_id, pali in enumerate(palis):
        for alg_id, algorithm in enumerate(algorithms.keys()):
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

        # initialize subplot data object for each run
        subplot_array = np.zeros((len(algorithms), len(n_factors)), dtype='float')

        # building subplot matrix for superplot render at end of runtime
        a = math.ceil(np.sqrt(runs))
        plt.subplot(a, a, 1+run, label="run "+ str(run))

        for n_factor in n_factors:

            # finding size of artificial palindrome using n_pali_factor and current n
            n_pali = int(n_factor * n_pali_factor)

            # seed method creates n_words of size n_factor with artificial pali
            # of size n_pali
            palis = seed(n_factor, n_pali, n_words)

            # processing input for all algorithms
            time_array, pali_array = process_algorithms(palis)

            # adding every algorithms performance to subplot_array with average
            # across each word ran
            for i, alg in enumerate(algorithms.keys()):
                subplot_array[i][(n_factor//interval)-1] = np.mean(time_array[i])

        # plot a line on current subplot for each algorithm
        for i, alg in enumerate(algorithms.keys()):
            plt.plot(n_factors, np.ravel(subplot_array[i]), label=alg)

        # formatting subplot
        plt.legend()
        plt.title("n_pali: {0}".format(n_pali))

    # formatting and rendering superplot
    plt.suptitle("n: {0}, interval: {1}, n_words: {2}".format(n, interval, n_words))
    plt.show()

    # to get constant array we are going to map a constant calculator using np or array
    # methods where we run constant function on every element in those two arrays and put into
    # third
    vfunc1 = np.vectorize(calculate_constant)
    vfunc2 = np.vectorize(outfile)

    for alg_id, alg_exp in enumerate(algorithms.values()):
        constant_array = vfunc1(n_factors, alg_exp, subplot_array[alg_id])
        print(max(constant_array))


        l = np.arange(0, n, 1)
        curve = l.__pow__(alg_exp)

        plt.plot(n_factors, SCALE*subplot_array[alg_id], label=alg + " empirical")
        plt.plot(curve, label=alg + " theoretical")
        plt.title("scale = {0}".format(SCALE))
        plt.legend()
        plt.show()


        file = open("alg{0}.csv".format(alg_id), "w")
        vfunc2(n_factors, subplot_array[alg_id], n_factors**alg_exp, constant_array, file)
        #
        # for i in enumerate(n_factors):
        #     print("{0},{1},{2},{3}".format(n_factors[i], subplot_array[alg_id], (n_factors[i]**alg_exp), constant_array[i]))
