import wrapper
import logging

logging.basicConfig(filename='pali.log', level=logging.DEBUG)

n = 100 # upper bound on n value
interval = 10 # interval to increment n
runs = 9 # of runs to perform
n_words = 20 # of words to consider for each simulation

# N_PALI_FACTOR is used to determine the size of the artificial insterted palindrome
lower_bound = .1
upper_bound = .9


wrapper.process(
        n, runs, n_words, lower_bound, upper_bound, interval
        )


# a run is a set of tests for a particular n_pali_factor value
# a simulation is a single instance for a single algorithm
