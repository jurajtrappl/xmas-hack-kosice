from scipy.special import comb
import math

"""
A set with an even number of elements will have equal numbers of positive and negative terms, which cancel each other out.
Only subsets with an odd number of elements contribute to the final sum.
"""
print(round(math.log(sum(comb(2023, k, exact=True) for k in range(1, 2024, 2))), 2))