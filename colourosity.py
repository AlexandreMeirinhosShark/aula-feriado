col = input("Qual é a tua cor preferida?: ")

if col == "azul":
    print("Azul é uma cor acalmante!")
else:
    if col == "verde":
        print("Verde é uma cor tranquila.")
    else:
        if col == "roxo":
            print("Roxo é uma cor rara.")
        else:
            if col == "vermelho" or col == "encarnado":
                print("Vermelho é uma cor vibrante!")
            else:
                if col == "laranja":
                    print("O que é que vem primeiro? A fruta, ou a cor?")
                else:
                    print(f"{col} é uma cor interessante.")
print ("pronto!")