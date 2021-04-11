def input_array():
    row, col = map(int,input().split())
    arr=[]
    for i in range(row):
        arr.append(list(map(int, input().split())))
    return arr

def main():
    arr1 = input_array()
    arr2 = input_array()
    arr3 = []
    for i in range(len(arr1)):
        new = []
        for j in range(len(arr1[0])):
            new.append(arr1[i][j]+arr2[i][j])
        arr3.append(new)
    for i in arr3:
        for j in i:
            print(j, end=" ")
        print()
main()
