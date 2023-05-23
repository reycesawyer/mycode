#!/usr/bin/env python3

#This shows a list of numbers
num = [ "1", "4", "7", "10" ]
num2 = [ "1", "4", "7", "10" ]

print(num)
print(num2)

#This is a list to add to it

mas = [ "yes", "no", "maybe so" ]

#This is the extend option

num.extend(mas)
print(num)
#This is the append option

num2.append(mas)
print(num2)
