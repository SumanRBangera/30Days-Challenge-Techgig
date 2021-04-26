def main():

 # Write code here 
   n = int(input())
   lst = list(map(int,input().split()))
   add1=0
   add2=0
   for i in range(n):
       if i%2==0:
           add1+=lst[i]
       else:
            add2+=lst[i]
   
   print(abs(add1-add2),end=" ")
   
main()
