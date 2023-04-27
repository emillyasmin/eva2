class ItemDAO():
    def __init__(self, con):
        self.con = con


    def inserir(self, item):
        try:
            sql = "INSERT INTO Item(disponibilidade, Material_codigo, observacao, localizacao) " \
                  "VALUES (%s, %s, %s, %s) "
            cursor = self.con.cursor()
            cursor.execute(sql, (item.disponibilidade, item.material, item.observacao, item.localizacao))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0


    def adicionar_item(self, item):
        try:
            sql = "UPDATE Item " \
                  "SET Emprestimo_codigo=%s " \
                  "WHERE codigo=%s AND" \
                  "     Emprestimo_codigo is null"

            cursor = self.con.cursor()
            cursor.execute(sql, (item.emprestimo, item.item))
            self.con.commit()
            return 1
        except:
            return 0


    def verificar_item(self, item):
        try:
            sql = "SELECT * FROM Item " \
                  "WHERE codigo = %s AND " \
                  "     Emprestimo_codigo is not null"
            cursor = self.con.cursor()
            print(item)
            cursor.execute(sql, (item,))
            print(cursor)
            item = cursor.fetchone()  # lastrowid, fetchone, fetchall
            return item
        except:
            return None


    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None and codigo == str(codigo):
                sql ="SELECT * FROM Item as i, Material as m " \
                     "WHERE i.Material_codigo = m.codigo AND" \
                     "      m.nome = %s"
                cursor.execute(sql, (codigo, ))
                item = cursor.fetchall()
                print(item)
                return item

            elif codigo != None and codigo == int(codigo):
                sql = "SELECT * FROM Item as i, Material as m " \
                      "WHERE i.Material_codigo = m.codigo AND" \
                      "      i.codigo = %s"
                cursor.execute(sql, (codigo,))
                item = cursor.fetchone()
                print(item)
                return item


            else:
                sql = "SELECT * FROM Item as i, Material as m " \
                      "WHERE i.Material_codigo = m.codigo"
                cursor.execute(sql)
                itens = cursor.fetchall()
                return itens

        except:
            return None


    def listar_itens(self, codigo):
        try:
            sql = "SELECT * FROM Item as i, Material as m, Emprestimo as e " \
                  "WHERE i.Material_codigo = m.codigo AND" \
                  "     i.Emprestimo_codigo = e.codigo AND" \
                  "     i.Emprestimo_codigo= %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (codigo, ))
            itens = cursor.fetchall()
            return itens

        except:
            return None


    def excluir(self, codigo=None, material=None):
        try:
            if material == None:
                sql = "DELETE FROM Item WHERE codigo = %s"
                cursor = self.con.cursor()
                cursor.execute(sql, (codigo,))
                self.con.commit()
                return cursor.rowcount
            else:
                sql = "DELETE FROM Item " \
                      "WHERE Material_codigo=%s"
                cursor = self.con.cursor()
                cursor.execute(sql, (material, ))
                self.con.commit()
                return cursor.rowcount
        except:
            return 0


    def atualizar(self, item):
        try:
            sql = "UPDATE Item " \
                  "SET disponibilidade=%s, observacao=%s, Material_codigo=%s, localizacao=%s " \
                  "WHERE codigo=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (item.disponibilidade, item.observacao, item.material, item.localizacao, item.codigo))
            self.con.commit()
            print(cursor.rowcount)
            return cursor.rowcount
        except:
            return 0


    def devolver(self, codigo):
        try:
            sql = "UPDATE Item " \
                  "SET Emprestimo_codigo= null " \
                  "WHERE Emprestimo_codigo=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (codigo, ))
            self.con.commit()
            print(cursor.rowcount)
            return cursor.rowcount
        except:
            return 0
