import array as arr

def maxAndSecondmax(arrLen, arrList):
    if arrLen < 2:
        return "Only One Item is given"
    else:
        big1 = int(max(arrList[0], arrList[1]))
        big2 = int(min(arrList[0], arrList[1]))
        for a in range(2, arrLen):
            if arrList[a] > big2:
                big2 = arrList[a]
            if arrList[a] > big1:
                big2 = big1
                big1 = arrList[a]
        return str(big1) + " " + str(big2)

if __name__ == '__main__':
    arr=[]
    #get array length
    print("Enter array Length : ")
    arrLength = int(input())
    if arrLength >=0:
        for a in range(0, arrLength):
            arr.append(int(input()))
        print("The Max and Second Max numbers are " + str(maxAndSecondmax(arrLength, arr)))
