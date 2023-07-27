meuDicionario = {
    "nome" : "Jeferson",
    "Sobrenome" : "Eugenio",
    "Anos" : 30,
    "Time" : "Inter"
}

print(meuDicionario);

frutaDicionario = {
    'maça' : 3,
    'laranja' : 7,
    'acabaxi' : 5
}

print(frutaDicionario.get('laranja'));
frutaDicionario['limão'] = 10;
print(frutaDicionario);

aluno = {
    'nome' : 'Jeferson',
    'idade' : 30,
    'hobbies' : ['futebol','video game','computador']
}

print(aluno);

carro = {
    'marca' : 'Audi',
    'ano' : 30,
    'modelo' : {'ss', 'ti', 'a3'}
}

print(carro);

frutaDicionario2 = {
    'maça' : 3,
    'laranja' : 7,
    'acabaxi' : 5,
    'limao' : 10
}

print('chaves encontrar:', frutaDicionario2.keys());
print('valores encontrar:', frutaDicionario2.values());
print('obj encontrar:', frutaDicionario2.items());