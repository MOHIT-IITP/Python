def PrimeNo(n):
  if(n==1):
    return False
  if(n==2):
    return True
  elif(n%2==0):
    return False
  else:
    for i in range(3,int(n**0.5)+1,2):
      if(n%i==0):
        return False
    return True
n=int(input("Enter the number"))
if(PrimeNo(n)):
  print("It is Prime No")
else:
  print("It is Not Prime")
