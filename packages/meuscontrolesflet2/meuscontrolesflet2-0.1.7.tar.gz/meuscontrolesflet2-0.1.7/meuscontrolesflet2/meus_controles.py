
from flet import*
from threading import Thread
from time import time, sleep
from pandas import DataFrame
from datetime import datetime
from re import findall
from pyperclip import copy



class PopupMenu(UserControl):
    def __init__(self, 
                 nome_ou_icone = None, 
                 lista_de_controles = None,
                 tooltip = None,
                 col = None,
            ):
        super().__init__()
        self.nome_ou_icone = nome_ou_icone
        self.tooltip = tooltip
        self._colu = col
        self.p = PopupMenuButton(tooltip = self.tooltip, col = self._colu)
        self.lista_de_controles = lista_de_controles
        self._Add_itens()

    @property
    def coluna(self):
        return self._colu
    
    @coluna.setter
    def coluna(self, valor):
        self._colu = valor
        # self.p.col = valor
        

    def _Add_itens(self):
        if isinstance(self.lista_de_controles, list) and len(self.lista_de_controles) > 0:
            self.p.items = [PopupMenuItem(content = i) for i in self.lista_de_controles]
        else:
            print('Não há itens para adicionar')

    def Add_item(self, *controle):
        for i in list(controle):
            self.p.items.append(PopupMenuItem(content = i,))
        # self.p.update()

    def build(self):
        if self.nome_ou_icone != None and (isinstance(self.nome_ou_icone, Icon) or isinstance(self.nome_ou_icone, Text)):
            self.p.content = self.nome_ou_icone
        return self.p


class ItensPoup: #classe para criar controles para a classe PopupMenu2
    def __init__(self,
                 
        icon = None,
        text = None,
        on_click = None ,
        data = None,
        cor = None,
              
                 
        ):
        self.icon = icon
        self.quebra_linha(text, largura=30)
        self.on_click = on_click
        self.data = data
        self.cor = cor

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, texto):
        self.quebra_linha(texto, largura=30)

    def quebra_linha(self, texto, largura=36):
        palavras = texto.split()
        linhas = []
        linha_atual = ''
        
        for palavra in palavras:
            if len(linha_atual) + len(palavra) <= largura:
                linha_atual += palavra + ' '
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra + ' '
        
        if linha_atual:
            linhas.append(linha_atual.strip())
        
        self._text  = '\n'.join(linhas)


class PopupMenu2(UserControl):
    def __init__(self, 
                 nome_ou_icone = None, 
                 controles:ItensPoup = None, #[icone, nome, on_click, data]
                 tooltip = None,
                 col = None,
            ):
        super().__init__()
        self.nome_ou_icone = nome_ou_icone
        self.tooltip = tooltip
        self._colu = col
        self.p = PopupMenuButton(tooltip = self.tooltip)
        self.lista_de_controles = controles
        self._Add_itens()

    @property
    def coluna(self):
        return self._colu
    
    @coluna.setter
    def coluna(self, valor):
        self._colu = valor
        # self.p.col = valor
        

    def _Add_itens(self):
        if isinstance(self.lista_de_controles, list) and len(self.lista_de_controles) > 0:
            self.p.items = [PopupMenuItem(icon = i.icon, text = i.text, on_click = i.on_click, data = i.data) for i in self.lista_de_controles]
        else:
            print('Não há itens para adicionar')

    def Add_item(self, *controle):
        
        for i in list(controle):
            if isinstance(i,ItensPoup ):
            # try:
            #     icon = i[0] 
            # except:
            #     icon = None
            # try:
            #     text = i[1] 
            # except:
            #     text = None
            # try:
            #     on_click = i[2] 
            # except:
            #     on_click = None
            # try:
            #     data = i[3]
            # except:  
            #     data = None
            
                self.p.items.append(PopupMenuItem(icon = i.icon, text = i.text, on_click = i.on_click, data = i.data))
        # self.p.update()

    def Add_item_control(self, *controle):        
        for i in list(controle):
            if isinstance(i,ItensPoup ):
                icone = Icon(i.icon, color = i.cor)
                texto = Text(i.text,color = i.cor)
                if i.icon == None:
                    icone.visible = False
                if i.text == None:
                    texto.visible = False
                conteudo = Row([icone,texto])
                if i.text == None and i.icon == None:
                    conteudo = None
                self.p.items.append(PopupMenuItem(content = conteudo, on_click=i.on_click))


    def Add_item_geral(self, *controle):        
        for i in list(controle):
            if isinstance(i,PopupMenuItem):
                self.p.items.append(i)


    def build(self):
        if self.nome_ou_icone != None and (isinstance(self.nome_ou_icone, Icon) or isinstance(self.nome_ou_icone, Text)):
            self.p.content = self.nome_ou_icone
        return self.p



class Tabs_new(UserControl):
    def __init__(self,
        data = None,
        on_change = None,
        tabs:list['nome',Control] = None,
        width=200,
        height=200,
        
                 
    ):
        super().__init__()
        self.data = data
        self.on_change = on_change
        self.w = width
        self.h = height
        self.tabs = tabs
        self.Construir_tabs()
        self.t = Tabs(
            selected_index=0,
            animation_duration=0,
            # divider_color  = 'blue',
            tabs=self.tabs_construidas,
            width=self.w,
            height=self.h,
            data = self.data,
            on_change=self.Func,
            # expand=1,
            
            )
        # self.height2 = None
        # self.width = None

    def Func(self,e):
        if self.on_change is not None:  
            return self.on_change(self,e)
        
    def Construir_tabs(self):
        self.tabs_construidas =  [Tab(text=i[0],  content = i[1]) for i in self.tabs]

    def Add_tab(self, *tabs:['nome',Control]):
        self.tabs_construidas +=  [Tab(text=i[0],  content = i[1]) for i in tabs]
        # self.t.update()

    @property
    def get_height(self):
        return self.h 
    @get_height.setter
    def set_height(self, valor):
        self.h = valor
        self.t.height = valor
        # self.t.update()

    @property
    def get_width(self):
        return self.w 
    @get_width.setter
    def set_width(self, valor):
        self.w = valor
        self.t.width = valor
        # self.t.update()


    def build(self):
        return self.t


class Dialogo(UserControl):
    def __init__(self,

                 title: str = 'título da janela',
                 content: Control | None = None,
                 on_dismiss: None = None,
                 salvar=None,
                 nome_json=None
                 ):
        super().__init__()
        # self.page = page
        self.titulo = title
        self._content = content
        self.on_dismiss = on_dismiss
        self.salvar = salvar
        self.nome_json = nome_json
        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text(self.titulo),
            content=self._content,
            actions=[
                TextButton("Salvar", on_click=self.Salvar),
                TextButton("Sair", on_click=self.close_dlg),
                # TextButton("No", on_click=self.close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=self.on_dismiss,
        )

    def build(self):
        return self.dlg_modal

    def open_dlg_modal(self):
        # self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.update()

    def att(self):
        # self._content = Text('casdada')
        self.dlg_modal.content = Text('casdada')
        self.update()

    def close_dlg(self, e):
        self.dlg_modal.open = False
        self.update()

    def Salvar(self, e):
        return self.salvar(e, self.nome_json)

    @property
    def Content(self):
        return self._content

    @Content.setter
    def Content(self, valor):
        self._content = valor
        self.dlg_modal.content = self._content
        self.update()

    @property
    def Titulo(self):
        return self.titulo

    @Titulo.setter
    def Titulo(self, valor):
        self.titulo = valor
        self.dlg_modal.title = Text(self.titulo)
        self.update()


class ShowDF(UserControl):
    def __init__(self,
                 df#DataFrame ou dicionário
                 ):
        super().__init__()
        self.df = df if type(df) != dict else DataFrame(df)
        self.d1 = DataTable(border = border.all(1,'white,0.9'),
                            heading_row_color = 'white,0.5',
                            heading_row_height = 80,
                            column_spacing = 15,
                            # heading_row_color=colors.BLACK12,
                            vertical_lines = border.all(20,'white'),
                            horizontal_margin = 0,
                            data_row_max_height = 70,
                            # data_row_min_height = 50,
                            divider_thickness = 0,
                            show_checkbox_column = True,
                            sort_column_index = 4,
                            sort_ascending = True,
                            # data_row_color={"hovered": "0x30FF0000"},
                            )
        self.textsize = 15
        self.Colunas_tabela()
        self.Linhas_tabela()

    def Colunas_tabela(self):
        self.d1.columns = [DataColumn(Row([Text(width=10),Text(i,selectable = True,theme_style=TextThemeStyle.TITLE_MEDIUM)],alignment='center')) for i in list(self.df.columns)]
        
    
    def Linhas_tabela(self):
        linhas = []
        df_lista = self.df.values.tolist()
        for l,i in enumerate(df_lista):
            cell = [ DataCell(Row([Text(width=10),Text(j,text_align='center',selectable = True, size = self.textsize)],alignment='left',spacing = 3,)) for j in i]
            cor  = 'black' if l % 2 == 0 else 'white,0.01'
            linhas.append(DataRow(cells = cell, color = cor))
        self.d1.rows = linhas
            
    def build(self):
        return self.d1


class TabelaMandadosAcoes(ShowDF):
    def __init__(self, df, funcao):
        self.larguras()
        super().__init__(df)
        self.funcao = funcao

    def larguras(self):
        self.largura = {
            'Nº do Processo:':80, 
            'Nº do mandado:':80, 
            'Destinatario do mandado:':100,
            'Endereco':650, 
            'ação':60, 
            'Tipo do mandado:':80, 
            'Audiência':90,
            'Final de prazo':90, 
            'telefone':70
        }
   
    def Colunas_tabela(self):
        for j,i in enumerate(list(self.df.columns)):
            match i:
                case 'ação':
                    largura = 85 
                case _:
                    largura = 90
            linha = Row([
                Text(i, text_align='center', selectable=True, width=self.largura[i],color = 'black',weight = 'bold',
                     theme_style=TextThemeStyle.TITLE_MEDIUM, col={'xs': 12}),
                # Row([
                    IconButton(icons.ARROW_DROP_UP_SHARP, width=25,on_click = self.ordem,data = [i,True],
                               icon_color='black,0.8', col={'xs': 6}),
                    IconButton(icons.ARROW_DROP_DOWN_SHARP, width=25,on_click = self.ordem,data = [i,False],
                               icon_color='black,0.8', col={'xs': 6}),
                    Text(width=10)
                # ], alignment='left', tight=True,)
                # Text(width=15)
            ],
                # horizontal_alignment='center',
                # alignment="spaceEvenly",
                tight=True,
                spacing=0,
                height=200,
                run_spacing=0)
            self.d1.columns.append(DataColumn(linha, data=i))

        # self.d1.columns = [DataColumn() for i in list(self.df.columns)] + [DataColumn(Text('Enviar'))
        self.d1.columns.append(DataColumn(Text(' Enviar ',color = 'black',), data='Enviar'))
        self.d1.columns.append(DataColumn(Text(' PDF ',color = 'black',), data='PDF'))
        self.d1.columns.append(DataColumn(Text(' Add ',color = 'black',), data='Add'))
        self.d1.columns.append(DataColumn(Text(' Mand.\ndireto ',color = 'black',), data='Mand.D'))

    def Linhas_tabela(self):
        linhas = []
        df_lista = self.df.values.tolist()
        indx = list(self.df.index)

        nomes_colunas = ['Nº do Processo:', 'Nº do mandado:', 'Destinatario do mandado:',
                         'Endereco', 'ação', 'Tipo do mandado:', 'Audiência',
                         'Final de prazo', 'telefone']
        


        acao1 = ['aguardar', 'cancelar', 'consultar', 'devolver', 'email', 'enviado', 'imp', 'impresso', 'ligar',
                 'Não encontrei', 'transferido', 'Transferir', 'voltar', 'zap']
        
        tipo1 = ['Afastamento',	'Avaliação',	'Busca',	'Citação',	'Citação e Intimação',	'Condução',	'Contramandado',
                 'Entrega',	'Imissão',	'Intimação',	'Intimação para Audiência',	'Notificação',	'Ofício',	'Penhora',	'Prisão',	'Reintegração']
        tipo1 = list(map(str.upper, tipo1))


        for l, i in enumerate(df_lista):
            cell = []

            for k, j, num_col in zip(list(self.df.columns), i, range(100)):

                if k in ['Destinatario do mandado:']:
                    cell.append(
                        DataCell(
                                    Row([
                                        Text(
                                                j, selectable=True,
                                                size=15,text_align = TextAlign.CENTER,
                                                weight = FontWeight.BOLD,
                                                width=self.largura[k]+100
                                            ),
                                        IconButton(icon = icons.SEARCH, scale = 1, icon_size = 13, data = [indx[l],'pesquisar',j], on_click=self.Func, tooltip = 'Pesquisar contato no zap')
                                    ], spacing=0, tight=True, run_spacing = 0),
                                    data = [indx[l],'copiado',j],
                                    on_double_tap = self.Func
                                )
                                
                        )
               
                elif k in ['Endereco']:
                    cell.append(DataCell(Text(j, selectable=True, size=12,text_align = TextAlign.START,
                                              width=self.largura[k]+100),
                                                data = [indx[l],'copiado',j],
                                                on_double_tap = self.Func                                              
                                              ))
                              
               
                elif k == 'ação':
                    match j:
                        case 'zap':
                            cor = 'green' 
                        case 'enviado':
                            cor = 'yellow,0.3'                         
                        case 'aguardar':
                            cor = 'blue,0.8'                        
                        case 'impresso':
                            cor = 'white,0.1'     
                        case 'devolver':
                            cor = 'red'
                        case 'imp':
                            cor = 'blue'
                        case 'Transferir':
                            cor = 'white,0.5'                                                                                                                   
                        case _:
                            cor = 'black'                    
                    cell.append(DataCell(Container(Row([Drop_new(acao1, value=j,alinhamento = Alignment(-1, 0),
                                                       width_person=self.largura[k]+50,
                                                       on_change=self.Func2,
                                                       data=[indx[l],'acao2',[l,num_col]])],
                                             alignment='left'),bgcolor=cor)))
                
                
                elif k == 'Tipo do mandado:':
                    v = list(map(str.upper, [j])) if j not in [None,'', '--'] else ['--']
                    tipo2 = tipo1[:]
                    if v[0] not in tipo1:
                        tipo2.append(v[0])
                    cell.append(DataCell(Row([Drop_new(tipo2, value=v[0], width_person=self.largura[k]+50,alinhamento = Alignment(-1, 0),
                                                       on_change=self.Func2, data=[indx[l],'tipo2',[l,num_col]])], alignment='center')))
               
               
                elif k == 'telefone':
                    cell.append(DataCell(Row([Text(j, selectable=True, 
                                              )],alignment='center', expand=1, width=120),
                                                data = [indx[l],'copiado',j],
                                                on_double_tap = self.Func    
                                              ))
              
                elif k in ['Nº do Processo:', 'Nº do mandado:']:
                    cell.append(DataCell(Row([Text(j, selectable=True, text_align='center',
                                              width=100)],alignment='center'),
                                            data = [indx[l],'copiado',j],
                                            on_double_tap = self.Func                                                
                                              ))
                
                elif k == 'Audiência':
                    try:
                        data_audiencia =  findall(r'(\d{2}/\d{2}/\d{4})', j)[0]
                    

                        current_time = datetime.now()
                        cor2  = None
                        # Função para converter string "dd/mm/yy" para datetime
                        def converter_para_datetime(data_string):
                            return datetime.strptime(data_string, '%d/%m/%Y')
                        if len(data_audiencia) > 5:
                            try:
                                data_convertida = converter_para_datetime(data_audiencia)
                            except:
                                print(j[:-9])
                                data_convertida = converter_para_datetime(j[:-9])

                            diferenca = data_convertida - current_time
                        

                            if diferenca.days < 8:
                                cor2  = 'red,0.5'
                            elif diferenca.days < 16:
                                cor2  = 'yellow,0.3'
                            else:
                                cor2  = None
                    except:
                        cor2  = None


                    cell.append(DataCell(Container(Row([Text(j, text_align='center', selectable=True,max_lines = 1, no_wrap = True)],alignment='center'),bgcolor=cor2),
                                            data = [indx[l],'copiado',j],
                                            on_double_tap = self.Func                                         
                                         ))
                
                elif k == 'Final de prazo':
                    try:
                        prazo = findall(r'(\d{2}/\d{2}/\d{4})', j)[0]
                        current_time = datetime.now()
                        cor2  = None
                        # Função para converter string "dd/mm/yy" para datetime
                        def converter_para_datetime(data_string):
                            return datetime.strptime(data_string, '%d/%m/%Y')
                        if len(prazo) > 5:
                            prazo_convertido = converter_para_datetime(prazo)

                            diferenca = prazo_convertido - current_time

                            if diferenca.days < 8:
                                cor2  = 'red,0.5'
                            elif diferenca.days < 16:
                                cor2  = 'yellow,0.3'
                            else:
                                cor2  = None
                    except:
                        cor2  = None


                    cell.append(DataCell(Container(Row([Text(j, text_align='center', selectable=True,max_lines = 1, no_wrap = True)],alignment='center'),bgcolor=cor2)))             
               
                else:
                    lagura = larg[k] if k in range(len(larg)) else 90
                    cell.append(DataCell(Row([Text(j, text_align='center', selectable=True,
                                              )],alignment='center')))

            cell.append(DataCell(Row([IconButton(icon=icons.SEND, 
                tooltip='Enviar Mandado', on_click=self.Func,
                data=[indx[l],'enviar'])])))
            
            cell.append(DataCell(Row([IconButton(icon=icons.PICTURE_AS_PDF_OUTLINED,
                tooltip='Enviar PDF', 
                on_click=self.Func, data=[indx[l],'pdf',[l]])])))
            
            cell.append(DataCell(Row([IconButton(icon=icons.PERM_CONTACT_CAL_ROUNDED,
                tooltip='Add Contato', 
                on_click=self.Func, data=[indx[l],'add'])])))     

            cell.append(DataCell(Row([IconButton(icon=icons.CANCEL_SCHEDULE_SEND_OUTLINED,
                tooltip='Enviar Mandado direto \npara o contato \naberto no zap', 
                on_click=self.Func, data=[indx[l],'Mand.D',[l]])])))                    

            cor = 'black' if l % 2 == 0 else 'white,0.05'
            linhas.append(DataRow(cells=cell, color=cor))
        self.d1.rows = linhas

    def FuncCopy(self, e):
        nome = e.control.data
        copy(nome)
        self.funcao(e)

    def Func(self, e):
        encontrou = False

        if e.control.data[1] in ['Mand.D','pdf']:
            for j,i in enumerate(list(self.df.columns)):
                if i == 'ação':
                    encontrou = True
                    break
            
            if encontrou:
                self.d1.rows[int(e.control.data[2][0])].cells[j].content.content.controls[0].getvalue = 'enviado'
                self.d1.rows[int(e.control.data[2][0])].cells[j].content.bgcolor = 'yellow,0.3'
                self.d1.update()




        self.funcao(e)

    def Func2(self, v, e):
        # print('mudar cor')
        match e.control.value:
            case 'zap':
                cor = 'green' 
            case 'enviado':
                cor = 'yellow,0.3'                         
            case 'aguardar':
                cor = 'blue,0.8'                        
            case 'impresso':
                cor = 'white,0.1'     
            case 'devolver':
                cor = 'red'
            case 'imp':
                cor = 'blue'
            case 'Transferir':
                cor = 'white,0.5'                                                                                                                   
            case _:
                cor = 'black'        
        # print(cor)
        self.d1.rows[int(e.control.data[2][0])].cells[e.control.data[2][1]].content.bgcolor = cor
        # print(self.d1.rows[int(e.control.data[2][0])].cells[e.control.data[2][1]].content.bgcolor)
        self.d1.update()
        self.funcao(e)

    def duplo_clic(self, e):
        print('duplo clic')


    def ordem(self,e):
        coluna, ascendente  = e.control.data
        self.df = self.df.sort_values(by=coluna,ascending = ascendente)
        self.Linhas_tabela()
        self.d1.update()


class TableCreate(UserControl):
    def __init__(self,borda: bool = False):
        super().__init__()
        self.borda = border.all(1,'white,0.3') if borda else None
        self.coluna = None
        self.linha = None
        self.d2 = DataTable(border = self.borda, heading_row_color = 'white,0.1')

    @property
    def Coluna(self):
        return self.coluna
    
    @Coluna.setter
    def Coluna(self,controle):
        self.d2.columns.append(DataColumn(controle))
        # self.update()

    @Coluna.setter
    def Colunas(self,list_controles):
        self.d2.columns = [DataColumn(i) for i in list_controles]
        # self.update()        
    
    @property
    def Linha(self):
        return self.linha

    @Linha.setter
    def Linha(self,linha):
        for i in enumerate(linha):
            cell = [ DataCell(j) for j in i]
        self.d2.rows.append(DataRow(cells = cell))
        # self.update() 

    @Linha.setter
    def linhas(self,list_linhas):
        linhas = []
        for l,i in enumerate(list_linhas):
            cell = [ DataCell(j) for j in i]
            cor  = 'black' if l % 2 == 0 else 'white,0.01'
            linhas.append(DataRow(cells = cell, color = cor))
        self.d2.rows = linhas
        # self.update()        

            
    def build(self):
        return self.d2


class ConfirmarSaida:
    def __init__(self,page, funcao=None):
        super().__init__()
        self.page = page
        self.funcao = funcao
        self.confirm_dialog = AlertDialog(
            modal=True,
            title=Text("Confirme!"),
            content=Text("Deseja realmente fechar o App?"),
            actions=[
                ElevatedButton("Sim", on_click=self.yes_click),
                OutlinedButton("Não", on_click=self.no_click),
            ],
            actions_alignment=MainAxisAlignment.END,
        )
        self.page.on_window_event = self.window_event
        self.page.window_prevent_close = True 
   


    def window_event(self, e):
            if e.data == "close":
                self.page.dialog = self.confirm_dialog
                
                self.confirm_dialog.open = True
                self.page.update()

    def yes_click(self,e):
        self.funcao
        self.page.window_destroy()

    def no_click(self,e):
        self.confirm_dialog.open = False
        self.page.update()


class Countdown(UserControl):
    def __init__(self, minutos, texto = ''):
        super().__init__()
        # self.page = Page
        self.minutos = minutos
        self.segundos = 60*minutos
        self.texto = texto
        self.pause = False

    def did_mount(self):
        self.running = True
        if self.minutos != '':            
            Thread(target=self.update_timer, daemon=True).start()

        else:
            self.countdown.value = self.texto
            self.update()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.segundos and self.running:
            h, mins = divmod(self.segundos, 60*60)
            mins, secs = divmod(mins, 60)
            h, mins, secs = int(h), int(mins), int(secs)
            if self.texto != '':
                self.countdown.value = "{:s} {:02d}:{:02d}:{:02d}".format(self.texto,h, mins, secs)
            else:
                self.countdown.value = "{:02d}:{:02d}:{:02d}".format(h, mins, secs)

            self.update()
            sleep(1)
            self.segundos -= 1
            while self.pause:
                sleep(0.3)
          

    def build(self):
        self.countdown = Text()
        return self.countdown
'''
class Quadro(UserControl):
    def __init__(self, 
                content = None,
                #  page = Page,
                 width = None, 
                 height = None,
                 expand = 0,
                 bgcolor = None,
                 border_color = 'blue',
                 
                 ):
        super().__init__()
        # self.page = page
        self.content = content
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.border_color = border_color
        self.expand = expand
        self.bgcolor = bgcolor
    
    def build(self):
        return Container(
        content = self.content,
        border_radius=10,
        alignment=Alignment(0,0),
        border= border.all(0.2, color = self.border_color),
        width= self.width,
        height= self.height,
        expand = self.expand,
        bgcolor = self.bgcolor
        )
'''
class Contador(UserControl):
    def __init__(self, 
                 segundos = 10,
                 cor = 'green',
                 size = 20

    ):
        super().__init__()
        self.segundos = segundos
        self.cor = cor
        self.size = size
        self.saida = Row(visible=False)
        self.pause_contador = False
        self.parar_contador = False
    


    @property
    def Pause(self):
        return self.pause_contador
    
    @Pause.setter
    def Pause(self, valor: bool):
        self.pause_contador = valor
        self.update()

    @property
    def Parar(self):
        return self.parar_contador
    @Parar.setter
    def Parar(self, valor:bool):
        self.parar_contador = valor
        self.update()


    def did_mount(self):
        self.Cont()

    def build(self):
        return self.saida


    def Cont(self):
        self.saida.visible = True
        super().update()
        while self.segundos >= 0:
            horas2, minutos2, segundos2 = self.converter_segundos_para_horas_min_segundos(self.segundos)
            self.saida.controls = [Text(f"{horas2}:{minutos2}:{segundos2}", color  = self.cor, size = self.size)]
            super().update()
            self.segundos += -1
            sleep(1)
            while self.pause_contador:
                sleep(0.1)
            if self.parar_contador:
                self.saida.controls = [Text()]
                super().update()

                break
        # self.saida.controls = [Text()]
        self.saida.visible = False
        super().update()
        





    def converter_segundos_para_horas_min_segundos(self, segundos):
        def Algarismos(numero, qtd=2):
            numero = int(numero)
            return str(numero).zfill(qtd)
        horas = segundos // 3600  # 3600 segundos em uma hora
        horas = Algarismos(horas)
        segundos %= 3600
        minutos = segundos // 60  # 60 segundos em um minuto
        minutos = Algarismos(minutos)
        segundos %= 60
        segundos = Algarismos(segundos)

        return horas, minutos, segundos
 
class Quadro_assync(UserControl):
    def __init__(self, 
                content = None,
                 tipo = 'r', #ou 'c'
                #  page = Page,
                 width = None, 
                 height = None,
                 expand = 1,
                 bgcolor = None,
                 border_color = 'white',
                 
                 ):
        super().__init__()
        # self._page = page
        self.tipo = tipo
        self.content = content #Row(content) if self.tipo == 'r' else Column(content)
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.border_color = border_color
        self.expand = expand
        self.bgcolor = bgcolor
    
    def build(self):
        return Container(
        content = self.content,
        alignment=Alignment(0,0),
        border = border.all(1, color = self.border_color),
        width= self.width,
        height= self.height,
        expand = self.expand,
        bgcolor = self.bgcolor
        )

class Drop_new(UserControl):
    def __init__(self, 
        opitions = [], 
        value = None,
        width_person = None,
        on_change = None,
        data = None,
        cor  = None,
        alinhamento = Alignment(0, 0),
        label = None

                
                ):
        super().__init__()
        self.opitions  = opitions
        self.value = value
        self._width = 30 if opitions == [] else 80
        self.on_change = on_change
        self.data = data
        self.cor = cor
        self.alinhamento = alinhamento
        self._label = label

        if width_person != None:
            self._width = width_person         
 
        self._drop = Dropdown(        
                alignment= self.alinhamento,
                options=[dropdown.Option(i) for i in self.opitions],
                text_size = 15,
                border_width = 0,
                border=None,
                content_padding = 5,
                # border_color='white',
                expand=0,
                scale=1,
                autofocus = 0,
                value = self.value,
                width = self._width,
                # aspect_ratio = 1,
                height = 25,
                dense = True,
                text_style = TextStyle(weight = 'bold'),
                on_change=self.mudou,
                data  = self.data,
                bgcolor = self.cor,
                label = self._label,
                                                  
        ) 

    def build(self):  
        return self._drop
    
    def mudou(self, e):
        self.value = self._drop.value
        if self.on_change != None:
            self.enviar_change(e)
        self.update()

    def enviar_change(self,e):
        self.on_change(self, e)


    @property
    def getvalue(self):
        return self._drop.value
    @getvalue.setter
    def getvalue(self, valor):
        self._drop.options.append(dropdown.Option(valor))
        self._drop.value = valor
        super().update()

class New_task(UserControl):
    def __init__(self,
        task_delete,
        nome='',
        duracao=3,
        inicio=70,
        fim=170,
        passo = 1,
        ):
        super().__init__()
        self.task_delete = task_delete
        self.nome_tarefa = TextField(hint_text = 'nome da tarefa', width = 200, capitalization = TextCapitalization.CHARACTERS, value = nome, height=30, border_width = 0,dense=True)
        self.duracao_tarefa = Drop_new([0.1,0.3,0.5]+[i for i in range(1,31)], duracao, width_person = 70)
        self.inicio_tarefa = Drop_new([i for i in range(30,301)], inicio, width_person = 70)
        self.fim_tarefa = Drop_new([i for i in range(30,311)], fim, width_person = 70)
        self.passo_tarefa = Drop_new([0,0.1,0.3,0.5,0.7,0.9]+[i for i in range(1,20)], passo, width_person = 70)



    def build(self):
        remover_tarefa = IconButton(icon_color ='blue',icon=icons.DELETE, on_click = self.clicked, data ='del', icon_size = 18)
        self.play_parefa = IconButton(icon_color ='blue',icon=icons.PLAY_ARROW, on_click = self.clicked, data ='play tarefa', icon_size = 18)
        pause_parefa = IconButton(icon_color ='blue',icon=icons.PAUSE, on_click = self.clicked, data ='pause tarefa', icon_size = 18)

        linha_tarefa = [
            remover_tarefa,
            self.nome_tarefa,
            self.duracao_tarefa,
            self.inicio_tarefa,
            self.fim_tarefa,
            self.passo_tarefa,
            self.play_parefa,
            pause_parefa
        ]
        # linha_tarefa = Row([Container(i, height=40, border= border.all(0.1, color = 'blue')) for i in linha_tarefa], alignment='center', expand=1)
        linha_tarefa = Row([Container_new2(i, 10,30,1) for i in linha_tarefa], tight=True, spacing=0,alignment='center', expand=1)
        # linha_tarefa = Container(linha_tarefa, height = 50, border= border.all(0.3, color = 'blue'), border_radius=13)
        
        return Container_new2(linha_tarefa, 10)
        # return linha_tarefa
    
    def clicked(self, e):
        self.task_delete(self,e)

class Slider_new(UserControl):
    def __init__(self,
                texto = None,
                 min = None,
                 max = None,
                 divisions = None,
                 fator = 1, #valor a ser multiplicado por value
                 digitos = 1,
                 width = 200,
                 on_change = None,
                 data = None, 
                 value = False,
    ):



        super().__init__()
        self.texto = texto
        self.min = min
        self.max = max
        self.divisions = divisions
        self.fator = fator
        self.digitos = digitos
        self.width = width
        self.on_change = on_change
        self.data = data
        self.value = value

        self.passo_fim2 = Slider(active_color = '#004499',thumb_color = '#333333',min = self.min, 
                                 max = self.max, divisions=self.divisions,value = self.value, 
                                 width=self.width,on_change=self.mudou, data = self.data)
        valor = round(self.passo_fim2.value*self.fator,self.digitos)
        if self.digitos == 0:
            valor = int(valor)
        self.texto2 = Text(f'{self.texto} ({valor})')

    def mudou(self,e):
        valor = round(self.passo_fim2.value*self.fator,self.digitos)
        if self.digitos == 0:
            valor = int(valor)
        self.texto2.value = f'{self.texto} ({valor})'
        self.value = valor
        self.on_change(e, self)
        self.update()

    def build(self):
        return Row([self.texto2, self.passo_fim2],alignment='start', tight = True, spacing=0,run_spacing = 0, height=30 )

    @property
    def getvalue(self):
        return self.passo_fim2.value
    @getvalue.setter
    def setvalue(self, valor):
        self.passo_fim2.value = valor
        self.value = valor
        valor2 = round(self.passo_fim2.value*self.fator,self.digitos)
        if self.digitos == 0:
            valor2 = int(valor2)
        self.texto2.value = f'{self.texto} ({valor2})'
        self.update()

class Slider_new2(UserControl):
    def __init__(self,
                texto = None,
                 min = None,
                 max = None,
                 divisions = None,
                 fator = 1, #valor a ser multiplicado por value
                 digitos = 1,
                 width = None,
                 on_change = None,
                 data = None, 
                 value = False,
                 col1 = 4,
                
    ):



        super().__init__()
        self.texto = texto
        self.min = min
        self.max = max
        self.divisions = divisions
        self.fator = fator
        self.digitos = digitos
        self.width = width
        self.on_change = on_change
        self.data = data
        self.value = value
        self.col1 = col1
        # self.getvalue = None

        self.texto2 = Text(f'{self.texto}', no_wrap = True)
        self.passo_fim2 = Slider(min = self.min, active_color = '#004499',thumb_color = '#333333',
                                 max = self.max, value = self.value, 
                                on_change=self.mudou, data = self.data,  col = 12-self.col1)
        self.caixa = TextField(value = f'{self.passo_fim2.value:.0f}', border_width = 1, width=50,height=45, dense=True , content_padding = 5,
                               text_align = "center", on_change = self.mudou2,)
        


    def mudou(self,e):
        # self.texto2.value = f'{self.texto} ({self.passo_fim2.value:.0f})'
        if self.digitos == 0:
            self.passo_fim2.value = int(self.passo_fim2.value)
        else:
            self.passo_fim2.value = round(float(self.passo_fim2.value), self.digitos)

        self.caixa.value = f'{self.passo_fim2.value}'
        if self.on_change != None:
            self.on_change(e, self)
        self.value = self.passo_fim2.value
        self.update()
    def mudou2(self,e):
        # self.texto2.value = f'{self.texto} ({self.passo_fim2.value:.0f})'
        self.passo_fim2.value = self.caixa.value 
        self.value = self.passo_fim2.value
        if self.on_change != None:
            self.on_change(e, self)
        self.update()       

    def build(self):
        return ResponsiveRow([Row([self.texto2, self.caixa], col = self.col1),self.passo_fim2, ],expand = 0,alignment='start', spacing=0,run_spacing = 0, height=30,)#,alignment='start', tight = True, spacing=0,run_spacing = 0, height=30 

    @property
    def getvalue(self):
        return self.passo_fim2.value
    @getvalue.setter
    def getvalue(self, valor):
        self.passo_fim2.value = valor
        self.value = valor
        valor2 = round(self.passo_fim2.value,self.digitos)
        if self.digitos == 0:
            valor2 = int(valor2)
        self.caixa.value = f'{valor}'
        # self.texto2.value = f'{self.texto} ({valor2})'
        self.update()

class Saidas(UserControl):
    def __init__(self,
        texto1 = '',
        texto2 = '',
        texto3 = '',
        texto4 = '',
        texto5 = '',
        texto6 = '',  
        cor = 'white',
        size = 20,                              
                  ):
        super().__init__()
        # self.t1 = texto1
        # self.t2 = texto2
        # self.t3 = texto3
        # self.t4 = texto4
        # self.t5 = texto5
        # self.t6 = texto6
        self._texto1a = Text(texto1, color = cor, size = size, visible=False)
        self._texto2a = Text(texto2, color = cor, size = size, visible=False)
        self._texto3a = Text(texto3, color = cor, size = size, visible=False)
        self._texto4a = Text(texto4, color = cor, size = size, visible=False)
        self._texto5a = Text(texto5, color = cor, size = size, visible=False)
        self._texto6a = Text(texto6, color = cor, size = size, visible=False)
        self.Visibles(                
                 texto1,
                 texto2,
                 texto3,
                 texto4,
                 texto5,
                 texto6
                 )
      
    def build(self):
        self.saida = Row(
            alignment= MainAxisAlignment.START,
            vertical_alignment = 'center',
            
            # height=300,
            tight = True,
            wrap = True,
            expand=1,
            run_spacing = 2,
            # runs_count=1,
            # max_extent=300,
            # child_aspect_ratio=8,
            # spacing=1,
            # run_spacing=10,
            # padding = 0, 
            controls=[
                        self._texto1a, self._texto2a, self._texto3a,self._texto4a,self._texto5a,self._texto6a
                    #   Column([self._texto1a, self._texto2a, self._texto3a],alignment = MainAxisAlignment.START),
                    #   Column([self._texto4a,self._texto5a,self._texto6a],alignment = MainAxisAlignment.START),
                    #   Row([],alignment = MainAxisAlignment.SPACE_AROUND),  
                                     
                      ],                                            
        )
        # self.saida = Container(self.saida, margin=margin.all(6))
        
        return self.saida
    
    def Visibles(self,                 
                 texto1,
                 texto2,
                 texto3,
                 texto4,
                 texto5,
                 texto6
                 ):
        if texto1 != '':
            self._texto1a.visible = True
        if texto2 != '':
            self._texto2a.visible = True
        if texto3 != '':
            self._texto3a.visible = True
        if texto4 != '':
            self._texto4a.visible = True
        if texto5 != '':
            self._texto5a.visible = True
        if texto6 != '':
            self._texto6a.visible = True 
    
      
    @property
    def texto1(self):       
        return self._texto1a.value
    
    @texto1.setter
    def texto1(self, texto):
        self._texto1a.value = texto 
        self._texto1a.size = 20
        self._texto1a.visible = True 
        self._texto1a.no_wrap = True
  
    @texto1.setter
    def texto1_color(self, color):
        self._texto1a.color = color
    @texto1.setter
    def texto1_size(self, size):
        self._texto1a.size = size 
    
    @property
    def texto2(self):       
        return self._texto2a.value
    
    @texto2.setter
    def texto2(self, texto):
        self._texto2a.value = texto 
        self._texto2a.size = 20
        self._texto2a.visible = True 
        self._texto2a.no_wrap = True
  
    @texto2.setter
    def texto2_color(self, color):
        self._texto2a.color = color
    @texto2.setter
    def texto2_size(self, size):
        self._texto2a.size = size 
    
    @property
    def texto3(self):       
        return self._texto3a.value
    
    @texto3.setter
    def texto3(self, texto):
        self._texto3a.value = texto 
        self._texto3a.size = 20
        self._texto3a.visible = True 
        self._texto3a.no_wrap = True
  
    @texto3.setter
    def texto3_color(self, color):
        self._texto3a.color = color
    @texto3.setter
    def texto3_size(self, size):
        self._texto3a.size = size 
    
    @property
    def texto4(self):       
        return self._texto4a.value
    
    @texto4.setter
    def texto4(self, texto):
        self._texto4a.value = texto 
        self._texto4a.size = 20
        self._texto4a.visible = True 
        self._texto4a.no_wrap = True
  
    @texto4.setter
    def texto4_color(self, color):
        self._texto4a.color = color
    @texto4.setter
    def texto4_size(self, size):
        self._texto4a.size = size 
    
    @property
    def texto5(self):       
        return self._texto5a.value
    
    @texto5.setter
    def texto5(self, texto):
        self._texto5a.value = texto 
        self._texto5a.size = 20
        self._texto5a.visible = True 
        self._texto5a.no_wrap = True
  
    @texto5.setter
    def texto5_color(self, color):
        self._texto5a.color = color
    @texto5.setter
    def texto5_size(self, size):
        self._texto5a.size = size 
    
    @property
    def texto6(self):       
        return self._texto6a.value
    
    @texto6.setter
    def texto6(self, texto):
        self._texto6a.value = texto 
        self._texto6a.size = 20
        self._texto6a.visible = True 
        self._texto6a.no_wrap = True
  
    @texto6.setter
    def texto6_color(self, color):
        self._texto6a.color = color
    @texto6.setter
    def texto6_size(self, size):
        self._texto6a.size = size 

class Saidas2(UserControl):
    def __init__(self, 
                 texto1 = '',
                 texto2 = '',
                 texto3 = '',
                 texto4 = '',
                 texto5 = '',
                 texto6 = ''
                 ):
        super().__init__()

        self.texto1 = Text(texto1, size = 20, visible=False)
        self.texto2 = Text(texto1, size = 20, visible=False)
        self.texto3 = Text(texto1, size = 20, visible=False)
        self.texto4 = Text(texto1, size = 20, visible=False)
        self.texto5 = Text(texto1, size = 20, visible=False)
        self.texto6 = Text(texto1, size = 20, visible=False)
        self.Visibles(                
                 texto1,
                 texto2,
                 texto3,
                 texto4,
                 texto5,
                 texto6
                 )
    def build(self):
        self.saida = Row(
            alignment= MainAxisAlignment.START,
            vertical_alignment = 'center',
            
            # height=300,
            tight = True,
            wrap = True,
            expand=1,
            run_spacing = 2,
            # runs_count=1,
            # max_extent=300,
            # child_aspect_ratio=8,
            # spacing=1,
            # run_spacing=10,
            # padding = 0, 
            controls=[
                      self.texto1,self.texto2,self.texto6o3,
                      self.texto4,self.texto5,self.texto6
                    #   Row([],alignment = MainAxisAlignment.SPACE_AROUND),  
                                     
                      ],                                            
        )
        # self.saida = Container(self.saida, margin=margin.all(6))
        
        return self.saida

    def Visibles(self,                 
                 texto1 ,
                 texto2,
                 texto6o3,
                 texto6o4,
                 texto6o5,
                 texto6
                 ):
        if texto1 != '':
            self.texto1.visible = True
        if texto2 != '':
            self.texto2.visible = True
        if texto6o3 != '':
            self.texto3.visible = True
        if texto6o4 != '':
            self.texto4.visible = True
        if texto6o5 != '':
            self.exto5.visible = True
        if texto6 != '':
            self.texto6.visible = True                                                            



    '''
class Pomodoro(UserControl):
    def __init__(self):
        super().__init__()
        self.pomodoro_control_thread = True
        self.tempo_pomodoro_set = 0.1
        self.Metro_normal = Metronomo()
        self.Metro_normal.pause = False
        self.parar = False
        self.tempo_descanso_value = 6
        self.quado_saida = Row()
        self.saida_respiro = Column(visible=False)



    def did_mount(self):
        self.Pomodoro()

    def build(self):
        return  Row([self.quado_saida, self.saida_respiro])  
    def Pomodoro(self):
        texto = 'Pomodoro inciado...'
        self.quado_saida.visible = True        
        self.quado_saida.controls = [Text(texto)]
        super().update()

        while self.pomodoro_control_thread:
            self.quado_saida.visible = True
            
            segundos = self.tempo_pomodoro_set*60
            while segundos >= 0:
                h, mins = divmod(segundos, 60*60)
                mins, secs = divmod(mins, 60)
                h, mins, secs = int(h), int(mins), int(secs)
                if texto != '':
                    contador = "{:s} {:02d}:{:02d}:{:02d}".format(texto,h, mins, secs)
                else:
                    contador = "{:02d}:{:02d}:{:02d}".format(h, mins, secs)

                self.quado_saida.controls = [Text(contador)]
                sleep(1)
                super().update()
                segundos -= 1
                while self.Metro_normal.pause:
                    sleep(0.3)
                if self.parar or not self.pomodoro_control_thread:
                    break

            if self.parar or not self.pomodoro_control_thread:
                self.quado_saida.visible = False
                self.quado_saida.controls = None
                break

            MessageBeep(MB_ICONHAND)

            self.Respiro()
            
            if not self.pomodoro_control_thread:
                break
            MessageBeep(MB_ICONHAND)

            if not self.pomodoro_control_thread:
                break
            texto = 'Volte a treinor por '

        self.quado_saida.controls =  None

    def Respiro(self):
        # self.Metro_normal.pause = True
        # estado_saida_treinamento = self.saida_treinamento.visible
        # estado_saida_quado = self.quado_saida.visible
        # self.saida_treinamento.visible = False
        self.quado_saida.visible = False
        self.saida_respiro.visible = True
        descan = int(self.tempo_descanso_value*60/19.4)
        # print(descan)
        # self.Metro_normal.pause = False
        self.parar = False
        width_max = 740
        respiro = Container(content=Text(),bgcolor= colors.YELLOW,width = 0, border_radius=40)
        def Inspire(d):
            # self.quado_saida.content = Text(f'INSPIRE ({d})')
            s = Saidas(f'INSPIRE ({d})', cor = colors.YELLOW, size = 50)
            # s.saida_tempo_de_treino.visible = True
            # self.saida.texto1_size = 50
            # self.saida.texto1_color= colors.YELLOW
            self.saida_respiro.controls = [Column([s, respiro])]
            # self.quado_saida.content.alignment= MainAxisAlignment.CENTER

        def Expire(d):
            s = Saidas(f'EXPIRE  ({d})', cor = colors.GREEN, size = 50)

            # s.saida_tempo_de_treino.visible = True
            # self.saida.texto1_size = 50
            # self.saida.texto1_color= colors.GREEN
            self.saida_respiro.controls = [Column([s, respiro])]
            # self.quado_saida.content.alignment= MainAxisAlignment.CENTER


        for d in range(descan,0,-1):
            a = time()
            Inspire(d)
            super().update()
            for i in range(0,width_max,6*2):
                respiro.width = i
                sleep(0.001)
                if self.parar:
                    break
                super().update()
            respiro.bgcolor = colors.GREEN
            Expire(d)
            super().update()
            if self.parar:
                break             
            for i in range(width_max,0,-1*2):
                respiro.width = i
                if self.parar:
                    break                    
                sleep(0.01567)
                super().update()
            respiro.bgcolor = colors.YELLOW
            b = time()-a
            print(b)

        # self.saida_treinamento.visible = estado_saida_treinamento
        # self.quado_saida.visible = estado_saida_quado
        # self.saida_respiro.controls = None
        self.saida_respiro.visible = False
        self.quado_saida.visible = True
        self.Metro_normal.pause = False
        respiro.width = 0
        super().update()
    '''

class SaveSelectFile(UserControl):
    def __init__(self, tipo = 'txt'):
        super().__init__()
        self.tipo = tipo
        self.pick_files_dialog = FilePicker(on_result=self.pick_files_result)
        self.nome_arquivo = None
        self.func = None

    def pick_files_result(self, e: FilePickerResultEvent):
        match self.func:
            case 'select':
                self.nome_arquivo = f'{e.files[0].path}'
            case 'save':
                self.nome_arquivo = f'{e.path}.{self.tipo}'
            case 'select_pasta':
                self.nome_arquivo = f'{e.path}'

        super().update()

        
    # @property
    def Save(self):
        self.func = 'save'
        self.pick_files_dialog.save_file(file_type = FilePickerFileType.CUSTOM, allowed_extensions = [self.tipo])
        while not self.nome_arquivo:
            sleep(0.3)
        self.update()
        return self.nome_arquivo
    
    def Select(self, tipo = None):
        self.nome_arquivo = None
        if tipo not in [None, '']:
            self.tipo = tipo
        self.func = 'select'
        self.pick_files_dialog.pick_files(file_type = FilePickerFileType.CUSTOM, allowed_extensions = [self.tipo])
        while self.nome_arquivo == None:
            sleep(0.3)
        self.update()
        return self.nome_arquivo  


    def Select_pasta(self):        
        self.func = 'select_pasta'
        self.pick_files_dialog.get_directory_path(dialog_title = 'selecione a pasta')
        while not self.nome_arquivo:
            sleep(0.3)
        self.update()
        return self.nome_arquivo            
    
    def build(self):
        return self.pick_files_dialog 
    
class Container_new3(UserControl):
    def __init__(self,
                 content = None, 
                 gradiente = ('black', 'white'),
                 height = None,
                 scale = 1,
                 border_radius = None,
                 rotação = 0.3,
                 ShadowColor = 'blue,0.6',
                 page = None,
                
        ):
        super().__init__()
        self.page = page
        self.content = content
        self.gradiente = gradiente
        self.height = height
        self.scale = scale
        self.border_radius = border_radius
        self.rot = rotação
        self.ShadowColor = ShadowColor

        self.horizontal = BorderSide(3, colors.with_opacity(0.4,'blue'))
        self.vertical = BorderSide(3, colors.with_opacity(0.9,'gray'))
        
        self.bor = Border(left=self.horizontal, top=self.horizontal, right=self.vertical, bottom=self.vertical)
        self.bor = border.all(5, colors.with_opacity(0.3,'red'))
    
        self.sombra =  BoxShadow(
            spread_radius=0,
            blur_radius=15,
            color=self.ShadowColor,
            offset=Offset(3, 3),
            blur_style=ShadowBlurStyle.NORMAL)  


        self.gradient =  gradient=LinearGradient(
            begin=Alignment(0, 1),
            end=Alignment(0, -1),
            
            colors=[
                self.gradiente[0],
                self.gradiente[0],
                self.gradiente[0],
                self.gradiente[0],
                self.gradiente[0],
                self.gradiente[1],
                        ],
            tile_mode=GradientTileMode.MIRROR,
            rotation=self.rot*3.14/180,
        )
        self.saida = Container(content=self.content,   
                         border=self.bor, 
                         shadow = self.sombra, 
                         scale = self.scale, 
                         height = self.height,
                         border_radius = self.border_radius,
                         gradient=self.gradient, 
                         padding = 0
                         )
    def build(self):
        return self.saida




def Container_new2(i, border_radius =20, height = None, scale = None, gradiente = ("black", "#777777")):
    horizontal = BorderSide(3, colors.with_opacity(0.4,'blue'))
    vertical = BorderSide(3, colors.with_opacity(0.9,'gray'))
    
    bor = Border(left=horizontal, top=horizontal, right=vertical, bottom=vertical)
    bor = border.all(5, colors.with_opacity(0.3,'red'))
    
    sombra =  BoxShadow(
        spread_radius=0,
        blur_radius=15,
        color=colors.with_opacity(0.6,'blue'),
        offset=Offset(3, 3),
        blur_style=ShadowBlurStyle.NORMAL)        
    gradiente =  gradient=LinearGradient(
        begin=Alignment(0, 1),
        end=Alignment(0, -1),
        
        colors=[
            gradiente[0],
            gradiente[0],
            gradiente[0],
            gradiente[0],
            gradiente[0],
            gradiente[1],
                    ],
        tile_mode=GradientTileMode.MIRROR,
        rotation=0*3.14/180,
    )
    return Container(content=i,   border=bor, shadow = sombra, scale = scale, height = height,border_radius = border_radius,gradient=gradiente, padding = 0)

def Botao( texto = None,  icon = None,size = 30,width = 80, height = 30,on_click = None, data = None, color  = 'blue', rot = 30, gradiente = ("black", "#777777")):   
    return Container_new2(TextButton(content = Text(texto, size=20, weight='bold', no_wrap=True, color=color), data = data,on_click=on_click, 
                                     width = width,height = height), gradiente = gradiente   )
def Botao2( texto = None,  icon = None,size = 30,width = 80, height = 50,on_click = None, data = None, color  = 'blue', rot = 30):
    bor2 = border.BorderSide(20, colors.with_opacity(1,color))
    bor = border.all(0, colors.with_opacity(0.3,'#995555')) 
    sombra =  BoxShadow(
        spread_radius=0,
        blur_radius=30,
        color=colors.with_opacity(0.6,color),
        offset=Offset(3, 3),
        blur_style=ShadowBlurStyle.NORMAL)
    gradiente =  gradient=LinearGradient(
        begin=Alignment(-1, -1),
        end=Alignment(-0.1, -0.1),
        
        colors=[
            "#777777",
            "#000000",
            "#000000",
                    ],
        tile_mode=GradientTileMode.MIRROR,
        rotation=rot*3.14/180,
    )


    if icon == None:
        conteudo = ElevatedButton(content = Text(texto, size=25, weight='bold', no_wrap=True, color=color),bgcolor = colors.with_opacity(0,'black'))
    else:
        conteudo = Icon(icon, color=color)
    return Container( 
        content= conteudo,
            # [
                # Text("1", color=colors.WHITE),
                # Text("2", color=colors.WHITE, right=0),
                # Text("3", color=colors.WHITE, right=0, bottom=0),
                # Text("4", color=colors.WHITE, left=0, bottom=0),
            # ]
        # ),
        # top = 5,
        alignment=Alignment(0, 0),
        bgcolor='green',
        width=width,
        height=height,
        # height=220,
        border_radius=15,
        on_click = on_click,
        shadow=sombra,
        gradient=gradiente,
        border= bor, 
        data = data,    
            

        )


def Slider_new3(texto,min = 10, max = 240, width=150 ):
    return Row([Row([Text(texto),Slider(min = min, max = max, width=width,active_color = '#004499',thumb_color = '#333333',)])],alignment='start', tight = True, spacing=0,run_spacing = 0, height=30 )

def main_test(page: Page):
    page.window_width = 1500
    page.window_height = 750


    t = Contador(3600, cor= 'blue', size = 15)
    # t.continuar_treinando = True
    def Parar(e):
        t.segundos = int(b.value)
    b = TextField( on_submit=Parar)

    def atualizar(e,slider):
        # Tempo_de_estudo = Slider_new2('Tempo de estudo', 10, 240,data = 'Tempo_de_estudo', width=200, value = 10, on_change = atualizar).bunda()
        print(slider)
        page.update()
   
    Tempo_de_estudo = Slider_new2('Tempo de estudo', 0, 5.0,data = 'Tempo_de_estudo', value = 4.3, on_change = atualizar, col1=2)
    # Tempo_de_estudo = Row([Text('asldjfshldkajl'),Slider(min = 10, max = 240, width=350)])
    # Tempo_de_estudo = Slider_new3('casa', 10,250,130)
    # Tempo_de_estudo = ResponsiveRow([
    # Column(col=6, controls=[Text("Column 1")]),
    # Column(col=6, controls=[Text("Column 2")])
    # ])
    largura  = Text()
    def page_resize(e):
        print("New page size:", page.window_width, page.window_height)
        print("New page size:", page.window_width, page.window_height)
        print("New page size:", page.window_width, page.window_height)
        largura.value = page.window_width
        sleep(5)
        page.update()


    page.on_resize = page_resize
    page.on_close = page_resize

    def aaa(e):
        pass
            
    conta = Container_new3(content = Text('casadas'), border_radius = 15, rotação=50, ShadowColor='blue,0.2')

    conta2 = TextButton('01', on_click=aaa)

    tab = Tabs_new(tabs = [['tab1',Column([Text('meu ovo')])], ['tab2',Column([Text('minha pica')])]])
    tab.set_height = 500
    tab.set_width = 400
    tab.Add_tab(('buceta',Container(Column([Row([Text('aoisdoaijsdoij')])]))),('tab1',Column([Text('meu ovo')])))
    
    page.add(tab)
    page.update()



if __name__ == '__main__':
    app(target=main_test)            
