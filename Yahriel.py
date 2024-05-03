# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import string



def decode_caesar(encrypted_msg):
    # Get uppercase alphabet list
    alphabet = list(string.ascii_uppercase)

    # Loop through the 26 letters
    for x in range(len(alphabet)):
        plaintext = ''
        # Loop through the encrypted message, calculate the shift, and get the corresponding letter
        for letter in encrypted_msg:
            index = alphabet.index(letter)
            index = index - x
            if index < 0:
                index = index + len(alphabet)
            plaintext += alphabet[index]
        print('SHIFT: ', x, ' TRANSLATION: ', plaintext)

_SBOX = [
        #S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        #S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        #S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
]

def decimalToBinary(n):
    return format(n, '04b')

def binaryToDecimal(binary):
    return int(binary,2)


def xor(a, b, n):
    ans = ""

    # Loop to iterate over the
    # Binary Strings
    for i in range(n):

        # If the Character matches
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

def fiestelEnc(hex_msg):
    bin_msg = bin(int('1'+hex_msg, 16))[3:]
    splitResult = []

    for i in range(0, len(bin_msg), 6):
        splitResult.append(bin_msg[i: i + 6])

    l_prev, r_prev = splitResult
    rounds = [
        [l_prev, r_prev]
    ]
    for x in range(1,4):
        l = rounds[x-1][0]
        r = rounds[x-1][1]
        s = calculateFromSbox(x-1, r)
        f = s + s[:2]
        print(f)
        new_r = xor(f, l, 6)
        rounds.append([r, new_r])
    return hex(int(rounds[3][0] + rounds[3][1],2))

def calculateFromSbox(sbox, val):
    left = val[0]+val[len(val)-1]
    middle = val[1:5]

    row = _SBOX[sbox][binaryToDecimal(left)][binaryToDecimal(middle)]
    bin_row = decimalToBinary(row)
    return bin_row

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    encVal = fiestelEnc('10f')
    print(encVal)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/