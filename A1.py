n = int(input("Digite um número: "))
num = n
fat = 1
while n>0:
        fat = fat*n
        n-=1
print(f"{fat} é o fatorial de {num}")