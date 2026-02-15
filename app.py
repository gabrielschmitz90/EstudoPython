import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Schmitz100@',
    database='Vendas'
)

cursor = conexao.cursor()


sql = 'update vendedor set nome = %s where id_vendedor = %s'

valores = ('gabriel schmitz', 1)

cursor.execute(sql, valores)

conexao.commit()

print(f'{cursor.rowcount} registro(s) atualizado(s)')