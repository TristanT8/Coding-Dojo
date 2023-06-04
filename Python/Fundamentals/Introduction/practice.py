# 1 Print 1-255
"""num = 1
if num <= 255:
    print(num)
    num += 1
"""
"""for i in range(256):
    print(i)
"""
#2 Print Odds 1-255
"""for i in range(256):
    if i%2 == 1:
        print(i)
"""
#3 Print Ints and Sum 0-255
"""sum=0
for i in range(256):
    print(i)
    sum+=i
    print(sum)

    #i += i
    #print(i)
"""
#4 Iterate and Print Array
"""numbers = [0,1,2,3,4,5]
i=0
for i in range (0,6):
    print(numbers[i])
    """
#5 Find and Print Max
"""number = [0,1,543,24,2343,534,0]
print (max(number))
"""
#6 Get and Print Average
# number = [0,1,543,24,343,534,0]
# print (sum(number)/len(number))

#7 Array with Odds
# new_array = []
# for i in range(256):
#     if i%2 == 1:
#         new_array.append(i)
# print(new_array)

# 8 Square the Values
# new_array = [1,3,5,2,4,6]
# for i in range (6):
#     print(new_array[i]**2)

#9 Greater than Y
# y = 34
# new_array = [26,5,17,38,41,13,52,100,21]

# for i in range(9):
#     if new_array[i] > y:
#         print(new_array[i])

#10 Zero Out Negative Numbers
# new_array = [26,-12,43,231,-3,21,-64,23,-5]
# for i in range(9):
#     if new_array[i] < 0:
#         new_array[i]=0
# print(new_array)

#11 Max, Min, Average
new_array = [26,-12,43,231,-3,21,-64,23,-5]
print(max(new_array))
print(min(new_array))
print(sum(new_array)/len(new_array))

print(max(new_array), min(new_array), sum(new_array)/len(new_array))
