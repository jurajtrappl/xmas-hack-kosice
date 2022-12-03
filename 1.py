import numpy as np
import pprint

BITS_PER_HEXA_DIGIT = 4

message = 0x42427E424242485060504844
length = len("42427E424242485060504844") * BITS_PER_HEXA_DIGIT
binary = f'{message:0>{length}b}'

# The task is named BitMap. What do we see? :)
lines = np.array_split(list(binary), len(binary) // 8)
print('\n'.join(map(lambda w: str(''.join(w)), lines)))