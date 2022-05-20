"""
criar um jogo da forca
"""

palavra = "futebol"
letras_digitadas = []
chance = 3

while True:
    if chance == 0:
        print("otario, perdeu hahaha. ")
        break


    letra = input("digite uma letra: ")

    if len(letra) > 1:
        print("digite apenas uma letra. ")
        continue

    letras_digitadas.append(letra)

    if letra in palavra:
        print(f"ACERTOU!! A letra '{letra}' existe na pallavra. ")
    else:
        print("Que pena, tente novamente. ")
        letras_digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_digitadas:
            print("uhuuu")
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    print(secreto_temporario)

    if secreto_temporario == palavra:
        print(f"voce concluiu a charada, a palavra correta é {palavra} ")
        break


    if letra not in palavra:
        chance -= 1

    print(f"voce ainda tem {chance} chances. ")
    print()









