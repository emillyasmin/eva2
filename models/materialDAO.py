class MaterialDAO():
    def __init__(self, con):
        self.con = con


    def inserir(self, material):
        try:
            sql = "INSERT INTO Material(nome, tipo) VALUES (%s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (material.nome, material.tipo))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0


    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                sql = "SELECT * FROM Material WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                material = cursor.fetchone()
                return material
            else:
                sql = "SELECT * FROM Material"
                cursor.execute(sql)
                materiais = cursor.fetchall()
                return materiais
        except:
            return None


    def atualizar(self, material):
        try:
            sql = "UPDATE Material " \
                  "SET nome=%s, tipo=%s " \
                  "WHERE codigo=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (material.nome, material.tipo, material.codigo))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0


    def excluir(self, codigo):
        try:
            sql = "DELETE FROM Material WHERE codigo = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (codigo,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0