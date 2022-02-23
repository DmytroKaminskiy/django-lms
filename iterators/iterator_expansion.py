lst = [1, 2, 3, 4]

#
for item in lst:
    print(item)

#
list_iter = iter(lst)
while True:
    try:
        item = next(list_iter)
        print(item)
    except StopIteration:
        break
