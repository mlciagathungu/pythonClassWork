text="Hello World"
print(len(text))
print(text.upper())
print(text.lower())
print(text.split())
print(text.replace("Hello", "John"))













# interger function

pos_num =28
neg_num=-1
float_num=1.0

print(abs(neg_num)) # returns  the positive version of the no
print(pow(pos_num,neg_num))  
print(divmod(pos_num,neg_num)) # (28 ,-1) quotient and remainder are returned as tuple 
print(round((pos_num/neg_num),2))
print(sum([pos_num,neg_num]))











nums=[3,9,8,3]
print(len(nums))
print(list(reversed(nums)))
print(min(nums))
print(max(nums))
nums.append(5)
print(nums)
print(nums.pop())
print(nums)
