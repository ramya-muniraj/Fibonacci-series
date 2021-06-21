def fibonacci(n):
    f1=0
    f2=1
    if n<1:
        print("invalid number")
    print(f1,end="")
    for i in range(1,n):
        print(f2,end=" ")
        next=f1+f2
        f1=f2
        f2=next
print("enter the n value")
n=int(input("n="))
fibonacci(n)
