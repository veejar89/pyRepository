def convertFive(n):
    givenNumber = str(n)
    givenNumber = givenNumber.replace("0", "5")
    return int(givenNumber)
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
