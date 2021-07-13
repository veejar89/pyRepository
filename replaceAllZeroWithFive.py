#You are given an integer N. You need to convert all zeroes of N to 5.
#Example 1:
#Input:
#N = 1004
#Output: 1554
#Explanation: There are two zeroes in 1004
#on replacing all zeroes with "5", the new
#number will be "1554".

def convertFive(n):
    givenNumber = str(n)
    givenNumber = givenNumber.replace("0", "5")
    return int(givenNumber)
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
