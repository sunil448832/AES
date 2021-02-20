

import numpy as np
from aes import *


input_key = [0x10, 0x00, 0x11, 0x11, 0x10, 0x10, 0x11,
             0x10, 0x00, 0x01, 0x01, 0x01, 0x11, 0x01, 0x11, 0x00]
plain_text = [0x00, 0x45, 0x15, 0x32, 0x1A, 0x8B, 0x7C,
              0x32, 0x01, 0x96, 0x12, 0xA6, 0x94, 0xD2, 0x56, 0x12]
key_matrix = np.array(input_key).reshape(4, 4).tolist()
plain_text = np.array(plain_text).reshape(4, 4).T


# key generation
aes = AES(SBOX_4B, CONS_4B, MIXING_CONS_4B, 4,
          10, SBOX_INV_4B, MIXING_CONS_INV_4B)
keys = aes.getAllKeys(key_matrix)


# encryption
print("text matrix is : ")
aes.showHex(plain_text)
cypher_text = aes.encryptText(plain_text, keys, show=True)
print('\nencrypted matrix is :')
aes.showHex(cypher_text)


# decryption
keys.reverse()
plain_text = aes.decryptText(cypher_text, keys, show=True)
print('\ndecrypted matrix is :')
aes.showHex(plain_text)
