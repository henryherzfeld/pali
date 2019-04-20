import wrapper
import logging

logging.basicConfig(filename='pali.log', level=logging.DEBUG)

n = 1000 # upper bound on n value
interval = 100 # interval to increment n
runs = 1 # of runs to perform
n_words = 10 # of words to consider for each simulation

# bounds are used to determine the size of the artificial insterted palindrome
lower_bound = .5
upper_bound = .9


wrapper.process(
        n, runs, n_words, lower_bound, upper_bound, interval
        )


# a run is a set of tests for a particular n_pali_factor value
# a simulation is a single instance for a single algorithm
