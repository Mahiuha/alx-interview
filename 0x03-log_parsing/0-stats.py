#!/usr/bin/python3
"""Log parsing """

if __name__ == '__main__':
    import sys
    import collections

    size, count = 0, 1

    my_dict = {"500": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "200": 0}

    def print_stadistics(size, my_dict):
        """print metrics"""
        print("File size: {}".format(size))
        od = collections.OrderedDict(sorted(my_dict.items()))
        for status, variable in od.items():
            if variable != 0:
                print("{}: {}".format(status, variable))

    try:
        """Validation computes metrics and print stadistics"""
        for line in sys.stdin:
            word = line.split()
            try:
                size += int(word[-1])
                for status in my_dict.keys():
                    if (word[-2] == status):
                        my_dict[status] += 1
                if count == 10:
                    print_stadistics(size, my_dict)
                    count = 0
            except:
                pass
            count += 1
    except KeyboardInterrupt:
        """Keyboard interrupt"""
        print_stadistics(size, my_dict)
        exit(0)
    print_stadistics(size, my_dict)
