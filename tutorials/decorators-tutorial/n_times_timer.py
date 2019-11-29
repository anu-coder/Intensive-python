'''
timer which runs the function n-times, and returns best, worst, average, sdev
'''
import time
from statistics import mean, stdev



def _calc_summary_stats(lst: list):
    sum_stats = {}
    sum_stats['best'] =  min(lst)
    sum_stats['worst'] = max(lst)
    sum_stats['average'] =  mean(lst)
    sum_stats['sdev'] = stdev(lst)
    sum_stats['n'] = len(lst)

    return(sum_stats)


def print_summary_stats(lst: list, roundoff=2):
    # BUG: Fix float representation for n.
    sum_stats = _calc_summary_stats(lst)
    msg = ', '.join([f'{k}: {v:.{roundoff}f}' for k, v in sum_stats.items()])
    print(msg)



def ntimes(n, roundoff=2):
    def normaldeco(func):
        def modfunc(*args, **kwargs):
            runtimes = [None]*n
            for i in range(n):
                start = time.time()
                rv = func(*args, **kwargs)
                elapsed = time.time() - start
                runtimes[i] = elapsed

            print_summary_stats(runtimes, roundoff=roundoff)

            return(rv)

        return(modfunc)

    return(normaldeco)




if __name__ == "__main__":
    import random

    @ntimes(n=10, roundoff=3)
    def slow_add(x, y):
        time.sleep(random.uniform(0.05, 0.15))
        return(x+y)

    print(slow_add(2, 2))