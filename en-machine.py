# Enigma machine
# Function to encrypt/decrypt

import string

# Set up the rotors and reflector for the Enigma machine
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Set the initial positions of the rotors
rotor1_pos = 0
rotor2_pos = 0
rotor3_pos = 0

# Set up the plugboard for the Enigma machine
plugboard = {"A": "B", "B": "A", "C": "D", "D": "C", "E": "F", "F": "E"}

# Function to perform the substitution using the rotors and reflector
def substitute(c):
  global rotor1_pos, rotor2_pos, rotor3_pos

  # Perform the substitution using the plugboard
  if c in plugboard:
    c = plugboard[c]

  # Advance the rotors
  rotor1_pos = (rotor1_pos + 1) % len(rotor1)
  if rotor1_pos == 0:
    rotor2_pos = (rotor2_pos + 1) % len(rotor2)
  if rotor1_pos == 0 and rotor2_pos == 0:
    rotor3_pos = (rotor3_pos + 1) % len(rotor3)

  # Perform the substitution using the rotors
  c = rotor3[(rotor3_pos + string.ascii_uppercase.index(c)) % len(rotor3)]
  c = rotor2[(rotor2_pos + string.ascii_uppercase.index(c)) % len(rotor2)]
  c = rotor1[(rotor1_pos + string.ascii_uppercase.index(c)) % len(rotor1)]

  # Perform the substitution using the reflector
  c = reflector[string.ascii_uppercase.index(c)]

  # Reverse the substitution using the rotors
  c = string.ascii_uppercase[rotor1.index(c) - rotor1_pos]
  c = string.ascii_uppercase[rotor2.index(c) - rotor2_pos]
  c = string.ascii_uppercase[rotor3.index(c) - rotor3_pos]

  # Perform the substitution using the plugboard
  if c in plugboard:
    c = plugboard[c]

  return c

# Function to encrypt a message using the Enigma machine
def encrypt(plaintext):
  ciphertext = ""
  for c in plaintext.upper():
    if c in string.ascii_uppercase:
      ciphertext += substitute(c)
    else:
      ciphertext += c
  return ciphertext

# Function to decrypt a message using the Enigma machine
def decrypt(ciphertext):
  return encrypt
