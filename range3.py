n=int(input("Enter range:"))
print("Numbers are divisible by 3 are ")
for i in range(n+1):
    if int(i%3)==0:
        print(i,end=" ")