import sqlite3
import tkinter as tk

banco = sqlite3.connect("Banco-de-Dados.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS manutenção("
               "Dia text,"
               "Mês text,"
               "Veículo text,"
               "Tipo_de_Manutenção text,"
               "Manutenção text,"
               "Causa text,"
               "Valor text)")
banco.commit()

banco.close()


def cadastrar_manutenção():
    banco = sqlite3.connect("Banco-de-Dados.db")
    cursor = banco.cursor()

    cursor.execute("INSERT INTO manutenção VALUES(:Dia,:Mês,:Veículo,:TipoManutenção,:Manutenção,:Causa,:Valor)",
                   {
                       'Dia':e_dia.get(),
                       'Mês':e_mes.get(),
                       'Veículo':e_veiculo.get(),
                       'TipoManutenção':e_TipoManutenção.get(),
                       'Manutenção':e_Manutenção.get(),
                       'Causa':e_causa.get(),
                       'Valor':e_valor.get()
                   }
                   )





    banco.commit()

    banco.close()

    e_dia.delete(0,'end')
    e_mes.delete(0,'end')
    e_veiculo.delete(0,'end')
    e_TipoManutenção.delete(0,'end')
    e_Manutenção.delete(0,'end')
    e_causa.delete(0,'end')
    e_valor.delete(0,'end')



janela = tk.Tk()
janela.title("cadastro Manutenção")

l_dia= tk.Label(janela,text='Dia')
l_dia.grid(row=0,column=0,padx=10,pady=10)

l_mes = tk.Label(janela,text='Mês')
l_mes.grid(row=1,column=0,padx=10,pady=10)

l_veiculo = tk.Label(janela,text='Veículo')
l_veiculo.grid(row=2,column=0,padx=10,pady=10)

l_TipoManutenção = tk.Label(janela,text='Tipo de Manutenção')
l_TipoManutenção.grid(row=3,column=0,padx=10,pady=10)

l_Manutenção= tk.Label(janela,text='Manutenção')
l_Manutenção.grid(row=4,column=0,padx=10,pady=10)

l_causa = tk.Label(janela,text='Causa')
l_causa.grid(row=5,column=0,padx=10,pady=10)

l_valor = tk.Label(janela,text='Valor')
l_valor.grid(row=6,column=0,padx=10,pady=10)


e_dia= tk.Entry(janela,text='Dia',width=30)
e_dia.grid(row=0,column=1,padx=10,pady=10)

e_mes = tk.Entry(janela,text='Mês',width=30)
e_mes.grid(row=1,column=1,padx=10,pady=10)

e_veiculo = tk.Entry(janela,text='Veículo',width=30)
e_veiculo.grid(row=2,column=1,padx=10,pady=10)

e_TipoManutenção = tk.Entry(janela,text='Tipo de Manutenção',width=30)
e_TipoManutenção.grid(row=3,column=1,padx=10,pady=10)

e_Manutenção= tk.Entry(janela,text='Manutenção',width=30)
e_Manutenção.grid(row=4,column=1,padx=10,pady=10)

e_causa = tk.Entry(janela,text='Causa',width=30)
e_causa.grid(row=5,column=1,padx=10,pady=10)

e_valor = tk.Entry(janela,text='Valor',width=30)
e_valor.grid(row=6,column=1,padx=10,pady=10)


botao_cadastrar =tk.Button(janela,text='Cadastrar Manutenção',command=cadastrar_manutenção)
botao_cadastrar.grid(row=7,column=0,padx=10,pady=10,columnspan=2,ipadx=80)

janela.mainloop()