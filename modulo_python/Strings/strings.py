s = "banana";
ss = 'banana';

print("primeiro variavel: ", s, id(s));

print("segundo variavel: ", ss);

s = s.replace("b", "z");

print("Substituir: ", s);

print("Primeira letra: " , s[0]);
print("Ultimo letra: " , s[-1]);

nome = input("Nome: ");
print(nome);

# Inserindo as variaveis no print com f
print(f"Bem vindo,", nome);
print("Bem vindo {}".format(nome));
print(f"Bem vindo {7*3}");

#Inserindo as variáveis no print com f
sobreNome = input("Sobrenome: ")
print(f"Bem-vindo, {nome} {sobreNome}");
print("Bem-vindo {} {}".format(nome, sobreNome))

#Concatenando strings
frase = "Olá, Mundo!"
print("Concatenando strings: ")
outraFrase = "Bem-vindo "
fraseCompleta = frase + ' ' + outraFrase;
print(fraseCompleta);
print()

#Tamanho da string
tamanho = len(frase);
print("Tamanho: ", tamanho);
print();

#Divindo uma string em sub strings
print("Divindo a string: ");
palavras = fraseCompleta.split();
print(palavras);

# Substituindo partes das string
print("Substituindo partes das strings: ");
novaFrase = frase.replace("mundo", "Python");
print(novaFrase);

#Convertendo para letras maiúsculas e minúsculas
print("Convertendo para letras maiúsculas e minúsculas:");
print("Maiúsculas: ", frase.upper());
print("Minúsculas: ", frase.lower());