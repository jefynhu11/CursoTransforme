tuplaNumeros = (1,2,3,4,5);
tuplaLetras = ('I', 'N', 'T', 'E', 'R');
tuplaMistos = (1, 'python', True);
set = {1,2,3,4,5};
lista = [1,2,3,4,5,6,7,8];
print(tuplaNumeros);
print(tuplaLetras);
print(tuplaMistos);
print("Variavel 'tuplaNumeros' para ver qual é tipo: ", type(tuplaNumeros));
print("Variavel 'set' para ver qual é tipo: ", type(set));
print("Variavel 'lista' para ver qual é tipo: ", type(lista));

# Acessando itens individualmente em tuplas
# print(tupla2[1]);
# tupla2[1] = "J";

# Fatiamento de itens na tupla
print(tuplaNumeros[1:4]);

# Concatenando tupla
tuplasNumero1 = 1,2,3;
tuplasNumero2 = 4,5,6;
tuplasConcatenado = tuplasNumero1 + tuplasNumero2;
print("Concatenando tuplas: ", tuplasConcatenado);

# Criando variaveis novas com os valores de uma tupla
a, b, c = tuplasNumero2;
print("Valores das variaveis: ");
print(a);
print(b);
print(c);
