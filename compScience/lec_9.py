## 24OCT

def revNum(n):
    while n>0:
        r=n%10
        print(r,end="")
        n//=10

def main():
    n=int(input("Enter n: "))
    revNum(n)

main()

## Write a program that finds all armstrong number between 100 & 999

def armstrong(n):
    sumCube=0
    old_n=n
    while n>0:
        r=n%10
        sumCube+=r**3
        n//=10
    if sumCube==old_n:
            return 1
    else:
            return 0
        
def main():
    for i in range(100,1000):
        p=armstrong(i)
        if p==1:
            print(i,end=" ")

main()

##EXPLANATION: armstrong function:
## sumCube: Stores the sum of the cubes of the digits of n.
## old_n: Stores the original number for comparison at the end.
## while n > 0: This loop iterates through each digit of n.
## r = n % 10: Extracts the last digit of n.
## sumCube += r ** 3: Adds the cube of r to sumCube.
## n //= 10: Removes the last digit from n.
## After the loop, it checks if sumCube is equal to old_n. If they are equal, n is an Armstrong number, and the function returns 1; otherwise, it returns 0.

## main function:
## Loops through all three-digit numbers (from 100 to 999).
## Calls armstrong(i) for each number i.
## If armstrong(i) returns 1, it prints i (meaning i is an Armstrong number).

## #How to count numbers

def count(n):
    count=0
    while n>0:
     n=n//10
     count+=1
    return count

##Given a number is binary representation,find the decimal equivalent of the number.
def findNoOfDigits(n):
    count=0
    while n>0:
        n//=10
        count+=1
    return count

def convertBinToDec(n):
    dec=0 #Store the resultant in decimal
    d=findNoOfDigits(n) #This function returns the number of digits in the binary number
    for i in range(d):
        r=n%10
        dec+=r*2**i
        n//=10
    return dec

def main():
    n=int(input("Enter the binary number: "))
    decEquiv=convertBinToDec(n)
    print("Decimal equivalent of",n,"is",decEquiv)

main()