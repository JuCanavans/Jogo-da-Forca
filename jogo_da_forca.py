import random
import os

def jogo_da_forca():
    inicio_game()

    palavra_secreta = gerando_palavra_secreta()
    letras_acertadas = letras_corretas(palavra_secreta)
    tentativas_limite = int(input('Digite a quantidade de tentativas: '))
    limpar_tela()
    

    print('Jogo da Forca!')
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    tentativas = 0

    while (not enforcou and not acertou):
        chute = chute_player()

        if (chute in palavra_secreta):
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
        
        numero_tentativas_restante(tentativas, tentativas_limite)
        enforcou = tentativas == tentativas_limite
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    #Condição se ganhou ou perdeu 
    if (acertou):
        exibir_ganhador()
    else:
        exibir_perdedor(palavra_secreta)
        print('End Game....')

def inicio_game():
    print('############################')
    print('Bem vindo ao Jogo da Forca!')
    print('############################\n')

def limpar_tela():
    #Função para deixar a tela mais limpa, lembrando de imoporta o OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def gerando_palavra_secreta():
    #chamando uma lista externa contendo as palavras 
    arquivo_palavras = open('palavras_forca.txt', 'r')
    palavras = []

    for linha in arquivo_palavras:
        linha = linha.strip()
        palavras.append(linha)

    arquivo_palavras.close()

    #Aqui estamos escolhendo a palavra de forma aleatoria
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def chute_player():
    #Aqui estamos recebendo o chute do player
    print('\n')
    chute = input('Digite uma letra: ')
    chute = chute.strip().upper()
    
    return chute

def numero_tentativas_restante(tentativas, tentativas_limite):
    numero_tentativas_restante = tentativas_limite - tentativas

    print(f'Voce ainda possui {numero_tentativas_restante}, tentativas.')
    
def letras_corretas(palavra):
    #A cada letra correta sera substituido o '_', para letra que o usuario chutou 
    return ["_" for letra in palavra]

def chute_correto(chute, letras_corretas, palavra_secreta):
    #Função para validar chute correto 
    index = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_corretas[index] = letra
        index += 1

def exibir_perdedor(palavra_secreta):
    print("")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def exibir_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if (__name__ == '__main__'):
    jogo_da_forca()

