import sqlite3
import tkinter as tk




banco = sqlite3.connect("Banco-de-Dados.db")
c = banco.cursor()

c.execute("CREATE TABLE IF NOT EXISTS troca_do_óleo("
          "Veículo text,"
          "placa text,"
          "Total_KM_Rodado pelo Veículo numeric,"
          "Macar_Modelo do óleo text,"
          "KM_Cadastrado_da_Última_Troca numeric,"
          "Troca_de_Óleo_em_quantos_KM numeric,"
          "Rodagem_do_Óleo numeric,"
          "Feedback_da_Troca_de_Óleo text)")
banco.commit()

banco.close()





def controle_oleo():
    banco = sqlite3.connect("Banco-de-Dados.db")
    c = banco.cursor()

    c.execute("INSERT INTO troca_do_óleo VALUES(:Veículo,:Placa,:KMrodado,:Modelo,:ÚltimaTroca,:TrocaDeÓleo,:RodagemÓleo,:Feedback)",
              {

                  'Veículo':e_veiculo.get(),
                  'Placa':e_placa.get(),
                  'KMrodado':e_KMrodado.get(),
                  'Modelo':e_Modelo.get(),
                  'ÚltimaTroca':e_ÚltimaTroca.get(),
                  'TrocaDeÓleo':e_TrocaDeÓleo.get(),
                  'RodagemÓleo':e_RodagemÓleo.get(),
                  'Feedback':e_Feedback.get()

              }
              )


    banco.commit()

    banco.close()

    e_veiculo.delete(0,'end')
    e_placa.delete(0,'end')
    e_KMrodado.delete(0,'end')
    e_Modelo.delete(0,'end')
    e_ÚltimaTroca.delete(0,'end')
    e_TrocaDeÓleo.delete(0,'end')
    e_RodagemÓleo.delete(0,'end')
    e_Feedback.delete(0,'end')


janela = tk.Tk()
janela.title("Controle do Óleo")


l_veiculo = tk.Label(janela,text='Veículo')
l_veiculo.grid(row=0,column=0,padx=10,pady=10)

l_placa = tk.Label(janela,text='Placa')
l_placa.grid(row=1,column=0,padx=10,pady=10)

l_KMrodado = tk.Label(janela,text='Total KM rodado')
l_KMrodado.grid(row=2,column=0,padx=10,pady=10)

l_Modelo = tk.Label(janela,text='Marca/Modelo')
l_Modelo.grid(row=3,column=0,padx=10,pady=10)

l_ÚltimaTroca = tk.Label(janela,text='KM Da última troca')
l_ÚltimaTroca.grid(row=4,column=0,padx=10,pady=10)

l_TrocaDeÓleo= tk.Label(janela,text='Troca em quantos KM')
l_TrocaDeÓleo.grid(row=5,column=0,padx=10,pady=10)

l_RodagemÓleo = tk.Label(janela,text='Rodagem do óleo')
l_RodagemÓleo.grid(row=6,column=0,padx=10,pady=10)

l_Feedback = tk.Label(janela,text='Feedback da troca de óleo')
l_Feedback.grid(row=7,column=0,padx=10,pady=10)



e_veiculo = tk.Entry(janela,text='Veículo',width=30)
e_veiculo.grid(row=0,column=1,padx=10,pady=10)

e_placa = tk.Entry(janela,text='Placa',width=30)
e_placa.grid(row=1,column=1,padx=10,pady=10)

e_KMrodado = tk.Entry(janela,text='Total KM rodado',width=30)
e_KMrodado.grid(row=2,column=1,padx=10,pady=10)

e_Modelo = tk.Entry(janela,text='Marca/Modelo',width=30)
e_Modelo.grid(row=3,column=1,padx=10,pady=10)

e_ÚltimaTroca = tk.Entry(janela,text='KM Da última troca',width=30)
e_ÚltimaTroca.grid(row=4,column=1,padx=10,pady=10)

e_TrocaDeÓleo= tk.Entry(janela,text='Troca em quantos KM',width=30)
e_TrocaDeÓleo.grid(row=5,column=1,padx=10,pady=10)

e_RodagemÓleo = tk.Entry(janela,text='Rodagem do óleo',width=30)
e_RodagemÓleo.grid(row=6,column=1,padx=10,pady=10)

e_Feedback = tk.Entry(janela,text='Feedback da troca de óleo',width=30)
e_Feedback.grid(row=7,column=1,padx=10,pady=10)


botao_cadastrar = tk.Button(janela,text='Cadastrar Troca de Óleo',command=controle_oleo)
botao_cadastrar.grid(row=8,column=0,padx=10,pady=10,columnspan=2,ipadx=80)




janela.mainloop()