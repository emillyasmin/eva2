class Material():
    def __init__(self, nome, tipo):
        self.codigo = 0
        self.nome = nome
        self.tipo = tipo


    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo
