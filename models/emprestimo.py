class Emprestimo:
    def __init__(self, tipo, dt_emp, usuario, dt_devolucao, status):
        self.codigo = None
        self.tipo = tipo
        self.dt_emp = dt_emp
        self.usuario = usuario
        self.dt_devolucao = dt_devolucao
        self.status =status


    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo