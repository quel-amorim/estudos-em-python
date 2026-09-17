class Maestria:
    def __init__(self,nome,ponto_forte,ponto_fraco ,elemento):
        self.nome = nome
        self.ponto_forte = ponto_forte
        self.ponto_fraco = ponto_fraco
        self.elemento = elemento
        #dicionario atributos
        self.atributos = {
            'vit' : 10,
            'str' : 10,
            'res' : 10
        }

    def exibir_atributos(self):
        return f"VIT :{self.atributos['vit']} STR :{self.atributos['str']} RES :{self.atributos['res']}"


    def __repr__(self):
        return f"{self.nome} Elemento :{self.elemento}\nPONTO FORTE :{self.ponto_forte} | PONTO FRACO :{self.ponto_fraco}\n{self.exibir_atributos()}"

class Lutador(Maestria):
    def __init__(self):
        super().__init__('LUTADOR','FORCA FÍSICA' ,'RESISTENCIA','TERRA')
        self.atributos['vit'] -=1
        self.atributos['str'] +=5
        self.atributos['res'] -=3

class Mago(Maestria):
    def __init__(self):
        super().__init__('MAGO','MÁGIA','FORCA FÍSICA','RAIO')
        self.atributos['str'] -= 7
        self.atributos['res'] +=8

class Arqueiro(Maestria):
    def __init__(self):
        super().__init__('ARQUEIRO' , 'LONGAS DISTANCIAS' , 'RESISTENCIA','VENTO')
        self.atributos['str'] += 7
        self.atributos['res'] -= 5


classes = {
    'lutador' : Lutador(),
    'mago' : Mago(),
    'arqueiro' : Arqueiro()
}
