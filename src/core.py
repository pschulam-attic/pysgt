from collections import defaultdict

try:
    import numpy as np
except ImportError:
    raise Exception("Cannot find numpy module, exiting...")

try:
    from sgt_smoother import gt_smooth as _gt_smooth
except ImportError:
    raise Exception("Cannot find sgt_smoother module, exiting...")

def make_smoothed_distribution(counts, vocab=None):
    ffs = sorted(_freq_of_freq(counts).items(), key=lambda x: x[0])
    r = np.array([x[0] for x in ffs], dtype=np.int)
    n_r = np.array([x[1] for x in ffs], dtype=np.double)
    _gt_smooth(r, n_r)
    
    freq_to_prob = dict( zip(r, n_r) )
    new_distribution = {}
    if not vocab:
        for k, v in counts.items():
            new_distribution[k] = freq_to_prob[v]
    else:
        pass
    return new_distribution

def _freq_of_freq(counts):
    freqs_of_freqs = defaultdict(int)
    for v in counts.values():
        freqs_of_freqs[v] += 1
    return freqs_of_freqs

def run_test(test_file):
    lines = (l.strip().split() for l in open(test_file))
    counts = dict( (x[1], int(x[0])) for x in lines)
    d = make_smoothed_distribution(counts)
    for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print "{0:<30}{1:.5e}".format(k, v)

if __name__ == "__main__":
    run_test("data/wordcounts.txt")