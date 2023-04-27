class Emprestimo:
    def __init__(self, tipo, dt_emp, usuario, dt_devolucao=""):
        self.codigo = None
        self.tipo = tipo
        self.dt_emp = dt_emp
        self.usuario = usuario
        self.dt_devolucao = dt_devolucao


    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo