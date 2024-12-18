# decoder.py by comradecheese
# dirty decoder of text files encoded by base16, base32 or base64
# written for the TryHackMe Intro To Python / Scripting room challenges
# usage: python decoder.py <file> <count> <base>
# example: python decoder.py encodedflag.txt 50 64

from base64 import *
import sys

def decodedata():
        # grab the first argument and read the file replacing newlines with null
        encoded_data = open(sys.argv[1], 'r').read().replace("\n", "")
        # grab the second argument and store as count
        count = int(sys.argv[2])
        # grab the third argument and store as base
        base = int(sys.argv[3])

        # this is gross -- i would rather a switch statment to better handle null
        # or incorrect values
        if base == 16:
                for i in range(count):
                        encoded_data = b16decode(encoded_data)
                print(encoded_data.decode())
        elif base == 32:
                for i in range(count):
                        encoded_data = b32decode(encoded_data)
                print(encoded_data.decode())
        elif base == 64:
                for i in range(count):
                        encoded_data = b64decode(encoded_data)
                print(encoded_data.decode())
        else:
                print("error!\nbase needs to be 16, 32 or 64")

decodedata()
