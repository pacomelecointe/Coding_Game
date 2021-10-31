import sys
import math
import string


l = int(input())
h = int(input())
t = input()
t = t.upper()

y = ''
for i in range(h):
    row = input() 

    for g in t : 
        if ( g.isalpha() == False) :   
            x = 26
        else : 
            x= string.ascii_uppercase.index(g)
        y += (row[l*x:l*(x+1)])
    y += ('\n')    
print(y)


