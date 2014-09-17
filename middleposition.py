class NotANumber(Exception): pass
class NoPair(Exception): pass

from itertools import islice

from sys import argv
def get_middle_position(*args):

    if args is ():
        return

    arguments = list(map(float,args))
    if all(type(value) is float for value in arguments):

        latitudes = list()
        longitudes = list()


        for latitude in islice(arguments, 0, None, 2):
            latitudes.append(latitude)

        for longitude in islice(arguments, 1, None, 2):
            longitudes.append(longitude)

        if len(latitudes) == len(longitudes):
            return sum(latitudes) / len(latitudes), sum(longitudes) / len(latitudes)

        else:
            raise(NoPair)

    else:
        raise(NotANumber)


if __name__ == '__main__':
    print(get_middle_position(*argv[1:]))