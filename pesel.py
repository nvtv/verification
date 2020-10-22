# coding: utf8
"""
**PESEL** is the national identification number used in Poland since 1979.

Having a PESEL in the form of *abcdefghijk*, one can check the validity of the number by computing the following expression:

1×*a* + 3×*b* + 7×*c* + 9×*d* + 1×*e* + 3×*f* + 7×*g* + 9×*h* + 1×*i* + 3×*j*

Then the last digit of the result should be subtracted from 10. If the result of the last operation is not equal to the last digit of a given PESEL, the PESEL is incorrect. This system works reliably well for catching one-digit mistakes and digit swaps.

Checking validity of PESEL: 44051401358 (number 8, the last digit, is the check digit for this PESEL):

    1×4 + 3×4 + 7×0 + 9×5 + 1×1 + 3×4 + 7×0 + 9×1 + 1×3 + 3×5 = 101

Getting the last digit of the result (101 % 10):

101 % 10 = 1

In order to get the check digit one need to take the 10s complement of the number. It is 0 if the modulo result is 0, and it is 5 when the modulo is equal to 5, otherwise it means the modulo result has to be subtracted from 10.

10 - 1 = 9

9 is not equal to the last digit of PESEL, which is 8, so the PESEL contains errors.

### Your task (`pesel.py`)

1. Write a function `check_pesel` that will verify the PESEL number and the date of birth of the person identified by this number.

   The function is supposed to take the PESEL number as a text string and return:

   - None if PESEL is incorrect
   - date of birth in the format `September 5, 1971` if the PESEL number is correct

2. Write the function `check_pesel_file`, which takes the file name as an argument and reads PESEL numbers from this file
   (one on each line). The function must create a file with the same name as the original file name
   with the extension changed to `.out`, containing each line of the person's date of birth, or the sign "-"
   in the case of an incorrect PESEL number.

   For example, calling `check_pesel_file("pesels.txt")` will create the file `pesels.out`. If the file `pesels.txt` contains

        90090515836
        87832165581

   This `pesels.out` will be as follows:

        May 5, 1990
        -

   It is worth considering how to use the function from the first point.
"""


def check_pesel(pesel):
    pass


def check_pesel_file(filename):
    pass