import numpy as np

# test data created with the following commands:
#
# >>> import numpy as np
# >>> np.savetxt('test.txt', np.vstack([np.random.uniform(size=(100)), np.random.uniform(size=100)]).T, delimiter='\t')

print(np.loadtxt('test.txt').mean(1))
