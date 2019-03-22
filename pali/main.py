import wrapper
import logging

logging.basicConfig(filename='pali.log', level=logging.DEBUG)

n = 3000
interval = 1000
runs = 3
n_words = 1 # of words to consider for each simulation
lower_bound = .5
upper_bound = .75


wrapper = wrapper.Wrapper(
        n, runs, n_words, lower_bound, upper_bound, interval
        )
