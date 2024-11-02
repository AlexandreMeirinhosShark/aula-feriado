import random
num = random.randrange(1, 5, 2)
num1 = int(input("Adivinha um número entre 1 e 5: "))
if num1 >= 1 and num1 <= 5:
    print("Número certo:", num)
    print("Número adivinhado:", num1)
    if num1 == num:
        print("Adivinhaste o número!")
    else:
        print("Estás errado!")
else:
    print("ce acha que eu sou estupido para nao saber que seu numero e absurdamente grande para adivinhar?")