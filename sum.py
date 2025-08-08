#prime number sum
j = int(input("Enter a number"))
c=0
for i in range(2,j):
    is_prime = True
    for k in range(2,i):
        if(i%k ==0 ):
            is_prime = False
            break
    if is_prime:
        c += i
        
print(c)