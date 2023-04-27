class UsuarioDAO():
    def __init__(self, con):
        self.con = con


    def inserir(self, usuario):
        try:
            sql = "INSERT INTO Usuario(matricula, senha, nome, email, tipo) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (usuario.matricula, usuario.senha, usuario.nome, usuario.email, usuario.tipo))
            self.con.commit()
            return 1
        except:
            return 0


    def autenticar(self, matricula, senha):
        try:
            sql = "SELECT * FROM Usuario WHERE matricula=%s AND senha=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (matricula, senha))

            usuario = cursor.fetchone()  # lastrowid, fetchone, fetchall
            return usuario

        except:
            return None


    def listar(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome != None:
                sql = "SELECT * FROM Usuario WHERE nome=%s"
                cursor.execute(sql, (nome, ))
                usuario = cursor.fetchone()
                return usuario
            else:
                sql = "SELECT * FROM Usuario"
                cursor.execute(sql)
                usuarios = cursor.fetchall()
                return usuarios
        except:
            return None


    def excluir(self, matricula):
        try:
            sql = "DELETE FROM Usuario WHERE matricula = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (matricula,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0