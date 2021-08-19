from random import randint
import os
import pandas as pd
import PySimpleGUI as sg
import datetime


def chamaTela2():
    layout2 = [
        [sg.Table(values=tabelai,
                  headings=header_list,
                  display_row_numbers=False,
                  auto_size_columns=True,
                  row_height=50,
                  num_rows=min(4, len(tabelai)))],
        [sg.Button('Voltar', size=(largura*3, altura), key='vti')]]
    return sg.Window('Treinos', layout=layout2, size=(780, 430), finalize=True, grab_anywhere=False)


def chamaTela3():
    layout3 = [
        [sg.Text('Data', size=(largura * 2, altura - 1), background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='dt1', background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='dt2', background_color='DarkRed', font='20')],
        [sg.Text('Músculo', size=(largura * 2, altura - 1), background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='gm1', background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='gm2', background_color='DarkRed', font='20')],
        [sg.Text('Series', size=(largura * 2, altura - 1), background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='sr1', background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='sr2', background_color='DarkRed', font='20')],
        [sg.Text('Repetições', size=(largura * 2, altura - 1), background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='rp1', background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='rp2', background_color='DarkRed', font='20')],
        [sg.Text('Peso ', size=(largura * 2, altura - 1), background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='ps1', background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='ps2', background_color='DarkRed', font='20')],
        [sg.Text('Exercícios', size=(largura * 2, altura - 1), background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='nde1', background_color='DarkRed', font='20'),
         sg.Text('', size=(largura * 2, altura - 1), key='nde2', background_color='DarkRed', font='20')],
        [sg.Text('Realizou\nTreino ?', size=(largura * 2, altura - 1), background_color='DarkRed', font='20'),
         sg.Checkbox('Primeiro CheckBox', size=(largura+8, altura), key='rt1', background_color='DarkRed', font='20'),
         sg.Checkbox('Segundo CheckBox', size=(largura+8, altura), key='rt2', background_color='DarkRed', font='20')],
        [sg.Button('Alterar\na Realização', size=(largura * 3, altura), key='ar'),
         sg.Button('Voltar', size=(largura*3, altura), key='vti')]]
    return sg.Window('Treino', layout=layout3, size=(600, 410), finalize=True)


tabela_incio = pd.read_excel('base_treino.xlsx', sheet_name='Treino')
tabela_peito = pd.read_excel('base_treino.xlsx', sheet_name='PEITO')
tabela_perna = pd.read_excel('base_treino.xlsx', sheet_name='PERNA')
tabela_costas = pd.read_excel('base_treino.xlsx', sheet_name='COSTAS')
tabela_biceps = pd.read_excel('base_treino.xlsx', sheet_name='BICEPS')
tabela_triceps = pd.read_excel('base_treino.xlsx', sheet_name='TRICEPS')
tabela_ombros = pd.read_excel('base_treino.xlsx', sheet_name='OMBROS')
tabela_abs = pd.read_excel('base_treino.xlsx', sheet_name='ABS')
writer = pd.ExcelWriter('base_treino.xlsx', engine='xlsxwriter')
tabelai = tabela_incio.values.tolist()
header_list = list(tabela_incio.columns)
largura = 10
altura = 3

sg.theme('DarkTeal12')
layout = [
    [sg.Text('Data', size=(largura*2, altura), background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='dt1', background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='dt2', background_color='DarkRed', font='20')],
    [sg.Text('Músculo', size=(largura*2, altura), background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='gm1', background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='gm2', background_color='DarkRed', font='20')],
    [sg.Text('Series', size=(largura*2, altura), background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='sr1', background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='sr2', background_color='DarkRed', font='20')],
    [sg.Text('Repetições', size=(largura*2, altura), background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='rp1', background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='rp2', background_color='DarkRed', font='20')],
    [sg.Text('Peso ', size=(largura*2, altura), background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='ps1', background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura), key='ps2', background_color='DarkRed', font='20')],
    [sg.Text('Exercícios', size=(largura*2, altura*2), background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura*2), key='nde1', background_color='DarkRed', font='20'),
     sg.Text('', size=(largura*3, altura*2), key='nde2', background_color='DarkRed', font='20')],
    [sg.Button('Gerar\ntreino', size=(largura+12, altura*2), key='gt'),
     sg.Button('Visualizar treinos\nanteriores', size=(largura+12, altura*2), key='vta'),
     sg.Button('Visualizar\ntreino de hoje', size=(largura+12, altura*2), key='vth'),
     sg.Button('Sair e salvar\no treino', size=(largura+12, altura*2), key='sair')]]


lista_grupo_menor = ['Triceps', 'Biceps', 'Ombro', 'Abs']
lista_grupo_maior = ['Peito', 'Costas', 'Perna']
lista_peso = ['Peso Corporal', '2Kg', '4Kg', '9Kg']
lista_series = [1, 2, 3, 4, 5]
lista_repeticoes = [10, 20, 30, 40, 50]
os.system('cls')
janela1 = sg.Window('Treino', layout=layout, size=(780, 500), finalize=True)
janela2, janela3 = None, None
data = datetime.datetime.now()
data_atual = data.strftime('%Y/%m/%d')
verificacao = True

while True:
    windons, event, valores = sg.read_all_windows()
    i = randint(0, 100)
    j = randint(0, 100)
    musculo_maior = lista_grupo_maior[i % 3]
    musculo_menor = lista_grupo_menor[j % 3]
    numero_series_maior = lista_series[i % 5]
    numero_series_menor = lista_series[j % 5]
    numero_repeticoes_maior = lista_repeticoes[i % 5]
    numero_repeticoes_menor = lista_repeticoes[j % 5]
    numero_peso_maior = lista_peso[i % 4]
    numero_peso_menor = lista_peso[j % 4]
    tabelai = tabela_incio.values.tolist()

    for data_tabela in tabela_incio['Data']:
        if data_atual == data_tabela:
            verificacao = False
    if event == sg.WINDOW_CLOSED or event == 'sair':
        break
    if event == 'gt' and not verificacao:
        sg.popup_error('Já foi realizado')
    if event == 'gt' and verificacao:
        verificacao = False
        janela1.Element('dt1').Update(f'{data_atual}')
        janela1.Element('dt2').Update(f'{data_atual}')
        janela1.Element('gm1').Update(f'{musculo_maior}')
        janela1.Element('gm2').Update(f'{musculo_menor}')
        janela1.Element('sr1').Update(f'{numero_series_maior}')
        janela1.Element('sr2').Update(f'{numero_series_menor}')
        janela1.Element('rp1').Update(f'{numero_repeticoes_maior}')
        janela1.Element('rp2').Update(f'{numero_repeticoes_menor}')
        janela1.Element('ps1').Update(f'{numero_peso_maior}')
        janela1.Element('ps2').Update(f'{numero_peso_menor}')
        text, list = '', [int]
        for _ in range((i % 3) + 1):
            if musculo_maior == 'Peito':
                k = randint(0, 8)
                while k in list:
                    k = randint(0, 8)
                list.append(k)
                text += tabela_peito["Exercícios"][k] + '\n'
                janela1.Element('nde1').Update(f'{text}')
            if musculo_maior == 'Costas':
                k = randint(0, 7)
                while k in list:
                    k = randint(0, 7)
                list.append(k)
                text += tabela_costas["Exercícios"][k] + '\n'
                janela1.Element('nde1').Update(f'{text}')
            if musculo_maior == 'Perna':
                k = randint(0, 8)
                while k in list:
                    k = randint(0, 8)
                list.append(k)
                text += tabela_perna["Exercícios"][k] + '\n'
                janela1.Element('nde1').Update(f'{text}')
        indice = len(tabela_incio)
        tabela_incio.loc[indice] = [musculo_maior, text, numero_repeticoes_maior, numero_series_maior,
                                    numero_peso_maior, data_atual, 'Não']
        text, list = '', [int]
        for _ in range((j % 4) + 1):
            if musculo_menor == 'Triceps':
                k = randint(0, 6)
                while k in list:
                    k = randint(0, 6)
                list.append(k)
                text += tabela_triceps["Exercícios"][k] + '\n'
                janela1.Element('nde2').Update(f'{text}')
            if musculo_menor == 'Biceps':
                k = randint(0, 9)
                while k in list:
                    k = randint(0, 9)
                list.append(k)
                text += tabela_biceps["Exercícios"][k] + '\n'
                janela1.Element('nde2').Update(f'{text}')
            if musculo_menor == 'Ombro':
                k = randint(0, 7)
                while k in list:
                    k = randint(0, 7)
                list.append(k)
                text += tabela_ombros["Exercícios"][k] + '\n'
                janela1.Element('nde2').Update(f'{text}')
            if musculo_menor == 'Abs':
                k = randint(0, 5)
                while k in list:
                    k = randint(0, 5)
                list.append(k)
                text += tabela_abs["Exercícios"][k] + '\n'
                janela1.Element('nde2').Update(f'{text}')
        indice = len(tabela_incio)
        tabela_incio.loc[indice] = [musculo_menor, text, numero_repeticoes_menor, numero_series_menor,
                                    numero_peso_menor, data_atual, 'Não']
    if event == 'vta':
        janela1.hide()
        janela2 = chamaTela2()
    if windons == janela2 and event == 'vti':
        janela2.hide()
        janela1.un_hide()
    if windons == janela3 and event == 'vti':
        janela3.hide()
        janela1.un_hide()
    if event == 'vth':
        if data_atual == tabela_incio['Data'][len(tabela_incio)-1]:
            janela1.hide()
            janela3 = chamaTela3()
            janela3.Element('dt1').Update(f'{data_atual}')
            janela3.Element('dt2').Update(f'{data_atual}')
            janela3.Element('gm1').Update(f'{tabela_incio["Muscúlos"][len(tabela_incio)-2]}')
            janela3.Element('gm2').Update(f'{tabela_incio["Muscúlos"][len(tabela_incio)-1]}')
            janela3.Element('sr1').Update(f'{tabela_incio["Séries"][len(tabela_incio)-2]}')
            janela3.Element('sr2').Update(f'{tabela_incio["Séries"][len(tabela_incio)-1]}')
            janela3.Element('rp1').Update(f'{tabela_incio["Repetições"][len(tabela_incio)-2]}')
            janela3.Element('rp2').Update(f'{tabela_incio["Repetições"][len(tabela_incio)-1]}')
            janela3.Element('ps1').Update(f'{tabela_incio["Peso"][len(tabela_incio)-2]}')
            janela3.Element('ps2').Update(f'{tabela_incio["Peso"][len(tabela_incio)-1]}')
            janela3.Element('nde1').Update(f'{tabela_incio["Exercícios"][len(tabela_incio)-2]}')
            janela3.Element('nde2').Update(f'{tabela_incio["Exercícios"][len(tabela_incio)-1]}')
            janela3.Element('rt1').Update(tabela_incio["Feito"][len(tabela_incio)-2] == "Sim")
            janela3.Element('rt2').Update(tabela_incio["Feito"][len(tabela_incio)-1] == "Sim")
        else:
            sg.popup_error(f'É obrigatório gerar o treino do dia: {data_atual}', font='45')
    if event == 'ar' and not verificacao:
        if valores['rt1']:
            # tabela_incio["Feito"][len(tabela_incio)-1] = 'Sim'
            tabela_incio.loc[(tabela_incio["Muscúlos"] == tabela_incio["Muscúlos"][len(tabela_incio)-2]) &
                             (tabela_incio.Data == data_atual), 'Feito'] = 'Sim'
            janela3.Element('rt1').Update(valores['rt1'])
            # tabela_incio.loc[:, ("Feito", len(tabela_incio) - 1)] = 'Sim'
        if not valores['rt1']:
            # tabela_incio["Feito"][len(tabela_incio) - 1] = 'Não'
            tabela_incio.loc[(tabela_incio["Muscúlos"] == tabela_incio["Muscúlos"][len(tabela_incio) - 2]) &
                             (tabela_incio.Data == data_atual), 'Feito'] = 'Não'
            janela3.Element('rt1').Update(valores['rt1'])
            # tabela_incio.loc[:, ("Feito", len(tabela_incio) - 1)] = 'Não'
        if valores['rt2']:
            # tabela_incio["Feito"][len(tabela_incio)-2] = 'Sim'
            tabela_incio.loc[(tabela_incio["Muscúlos"] == tabela_incio["Muscúlos"][len(tabela_incio) - 1]) &
                             (tabela_incio.Data == data_atual), 'Feito'] = 'Sim'
            janela3.Element('rt2').Update(valores['rt2'])
            # tabela_incio.loc[:, ("Feito", len(tabela_incio) - 2)] = 'Sim'
        if not valores['rt2']:
            # tabela_incio["Feito"][len(tabela_incio) - 2] = 'Não'
            tabela_incio.loc[(tabela_incio["Muscúlos"] == tabela_incio["Muscúlos"][len(tabela_incio) - 1]) &
                             (tabela_incio.Data == data_atual), 'Feito'] = 'Não'
            janela3.Element('rt2').Update(valores['rt2'])
            # tabela_incio.loc[:, ("Feito", len(tabela_incio) - 2)] = 'Não'
        sg.popup('Ateração concluída', font='45')

# for indice in tabela_peito.index:
    # tabela_peito.loc[indice, 'Vezes que treinou'] = f"=COUNTIF(Treino!B:B;'*'&A{indice+2}&'*')"

tabela_incio.to_excel(writer, sheet_name='Treino', index=False)
tabela_peito.to_excel(writer, sheet_name='PEITO', index=False)
tabela_perna.to_excel(writer, sheet_name='PERNA', index=False)
tabela_costas.to_excel(writer, sheet_name='COSTAS', index=False)
tabela_biceps.to_excel(writer, sheet_name='BICEPS', index=False)
tabela_triceps.to_excel(writer, sheet_name='TRICEPS', index=False)
tabela_ombros.to_excel(writer, sheet_name='OMBROS', index=False)
tabela_abs.to_excel(writer, sheet_name='ABS', index=False)
writer.save()
