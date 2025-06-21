#grade calculator 
print('\t\t\t\t\t\t\t Grade calculator')
sum=0
for i in range(5):
    number=int(input('enter number of subjects'))
    sum+=number
print('your total number out of 500 is ',sum)
if sum>=450:
    print('grade is A+')
elif 450>sum>400:
    print('grade is A')
elif 400>sum>350:
    print('grade is B+')
elif 350>sum>300:
    print('grade is B')
else:
    print('grade is fail')