# input from user
name = input("Enter your name: ")
print("Hello "+name+"!")

# type casting
#convert to integer
age = int(input("Enter your age: "))

#convert to float
height = float(input("Enter your height: "))

#convert to string
number = 123
text = str(number)

print(age)
print(height)
print(text)

simple calculator

# conditional statements if-else-elif
#voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
  print("you are eligible")
else:
  print("your are not eligible")

#positive neagative and zero integers
number = int(input("Enter the number: "))
if number == 0:
  print("Zero")
elif number < 0:
  print("Negative number")
else:
  print("Positive number")

#Loops 
#while loop
i = 1
while i <= 10:
  print(i)
  i+=1

#for loop
for i in range(1,6):
  if i == 5:
    break
  print(i)

for i in range(1,6):
  if i == 3:
    continue
  print(i)

#multiplication table
num = int(input("Enter the number: "))
for i in range(1,11):
  # print(num,"*",i,"=",num*i)
  print(f"{num} x {i} = {num*i}")

#sum of 1st n numbers
n = int(input("Enter the number: "))
sum = 0
for i in range(n+1):
  sum +=i
print(f"sum is: {sum}")

#strings

a = "surya"
b = "prakash"
c = "it is " \
"a multi line" \
" string"

#accessing character in a string
name = "SURYA"
print(name[1])
print(name[4])
print(name[-1])

#string slicing
text = "DevOps Dash Board"
print(text[0:6])
print(text[7:])
print(text[::-1])
print(len(text))
print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())
print(text.strip())
print(text.replace("a","s"))
print(text.find("B"))
print(text.split(','))

#functions
def main():
    number = int(input("Enter the number: "))
    power = pow(number,2)
    print(power)
main()


def get_guess():
  guess = int(input("Enter a guess: "))
  return guess

def main():
  guess = get_guess()
  if guess == 50:
    print("CORRECT")
  else:
    print("INCORRECT")
main()


def greet(input):
  if "hello" in input:
    print("hello, there")
  else:
    print("I'm not sure what you mean")

greet("hello, computer")