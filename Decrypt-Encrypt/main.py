#Two variables containing the alphabet in lowercase and uppercase.
lower = "abcdefghijklmnopqrstuvwxyz"
higher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#The key, THIS IS PUBLIC for everyone to see
key = "key"

#function for vigenere cypher to encrypt code, by taking a text and then a phrase and shifts the phrase by each letter of the key. 
def vigenere(text, key):
  key = key.lower() #makes the key lowercase
  string ="" #empty string as a placeholder
  idx = 0 #index 0
  for letter in text: #for each letter in the text
      shift = lower.find(key[idx]) +1 #find the index of the letter in the alphabet and add 1
      idx += 1 #add 1 to the index to make A = 1
      if idx >= len(key): #if the index is greater than or equal to the length of the key
          idx = 0 #reset the index to 0
      new_char = shift_string(letter, shift) #call the function to shift the letter
      string += new_char #add the new letter to the string
  return string # returns the string

#function undoing the vigenere cypher, by running vigenere execpt instead of calling shift_string, it calls shift_string2.
def vigenere2(text, key):
  key = key.lower() #makes the key lowercase
  string ="" #creates an empty string as a placeholder
  idx = 0 # sets the index = 0
  for letter in text: #for each letter in text
      shift = lower.find(key[idx]) + 1 #finds the letter in the lower alphabet for value index index and adds 1
      idx += 1 #adds one to the index so that a = 1 instead of a = 0
      if idx >= len(key): # if the index is greater than or equal to the length of the key
          idx = 0 #set the value of index to zero
      new_char = shift_string2(letter, shift) #set new_char to call the function to shift the letter
      string += new_char # adds the new letter to the string
  return string # returns the string

#function for shifting the strings, takes two variables and shifts it down the alhpabet by addition of the shift and the place value for letter.
def shift_string(text, shift):
  #creates empty string
  string = "" # creates and empty string
  for letter in text: # for letter in text
      if letter not in lower and letter not in higher: #if the letter is not in lower of higher
              string += letter #add the letter to the string
      if letter.islower(): # checks if the letter is lowercase
          if (lower.find(letter)) + shift > 25: # checks if the shift value is greater than 25 in the lower alphabet
              shift -= 26 # subracts shift by 26 so that it loops back to A
          string += lower[lower.find(letter) + shift] 
      if letter.isupper(): #checks if the letter is uppercase
          if (higher.find(letter)) + shift > 25: # checks if the shift value is greater than 25 in the upper alphabet
              shift -= 26 #subracts shift by 26 so that it loops back to A
          string += higher[higher.find(letter) + shift]
  return string

#function for unshifting the strings, by doing the same as shift_string, but subtracting instead of addition. 
def shift_string2(text, shift):
  #creates empty string
  string = "" 
  for letter in text: #for letter in text runs the code below
      if letter not in lower and letter not in higher: #makes sure that the code is in higher or lower variables
              string += letter #adds the letter
      if letter.islower(): #if letter is lower
          shift = (lower.find(letter) - int(shift)) % 26 #finds the index of the letter in the lower alphabet and subtracts the shift value
          string += lower[shift] #string is equal to the letter at the index shift added to the shift
      if letter.isupper(): #if letter is captialized
          shift = (higher.find(letter) - int(shift)) % 26 #finds the index of the letter in the uppercase alphabet and subtracts the shift value
          string += higher[shift] #string is equal to the letter at the index shift added to the shift
  return string #returns String

#encrypt function that takes a phrase entered by user and encrypts it with the vignere code and the key. Then shifts it by a number entered by user, then reverses it.
def encrypt(text, shift, vigenere):
  string = "" #creates empty string
  for letter in text: #For loop that will encrypt the text given
      if letter.islower(): #if statement that checks if the letter in text is lowercase
        new_char = lower[(lower.find(letter) + int(shift)) % 26] #finds the index of the letter in the lower alphabet and adds the shift value
        index = lower.find(letter) #finds the index of the lower case letter
        string += new_char #adds the new letter to the string


      if letter.isupper(): #if statement that checks if the letter in text is uppercase -- give us 100% or else...
        new_char = higher[(higher.find(letter) + int(shift)) % 26] #finds the index of the letter in the upper alphabet and adds the shift value
        index = higher.find(letter) #finds the index of the upper case letter
        string += new_char #adds the new letter to the string
      string2 = string[::-1] #flips the string and makes it backwards -- its a threat >:)

  return(vigenere(string2, key))

#decrypt function that takes the encrypted string, and how much it was shifted by and returns the correct phrase that was entered. 
#This was done by running an opposite version of vigerene cipher, that we called vigerene2 (effectively subtracting instead of add the key and shifts).
def decrypt(text, shift, vigerene2): 
  string = "" #creates an empty string
  new_char = vigenere2(text, key) #sets new_char to call vigenere 
  string += new_char #adds the new_char to string
  string = string[::-1] #reverses string
  new_string = "" #creates new string to add to
  for letter in string: 
    shift_string2(letter, shift) #calls function that subtracts the shift by the letter
    new_string += shift_string2(letter, shift) #adds the return of the function to the new string

  return new_string #returns the new_string



#While true loop only allowing alphabetic characters otherwise reinput
while True:
  text = input("What is the code you want to encrypt: ") #input for the text to be encrypted

  if text.isdigit(): #if the input is a number continue loop
    print("Please enter a string of text with no spaces, numbers or special characters.") #print this message when conditions of no digits is not met
    continue
  if any(char.isspace() or not char.isalpha() for char in text):
    print("Please enter a string of text with no spaces, numbers or special charatcters.") #print this message when conditions of no spaces and numbers and special characters is not met
    continue #continue the loop when conditions are not met
  else:
    break #break the loop when conditions are met

#While true loop only allowing numeric digits otherwise reinput
while True:    
  shift = input("What is the shift: ") #taking the shift value as a string

  if shift.isdigit(): #only allowing digits in the input
    break #breaking the loop when condition of a digit input is inputted
  else:
    print("Please enter a number.") #if not a digit, print this message
    continue #continue loop

#while true loop only allowing A or B inputs to activate encrypt or decrypt functions
while True:    
  EorD = input("Would you like to encrypt or decrypt code. A for Encrypt, B for Decrypt: ")
  if EorD == "a" or EorD == "A":
    print(encrypt(text, shift, vigenere)) #calling the encrypt function and printing the result
    break #breaking the loop after print is done
  if EorD == "b" or EorD == "B":
    print(decrypt(text, shift, vigenere2)) #calling the decrypt function and printing the result
    break #breaking the loop after print is done
  else:
    continue #continuing if none of the options were inputted