class Emprestimo_has_itemDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, emprestimo_has_item):
        try:
            sql = "INSERT INTO Emprestimo_has_item(Emprestimo_codigo, Item_codigo) " \
                  "VALUES (%s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (emprestimo_has_item.emprestimo,
                                 emprestimo_has_item.item))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0