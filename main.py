#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_index_list_letters = []
random_index_list_symbols = []
random_index_list_numbers = []

random_letters_list = []
random_symbols_list = []
random_numbers_list = []

for i in range(0,nr_letters):
  random_index_list_letters.append(random.randint(0,len(letters)-1))
for i in range(0,nr_symbols):
  random_index_list_symbols.append(random.randint(0,len(symbols)-1))
for i in range(0,nr_numbers):
  random_index_list_numbers.append(random.randint(0,len(numbers)-1))

for index in random_index_list_letters:
  random_letters_list.append(letters[index])

for index in random_index_list_symbols:
  random_symbols_list.append(symbols[index])

for index in random_index_list_numbers:
  random_numbers_list.append(numbers[index])

combined_list = random_letters_list + random_symbols_list + random_numbers_list

combined_list_index = []
for i in range(0,len(combined_list)):
  combined_list_index.append(i)

random.shuffle(combined_list_index)

password = []
for i in combined_list_index:
  password.append(combined_list[i])

password_string = ""
for i in password:
  password_string += i
print(f"Your new random password is {password_string}")