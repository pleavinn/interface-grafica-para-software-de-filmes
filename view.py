
import sys
import tkinter as tk
from tkinter import ttk


def donothing():
    pass


class View():
    def __init__(self):
        self.root = tk.Tk()

        self.menu()
        self.filme()
        self.status()
        self.genero()

        self.root.bind('<Escape>', self.close)

        self.root.mainloop() # ✿ comando necessário para manter a janela aberta ✿ #

    def menu(self):
        # ✿ cria o menu ✿
        menubar = tk.Menu(self.root)
        # ✿ associa o menu na barrinha de menu ✿
        self.root.config(menu=menubar)

        # ✿ cria o menu Arquivo e Ajuda ✿
        fileMenu = tk.Menu(menubar, tearoff=0)
        helpMenu = tk.Menu(menubar, tearoff=0)

        # ✿ insere os menus modo cascata ✿
        menubar.add_cascade(label='Arquivo', menu=fileMenu)
        menubar.add_cascade(label='Ajuda', menu=helpMenu)

        # ✿ insere "novo" no menu arquivo ✿
        fileMenu.add_command(label='Novo', command=self.novo)
        fileMenu.add_separator()

        # ✿ cria outro menu dentro do menu arquivo ✿
        # ✿ cria o menu ✿
        salvarMenu = tk.Menu(menubar, tearoff=0)

        # ✿ insere o menu salvar dentro do menu arquivo
        fileMenu.add_cascade(label='Salvar', menu=salvarMenu)

        # ✿ insere o salvar e salvar como ✿
        salvarMenu.add_command(label='Salvar', command=donothing)
        salvarMenu.add_command(label='Salvar Como', command=donothing)

        fileMenu.add_separator()

        # ✿ insere os ccomandos "relatorio" e "sair" dentro do menu "arquivo" ✿
        fileMenu.add_command(label='Relatório', command=self.relatorio)
        fileMenu.add_command(label='Sair', command=self.close)

        # ✿ no menu Ajuda, insere os comandos ajuda e sobre ✿
        helpMenu.add_command(label='Ajuda', command=donothing)
        helpMenu.add_command(label='Sobre', command=donothing)


    #Cria a função filme e adiciona um container para colocar label e entry "Filme" "Diretor" e "Review"#
    def filme(self):
        container = tk.Frame(self.root)
        container.pack()

        # ✿ "label" posiciona um texto na tela ✿ 
        labelFilme = tk.Label(container, width=20, text='Filme')
        # ✿ "grid" e o comando utilizado para posicionar, levando em conta colunas e linhas
        labelFilme.grid(column=0, row=0, padx=5, pady=5)

        # ✿ "entry" e o comando utilizado para inserir uma caixa de entrada de texto
        self.entryFilme = tk.Entry(container, width=20)
        # ✿ posicionando nossa caixa de texto
        self.entryFilme.grid(column=0, row=1, padx=5, pady=5)
        

        #✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿
        ###### R E P E T I N D O ###### colocando e posicionando textos e entrada de texto#
        #✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿
        labelDiretor = tk.Label(container, width=20, text='Diretor')
        labelDiretor.grid(column=0, row=2, padx=5, pady=5)
        self.entryDiretor = tk.Entry(container, width=20)
        self.entryDiretor.grid(column=0, row=3, padx=5, pady=5)

        #✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿#✿

        labelReview = tk.Label(container, width=20, text='Review')
        labelReview.grid(column=0, row=4, padx=5, pady=5)
        self.entryReview = tk.Entry(container, width=20)
        self.entryReview.grid(column=0, row=5, padx=5, pady=5)

    def status(self):
        container = tk.Frame(self.root)
        container.pack()

        labelStatus = tk.Label(container, width=20, text='Status:')
        labelStatus.grid(column=0, row=1, padx=5, pady=5)

        # cria uma variável para receber o valor do radiobutton ✿
        self.radioValue = tk.StringVar()

        # cria um radiobutton chamado assistido

        self.radioUm = tk.Radiobutton(container, text='Assistido', width=20,
                                      variable=self.radioValue, value='assistido',
                                      anchor=tk.W)
        # insere e posiciona o botao Assistido
        self.radioUm.grid(column=1, row=0, padx=5, pady=5)

        self.radioDois = tk.Radiobutton(container, text='Watchlist', width=20,
                                        variable=self.radioValue,
                                        value='listado',
                                        anchor=tk.W)
        self.radioDois.grid(column=1, row=1, padx=5, pady=5)

        self.radioTres = tk.Radiobutton(container, text='Favoritos', width=20,
                                        variable=self.radioValue,
                                        value='favoritos',
                                        anchor=tk.W)
        self.radioTres.grid(column=1, row=2, padx=5, pady=5)

    def genero(self):
        container = tk.Frame(self.root)
        container.pack()

        labelGenero = tk.Label(container, width=20, text='Gênero')
        labelGenero.grid(column=0, row=0, padx=5, pady=5)

        # cria um combobox com as opções de generos de filme ✿
    
        self.comboGenero = ttk.Combobox(container, width=20,
                                            values=['Ação',
                                                    'Aventura',
                                                    'Cinema de Arte',
                                                    'Comédia'
                                                    'Dança',
                                                    'Documentário',
                                                    'Drama',
                                                    'Espionagem',
                                                    'Faroeste',
                                                    'Fantasia',
                                                    'Ficção Científica',
                                                    'Filmes de Guerra',
                                                    'Mistério',
                                                    'Musical',
                                                    'Romance',
                                                    'Terror',])
        self.comboGenero.grid(column=1, row=0, padx=5, pady=5)


        # cria o texto nota ✿

        labelGenero = tk.Label(container, width=20, text='Nota')
        labelGenero.grid(column=0, row=1, padx=5, pady=5)

        # cria uma variável para receber a nota
        self.nota = tk.DoubleVar()

        # cria a barrinha para inserir valor
        escalaNota = tk.Scale(container, from_=0, to=100, width=20,
                                 length=200, variable=self.nota,
                                 orient=tk.HORIZONTAL)
        escalaNota.grid(column=1, row=1, padx=5, pady=5)

    # da funcao ao botao relatorio inserido no menu arquivo > quando o usuario apertar ele ira exibir os dados inseridos no terminal do vscode
    def relatorio(self):
        print('Filme:', self.entryFilme.get())
        print('Diretor:', self.entryDiretor.get())
        print('Review:', self.entryReview.get())
        print('Status:', self.radioValue.get())
        print('Genero:', self.comboGenero.get())
        print('Nota:', self.nota.get())

    # da funcao ao botao novo que ira limpar os dados inseridos
    def novo(self):
        self.entryFilme.delete(0, 100)
        self.entryDiretor.delete(0, 100)
        self.entryReview.delete(0, 100)
        self.radioUm.deselect()
        self.radioDois.deselect()
        self.radioTres.deselect()
        self.comboGenero.set('')
        self.nota.set(0)

        print('Titulo:', self.entryFilme.get())
        print('Autor:', self.entryDiretor.get())
        print('Review:', self.entryReview.get())
        print('Status:', self.radioValue.get())
        print('Genero:', self.comboGenero.get())
        print('Nota:', self.nota.get())

    def close(self, evento=None):
        sys.exit()


Janela = View()
