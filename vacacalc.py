#!/usr/bin/env python3

print("How many years have you been an employee?")
emyears = int(input())

if emyears >= 5: 
    vacadays = emyears * 2
else:
    vacadays = emyears * 1

print ('You have', vacadays, 'vacation days!')

