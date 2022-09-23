import sqlite3
import tkinter as tk

banco = sqlite3.connect("Banco-de-Dados.db")
cursor = banco.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Entregas ('
               'Id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'Placa text,'
               'CPF_Motorista text,'
               'Saída text,'
               'Destino text,'
               'Tipo_de_Carga text,'
               'Parada text,'
               'Data_de_saida text,'
               'Data_Prevista text,'
               'Data_de_Chegada text,'
               'Status text,'
               'Feedback_detalhado text)')

banco.commit()

banco.close()


def cadastrar_entrega():
    banco = sqlite3.connect("Banco-de-Dados.db")
    cursor = banco.cursor()

    cursor.execute('INSERT INTO ControleEntregas VALUES(:id,:placa,:cpf,:saida,:destino,:tipo_carga,:parada,:datasaida,:dataprevista,:datachegada,:status,:feedback_detalhado)',

        {
            'id': None,
            'placa': e_placa.get(),
            'cpf': e_cpf.get(),
            'saida': e_saida.get(),
            'destino': e_destino.get(),
            'tipo_carga': e_tipo_carga.get(),
            'parada': e_parada.get(),
            'datasaida': e_datasaida.get(),
            'dataprevista': e_dataprevista.get(),
            'datachegada': e_datachegada.get(),
            'status': e_status.get(),
            'feedback_detalhado': e_feedback_detalhado.get(),

        }

        )
    banco.commit()
    banco.close()


    e_placa.delete(0, 'end')
    e_cpf.delete(0, 'end')
    e_saida.delete(0, 'end')
    e_destino.delete(0, 'end')
    e_tipo_carga.delete(0, 'end')
    e_parada.delete(0, 'end')
    e_datasaida.delete(0, 'end')
    e_dataprevista.delete(0, 'end')
    e_datachegada.delete(0, 'end')
    e_status.delete(0, 'end')
    e_feedback_detalhado.delete(0, 'end')


janela = tk.Tk()
janela.title("Cadastrar Entrega")

l_placa = tk.Label(janela, text='Placa')
l_placa.grid(row=1, column=0, padx=10, pady=10)

l_cpf = tk.Label(janela, text='CPF do Motorista ')
l_cpf.grid(row=3, column=0, padx=10, pady=10)

l_saida = tk.Label(janela, text='Saída')
l_saida.grid(row=4, column=0, padx=10, pady=10)

l_destino = tk.Label(janela, text='Destino')
l_destino.grid(row=5, column=0, padx=10, pady=10)

l_tipo_carga = tk.Label(janela, text='Tipo Carga')
l_tipo_carga.grid(row=6, column=0, padx=10, pady=10)

l_parada = tk.Label(janela, text='Parada(s)')
l_parada.grid(row=7, column=0, padx=10, pady=10)

l_datasaida = tk.Label(janela, text='Data de Saída')
l_datasaida.grid(row=8, column=0, padx=10, pady=10)

l_dataprevista = tk.Label(janela, text='Data Prevista')
l_dataprevista.grid(row=9, column=0, padx=10, pady=10)

l_datachegada = tk.Label(janela, text='Data de Chegada')
l_datachegada.grid(row=10, column=0, padx=10, pady=10)

l_status = tk.Label(janela, text='Status')
l_status.grid(row=11, column=0, padx=10, pady=10)

l_feedback_detahado = tk.Label(janela, text='Feedback Detalhado')
l_feedback_detahado.grid(row=12, column=0, padx=10, pady=10)



e_placa = tk.Entry(janela, text='Placa', width=30)
e_placa.grid(row=1, column=1, padx=10, pady=10)

e_cpf = tk.Entry(janela, text='CPF do Motorista ', width=30)
e_cpf.grid(row=3, column=1, padx=10, pady=10)

e_saida = tk.Entry(janela, text='Saída', width=30)
e_saida.grid(row=4, column=1, padx=10, pady=10)

e_destino = tk.Entry(janela, text='Destino', width=30)
e_destino.grid(row=5, column=1, padx=10, pady=10)

e_tipo_carga = tk.Entry(janela, text='Tipo Carga', width=30)
e_tipo_carga.grid(row=6, column=1, padx=10, pady=10)

e_parada = tk.Entry(janela, text='Parada', width=30)
e_parada.grid(row=7, column=1, padx=10, pady=10)

e_datasaida = tk.Entry(janela, text='Data de Saída', width=30)
e_datasaida.grid(row=8, column=1, padx=10, pady=10)

e_dataprevista = tk.Entry(janela, text='Data Prevista', width=30)
e_dataprevista.grid(row=9, column=1, padx=10, pady=10)

e_datachegada = tk.Entry(janela, text='Data de Chegada', width=30)
e_datachegada.grid(row=10, column=1, padx=10, pady=10)

e_status = tk.Entry(janela, text='Status', width=30)
e_status.grid(row=11, column=1, padx=10, pady=10)

e_feedback_detalhado = tk.Entry(janela, text='Feedback Sobre a Entrega', width=30)
e_feedback_detalhado.grid(row=12, column=1, padx=10, pady=10)

botao_cadastrar = tk.Button(janela, text='Cadastrar Entrega', command=cadastrar_entrega)
botao_cadastrar.grid(row=13, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

janela.mainloop()