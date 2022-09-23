import tkinter as tk
import sqlite3


conexao = sqlite3.connect('Banco_Dados.db')

c = conexao.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS Cadastro_Motorista(
   Id INTEGER PRIMARY KEY AUTOINCREMENT,
   Nome text,
   Idade text,
   RG text,
   CPF text,
   Telefone text,
   CEP text,
   Rua text,
   Bairro text,
   Número text,
   Cidade text,
   Estado text,
   Registro_Habilitação text,
   Categoria_Habilitação text
    )
''')
conexao.commit()

conexao.close()


def cadastrar_motorista():
    conexao = sqlite3.connect('Banco-de-Dados.db')
    c = conexao.cursor()

    c.execute("INSERT INTO CadastroMotorista VALUES(:id,:nome,:idade,:rg,:cpf,:telefone,:cep,:rua,:bairro,:numero,:cidade,:estado,:registro,:categoria)",
              {
                 'id':None,
                 'nome':e_nomecompleto.get(),
                  'idade':e_idade.get(),
                  'rg':e_rg.get(),
                  'cpf':e_cpf.get(),
                  'telefone':e_telefone.get(),
                  'cep':e_cep.get(),
                  'rua':e_rua.get(),
                  'bairro':e_bairro.get(),
                  'numero':e_numero.get(),
                  'cidade':e_cidade.get(),
                  'estado':e_estado.get(),
                  'registro':e_registro.get(),
                  'categoria':e_categoria.get()

              }
              )
    conexao.commit()

    conexao.close()

    e_nomecompleto.delete(0,'end')
    e_idade.delete(0,'end')
    e_rg.delete(0,'end')
    e_cpf.delete(0,'end')
    e_telefone.delete(0,'end')
    e_cep.delete(0,'end')
    e_rua.delete(0,'end')
    e_bairro.delete(0,'end')
    e_numero.delete(0,'end')
    e_cidade.delete(0,'end')
    e_estado.delete(0,'end')
    e_registro.delete(0,'end')
    e_categoria.delete(0,'end')


janela = tk.Tk()
janela.title('Cadastro de Motoristas')

l_nomecompleto = tk.Label(janela,text='Nome Completo')
l_nomecompleto.grid(row=0,column=0,padx=10,pady=10)

l_idade = tk.Label(janela,text='Idade')
l_idade.grid(row=1,column=0,padx=10,pady=10)

l_rg = tk.Label(janela,text='RG')
l_rg.grid(row=2,column=0,padx=10,pady=10)

l_cpf = tk.Label(janela,text='CPF')
l_cpf.grid(row=3,column=0,padx=10,pady=10)

l_telefone = tk.Label(janela,text='Telefone')
l_telefone.grid(row=4,column=0,padx=10,pady=10)

l_cep = tk.Label(janela,text='CEP')
l_cep.grid(row=5,column=0,padx=10,pady=10)

l_rua = tk.Label(janela,text='Rua')
l_rua.grid(row=6,column=0,padx=10,pady=10)

l_bairro= tk.Label(janela,text='Bairro')
l_bairro.grid(row=7,column=0,padx=10,pady=10)

l_numero = tk.Label(janela,text='Número')
l_numero.grid(row=8,column=0,padx=10,pady=10)

l_cidade = tk.Label(janela,text='Cidade')
l_cidade.grid(row=9,column=0,padx=10,pady=10)

l_estado = tk.Label(janela,text='Estado')
l_estado.grid(row=10,column=0,padx=10,pady=10)

l_registro = tk.Label(janela,text='Registro Habilitação')
l_registro.grid(row=11,column=0,padx=10,pady=10)

l_categoria = tk.Label(janela,text='Categoria Habilitação')
l_categoria.grid(row=12,column=0,padx=10,pady=10)



#entrys



e_nomecompleto = tk.Entry(janela,text='Nome Completo',width=30)
e_nomecompleto.grid(row=0,column=1,padx=10,pady=10)

e_idade = tk.Entry(janela,text='Idade',width=30)
e_idade.grid(row=1,column=1,padx=10,pady=10)

e_rg = tk.Entry(janela,text='RG',width=30)
e_rg.grid(row=2,column=1,padx=10,pady=10)

e_cpf = tk.Entry(janela,text='CPF',width=30)
e_cpf.grid(row=3,column=1,padx=10,pady=10)

e_telefone = tk.Entry(janela,text='Telefone',width=30)
e_telefone.grid(row=4,column=1,padx=10,pady=10)

e_cep = tk.Entry(janela,text='CEP',width=30)
e_cep.grid(row=5,column=1,padx=10,pady=10)

e_rua = tk.Entry(janela,text='Rua',width=30)
e_rua.grid(row=6,column=1,padx=10,pady=10)

e_bairro= tk.Entry(janela,text='Bairro',width=30)
e_bairro.grid(row=7,column=1,padx=10,pady=10)

e_numero = tk.Entry(janela,text='Número',width=30)
e_numero.grid(row=8,column=1,padx=10,pady=10)

e_cidade = tk.Entry(janela,text='Cidade',width=30)
e_cidade.grid(row=9,column=1,padx=10,pady=10)

e_estado = tk.Entry(janela,text='Estado',width=30)
e_estado.grid(row=10,column=1,padx=10,pady=10)

e_registro = tk.Entry(janela,text='Registro Habilitação',width=30)
e_registro.grid(row=11,column=1,padx=10,pady=10)

e_categoria = tk.Entry(janela,text='Categoria Habilitação',width=30)
e_categoria.grid(row=12,column=1,padx=10,pady=10)

botao_cadastrar =tk.Button(janela,text='Cadastrar Motorista', command=cadastrar_motorista)
botao_cadastrar.grid(row=13,column=0,padx=10,pady=10,columnspan=2,ipadx=80)







janela.mainloop()