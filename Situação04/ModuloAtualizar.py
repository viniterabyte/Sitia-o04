from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def atualizarCadastro(id, tipo, desc, val,cate, data):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tb_producao
            SET tipo_mov='{tipo}', descrisao='{desc}',
            valor='{val}', categoria='{cate}', data_mov='{data}' WHERE id_fin='{id}'
              """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()

