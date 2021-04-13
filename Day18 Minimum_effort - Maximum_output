def main():

 # Write code here 
    n = int(input())
    start, end = 0, n-1
    arr = list(map(int,input().split()))
    sortarr = sorted(arr)
    while arr[start] == sortarr[start]:
        start += 1
    while arr[end] == sortarr[end]:
        end -= 1
    for i in range(start,end+1):
        if i==end:
            print(arr[i],end='')
        else:
            print(arr[i], end= " ")
main()
