def main():

 # Write code here 
 n = int(input())
 d = []
 for i in range(n):
     d.append(input())
 d = sorted(d)
 for i in range(len(d)):
    if d[i]==d[-1]:
        print(d[i],end=" ")
    else:
        print(d[i])
    

main()
