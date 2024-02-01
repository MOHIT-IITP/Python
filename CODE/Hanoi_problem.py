# Tower of Hanoi code (python )

def hanoi(n,a,c,b):
	if n>0:
		hanoi(n-1,a,b,c)
		print(f"move {a} to {c}")
		hanoi(n-1,b,c,a)


n=int(input("Enter the number : "))
hanoi(n,'A','C','B')