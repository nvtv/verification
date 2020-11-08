# coding: utf8
"""
**PESEL** is the national identification number used in Poland since 1979.

Having a PESEL in the form of *abcdefghijk*, one can check the validity of the number by computing
the following expression:

1×*a* + 3×*b* + 7×*c* + 9×*d* + 1×*e* + 3×*f* + 7×*g* + 9×*h* + 1×*i* + 3×*j*

Then the last digit of the result should be subtracted from 10. If the result of the last operation
is not equal to the last digit of a given PESEL, the PESEL is incorrect. This system works reliably
well for catching one-digit mistakes and digit swaps.

Checking validity of PESEL: 44051401358 (number 8, the last digit, is the check digit for this PESEL):

    1×4 + 3×4 + 7×0 + 9×5 + 1×1 + 3×4 + 7×0 + 9×1 + 1×3 + 3×5 = 101

Getting the last digit of the result (101 % 10):

101 % 10 = 1

In order to get the check digit one need to take the 10s complement of the number. It is 0 if the modulo
result is 0, and it is 5 when the modulo is equal to 5, otherwise it means the modulo result has to
be subtracted from 10.

10 - 1 = 9

9 is not equal to the last digit of PESEL, which is 8, so the PESEL contains errors.

### Date of birth

PESEL also a encodes birthdate. It is stored in the first six digits os the number in the form
`YYMMDDxxxxxx`, where YYMMDD is the date of birth (with century encoded in month field).
The PESEL system has been designed to cover five centuries. To distinguish people born in
different centuries, numbers are added to the MM field: 

- for birthdates between 1900 and 1999: no change to `MM` field is made
- for other birthdates:
  - 2000–2099: month field number is increased by 20
  - 2100–2199: month + 40
  - 2200–2299: month + 60
  - 1800–1899: month + 80

For example, a person born on *December 24, 2002* would have a PESEL number starting with `023224`
and person born on *December 24, 1902* would have a PESEL number starting with `021224`.

### Your task (`pesel.py`)

1. Write a function `check_pesel` that will verify the PESEL number and the date of birth of the person
identified by this number.

   The function is supposed to take the PESEL number as a text string and return:

   - None if PESEL is incorrect
   - date of birth in the format `September 5, 1971` if the PESEL number is correct

2. Write the function `check_pesel_file`, which takes the file name as an argument and reads PESEL numbers
   from this file (one on each line). The function must create a file with the same name as the original file name
   with the extension changed to `.out`, containing each line of the person's date of birth, or the sign "-"
   in the case of an incorrect PESEL number.

   For example, calling `check_pesel_file("pesels.txt")` will create the file `pesels.out`. If the file
   `pesels.txt` contains

        90090515836
        87832165581

   This `pesels.out` will be as follows:

        May 5, 1990
        -

   It is worth considering how to use the function from the first point.
"""
def check_pesel(pesel):
    pesel_in_list = [int(x) for x in str(pesel)]
    if len(pesel_in_list) != 11:
        return None
    month = {	"1":'Janauary',
		"02":'February',
		"03":'March',
		"04":'April',
		"05":'May',
		"06":'June',
		"07":'July',
		"08":'August',
		"09":'September',
		"10":'October',
		"11":'November',
		"12":'December'	}
    ##FITST STEP##
    pesel_copy = pesel_in_list.copy()
    pesel_copy[0] =pesel_in_list[0]*1
    pesel_copy[1] =pesel_in_list[1]*3
    pesel_copy[2] =pesel_in_list[2]*7
    pesel_copy[3] =pesel_in_list[3]*9
    pesel_copy[4] =pesel_in_list[4]*1
    pesel_copy[5] =pesel_in_list[5]*3
    pesel_copy[6] =pesel_in_list[6]*7
    pesel_copy[7] =pesel_in_list[7]*9
    pesel_copy[8] =pesel_in_list[8]*1
    pesel_copy[9] =pesel_in_list[9]*3
    sum_of_pesel_copy = sum(pesel_copy)-pesel_copy[10]
    last_digit = sum_of_pesel_copy%10
    last_substracted = 10 - last_digit
    if last_substracted != pesel_in_list[10]:
        return None
    else:
        if pesel_in_list[2]*10+pesel_in_list[3] < 21:
            str1 = str(pesel_in_list[2])
            str2= str(pesel_in_list[3])
            month_for_that_pesel = str1 + str2
            if pesel_in_list[4] != 0:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[4]) + str(pesel_in_list[5]) + ", " + "19" + str(pesel_in_list[0]) + str(pesel_in_list[1])
            else:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[5]) + ", " + "19" + str(pesel_in_list[0]) + str(pesel_in_list[1])
        elif pesel_in_list[2]*10+pesel_in_list[3] > 21 and pesel_in_list[2]*10+pesel_in_list[3] < 32:
            str1 = str(pesel_in_list[2] - 2)
            str2= str(pesel_in_list[3])
            month_for_that_pesel = str1 + str2
            if pesel_in_list[4] != 0:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[4]) + str(pesel_in_list[5]) + ", " + "20" + str(pesel_in_list[0]) + str(pesel_in_list[1])
            else:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[5]) + ", " + "20" + str(pesel_in_list[0]) + str(pesel_in_list[1])
        elif pesel_in_list[2]*10+pesel_in_list[3] > 32 and pesel_in_list[2]*10+pesel_in_list[3] < 52:
            str1 = str(pesel_in_list[2] - 2)
            str2= str(pesel_in_list[3])
            month_for_that_pesel = str1 + str2
            if pesel_in_list[4] != 0:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[4]) + str(pesel_in_list[5]) + ", " + "21" + str(pesel_in_list[0]) + str(pesel_in_list[1])
            else:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[5]) + ", " + "21" + str(pesel_in_list[0]) + str(pesel_in_list[1])
        elif pesel_in_list[2]*10+pesel_in_list[3] > 52 and pesel_in_list[2]*10+pesel_in_list[3] < 72:
            str1 = str(pesel_in_list[2] - 6)
            str2= str(pesel_in_list[3])
            month_for_that_pesel = str1 + str2
            if pesel_in_list[4] != 0:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[4]) + str(pesel_in_list[5]) + ", " + "22" + str(pesel_in_list[0]) + str(pesel_in_list[1])
            else:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[5]) + ", " + "22" + str(pesel_in_list[0]) + str(pesel_in_list[1])
        elif pesel_in_list[2]*10+pesel_in_list[3] > 72 and pesel_in_list[2]*10+pesel_in_list[3] < 92 :
            str1 = str(pesel_in_list[2] - 8)
            str2= str(pesel_in_list[3])
            month_for_that_pesel = str1 + str2
            if pesel_in_list[4] != 0:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[4]) + str(pesel_in_list[5]) + ", " + "18" + str(pesel_in_list[0]) + str(pesel_in_list[1])
            else:
                return str(month[month_for_that_pesel]) + " " + str(pesel_in_list[5]) + ", " + "18" + str(pesel_in_list[0]) + str(pesel_in_list[1])
def check_pesel_file(filename):
    with open("data.out", 'w') as out_file:
        out_file.write("")
    with open(filename) as files:
        pesels = files.readlines()
        for pesel in pesels:
            pesel = pesel.rstrip()
            p = check_pesel(pesel)
            if p == None:
                p = "-\n"
            else:
                p = p + "\n"
            with open("data.out", 'a') as out_file:
                out_file.write(p)