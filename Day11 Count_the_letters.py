def main():

 # Write code here 
 c1=0
 c2=0
 string=input()
 for i in string:
    if ord(i)>=65 and ord(i)<=90:
        c1+=1
    if ord(i)>=97 and ord(i)<=122:
        c2+=1
 print(c1)
 print(c2)
main()
