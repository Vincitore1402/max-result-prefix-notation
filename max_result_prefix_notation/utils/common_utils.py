import itertools


def arrays_difference(array_1, array_2):
    return list(itertools.filterfalse(lambda x: x in array_1, array_2)) + list(
        itertools.filterfalse(lambda x: x in array_2, array_1)
    )
