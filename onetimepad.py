import secrets
from random import randint
import os
import time
import sys
import getpass

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
secretsGenerator = secrets.SystemRandom()

def generate_otp(sheets, length):
	for sheet in range(sheets):
		with open("otp" + str(sheet) + ".txt","w") as f:
			for i in range(length):
				f.write(str(secretsGenerator.randint(0,32))+"\n")

def load_sheet(filename):
	with open(filename, "r") as f:
		contents = f.read().splitlines()
	return contents

def get_plaintext():
	plaintext = input('Please type your message:   ')
	return plaintext.lower()

def load_file(filename):
	with open(filename, "r") as f:
		contents = f.read()
	return contents

def save_file(filename, data):
	with open(filename, 'w') as f:
		f.write(data)

def encrypt(plaintext, sheet):
	ciphertext = ''
	for position, character in enumerate(plaintext):
		if character not in ALPHABET:
			ciphertext += character
		else:
			encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
			ciphertext += ALPHABET[encrypted]
	return ciphertext

def decrypt(ciphertext, sheet):
	plaintext = ''
	for position, character in enumerate(ciphertext):
		if character not in ALPHABET:
			plaintext += character
		else:
			decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
			plaintext += ALPHABET[decrypted]
	return plaintext

def dangerfile(filename):  
    return filename