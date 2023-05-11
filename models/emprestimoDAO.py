class EmprestimoDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, emprestimo):
        try:
            sql = "INSERT INTO Emprestimo(tipo, dt_emp, dt_devolucao, Usuario_matricula) " \
                  "VALUES (%s, %s, %s, %s)"

            cursor = self.con.cursor()
            print(sql)
            cursor.execute(sql, (emprestimo.tipo,
                                 emprestimo.dt_emp,
                                 emprestimo.dt_devolucao,
                                 emprestimo.usuario))
            print(cursor)
            self.con.commit()
            codigo = cursor.lastrowid
            print(codigo)
            return codigo
        except:
            return 0


    def excluir(self, codigo):
        try:
            sql = "DELETE FROM Emprestimo WHERE codigo = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (codigo,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0


    def excluirItens(self, codigo):
        try:
            sql = "DELETE FROM Emprestimo_has_item WHERE Emprestimo_codigo = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (codigo,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0


    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None and codigo == str(codigo):
                data = codigo
                sql ="SELECT e.codigo, e.tipo, e.dt_emp, e.dt_devolucao, u.nome, u.matricula" \
                     " FROM Emprestimo as e, Usuario as u" \
                     " WHERE e.Usuario_matricula = u.matricula AND" \
                     "      e.dt_emp = %s"
                cursor.execute(sql, (data, ))
                emprestimos = cursor.fetchall()
                return emprestimos

            elif codigo != None:
                sql ="SELECT e.codigo, e.tipo, e.dt_emp, e.dt_devolucao, u.nome, u.matricula" \
                     " FROM Emprestimo as e, Usuario as u" \
                     " WHERE e.Usuario_matricula = u.matricula AND" \
                     "      e.codigo = %s"
                cursor.execute(sql, (codigo, ))
                emprestimo = cursor.fetchone()
                return emprestimo

            else:
                sql = "SELECT * FROM Emprestimo as e, Usuario as u" \
                          " WHERE e.Usuario_matricula = u.matricula"
                cursor.execute(sql)
                emprestimos = cursor.fetchall()
                return emprestimos

        except:
            return None


    def devolver(self, codigo, data):
        try:
            sql = "UPDATE Emprestimo " \
                  "SET dt_devolucao=%s " \
                  "WHERE codigo=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (data, codigo))
            self.con.commit()
            print(cursor.rowcount)
            return cursor.rowcount
        except:
            return 0