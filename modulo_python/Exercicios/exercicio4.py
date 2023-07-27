print("1-Utilizando um loop 'while', imprima os números de 1 a 10.")
quantidade = 1
while quantidade <= 10:
  print(quantidade);
  quantidade += 1;
print("===================");
print("2- Utilizando um loop 'for', imprima os números de 1 a 10.")
for quantidade in range(1, 11):
  print(quantidade);
print("===================");
print("3- Utilizando um loop 'while', calcule a soma dos números de 1 a 100.")
contador = 1;
calculeSoma = 0;
while contador != 101:
    calculeSoma = calculeSoma + contador;
    contador += 1;
print("Resultado soma: ", calculeSoma);
print("===================");
print("4- Utilizando um loop 'for', calcule a soma dos números de 1 a 100.")
calculeSoma = 0;
for soma in range(1,101):
    calculeSoma += soma;
print("SOMA:", calculeSoma);
print("===================");
print("5- Utilizando um loop 'while', imprima os números pares de 1 a 20.")
contador = 1;
while contador < 21:
    if contador % 2 == 0 :
        print(contador);
    contador += 1;
print("===================");
print("6- Utilizando um loop 'for', imprima os números pares de 1 a 20.")
for numero in range(1,21):
    if numero % 2 == 0 :
        print(numero);
print("===================");
print("7- Utilizando um loop 'while', inverta uma string digitada pelo usuário.")
string = input("Digite uma string: ")
indice = len(string) - 1
string_invertida = ""
while indice >= 0:
    string_invertida += string[indice]
    indice -= 1
print("A string invertida é:", string_invertida)
print("===================");
print("8- Utilizando um loop 'for', verifique se uma palavra digitada pelo usuário é um palíndromo (lê-se da mesma forma de trás para frente)")
palavra = input("Digite uma palavra: ")
palavra_invertida = ""
for letra in palavra:
    palavra_invertida = letra + palavra_invertida
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
print("===================");
print("9- Utilizando um loop 'while', encontre o menor número inteiro cujo quadrado seja maior do que 1000.")
numero = 1
while numero ** 2 <= 1000:
    numero += 1
print("O menor número inteiro cujo quadrado é maior que 1000 é:", numero)
print("===================");
print("10- Utilizando um loop 'for', imprima os elementos de uma lista em ordem inversa.")
lista = [1, 2, 3, 4, 5]
for indice in range(len(lista)-1, -1, -1):
    print(lista[indice])
print("===================");