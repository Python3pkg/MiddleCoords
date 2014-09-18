from itertools import islice
from sys import argv

class NoPair(Exception):
    pass



def get_middle_position(*args):
    """
    >> get_middle_position(5,5,7,7) -> (6,6)
    >> get_middle_position(2.5, 2.5, 7.5, 7.5) -> (5.5)

    :param args: any number of coordinates, must be paired as latitude+longitude
    :return: tuple of coordinate between all of given coordinates, None if given no args
    """

    if args is ():
        return

    arguments = list(map(float, args))

    latitudes = list()
    longitudes = list()

    for latitude in islice(arguments, 0, None, 2):
        latitudes.append(latitude)

    for longitude in islice(arguments, 1, None, 2):
        longitudes.append(longitude)

    if len(latitudes) == len(longitudes):
        return sum(latitudes) / len(latitudes), sum(longitudes) / len(longitudes)

    else:
        raise NoPair

if __name__ == '__main__': # pragma: no cover
    print(get_middle_position(*argv[1:]))