import random
print("Welcome to Password Generator")
letters=int(input("How many letters would you like in your password= "))
symbols=int(input("How many symbols would you like in your password= "))
numbers=int(input("How many numbers would you like in your password= "))
list_of_letters=['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f',
 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l',
 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r',
 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
 'Y', 'y', 'Z', 'z']
list_of_symbols=['!','@','#','$','%','^','&','*','(',')']
list_of_numbers=['1','2','3','4','5','6','7','8','9']
password=[]
for i in range(1,letters+1):
  l=random.choice(list_of_letters)
  password.append(l)
for i in range(1,symbols+1):
  s=random.choice(list_of_symbols)
  password.append(s)
for i in range(1,numbers+1):
  n=random.choice(list_of_numbers)
  password.append(n)
print(password)
random.shuffle(password)
print(password)
for i in password:
  print(i,end="")