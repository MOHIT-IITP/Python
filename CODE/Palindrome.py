def pali(L):
    if not L:
        return True
    elif L[0]==L[-1]:
        return pali(L[1:-1])
L=input("Enter the word do youo wanna check : ")
print(pali(L))
