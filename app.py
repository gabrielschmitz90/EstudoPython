import mysql.connector
import pandas as pd

try:

    df = pd.read_excel('Pasta1.xlsx', engine='openpyxl')
    df.columns = df.columns.str.strip()
    
    print(f"Colunas detectadas: {df.columns.tolist()}")
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Schmitz100@',
        database='Vendas'
    )
    cursor = conexao.cursor()

    sql = "insert into vendedor (email, meta_vendas, salario, nome) values (%s, %s, %s, %s) on duplicate key update email=values(email), meta_vendas=values(meta_vendas), salario=values(salario)"

    vendedores_atualizados = 0

    for index, linha in df.iterrows():
        # Preparamos os valores garantindo que o nome não tenha espaços extras
        nome_planilha = str(linha['nome']).strip()
        
        valores = (
            linha['email'], 
            float(linha['meta_vendas']), 
            float(linha['salario']), 
            nome_planilha
        )
        
        cursor.execute(sql, valores)
        
        # Verificamos se o MySQL realmente encontrou essa linha
        if cursor.rowcount > 0:
            print(f"✅ {nome_planilha}: Dados atualizados.")
            vendedores_atualizados += 1
        else:
            print(f"⚠️ {nome_planilha}: Não encontrado no banco (verifique a grafia).")

    # 4. SALVAR as alterações (Sem isso, nada muda no banco!)
    conexao.commit()
    
    print("-" * 30)
    print(f"Fim do processo! Total de linhas alteradas: {vendedores_atualizados}")

except FileNotFoundError:
    print("❌ Erro: O arquivo 'Pasta1.xlsx' não foi encontrado.")
except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("🔌 Conexão encerrada.")