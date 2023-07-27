import random

class JogoAdivinhar:
    def __init__(self):
        self.nome = '';
        self.inferior = 0;
        self.superior = 0;
        self.maxTentativa = 0;
        self.numero_secreto = 0;
        self.jogar = True;
    
    def jogo(self):
        tentativas = 0;
        chanceTentativas = self.maxTentativa;
        while tentativas < self.maxTentativa:

            palpite = int(input("Digite o seu palpite: "));
            tentativas += 1;
        
            if palpite < self.numero_secreto:
                print(f"{tentativas} TENTATIVA!");
                chanceTentativas -= 1
                print(f"Você tem chance {chanceTentativas} TENTATIVA!");
                print("Tente um número maior!");
                print("===========================");
            elif palpite > self.numero_secreto:
                print(f"{tentativas} TENTATIVA!");
                chanceTentativas -= 1
                print(f"Você tem chance {chanceTentativas} TENTATIVA!");
                print("Tente um número menor!");
                print("===========================");
            elif palpite == self.numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas!");
                print("===========================");
                break;
            else:
                print("Não acertou...");
                print("===========================");
        
        print(f"---> Número secreto é {self.numero_secreto}! <--- e reinicia o jogo");
        print("===========================");
        
        while True:
            print("QUER CONTINUAR O JOGO?");
            opcao = input("Digite [s] SIM e [n] NÃO: ");
            print("===========================");
            if opcao == 's':
                print("CONTINUA O JOGO");
                print("===========================");
                break;
            elif opcao == 'n':
                print("TERMINA O JOGO");
                print("===========================");
                self.jogar = False;
                break;
            else:
                print("INVALIDO");
                print("===========================");

    def iniciar(self):
        while self.jogar:
            self.nome = (input("Digite seu nome: "));
            self.limite_inferior = int(input("Digite um numero inferior: "));
            self.limite_superior = int(input("Digite um numero superior: "));
            self.maxTentativa = int(input("Digite um numero quanto pode tentativa: "));
            print("===========================");

            self.numero_secreto = random.randint(self.limite_inferior, self.limite_superior);

            print("Bem-vindo ao jogo de adivinhação de números!");
            print(f"Estou pensando em um número entre {self.limite_inferior} e {self.limite_superior}.");
            print("===========================");
            self.jogo();

JogoAdivinhar().iniciar();