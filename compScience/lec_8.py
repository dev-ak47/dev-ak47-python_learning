def findAvg(n):
    sum=0
    for i in range(n):
        a=eval(input("Enter number: "))
        sum+=a
    avg=sum/n
    return avg
    
def main():
        n=int(input("Enter the number of elements whose average is to be calculated: "))
        avg=findAvg(n)
        print("The average of",n,"given numbers is: ",avg)

main()

# ##The objective is to print the odd numbers from 0 to n, where n is input by the user.

def findOdd(n):
    for i in range(n+1):
        if i%2!=0:
            print(i,end=" ")

def main():
    n=int(input("Enter the ending number: "))
    findOdd(n)
main()

# ##Suppose you want to print the odd numbers from 1 to n inclusive,where n is input by the user.

def findOdd1(n):
    for i in range(n+1):
        if i<5:
            pass ##It will simply pass and do nothing.
        else:
            if i%2==1:
                print(i,end=" ")


def main():
    n=int(input("Enter the ending number: "))
    findOdd1(n)
main()

# ##Do the same thing without using the pass
def printOdd2(s,n):
    for i in range(s,n+1):
        if i%2==1:
            print(i,end=" ")

def main():
    s=int(input("Enter the starting number: "))
    n=int(input("Enter the ending number: "))
    printOdd2(s,n)

main()

# ##Changing stepsize in range() function 
def printOdd3(s,n):
    step=2
    for i in range(s,n+1,step):
        print(i,end=" ")

def main():
    s=int(input("Enter the starting number: "))
    n=int(input("Enter the ending number: "))
    printOdd3()

main()

### Print the following sequence
### 0,1,1,2,3,5,8,13,21,....$. This sequence is called fibonacci sequence.
### Here x(i)= x(i-1)+x(i-2)
###Write a program that computes the nth fibocacci number,where
### n is input by the user.The fibonacci series will start from 0 and 1.

def seq(n):
    x1=0
    x2=1
    print(x1,x2,end=" ")
    for i in range(2,n+1):
        x=x1+x2
        print(x,end=" ")
        x1=x2
        x2=x

def main():
    n=int(input("Enter the limit upto which you want the sequence: "))
    seq(n)

main()

##Write a program to print the digits of a program.Suppose the number entered is 472,then the program should print 274(opposite).
def num(d,n):
    for i in range(d): 
        r=n%10 
        print(r,end=" ") 
        n=n//10 


def main():
    d=int(input("Enter the number of digits of the number: "))
    n=int(input("Enter the number: "))
    num(d,n)

main()

##Do the same task without asking the user for the number of digits.

def printDigit1(n):
    while n>0:
        r=n%10
        print(r,end=" ")
        n=n//10

def main():
    n=int(input("Enter the number: "))
    printDigit1(n)

main()