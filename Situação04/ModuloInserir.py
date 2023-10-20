from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def inserir(tipo, desc, val, cate, data):
    conexao, cursor = conectar()
    try:
        sql = f"""INSERT INTO tb_financas
                (tipo_mov, descriçao, valor, categoria, data_mov)
                VALUES
                ('{tipo}','{desc}','{val}', '{cate}','{data}')
                """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()

