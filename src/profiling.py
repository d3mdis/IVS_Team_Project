import sys
import math_lib as math_lib

## @file profiling.py
## @author Denis Ragan (xragan00)
## @brief Profiling


mathLib = math_lib.MathLib()

## @brief Reads standard input
## From user
## From file
## @returns Array of numbers

def read_from_stdin():
    arr = []
    for line in sys.stdin:
        if line.rstrip() == '':
            break
        if '\t' in line:
            arr.extend(line.split("\t"))
        else:
            arr.extend((line.split(" ")))
        arr = [item if isinstance(item, float) else float(item) for item in arr]
    return arr

## @brief Counts mean, variance and standard deviation
## @params Array of numbers
## @returns Standard deviation

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
