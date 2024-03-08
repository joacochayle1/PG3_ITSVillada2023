
def palindromo(palabra):
    if (palabra==palabra[::-1]):
        return True
    else:
        return False
palabraver=input("escriba una palabra para verificar si es palíndromo: ")
print(palindromo(palabraver))


