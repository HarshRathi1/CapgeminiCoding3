'''You’re given an array of integers, print the number of times each integer has occurred in the array.
Example
Input :
10
1 2 3 3 4 1 4 5 1 2
Output :
1 occurs 3 times
2 occurs 2 times
3 occurs 2 times
4 occurs 2 times
5 occurs 1 times'''
l=int(input())
arr=list(i for i in input().split())
dup=[]
for i in arr:
    if i not in dup:
        dup.append(i)
        c=arr.count(i)
        print("{0} occurs {1} times".format(i,c))