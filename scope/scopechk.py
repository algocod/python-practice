num1 = 5
num2 = 6
if num1 < num2:
    print('level 1 ')
    num3 = 6
print(num3)# scope of num3 outlives the if condition . This sounds like its top to bottom as in top code cant access yet to be created variables in bottom but bottom code can access the variables earlier in the top