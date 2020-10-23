from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='fox'
password='hello'
cipher=''

import sys

if (len(sys.argv)>1):
	cipher=(sys.argv[1])
if (len(sys.argv)>2):
	password=(sys.argv[2])

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


ciphertext=binascii.unhexlify(cipher)

try:
    plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
    print plaintext
    plaintext = Padding.removePadding(plaintext,mode='CMS')
    print "  decrypt: "+plaintext
except: print "Error!"


plaintext=val
