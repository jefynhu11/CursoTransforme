from veiculo import Veiculo
loop = True;
veiculo = Veiculo(portas=4);
veiculo.audi();
veiculo.fiat();

while loop:
    menu = """
    Marca dos veiculos
    -----------
    [1] = AUDI
    [2] = FIAT
    [3] = FORD
    [4] = SAIR
    -----------
    """;
    print(menu);
    opcao = int(input("Escolhe um opção: "))
    if opcao == 1:
        veiculo.audi();
        veiculo.info();
    elif opcao == 2:
        veiculo.fiat();
        veiculo.info();
    elif opcao == 3:
        veiculo.ford();
        veiculo.info();
    elif opcao == 4:
        loop = False;
        print("=====================")
        print("Saindo o programa...");
        print("=====================")
    else:
        print("=====================")
        print("Invalido!");
        print("=====================")
