import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class IndicacaoFilmes:

    def __init__(self):
        self.generos = {
            'Ação': ['Ação Urbana', 'Ação militar', 'Ação Policial', 'Ação de Artes Marciais', 'Ação de Ficção '
                                                                                               'Científica',
                     'Ação de Heróis', 'Ação faroeste'],

            'Animação': ['Animação Infantil', 'Animação Adulta', 'Animação Stop-Motion', 'Animação 2D', 'Animação 3D'],

            'Aventura': ['Aventura épica', 'Aventura histórica', 'Aventura científica', 'Aventura de ação',
                         'Aventura de mistério'],

            'Comédia': ['Comédia Romântica', 'Comédia de Humor Físico', 'Comédia de Sátira', 'Comédia de Besteirol'],

            'Documentário': ['Documentário de natureza', 'Documentário histórico', 'Documentário de atualidades',
                             'Documentário de arte'],

            'Drama': ['Drama Histórico', 'Drama Contemporâneo', 'Drama Biográfico', 'Drama Familiar', 'Drama Social'],

            'Fantasia': ['Fantasia épica', 'Fantasia medieval', 'Fantasia cientifica', 'Fantasia urbana',
                         'Fantasia infantil'],

            'Ficção': ['Ficção Policial', 'Ficção de Espionagem', 'Ficção Científica', 'Ficção Histórica'],

            'Musical': ['Musical Biográfico', 'Musical de época', 'Musical teen'],

            'Romance': ['Romance clássico', 'Romance histórico', 'Romance contemporâneo', 'Romance de comédia',
                        'Romance de drama'],

            'Terror': ['Terror Sobrenatural', 'Terror Psicológico', 'Terror Gore', 'Terror Slasher', 'Terror Found '
                                                                                                     'Footage'],

            'Suspense': ['Suspense policial', 'Suspense político', 'Suspense psicológico', 'Suspense de ação',
                         'Suspense de terror'],

            'Trash': ['Thrash']
        }

        self.subgeneros = {

            # 1 = Ação
            'Ação': {
                'Ação Urbana': ['Homem-Aranha Através do Aranhaverso', 'O protetor'],

                'Ação Militar': ['O Resgate do Soldado Ryan', 'Rambo', 'Red - Aposentados e Perigosos'],

                'Ação Policial': ['Anjos da Lei', 'Tropa de Elite', 'John Wick'],

                'Ação De Artes Marciais': ['The Karate Kid', 'Creed Nascido Para Lutar',
                                           'Tudo em Todo o Lugar ao Mesmo Tempo', 'O Tigre e o Dragão'],

                'Ação De Ficção Científica': ['Avatar', 'O Planeta dos Macacos', 'Duna'],

                'Ação De Heróis': ['O Batman', 'Liga da Justiça de Zack Snyder', 'Os Vingadores'],

                'Ação Faroeste': ['Django Livre', 'Sete Homens e um Segredo', 'Era Uma Vez no Oeste'],
            },

            # 2 = Animação
            'Animação': {
                'Animação Infantil': ['Irmão Urso', 'Divertida Mente', 'Lilo & Stitch'],

                'Animação Adulta': ['Túmulo de Vagalumes', 'Festa da Salsicha'],

                'Animação De Stop-Motion': ['Coraline', 'A Noiva Cadáver', 'A Fuga das Galinhas',
                                            'O Estranho Mundo de Jack'],

                'Animação 2D': ['O Caminho para El Dorado', 'Aladdin', 'Bambi'],

                'Animação 3D': ['Procurando Nemo', 'Toy Story', 'Soul']
            },

            # 3 = Aventura
            'Aventura': {
                'Aventura Épica': ['Senhor dos Anéis A Sociedade do Anel', '007 - Operação Skyfall',
                                   'Príncipe da Pérsia - As areias do tempo'],

                'Aventura Histórica': ['Tróia', '300', 'Gladiador'],

                'Aventura Científica': ['Star Wars Episódio 1 – A Ameaça Fantasma', 'Guardiões da Galáxia',
                                        'Eu, Robô'],

                'Aventura De Ação': ['Os Mercenários', 'O Regresso', 'Mad Max Estrada da Fúria'],

                'Aventura De Mistério': ['Scooby-Doo', 'Maze Runner', 'Enola Holmes']
            },

            # 4 = Comédia
            'Comédia': {
                'Comédia Romântica': ['Esposa de Mentirinha', 'Como se Fosse a Primeira Vez',
                                      'Os Homens São de Marte e É Pra Lá Que Eu Vou', 'Minha Mãe é uma Peça'],

                'Comédia De Humor Físico': ['As Férias de Mr Bean', 'O Máskara', 'Mussum, um Filme do Cacildis'],

                'Comédia De Sátira': ['Os Vampiros que se Mordam', 'Super-Herói O filme', 'Borat - O Segundo Melhor '
                                                                                          'Repórter do Glorioso País '
                                                                                          'Cazaquistão Viaja à América'
                                      ],

                'Comédia Besteirol': ['Gente Grande', 'American Pie', 'As Branquelas']
            },

            # 5 = Documentário
            'Documentário': {
                'Documentário De Natureza': ['Nosso Planeta', 'A Marcha dos Pinguins', 'Born In China'],

                'Documentário Histórico': ['Quem Matou Malcolm X', 'Guerras do Brasil doc', 'Ascensão Império Otomano'
                                           ],

                'Documentário De Atualidades': ['O Dilema das Redes', 'Privacidade Hackeada', 'Inventando Anna',
                                                'Nascido em Gaza'],

                'Documentário De Arte': ['Emicida AmarElo - É Tudo Pra Ontem', 'Laerte-se', 'Escada para o Céu A arte'
                                                                                            ' de Cai Guo-Qiang']
            },

            # 6 = Drama
            'Drama': {
                'Drama Histórico': ['Até o último homem', 'O Último Samurai', 'Judas e o Messias Negro', 'Tetris'],

                'Drama Contemporâneo': ['Sempre ao seu Lado', 'Extraordinário'],

                'Drama Biográfico': ['Elis', 'Meu Nome é Gal', 'Carandiru O Filme'],

                'Drama Familiar': ['A Baleia', 'Ponte Para Terabithia', 'Marley & Eu'],

                'Drama Social': ['Última Parada 174', 'Irmã Dulce', 'Um Dia com Jerusa', 'Que Horas ela Volta',
                                 'Parasita', 'Infiltrado na Klan']
            },

            # 7 = Fantasia
            'Fantasia': {
                'Fantasia Épica': ['Senhor dos Anéis A Sociedade do Anel', 'As Crônicas de Nárnia O Leão A Feiticeira '
                                                                           'e o Guarda Roupa',
                                   'Harry Potter e a Pedra Filosofal'],

                'Fantasia Medieval': ['Coração de Dragão', 'Willow - Na Terra da Magia', 'Malévola', 'Eragon'],

                'Fantasia Científica': ['Blade Runner - O Caçador de Androides', 'O Preço do Amanhã', 'No Limite do '
                                                                                                      'Amanhã'],

                'Fantasia Urbana': ['Bright', 'O Lar das Crianças Peculiares', 'Animais Fantásticos e Onde Habitam'],

                'Fantasia Infantil': ['Abracadabra', 'O Castelo Animado', 'A Viagem de Chihiro']
            },

            # 8 = Ficção
            'Ficção': {
                'Ficção Policial': ['Robocop - O Policial do Futuro', 'Batman Begins', 'Blade Runner 2049'],

                'Ficção De Espionagem': ['007 - Sem Tempo para Morrer', 'Missão Impossível', 'Kingsman Serviço '
                                                                                             'Secreto'],

                'Ficção Científica': ['Interestelar', '2001 Uma Odisseia no Espaço', 'ET O Extraterrestre'],

                'Ficção Histórica': ['Ben-Hur', '12 Anos de Escravidão', '10000 AC']
            },

            # Musical
            'Musical': {
                'Musical Biográfico': ['Bohemian Rhapsody', 'Tim Maia', 'Rocketman'],

                'Musical De Época': ['Os Miseráveis', 'Chicago', 'Grease'],

                'Musical Teen': ['High School Musical', 'Camp Rock', 'Escola de Rock']
            },

            # Romance
            'Romance': {
                'Romance Clássico': ['Lendas da Paixão', 'Vestígios do Dia', 'Para Todos os Garotos que já Amei'],

                'Romance Histórico': ['Maria Antonieta', 'A Cozinheira de Castamar', 'Cidade de Gelo'],

                'Romance Contemporâneo': ['Através da Minha Janela', 'Cartas para Julieta', 'Alguém Avisa'],

                'Romance De Comédia': ['Tudo que Uma Garota Quer', 'Casamento Armado', 'Amor de Aluguel',
                                       'Os Homens são de Marte e é pra lá que eu vou'],

                'Romance De Drama': ['After', 'La La Land Cantando Estações', 'Crepúsculo', 'Me Chame Pelo Seu Nome',
                                     'Juno']
            },

            # Terror
            'Terror': {
                'Terror Sobrenatural': ['Atividade Paranormal', 'Invocação do Mal', 'Mama'],

                'Terror Psicológico': ['O Iluminado', 'Fragmentado', 'Corra!'],

                'Terror Gore': ['A Morte do Demônio', 'Terrifier', 'Jogos Mortais'],

                'Terror Slasher': ['O Massacre da Serra Elétrica', 'Pânico', 'A Hora do Pesadelo'],

                'Terror Found Footage': ['Atividade Paranormal', 'Cloverfield - Monstro', 'A Visita']
            },

            # Suspense
            'Suspense': {
                'Suspense Policial': ['Tropa de Elite 2 O Inimigo Agora é Outro', 'Cidade de Deus', 'Os Bad Boys'],

                'Suspense Político': ['Snowden', 'V de Vingança', 'Operação Valquíria'],

                'Suspense Psicológico': ['Donnie Darko', 'Coringa', 'Observador'],

                'Suspense De Ação': ['Kill Bill Volume 1', 'O Impossível', 'Uma Noite de Crime'],

                'Suspense De Terror': ['Ilha do Medo', 'A Casa Monstro', 'Sorria']
            },

            # Thrash
            'Trash': {
                'Trash': ['Rubber, O Pneu Assassino', 'Anaconda', 'Sharknado',
                          'O Ataque dos Tomates Assassinos']
            }

        }

        self.sinopses = {}
        self.carregar_sinopses()

        self.imagens = {}


    def carregar_imagens(self):
        for genero, subgeneros in self.subgeneros.items():
            for subgenero, filmes in subgeneros.items():
                for filme in filmes:

                    caminho_imagem = os.path.join("imagens", f"{filme.lower().replace(' ', '_')}.png")

                    try:
                        imagem = Image.open(caminho_imagem)
                        imagem = imagem.resize((150, 200))
                        imagem = ImageTk.PhotoImage(imagem)
                        self.imagens[filme] = imagem
                    except FileNotFoundError:
                        print(f"Imagem não encontrada para {filme}. Certifique-se de tê-la na pasta do projeto.")

    def carregar_sinopses(self):
        try:
            with open("sinopses.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:

                    partes = linha.strip().split(';')

                    if len(partes) >= 2:
                        filme = partes[0].strip()
                        sinopse = partes[1].strip()
                        self.sinopses[filme] = sinopse
        except FileNotFoundError:
            print("Arquivo 'sinopses.txt' não encontrado. Certifique-se de tê-lo criado na pasta do projeto.")

    def mostrar_sinopse(self, filme_selecionado):
        sinopse = self.sinopses.get(filme_selecionado, "Sinopse não encontrada.")
        return sinopse

    def exibir_sinopse_em_janela(self, filme_selecionado):

        sinopse = self.mostrar_sinopse(filme_selecionado)

        imagem = self.imagens.get(filme_selecionado)

        nova_janela = tk.Toplevel()

        nova_janela.title(f"Sinopse de {filme_selecionado}")

        if imagem:
            label_imagem = ttk.Label(nova_janela, image=imagem)
            label_imagem.image = imagem
            label_imagem.pack(pady=10)

        text_sinopse = tk.Text(nova_janela, height=10, width=50, wrap=tk.WORD)
        text_sinopse.pack(pady=10)
        text_sinopse.insert(tk.END, sinopse)

        text_sinopse.config(state=tk.DISABLED)


    def programa(self):
        root = tk.Tk()
        root.title("Indicação de Filmes")

        self.carregar_imagens()

        def escolher_filme():
            opcao_genero_texto = self.combo_genero.get()
            opcao_subgenero_texto = self.combo_subgenero.get()

            filmes = self.subgeneros[opcao_genero_texto].get(opcao_subgenero_texto, [])

            if not filmes:
                self.resultado.config(text="Nenhum filme encontrado para o subgênero selecionado.")
                return

            filme_escolhido = self.combo_filme.get()

            # Exibir a sinopse em uma nova janela
            self.exibir_sinopse_em_janela(filme_escolhido)

        self.label_genero = ttk.Label(root, text="Gênero:")
        self.label_genero.grid(row=0, column=0, padx=5, pady=5)

        self.combo_genero = ttk.Combobox(root, values=list(self.generos.keys()), state='readonly')
        self.combo_genero.grid(row=0, column=1, padx=5, pady=5)
        self.combo_genero.set("")

        self.label_subgenero = ttk.Label(root, text="Subgênero:")
        self.label_subgenero.grid(row=1, column=0, padx=5, pady=5)

        self.combo_subgenero = ttk.Combobox(root, values=[], state='readonly')
        self.combo_subgenero.grid(row=1, column=1, padx=5, pady=5)

        self.label_filme = ttk.Label(root, text="Filme:")
        self.label_filme.grid(row=2, column=0, padx=5, pady=5)

        self.combo_filme = ttk.Combobox(root, values=[], state='readonly')
        self.combo_filme.grid(row=2, column=1, padx=5, pady=5)

        self.button_escolher_filme = ttk.Button(root, text="Confirmar", command=escolher_filme)
        self.button_escolher_filme.grid(row=3, column=0, columnspan=2, pady=10)

        self.resultado = ttk.Label(root, text="")
        self.resultado.grid(row=4, column=0, columnspan=2, pady=10)

        def atualizar_subgenero(event):
            opcao_genero_texto = self.combo_genero.get()
            subgeneros = list(map(str.title, self.subgeneros[opcao_genero_texto]))
            self.combo_subgenero["values"] = subgeneros
            self.combo_subgenero.set("")
            atualizar_filmes()

        def atualizar_filmes(*args):

            opcao_genero_texto = self.combo_genero.get()
            opcao_subgenero_texto = self.combo_subgenero.get()

            if opcao_genero_texto and opcao_subgenero_texto:

                filmes = self.subgeneros[opcao_genero_texto].get(opcao_subgenero_texto, [])
                self.combo_filme["values"] = filmes

                if filmes:
                    self.combo_filme.set("")
                else:
                    self.combo_filme.set("")
            else:
                self.combo_filme.set("")

        self.combo_genero.bind("<<ComboboxSelected>>", atualizar_subgenero)
        self.combo_subgenero.bind("<<ComboboxSelected>>", atualizar_filmes)

        root.mainloop()



indiFilmes = IndicacaoFilmes()

indiFilmes.programa()
