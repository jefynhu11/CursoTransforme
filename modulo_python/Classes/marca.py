class Marca:

    def __init__(self):
        self.modelo = '';
        self.cor = '';

    def audi(self):
        self.modelo = 'A3';
        self.cor = 'preto';

    def fiat(self):
        self.modelo = 'uno';
        self.cor = 'azul';

    def ford(self):
        self.modelo = 'focus';
        self.cor = 'branco';

    def modelo(self):
        return self.modelo
    
    def cor(self):
        return self.cor