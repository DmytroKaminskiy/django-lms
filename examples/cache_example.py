from time import sleep, time

CACHE = {}


def foo(num, x):
    global CACHE

    key_cache = f'foo::{num}::{x}'  # {num}{x} foo(22, 2) foo(2, 22)

    print(f'Cache is: {CACHE}')

    if key_cache in CACHE:
        return CACHE[key_cache]
    else:
        sleep(num)
        result = (num ** 2) + x
        CACHE[key_cache] = result
        return result

def sub(x, y):
    global CACHE
    key = f'sub::{x}::{y}'
    print(f'Cache in sub: {CACHE}')
    if key in CACHE:
        return CACHE[key]
    else:
        result = x - y
        CACHE[key] = result
        return result

start = time()
############
print(foo(2, 1))  # -> 5
print(foo(2, 1))  # -> 5
print(foo(2, 2))  # -> 6
print(foo(2, 2))  # -> 6

print(sub(2, 2))  # -> 0
print(sub(2, 2))  # -> 0

############
end = time()
print(f'Took time: {end - start}')