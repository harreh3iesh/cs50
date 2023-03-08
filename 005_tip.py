'''
Lesson: 002
Tip calculator
03/06/2023


Implement two functions:

1. dollars_to_float
    a. accept a str as input (formatted as $##.##, wherein each # is a decimal digit)
    b. remove the leading $
    c. return the amount as a float.
    For instance, given $50.00 as input, it should return 50.0.

2. percent_to_float,
    a. str as input (formatted as ##%, wherein each # is a decimal digit),
    b. remove the trailing %, and return the percentage as a float.
    For instance, given 15% as input, it should return 0.15.

https://hackernoon.com/how-to-build-a-tip-calculator-in-python
'''


def dollars_to_float(d):
    normalizeDollarString = d[1:]
    normalizeDollarFloat = float(normalizeDollarString)
    return normalizeDollarFloat


def percent_to_float(p):
    normalizePercentString = p[:2]
    normalizePercentFloat = float(normalizePercentString)
    return normalizePercentFloat


if __name__ == '__main__':
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent) / 100
    print(f"Leave ${tip:.2f}")
