"""
assignment1.py
@author: Sami Cemek
@date: 02-21-2024
@description: This file contains the solutions to the questions in the first assignment of the Cryptography (CSCI 4525) course.
To see the output of the functions, please uncomment the function calls that are labeled as "Test".
"""

import math

# Question 1


# Caesar Cipher Decryption with exhaustive-key search
def decrypt_shift_cipher():
    # cipher_text = input("Enter the cipher text: ")
    cipher_text = "ZWQPFLQUFEFKQNFIBQFEQZDGFIKREKQGIFSCVDJQQZKQZJQEFKQCZBVCPQKYRKQPFLQNZCCQUFQZDGFIKREKQNFIBQQIZTYRIUQYRDDZEX"
    for shift in range(26):
        decrypted_message = ""
        for char in cipher_text:
            if char.isalpha():
                decrypted_message += chr(
                    (ord(char) + shift - 65) % 26 + 65
                )  # 65 is the ASCII value of 'A'
            else:
                decrypted_message += char
        print("The decrypted message with shift", shift, "is: ", decrypted_message)


# Test
# decrypt_shift_cipher()

# -------------------------------------------------------------------------------------

# Question 2


# Euclidean Division Algorithm
def euclidean_division_algorithm(a, b):
    while b != 0:
        print("a = " + str(a))
        print("b = " + str(b))
        print("q = " + str(a // b))
        print("r = " + str(a % b))
        print("----------------")
        q = a // b
        r = a % b
        a = b
        b = r
    return a


def euclidean_division_algorithm_extended(a, b):
    while b != 0:
        a, b = b, a % b
    return


# Test
# print(euclidean_division_algorithm(420, 17))
# print(euclidean_division_algorithm_extended(420, 17))

# -------------------------------------------------------------------------------------


# Question 3


# space-improved version of the Euclidean Division Algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Multiplicative Inverse
def find_multiplicative_inverses(modulo):
    inverses = []
    for i in range(1, modulo):
        if gcd(i, modulo) == 1:
            inverses.append(i)
    return inverses


# Test
# Z36 = 36
# multiplicative_inverses = find_multiplicative_inverses(Z36)
# print("Elements in Z36 with multiplicative inverses:", multiplicative_inverses)
# print("Total number of multiplicative inverses in Z36:", len(multiplicative_inverses))

# -------------------------------------------------------------------------------------


# Question 6
# Exhaustive-key search with Affine Cipher Decryption


# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 26) = 15
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# Calculate the modular multiplicative inverse of an integer a modulo m
# I rewrote the function to return the modular inverse of a number, the other function returns an array
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m


# affine cipher decryption function
# returns the plain text
def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            char_num = ord(char) - ord("A")
            char_num = (modinv(a, 26) * (char_num - b)) % 26
            plaintext += chr(char_num + ord("A"))
        else:
            plaintext += char
    return plaintext


# exhaustive_search over Z26
def exhaustive_search(ciphertext):
    for a in range(1, 26):
        if math.gcd(a, 26) == 1:
            for b in range(26):
                decrypted_text = affine_decrypt(ciphertext, a, b)
                print(f"Key: ({a}, {b}), Decrypted text: {decrypted_text}")


# Test the exhaustive_search function
ciphertext = (
    "EILYTAELJDILHGCJLNQJLUGTTAJLUATJVAFLKJZLEILUATJVAFLJDILPQJQVILNQJLUGTTAJLYTAELKJZ"
)
# exhaustive_search(ciphertext)
