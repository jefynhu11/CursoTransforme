import random

jogo = True;
menu = """
        Bem-vindo ao jogo de adivinhação de números!
        =============================
        1 - Número intervalo: (1 - 20)
        2 - Número intervalo: (1 - 50)
        3 - Número intervalo: (1 - 100)
        4 - Sair o jogo
        =============================
        """

def adivinhar(numero_secreto):
    tentativas = 0

    max_tentativas = int(input("Digite um numero quanto pode tentativa: "));
    print(f"Você tem maximo {max_tentativas} de tentativas!");
    print("===========================");

    while tentativas < max_tentativas:
        palpite = int(input("Digite o seu palpite: "));
        tentativas += 1

        if palpite < numero_secreto:
            print(f"{tentativas} TENTATIVA!");
            print("Tente um número maior!");
            print("===========================");
        elif palpite > numero_secreto:
            print(f"{tentativas} TENTATIVA!");
            print("Tente um número menor!");
            print("===========================");
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!");
            break

    if palpite != numero_secreto:
        print("Não acertou...");

    print(f"---> Número secreto é {numero_secreto}! <--- e reinicia o jogo");

print("Bem-vindo ao jogo de adivinhação de números!");

while jogo:
    print(menu);
    entrada = int(input("Escolhe opções. [1] [2] [3] [4]: "))
    print("===========================");
    match entrada:
        case 1:
            numero_secreto = random.randint(1, 20);
            print("Escolheu numero entre 1 - 20");
            adivinhar(numero_secreto);
        case 2:
            numero_secreto = random.randint(1, 50);
            print("Escolheu numero entre 1 - 50");
            adivinhar(numero_secreto);
        case 3:
            numero_secreto = random.randint(1, 100);
            print("Escolheu numero entre 1 - 100");
            adivinhar(numero_secreto);
        case 4:
            print("Saindo o jogo!");
            jogo = False;
        case _:
            print("INVALIDO!");
