N = 100
trees = [False] * (N + 1)

def switch(tree):
    return True if not tree else False

for i in range(1, N + 1):
    """
    The elves come in randomly and each of them switches the lights on exactly the trees that are multiples of the elf's number.
    """
    for j in range(i, N + 1, i):
        trees[j] = switch(trees[j])

print(sum(trees))