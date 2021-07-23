
#Given an array of distinct elements. Find the third largest element in it.
#Input:
#N = 5
#A[] = {2,4,1,3,5}
#Output: 3

import array as arr
def thirdLargestInt(intLen, arrValues):
    if intLen < 3:
        return -1
    else:
        big1 = int(max(arrValues[0], arrValues[0]))
        big2 = int(min(arrValues[0], arrValues[0]))
        big3 = -1
        for a in range(2, intLen):
            if arrValues[a] > big3:
                big3 = arrValues[a]
            if arrValues[a] > big2:
                big3 = big2
                big2 = arrValues[a]
            if arrValues[a] > big1:
                big2 = big1
                big1 = arrValues[a]
    return int(big3)
if __name__=='__main__':
    arr = []
    print("Enter the length of Array: ")
    n = int(input())
    for i in range(n):
        print("Enter the number at index " + str(i) + ": ")
        arr.append(int(input()))
    print("Third Largest Number is " + str(thirdLargestInt(n, arr)))
