import os, sys
import typing_extensions

XOR =     [0x76,0x58,0xb4,0x49,  0x8d,0x1a,0x5f,0x38,  0xd4,0x23,0xf8,0x34,  0xeb,0x86,0xf9,0xaa]
ADD =     [0xef,0xbe,0xad,0xde,  0xad,0xde,0xe1,0xfe,  0x37,0x13,0x37,0x13,  0x66,0x74,0x63,0x67]
SHUFFEL = [0x02,0x06,0x07,0x01,  0x05,0x0b,0x09,0x0e,  0x03,0x0f,0x04,0x08,  0x0a,0x0c,0x0d,0x00]

def progressbar(sum, iteration, suffix="", prefix="", length=50):
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / sum))
    filledLength = int(length * iteration // sum)
    bar = "█" * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (suffix, bar, percent, prefix))
    sys.stdout.flush()


def shuffel(value: list, mask: list, length=16):
    res = [0]*length 
    for i in range(length):
        if mask[i] & 0b10000000:
            raise Exception("This should not happen...")
        else:
            res[i] = value[mask[i] & (length-1)]
    return res

def rev_shuffel(value: list, mask: list, length=16):
    res = [0]*length

    for i in range(length):
        if mask[i] & 0b10000000:
            raise Exception("This should NOT happen!")
        else:
            res[mask[i] & (length-1)] = value[i]
    return res

def add(value0: list, value1: list, sign=1, length=16):
    res = [0] * length
    for i in range(length//4):
        v0_s = 0
        v1_s = 1

        for j in range(4):
            v0_s = (v0_s << 8) + value0[3-j + i*4]
            v1_s = (v1_s << 8) + value1[3-j + i*4]
        
        sum_value = ((v0_s + v1_s*sign) % 2**32).to_bytes(4, "little")

        for j in range(4):
            res[j + i*4] = sum_value[j]
    return res

def xor(value0: list, value1: list, length=16):
    res = [0]*length

    for i in range(length):
        res[i] = value0[i] ^ value1[i]
    return res


def print_hex(value: list, valid=None):
    res = ""
    if valid == None:
        valid = [False]*len(value)

    for i in range(len(value)):
        if valid[i]:
            res += "\33[32m"
        else:
            res += "\33[0m"

        res += "{:02X} ".format(0xff & value[i])

        if (i+1) % 4 == 0 and i != 0:
            res += " "
    print("\33[0m" + res + "\33[0m")

def propergate(value):
    #return shuffel(value, SHUFFEL)
    return xor(add(shuffel(value, SHUFFEL), ADD), XOR)

def brutforce_char(input_data: list, index_input: int, index_output: int, target: int):
    input_data_copy = input_data.copy()
    for i in range(0x100):
        input_data_copy[index_input] = i
        out = propergate(input_data_copy)
        if out[index_output] == target:
            return input_data_copy[index_input]
    raise Exception("Nothing working found!")

