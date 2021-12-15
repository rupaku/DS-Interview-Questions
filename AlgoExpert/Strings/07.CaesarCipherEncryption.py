'''
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
'''
#O(n) | O(n)
def caesarCipherEncryptor(string, key):
    # Write your code here.
    new_letters = []
	new_key = key % 26
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	for letter in string:
		new_letters.append(get_new_letter(letter,new_key,alphabet))
	return "".join(new_letters)

def get_new_letter(letter,key,alphabet):
	new_letter_code = alphabet.index(letter) + key
	return alphabet[new_letter_code % 26]