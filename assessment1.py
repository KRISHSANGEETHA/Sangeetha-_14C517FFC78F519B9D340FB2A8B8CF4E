#recursive function-factorial 
def factorial (n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1) #recursive call 
print(format("factorial-recursive",'^40'))
n=int (input("enter number to find factorial:"))
print("factorial of",n, "is:",factorial(n))