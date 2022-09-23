import sqlite3
import tkinter as tk

conexao = sqlite3.connect("Banco-de-Dados.db")

c = conexao.cursor()


c.execute("CREATE TABLE Troca_do_Pneu ("
          "Veículo text,"
          "Placa text,"
          "Total_KM_Rodado pelo Veículo numeric,"
          "KM_Cadastrado_da_último_troca numeric,"
          "Troca_de_pneu_em_quantos_KM numeric,"
          "Rodagem_do_Pneu numeric,"
          "Feedback_do_Pneu text)")
conexao.commit()

conexao.close()

def cadastro_pneu():
    conexao = sqlite3.connect("Banco-de-Dados.db")
    c = conexao.cursor()

    c.execute("INSERT INTO Troca_do_Pneu VALUES(:Veículo,:Placa,:TotalRodado,:ÚltimaTroca,:TrocaPneu,:Rodagem,:Feedback)",
              {
                  'Veículo':e_veiculo.get(),
                  'Placa':e_veiculo.get(),
                  'TotalRodado':e_TotalRodado.get(),
                  'ÚltimaTroca':e_ÚltimaTroca.get(),
                  'TrocaPneu':e_TrocaPneu.get(),
                  'Rodagem':e_Rodagem.get(),
                  'Feedback':e_Feedback.get()

              }


              )
    conexao.commit()

    conexao.close()

    e_veiculo.delete(0,'end')
    e_Placa.delete(0,'end')
    e_TotalRodado.delete(0,'end')
    e_ÚltimaTroca.delete(0,'end')
    e_TrocaPneu.delete(0,'end')
    e_Rodagem.delete(0,'end')
    e_Feedback.delete(0,'end')

janela = tk.Tk()
janela.title('Troca do Pneu')

l_veiculo = tk.Label(janela,text='Veículo')
l_veiculo.grid(row=0,column=0,padx=10,pady=10)

l_Placa = tk.Label(janela,text='Placa')
l_Placa.grid(row=1,column=0,padx=10,pady=10)

l_TotalRodado = tk.Label(janela,text='Total KM Rodado Pelo Veículo')
l_TotalRodado.grid(row=2,column=0,padx=10,pady=10)

l_ÚltimaTroca = tk.Label(janela,text='KM Cadastrado do Último Pneu')
l_ÚltimaTroca.grid(row=3,column=0,padx=10,pady=10)

l_TrocaPneu = tk.Label(janela,text='Troca de Pneu em quantos KM')
l_TrocaPneu.grid(row=4,column=0,padx=10,pady=10)

l_Rodagem = tk.Label(janela,text='Rodagem do Pneu')
l_Rodagem.grid(row=5,column=0,padx=10,pady=10)

l_Feedback = tk.Label(janela,text='Feedback do Pneu')
l_Feedback.grid(row=6,column=0,padx=10,pady=10)



e_veiculo = tk.Entry(janela,text='Veículo',width=30)
e_veiculo.grid(row=0,column=1,padx=10,pady=10)

e_Placa = tk.Entry(janela,text='Placa',width=30)
e_Placa.grid(row=1,column=1,padx=10,pady=10)

e_TotalRodado = tk.Entry(janela,text='Total KM Rodado Pelo Veículo',width=30)
e_TotalRodado.grid(row=2,column=1,padx=10,pady=10)

e_ÚltimaTroca = tk.Entry(janela,text='KM Cadastro da Última troca',width=30)
e_ÚltimaTroca.grid(row=3,column=1,padx=10,pady=10)

e_TrocaPneu = tk.Entry(janela,text='Troca de Pneu em Quantos KM ',width=30)
e_TrocaPneu.grid(row=4,column=1,padx=10,pady=10)

e_Rodagem = tk.Entry(janela,text='Rodagem do Pneu',width=30)
e_Rodagem.grid(row=5,column=1,padx=10,pady=10)

e_Feedback = tk.Entry(janela,text='Feedback do Pneu',width=30)
e_Feedback.grid(row=6,column=1,padx=10,pady=10)

botao_cadastrar =tk.Button(janela,text='Cadastrar Troca do Pneu',command=cadastro_pneu)
botao_cadastrar.grid(row=7,column=0,padx=10,pady=10,columnspan=2,ipadx=80)



janela.mainloop()