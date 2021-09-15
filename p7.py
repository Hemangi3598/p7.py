# wapp to read radius from the user
# print area and circumference

n1 = float(input("enter radius"))
pi = 3.1459
area = pi* n1* n1
circum = 2* pi* n1

print(" area = ",round(area,2))
print(" circum = ", round(circum,2))

# float() funtion can read decimal numbers and integers both 
# so using float() functn is always benificial 
# instead of defining pi we can directly write 3.1459 directly
