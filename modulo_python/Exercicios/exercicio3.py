# 1-Escreva um programa que solicite ao usuário dois números
# inteiros e exiba a soma, subtração, multiplicação e divisão entre
# esses números.
print('1)');
numero1 = int(input("Digite numero: "));
numero2 = int(input("Digite numero: "));
print("Soma:",numero1 + numero2);
print("Subtração:",numero1 - numero2);
print("Multiplicação:",numero1 * numero2);
if numero2 != 0:
    print("Divisão:",numero1 / numero2);
else:
    print("Divisão: Não pode ser 0 divisão")
print('===============================');
# 2- Escreva um programa que solicite ao usuário uma temperatura
# em graus Celsius e verifique se ela está acima do ponto de
# ebulição da água (100°C). Caso positivo, exiba a mensagem "A
# água está fervendo!".
print('2)');
grausCelsius = int(input("Digite numero graus Celsius: "));
if grausCelsius > 100:
    print("A água está fervendo!");
else:
    print("A água não está fervendo!")
print('===============================');
# 3- Escreva um programa que solicite ao usuário um número
# inteiro e verifique se ele é par ou ímpar.
print('3)');
numero = int(input("Digite um numero: "));
if numero % 2 == 1:
    print("É impar");
else:
    print("É par");
print('===============================');
# 4- Escreva um programa que solicite uma senha ao usuário e
# verifique se a senha está correta. Considere a senha correta como
# "123456".
print('4)');
senha = int(input("Digite numero a senha: "));
if senha == 123456:
    print("A senha está correta.");
else:
    print("A senha não está correta.")
print('===============================');
# 5- Escreva um programa que solicite ao usuário uma idade e
# verifique se ela está entre 18 e 30 anos (inclusive).
print('5)');
idade = int(input("Digite um idade: "));
if (idade >= 18 and idade <= 30):
    print("A idade está dentro 18 a 30 anos.");
else:
    print("A idade não está dentro 18 a 30 anos");
print('===============================');
# 6- Escreva um programa que solicite ao usuário três números
# inteiros e verifique se pelo menos um deles é positivo.
print('6)');
numero1 = int(input("Digite um numero: "));
numero2 = int(input("Digite um numero: "));
numero3 = int(input("Digite um numero: "));

if (numero1 > 0 or numero2 > 0 or numero3 > 0):
    print("Existe um deles é positivo");
else:
    print("nenhum um deles é positivo");

print('===============================');
# 7- Escreva um programa que solicite ao usuário uma letra e
# verifique se ela é uma vogal (a, e, i, o, u).
print('7)');
letra = input("Digite uma letra: ");
if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
    print("É uma vogal");
else:
    print("Não é vogal");
print('===============================');
# 8- Escreva um programa que solicite ao usuário um número
# inteiro e verifique se ele é positivo, negativo ou zero.
print('8)');
numero1 = int(input("Digite um numero: "));
if numero1 > 0:
    print("Numero é positivo");
elif numero1 < 0:
    print("Numero é negativo");
else:
    print("Numero é zero");
print('===============================');
# 9- Escreva um programa que solicite ao usuário três números e
# verifique se eles estão em ordem crescente.
print('9)');
numero1 = int(input("Digite um numero: "));
numero2 = int(input("Digite um numero: "));
numero3 = int(input("Digite um numero: "));
if numero1 < numero2 and numero2 < numero3:
    print("Os numeros são crescente:", numero1, numero2, numero3);
else:
    print("Os numero não são crescente:", numero1, numero2, numero3);
print('===============================');
# 10- Escreva um programa que solicite ao usuário um número
# inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo.
print('10)');
numero1 = int(input("Digite um numero: "));
if ((numero1 % 3) == 0 and (numero1 % 5) == 0):
    print("Resultado é: 0" );
else:
    print("Resultado não é: 0" );