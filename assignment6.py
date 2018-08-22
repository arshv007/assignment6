#Ques1
def sphere(r):
    a=4*3.14*r*r
    print(a)

r=int(input('Enter Radius:'))
sphere(r)

#Ques2

def perfect(num):
    sum=0
    i=1
    while i<num:
        if(num%i==0):
            sum=sum+i
        i+=1
        
    if num!=1 and sum==num:
         print (num)
         
print('The Perfect Numbers:')
for i in range (1,1000):
    perfect(i)

#Ques3
def multi():
    n=int(input('Enter integer:'))
    for i in range(1,11):
        print(n,'x',i,'=',n*i)

multi()
    
#Ques4
def exponent(a,b):
    
    if(b==1):
        return a
    else:
        return a*exponent(a,b-1)
a=int(input("Enter base: "))
b=int(input("Enter exponential number: "))
c=exponent(a,b)
print(c)
