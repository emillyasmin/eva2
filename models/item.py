class Item():
    def __init__(self, disponibilidade, material, observacao='', localizacao= '', emprestimo=''):
        self.codigo = None
        self.disponibilidade = disponibilidade
        self.material = material
        self.emprestimo = emprestimo
        self.observacao = observacao
        self.localizacao = localizacao


    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo
