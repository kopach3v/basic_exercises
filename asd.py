
def change(lst):
    lst[0], lst[-1] = lst [-1], lst[0]
    return lst
print(change([1, 2, 3]))
print(change([1, 2, 3, 4, 5]))
print(change(['н', 'л', 'о', 'с']))