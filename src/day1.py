
"""
part1 snippet
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel
needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

part2 snippet
So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just
calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2).
216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account
the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
"""

import pandas as pd


def compute_fuel(mass):

    fuel = int(mass / 3) - 2
    return fuel


def compute_fuel2(mass):

    fuel = compute_fuel(mass)

    if fuel > 0:
        fuel += compute_fuel2(fuel)
        return fuel
    else:
        return 0


def test_fuel():

    assert compute_fuel(12) == 2
    assert compute_fuel(14) == 2
    assert compute_fuel(1969) == 654
    assert compute_fuel(100756) == 33583


def test_fuel2():

    assert compute_fuel2(14) == 2
    assert compute_fuel2(1969) == 966
    assert compute_fuel2(100756) == 50346


if __name__ == "__main__":

    ff = "day1data.csv"

    masses = pd.read_csv(ff, header=None).iloc[:,0]

    total_sum = masses.apply(compute_fuel).sum()
    total_sum2 = masses.apply(compute_fuel2).sum()

    print(total_sum)
    print(total_sum2)
