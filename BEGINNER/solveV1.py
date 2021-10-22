from typing import Text
from PIL.Image import TRANSPOSE
from solve_tools import *


correct_data = [True, True, True, True,     True, True, True, True,     True, True, True, True,     True, True, True, True]
input_data = [ ord("C"),  ord("T"), ord("F"), ord("{"),    0x53, 0x31, 0x4d, 0x44,    0x66, 0x30, 0x72, 0x4d,     0x33, 0x21, ord("}"), 0]
output_data = propergate(input_data)

print_hex(input_data, correct_data)
print_hex(output_data, shuffel(correct_data, SHUFFEL))


OUT_INDEX = 0x5
IN_INDEX = 0xb
TARGET = 0x31

#print(hex(brutforce_char(input_data, IN_INDEX, OUT_INDEX, TARGET)))


def solveA():
    input_data_copy = input_data.copy()
    for i in range(0x100):
        input_data_copy[0xa] = i

        out = propergate(input_data_copy)
        input_data_copy[0xc] = out[0xc]
        out = propergate(input_data_copy)
        input_data_copy[0xd] = out[0xd]
        out = propergate(input_data_copy)

        print_hex(input_data_copy, correct_data)
        print_hex(out, shuffel(correct_data, SHUFFEL))

        if out[0xe] == input_data_copy[0xe]:
            print(i)
            break

res = ""

for i in input_data:
    res += chr(i)

print(res)