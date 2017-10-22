import math
import random


def karatsuba_multiplication(int1, int2):
    """Karatsuba implementation of integer multiplication."""

    if isinstance(int1, int):
        int1 = str(int1)

    if isinstance(int2, int):
        int2 = str(int2)

    n_int1 = len(int1)
    n_int2 = len(int2)
    highest_pow_2 = max(2**math.ceil(math.log(n_int1, 2)),
                        2**math.ceil(math.log(n_int2, 2)))

    if not highest_pow_2 == n_int1:
        int1 = (highest_pow_2 - n_int1) * '0' + int1

    if not highest_pow_2 == n_int2:
        int2 = (highest_pow_2 - n_int2) * '0' + int2

    n = len(int1)

    if n == 1:
        return int(int1) * int(int2)
    else:
        int1_left_half = int1[:n // 2]
        int1_right_half = int1[n // 2:]
        int2_left_half = int2[:n // 2]
        int2_right_half = int2[n // 2:]

        sum_int1_left_right = int(int1_left_half) + int(int1_right_half)
        sum_int2_left_right = int(int2_left_half) + int(int2_right_half)

        res_ac = karatsuba_multiplication(
            int1_left_half, int2_left_half)
        res_ab_cd = karatsuba_multiplication(
            sum_int1_left_right, sum_int2_left_right)
        res_bd = karatsuba_multiplication(
            int1_right_half, int2_right_half)

        return 10**n * res_ac + 10**(n // 2) * (res_ab_cd - res_ac - res_bd) \
            + res_bd


def recursive_integer_multiplication(int1, int2):
    """Recursive implementation of integer multiplication."""

    if isinstance(int1, int):
        int1 = str(int1)

    if isinstance(int2, int):
        int2 = str(int2)

    n_int1 = len(int1)
    n_int2 = len(int2)
    highest_pow_2 = max(2**math.ceil(math.log(n_int1, 2)),
                        2**math.ceil(math.log(n_int2, 2)))

    if not highest_pow_2 == n_int1:
        int1 = (highest_pow_2 - n_int1) * '0' + int1

    if not highest_pow_2 == n_int2:
        int2 = (highest_pow_2 - n_int2) * '0' + int2

    n = len(int1)

    if n == 1:
        return int(int1) * int(int2)
    else:
        int1_left_half = int1[:n // 2]
        int1_right_half = int1[n // 2:]
        int2_left_half = int2[:n // 2]
        int2_right_half = int2[n // 2:]

        res_ac = recursive_integer_multiplication(
            int1_left_half, int2_left_half)
        res_ad = recursive_integer_multiplication(
            int1_left_half, int2_right_half)
        res_bc = recursive_integer_multiplication(
            int1_right_half, int2_left_half)
        res_bd = recursive_integer_multiplication(
            int1_right_half, int2_right_half)

        return int(10**n * res_ac + 10**(n // 2) * (res_ad + res_bc) + res_bd)


def grade_school_algorithmn(int1, int2):
    """Implementation of the Grade-School Algorithm
    for multiplying two integers."""

    int1_str = str(int1)
    int2_str = str(int2)

    res = 0
    for digit_pos, digit_int2 in enumerate(int2_str[::-1]):
        res_temp = ''
        carry = 0
        for digit_int1 in int1_str[::-1]:
            res_pair_mult = str(int(digit_int1) * int(digit_int2) + carry)
            if len(res_pair_mult) == 1:
                res_pair_mult = '0' + res_pair_mult
            res_temp = res_pair_mult[1] + res_temp
            carry = int(res_pair_mult[0])
        res_temp = str(carry) + res_temp
        res = res + int(res_temp + digit_pos * '0')

    return res


if __name__ == '__main__':
    for i in range(10**3):
        int1 = random.randint(0, 10**128)
        int2 = random.randint(0, 10**128)
        assert(int1 * int2 == grade_school_algorithmn(int1, int2)
               ), ("Grade-School Algorithm for multiplying two integers is not "
                   "implemented correctly.")
        assert(int1 * int2 == recursive_integer_multiplication(int1, int2)
               ), ("Recursive Algorithm for multiplying two integers is not "
                   "implemented correctly.")
        assert(int1 * int2 == karatsuba_multiplication(int1, int2)
               ), ("Karatsuba Algorithm for multiplying two integers is not "
                   "implemented correctly.")
