import sys
import math_lib as math_lib

mathLib = math_lib.MathLib()

#   Reads standard input from user or piped file


def read_from_stdin():
    arr = []
    for line in sys.stdin:
        if line.rstrip() == '':
            break
        if '\t' in line:
            arr.extend(line.split("\t"))
        if ' ' in line:
            arr.extend((line.split(" ")))
        arr = [item if isinstance(item, float) else float(item) for item in arr]
    return arr

#   Counts mean, variance and standard deviation
#   using functions from our math library


def standard_deviation(arr) -> float:
    mean = mathLib.divide(sum(arr), len(arr))

    print("Mean =", mean)

    arr = [mathLib.subtract(item, mean) for item in arr]
    arr = [mathLib.power(item, 2) for item in arr]
    variance = mathLib.divide(sum(arr), mathLib.subtract(len(arr), 1))

    print("Variance =", variance)

    std_deviation = mathLib.root(variance, 2)

    print("Standard Deviation =", std_deviation)
    return std_deviation


if __name__ == "__main__":
    standard_deviation(read_from_stdin())
