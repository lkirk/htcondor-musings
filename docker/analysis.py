import argparse

import numpy as np

# test data created with the following commands:
#
# >>> import numpy as np
# >>> np.savetxt('test.txt', np.vstack([np.random.uniform(size=(100)), np.random.uniform(size=100)]).T, delimiter='\t')


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--input', required=True)
arg_parser.add_argument('--output', required=True)
args = arg_parser.parse_args()

with open(args.output, 'w') as out_fh:
    print(np.loadtxt(args.input).mean(1), file=out_fh)
    print('oh hi folks', file=out_fh)
