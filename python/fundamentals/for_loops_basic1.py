for number in range (0, 101, 1):
  print(number)


for number in range (5, 1001, 5):
  print(number)

for num in range (0, 101, 1):
  if(num % 5 == 0):
    print("Coding")

  if (num % 10 == 0):
    print("Coding Dojo")

maximum = int(input("500,000:"))
Oddtotal = 0

# Find Sum of odd numbers bethween 0 - 500,000
x=int(input('0: '))
y=int(input('500000:'))

def SumOdds(x,y):
  count=0
  for i in range(x,y):
     if (int(i%2==1)):
        count=count+i

  print(count)
SumOdds(x,y)

# Print positive numbers starting at 2018, counting down by fours

# Flexible Counter
lowNum = int(input("2:"))
highNum = int(input("9:"))
mult = int(input("3:"))


   