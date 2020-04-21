# There are 3 control flows in python - if for while
a = 2
b = 5
print(a+b)
if (a+b)==10:
    print('addition is wrong')
elif (a+b)>10:
    print('addition is not correct')

else:
    print('addition is correct')

#while statement
condition = 1
while condition<10:
    print(condition)
    condition+=1   # condition = condition +1

i = 1
while i<=10:
    print(i)
    i+=1  # or i = i+1

# For loop
for i in range(1,5):
    print(i)
else:
    print('for loop is over')






