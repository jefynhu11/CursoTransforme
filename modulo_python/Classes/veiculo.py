from marca import Marca

class Veiculo(Marca):
    def __init__(self, portas, rodas=4):
        self.portas = portas;
        self.rodas = rodas;
        self.modelo = Marca.modelo;
        self.cor = Marca.cor;

    def info(self):
        informacao = f"""
        =====================
        Portas: {self.portas}
        Rodas: {self.rodas}
        Modelo: {self.modelo}
        Cor: {self.cor}
        =====================
        """;
        print(informacao);