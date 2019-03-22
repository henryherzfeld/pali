import numpy
from seeder import seed
# import matplotlib
import time
import bf_pali, dp_pali, ex_pali, ma_pali
import logging

logger = logging.getLogger(__name__)

algorithms = [
        'bf',
        # 'dp',
        # 'ex',
        # 'ma'
]

class Run:
    input = []

    def __init__(self, input):
        self.input = input

    def start(self):

        results = []

        for i, input in enumerate(self.input):
            result = []

            for algorithm in algorithms:
                a = algorithm + "_pali.pali(" + str(input) + ")"
                result.append(eval(a))
            results.append(result)

        return results

class Wrapper:
    n = 0
    runs = 0
    rands = []

    def __init__(self, n, q, n_words, np1, np2, interval):
        self.n = n
        self.runs = q

        run_interval = (np2 - np1)/q
        tot_time = 0
        metrics = {}

        for run_id in range(q):
            p = 0
            n_pali_factor = round(np1 + (run_interval * run_id), 3)

            while p < n:
                p = p + interval
                n_pali = p * n_pali_factor

                input = seed(p, n_pali, n_words)
                run = Run(input)

                start = time.clock()
                metrics[run_id + p] = run.start()
                end = time.clock()
                elapsed = end - start
                print(round(elapsed, 4))

        print(metrics)

# x[1][2] = (a1(word1, word2, word3), a2(word1, word2, word3),...)
# 1 = run_id, 2 = p
#TODO: stop collecting solutions, log them
# build final metric array with following props:
    # 2 dimensions
    # 1st: run
    # 2nd: n
    # 3rd: alg
