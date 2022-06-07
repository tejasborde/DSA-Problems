import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')




s1="Tejas"
s2="Tejas"

#Both Variables pointing to same location
print(id(s1))
print(id(s2))

print("\n\n")

#But if we change the value of s2 it will point to address other than s1
s2="T"
print(id(s1))
print(id(s2))