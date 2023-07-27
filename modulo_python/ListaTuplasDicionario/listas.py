listaNumero = [1,2,3,4,5];
print(listaNumero);
listaString = ["a","b","c"];
print(listaString);
listaMisto = [1,"a",3.14,True];
print(listaMisto);

print("=============");

frutas = ["banana", "morango"]
print(frutas);
print(frutas[1]);
frutas[1] = "Laranja";

print("Tamanho 1: ", len(frutas));

frutas.append("Maça");
print(frutas);

print("Tamanho 2: ", len(frutas));

print("=============");

listaNova = [1, ["a", "b"]];
print(listaNova[1][0]);

print("=============");

lista1 = [1,2,3];
lista2 = [4,5,6];
listaConcatenada = lista1 + lista2;
print(listaConcatenada);

print("=============");

listaRepetida = [3] * 3;
print(listaRepetida);

print("=============");

letras = ["a", "b", "c", "d"];
sublista = letras[1:4];
print(sublista);

print("=============");

marca = ["FIAT", "FORD", "AUDI"];
marca.append("GM");
print(marca);
marca.insert(1, "TESTE");
print(marca);
marcaRemover = marca.remove("TESTE");
print("marca: ", marca);
print("marca remover: ", marcaRemover);
marcaRemover = marca.pop(2);
print(marcaRemover);

print("=============");
cores = ["marrom", "roxo", "amarelo", "azul", "branco", "vermelho"];
print("Cores: ", cores);
cores.sort();
print("Ordem: ", cores);

print("=============");
from random import shuffle
shuffle(cores);
print("Embaralhado: ", cores);