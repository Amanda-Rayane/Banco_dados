import sqlite3
import tkinter as tk


banco = sqlite3.connect("Banco-de-Dados.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS veículo("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "Placa text,"
               "Marca text,"
               "Cor text,"
               "Ano_do_Veículo text,"
               "Vencimento_do_Documento text)")

banco.commit()

banco.close()



def cadastrar_veiculo():
    banco = sqlite3.connect("Banco-de-Dados.db")
    cursor = banco.cursor()

    cursor.execute("INSERT INTO veículo VALUES(:id,:placa,:marca,:cor,:AnoVeiculo,:vencimento)",
                   {
                       'id':None,
                       'placa':e_placa.get(),
                       'marca':e_marca.get(),
                       'cor':e_cor.get(),
                       'AnoVeiculo':e_AnoVeiculo.get(),
                       'vencimento':e_vencimento.get()

                   }
                   )
    banco.commit()

    banco.close()

    e_placa.delete(0,'end')
    e_marca.delete(0, 'end')
    e_cor.delete(0, 'end')
    e_AnoVeiculo.delete(0, 'end')
    e_vencimento.delete(0, 'end')


janela = tk.Tk()
janela.title("Cadastro do Veículo")

l_placa= tk.Label(janela,text='Placa')
l_placa.grid(row=0,column=0,padx=10,pady=10)

l_marca= tk.Label(janela,text='Marca')
l_marca.grid(row=1,column=0,padx=10,pady=10)

l_cor= tk.Label(janela,text='Cor')
l_cor.grid(row=2,column=0,padx=10,pady=10)

l_AnoVeiculo= tk.Label(janela,text='Ano do Veículo')
l_AnoVeiculo.grid(row=3,column=0,padx=10,pady=10)

l_vencimento= tk.Label(janela,text='Vencimento do Documento')
l_vencimento.grid(row=4,column=0,padx=10,pady=10)




e_placa= tk.Entry(janela,text='Placa',width=30)
e_placa.grid(row=0,column=1,padx=10,pady=10)

e_marca= tk.Entry(janela,text='Marca',width=30)
e_marca.grid(row=1,column=1,padx=10,pady=10)

e_cor= tk.Entry(janela,text='Cor', width=30)
e_cor.grid(row=2,column=1,padx=10,pady=10)

e_AnoVeiculo= tk.Entry(janela,text='Ano do Veículo',width=30)
e_AnoVeiculo.grid(row=3,column=1,padx=10,pady=10)

e_vencimento= tk.Entry(janela,text='Vencimento do Documento', width=30)
e_vencimento.grid(row=4,column=1,padx=10,pady=10)


botão_cadastrar=tk.Button(janela,text= 'Cadastrar Veículo',command=cadastrar_veiculo)
botão_cadastrar.grid(row=6,column=0,padx=10,pady=10,columnspan=2,ipadx=80)


janela.mainloop()