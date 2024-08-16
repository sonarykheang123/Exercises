#Ex1 - String Enter text and display it one by one
text=input("enter here:")
for i in  range (len(text)):
    print(text[i])

#Ex2 - String Enter text and display number of letter
text=input("enter here:")
for i in range(len(text)):
     print(i)


#Ex3 - String Enter text and check if it contains capital letter or not
#Display "Yes" if capital
#display "No" if all lowercase letter
text = input("Enter your text: ")
index = 0
result = "No"
while index < len(text):
    if text[index].isupper():
        result = "Yes"
        index = len(text)
    index += 1  
print(result)
#Ex4 - String  We have text = "3 4 5 6"
#Q1 - display number 1 by one without space
text = "3 4 5 6" 
result = ""
for i in range (len(text)):
    if text[i]!=" ":
       result += str(text[i])
print(result)


#Q2 - Sum all number (Total: 18)
text = input("Enter your text:") 
sumOftext = 0
for i in range (len(text)):
    sumOftext += int(text[i])
print(sumOftext)


#Ex5 - String We have text = "454639"
#-----Q1 - Count odd and even number in text----#
text=input("enter here:")
countOdd=0
countEven=0
for i in range (len(text)):
    if i % 2==0:
        countEven+=1
    if i % 2==1:
        countOdd+=1
print(countOdd)
print(countEven)
#Q2 - Sum all number
text = input("Enter your text:") 
sumOfText = 0
for i in range (len(text)):
    sumOfText += int(text[i])
print(sumOfText)
#Q3 - Sum only even number 
text = "454639"
sumEven = 0
for i in range (len(text)):
    if int (text[i]) % 2 == 0:  
        sumEven += int(text[i]) 
print(sumEven)
#Q4 - Reverse
text="454639"
t=len(text)-1
result=""
for i in range (len(text)):
   result+=text[t-i]
print(result)


#Ex6 - NumberEnter number and check if odd number print "Odd" otherwise print "Even"
number=int(input("enter here:"))
if number % 2==1:
    print("Odd number")
else:
    print("even number")

# Ex7 - numberEnter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
num=int(input("enter number:"))
while num >=10 and num <= 20:
      print("continue")
      num=int(input("enter number:"))
print("Out of range")
         
# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
text="9394884039"
Count_eight=0
for i in range (len(text)):
      if text[i]=="8":
            Count_eight+=1
print(Count_eight)
#Q2 - What is first index of letter 8
text="9394884039"
isFound_8 = False
index = 0
while not isFound_8:
    index += 1
    if text[index] == "8":
        isFound_8 = True
        result = index
print(result)

#Ex9 - String
#We have string = "3 4 5 6"
#Q1 - Remove space and keep result = "3456"
text = "3 4 5 6" 
result = ""
for i in range (len(text)):
    if text[i]!=" ":
       result += text[i]
print(result)
#Q2 - Multiple each letter by 2 result = "6 8 10 12"
text = "3 4 5 6"
result = ""
for i in range (len(text)):
    if text[i]!=" ":
       result += str(int(text[i])*2) + " "
print(result)

#Ex10 - Number
#Enter 5 numbers and find maximum and minimum value
#Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
number = int(input("Enter number:"))
number_max = number
number_min = number
for i in range(5):
    number = int(input("Enter number:"))
    if number > number_max:
        number_max = number
    if number < number_min:
        number_min = number
print("Max =", number_max, "Min =", number_min)





  

