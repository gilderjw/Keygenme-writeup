#!/usr/bin/env python

import random

vowels = "AEIOUY"
consonants = "BCDFGHJKLMNPQRSTVWXZ"

def generate_key():
  answer = ""

  for k in range(31):
    if k % 2 == 0:
      answer += random.choice(consonants)
    else:
      answer += random.choice(vowels)

  return answer

while True:
  raw_input("Press enter to generate key...")
  print(generate_key())
