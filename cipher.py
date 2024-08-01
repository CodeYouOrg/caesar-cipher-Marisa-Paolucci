#Caesar Cipher with a shift of 5
# first created a dictionary with the shift 5 key for each letter in the alphabet.

substitution = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

user_sentence = input("Please enter a sentence: ")
user_sentence = user_sentence.lower() # this will change all uppercase to lowercase letters.

secret_code = "" # initialize the secret_code variable
for char in user_sentence: # creating a for loop to iterate through the user's sentence
    if char in substitution:
        char = substitution[char] # changes the user's letters into the dictionary letters. The non-substitution remain as they are (punctuation and white spaces).
    secret_code += char # The += will add everything on the left to the right. 

print(secret_code) 
