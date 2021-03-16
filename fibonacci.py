print("Hello MyCaptain")
a=0
b=1
num=int(input("Please enter number of terms to be shown in the series: "))
if(num<=0):
    print("Invalid syntax...enter correct number: ")
elif(num==1):
    print(a)
elif(num==2):
    print("{},{}".format(a,b),end='')
else:
    print("{},{}".format(a,b),end='')
    for x in range(2,num):
        c=a+b
        print(",{}".format(c),end='')
        a=b
        b=c 
