import sqlite3
import tkinter as tk

banco = sqlite3.connect('Banco-de-Dados.db')
c = banco.cursor()

c.execute('CREATE TABLE Controle_de_Viagem('
          'CPF_Motorista text,'
          'Placa_Veículo text,'
          'Posto text,'
          'Combustível text,'
          'Valor_Unitário text,'
          'Quantidade_em_Litro text,'
          'Total_pago real,'
          'Saída text,'
          'Destino text,'
          'KM_Inicial_do_Veículo text,'
          'KM_da_Viagem text,'
          'KM_Final text,'
          'Pedágio text,'
          'Alimentação text,'
          'Hospedagem text,'
          'Pago_Total text)')

banco.commit()

banco.close()



def cadastrar_rodagem():
    banco = sqlite3.connect('Banco-de-Dados.db')
    c = banco.cursor()

    c.execute("INSERT INTO Controle_de_Viagem VALUES(:cpf,:placa,:posto,:combustivel,:valor_unitario,:quantidade,"
              ":total_pago,:saida,:destino,:kminicial,:kmviagem,:kmfinal,:pedagio,:alimentacao,:hospedagem,:pago_total)",
              {
                  'cpf':e_cpf.get(),
                  'placa':e_placa.get(),
                  'posto':e_posto.get(),
                  'combustivel':e_combustivel.get(),
                  'valor_unitario':e_valor_unitario.get(),
                  'quantidade':e_quantidade.get(),
                  'total_pago':e_total_pago.get(),
                  'saida':e_saida.get(),
                  'destino':e_destino.get(),
                  'kminicial':e_kminicial.get(),
                  'kmviagem':e_kmviagem.get(),
                  'kmfinal':e_kmfinal.get(),
                  'pedagio':e_pedagio.get(),
                  'alimentacao':e_alimentacao.get(),
                  'hospedagem':e_hospedagem.get(),
                  'pago_total':e_pago_total.get()
              }

              )
    banco.commit()

    banco.close()

    e_cpf.delete(0,'end')
    e_placa.delete(0,'end')
    e_posto.delete(0,'end')
    e_combustivel.delete(0,'end')
    e_valor_unitario.delete(0,'end')
    e_quantidade.delete(0,'end')
    e_total_pago.delete(0,'end')
    e_saida.delete(0,'end')
    e_destino.delete(0,'end')
    e_kminicial.delete(0,'end')
    e_kmviagem.delete(0,'end')
    e_kmfinal.delete(0,'end')
    e_pedagio.delete(0,'end')
    e_alimentacao.delete(0,'end')
    e_hospedagem.delete(0,'end')
    e_pago_total.delete(0,'end')




janela = tk.Tk()
janela.title("Cadastrar Rodagem")

l_cpf = tk.Label(janela,text='CPF Motorista')
l_cpf.grid(row=0,column=0,padx=10,pady=10)

l_placa= tk.Label(janela,text='Placa')
l_placa.grid(row=1,column=0,padx=10,pady=10)

l_posto = tk.Label(janela,text='Posto')
l_posto.grid(row=2,column=0,padx=10,pady=10)

l_combustivel = tk.Label(janela,text='Combustível')
l_combustivel.grid(row=3,column=0,padx=10,pady=10)

l_valor_unitario= tk.Label(janela,text='Valor Unitário')
l_valor_unitario.grid(row=4,column=0,padx=10,pady=10)

l_quantidade = tk.Label(janela,text='Quantidade em Litro')
l_quantidade.grid(row=5,column=0,padx=10,pady=10)

l_total_pago = tk.Label(janela,text='Total Pago')
l_total_pago.grid(row=6,column=0,padx=10,pady=10)

l_saida = tk.Label(janela,text='Saída')
l_saida.grid(row=7,column=0,padx=10,pady=10)

l_destino = tk.Label(janela,text='Destino')
l_destino.grid(row=8,column=0,padx=10,pady=10)

l_kminicial = tk.Label(janela,text='KM Inicial do Veículo')
l_kminicial.grid(row=9,column=0,padx=10,pady=10)

l_kmviagem= tk.Label(janela,text='KM da Viagem')
l_kmviagem.grid(row=10,column=0,padx=10,pady=10)

l_kmfinal = tk.Label(janela,text='KM Final')
l_kmfinal.grid(row=11,column=0,padx=10,pady=10)

l_pedagio = tk.Label(janela,text='Pedágio')
l_pedagio.grid(row=12,column=0,padx=10,pady=10)

l_alimentacao = tk.Label(janela,text='Alimetação')
l_alimentacao.grid(row=13,column=0,padx=10,pady=10)

l_hospedagem= tk.Label(janela,text='Hospedagem')
l_hospedagem.grid(row=14,column=0,padx=10,pady=10)

l_pago_total = tk.Label(janela,text='Pago Total ')
l_pago_total.grid(row=15,column=0,padx=10,pady=10)


e_cpf= tk.Entry(janela,text='CPF Motorista',width=30)
e_cpf.grid(row=0,column=1,padx=10,pady=10)

e_placa= tk.Entry(janela,text='Placa',width=30)
e_placa.grid(row=1,column=1,padx=10,pady=10)

e_posto= tk.Entry(janela,text='Posto',width=30)
e_posto.grid(row=2,column=1,padx=10,pady=10)

e_combustivel= tk.Entry(janela,text='Combustível',width=30)
e_combustivel.grid(row=3,column=1,padx=10,pady=10)

e_valor_unitario= tk.Entry(janela,text='Valor Unitário',width=30)
e_valor_unitario.grid(row=4,column=1,padx=10,pady=10)

e_quantidade= tk.Entry(janela,text='Quantidade em Litro',width=30)
e_quantidade.grid(row=5,column=1,padx=10,pady=10)

e_total_pago= tk.Entry(janela,text='Total Pago',width=30)
e_total_pago.grid(row=6,column=1,padx=10,pady=10)

e_saida= tk.Entry(janela,text='Saída',width=30)
e_saida.grid(row=7,column=1,padx=10,pady=10)

e_destino= tk.Entry(janela,text='Destino',width=30)
e_destino.grid(row=8,column=1,padx=10,pady=10)

e_kminicial= tk.Entry(janela,text='KM Inicial do Veículo',width=30)
e_kminicial.grid(row=9,column=1,padx=10,pady=10)

e_kmviagem= tk.Entry(janela,text='KM da Viagem ',width=30)
e_kmviagem.grid(row=10,column=1,padx=10,pady=10)

e_kmfinal= tk.Entry(janela,text='KM Final',width=30)
e_kmfinal.grid(row=11,column=1,padx=10,pady=10)

e_pedagio= tk.Entry(janela,text='Pedágio',width=30)
e_pedagio.grid(row=12,column=1,padx=10,pady=10)

e_alimentacao= tk.Entry(janela,text='Alimentação',width=30)
e_alimentacao.grid(row=13,column=1,padx=10,pady=10)

e_hospedagem= tk.Entry(janela,text='Hospedagem',width=30)
e_hospedagem.grid(row=14,column=1,padx=10,pady=10)

e_pago_total= tk.Entry(janela,text='Pago Total',width=30)
e_pago_total.grid(row=15,column=1,padx=10,pady=10)

botao_cadastrar= tk.Button(janela,text='Cadastrar Rodagem',command=cadastrar_rodagem)
botao_cadastrar.grid(row=16,column=0,padx=10,pady=10,columnspan=2,ipadx=80)



janela.mainloop()