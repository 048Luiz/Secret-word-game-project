"""
Faça um jogo para o usuário advinhar qual a palavra secreta. 
Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letras.
Qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
Se a letra digitada estiver na palavra secreta exiba a letra
se a letra digitada não estiver na palavra secreta exiba *
Faça a contagem de tentativas do usuário.
"""

palavra_secreta = "abacaxi"
letras_acertadas = ""
tentativas = 0
print("Jogo da Forca")

while True:
    letra_digitada = input("Digite uma letra: ").lower()
    tentativas += 1
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        print(f"Você acertou a letra '{letra_digitada}'!")
    else:
        print(f"A letra '{letra_digitada}' não está na palavra secreta.")
    palavra_formada = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += "*"
    print(f"Palavra formada: {palavra_formada}")
    if palavra_formada == palavra_secreta:
        print(f"Parabéns! Você acertou a palavra secreta '{palavra_secreta}' em {tentativas} tentativas.")
        break