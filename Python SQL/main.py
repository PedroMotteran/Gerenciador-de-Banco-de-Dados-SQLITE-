import pyodbc
from tkinter import *
from tkinter import ttk






def verificar_usuario():
    #codigo para verificar se o usuario está no banco de dados
    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=Projeto_Compras.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?',(nome_do_usuario_entry.get()), (senha_do_usuario_entry.get()))    
    credenciais = cursor.fetchone()

    if credenciais:
        main_Window.destroy()
        


        dadosConexao = ("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=Projeto_Compras.db")

        #CRIANDO A CONEXÃO
        conexao = pyodbc.connect(dadosConexao)
        print('conectado com sucesso brother')
        #FERRAMENTA QUE VOU USAR PARA EXECUTAR COMANDOS EM SQL
        cursor = conexao.cursor()

        #AGORA VOU SELECIONARA TABELA QUE EU QUERO PUXAR OS DADOS
        cursor.execute("Select * From Usuarios")

        tabelaUsuarios = cursor.fetchall()

        tela_cadastro = Tk()
        tela_cadastro.title
        tela_cadastro.configure(bg='#33CC33')
        tela_cadastro.attributes('-fullscreen', True)

        def listar_dados():
            for a in treeview.get_children():
                treeview.delete(a)
            cursor.execute('Select * From Produtos')
            dados = cursor.fetchall()
            for valores in dados:
                treeview.insert('', 'end', values=(valores[0], valores[1], valores[2], valores[3]))
            

        def cadastrar():
            janela_cadastrar = Toplevel(tela_cadastro) 
            janela_cadastrar.title('Janela de cadstro')
            janela_cadastrar.configure(bg='#F5F5F5')

            largura_window = 450
            altura_window = 226

            #OBTENDO AS MEDIDAS DA TELA DO COMPUTADOR
            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()

            #DEFINIR A POSIÇÃO INICIAL DA MAIN_WINDOW
            pos_x = (largura_tela // 2) - (largura_window // 2)
            pos_y = (altura_tela // 2) - (altura_window // 2)

            dados = cursor.fetchall()
            for valores in dados:
                treeview.insert('', 'end', values=(valores[0], valores[1], valores[2], valores[3]))

            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_window, altura_window, pos_x, pos_y))

            for i in range(3):
                janela_cadastrar.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i, weight=1)

        
            estilo_borda = {'borderwidth': 2, 'relief' : 'groove'}
            Label(janela_cadastrar, text='Nome do produto:', font='Arial 12', bg='#FFFFFF', ).grid(row=0, column=0, padx=10, pady=10, stick='W')
            nome_produto_cadastrar = Entry(janela_cadastrar, font='Arial 12', **estilo_borda)
            nome_produto_cadastrar.grid(row=0, column=1, padx=10, pady=10)

            Label(janela_cadastrar, text='Descrição do produto:', font='Arial 12', bg='#FFFFFF', ).grid(row=1, column=0, padx=10, pady=10, stick='W')
            descricao_produto_cadastrar = Entry(janela_cadastrar, font='Arial 12', **estilo_borda)
            descricao_produto_cadastrar.grid(row=1, column=1, padx=10, pady=10)

            Label(janela_cadastrar, text='Preço do produto:', font='Arial 12', bg='#FFFFFF', ).grid(row=2, column=0, padx=10, pady=10, stick='W')
            preco_produto_cadastrar = Entry(janela_cadastrar, font='Arial 12', **estilo_borda)
            preco_produto_cadastrar.grid(row=2, column=1, padx=10, pady=10)



            def salvar_dados():
                #CRIEI UMA TUPLA COM OS VALORES DE NOME DESCRIÇAO E PREÇO
                novo_produto_cadastro = (nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get())

                cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, Preco) Values(?, ?, ?)", novo_produto_cadastro)
                conexao.commit()
                print('Dados salvos com sucesso')
                janela_cadastrar.destroy()
                listar_dados()

            botao_salvar_dados = Button(janela_cadastrar, text='Salvar dados', font=('Arial', 12), command=salvar_dados)
            botao_salvar_dados.grid(row=3, column=0, columnspan=2, padx=10, pady=5, stick='NSEW')

            botao_cancelar = Button(janela_cadastrar, text='Cancelar', font=('Arial', 12), command=janela_cadastrar.destroy)
            botao_cancelar.grid(row=4, column=0, columnspan=2, padx=10, pady=5, stick='NSEW')


                
        botao_novo_produto = Button(tela_cadastro, text='Novo Produto', font='Arial 18', command=cadastrar)
        botao_novo_produto.grid(row=7, column=0, columnspan=4, stick='NSEW', pady=10, padx=10)



        Label(tela_cadastro, text='Nome do Produto:', font='Arial 16', bg='#F5F5F5').grid(row=0, column=2, padx=10, pady=10)
        pesquisa_produto = Entry(tela_cadastro, font='Arial 16')
        pesquisa_produto.grid(row=0, column=3, padx=10, pady=10)

        Label(tela_cadastro, text='Descrição do Produto:', font='Arial 16', bg='#F5F5F5').grid(row=0, column=4, padx=10, pady=10)
        pesquisa_desc = Entry(tela_cadastro, font='Arial 16')
        pesquisa_desc.grid(row=0, column=5, padx=10, pady=10)

        Label(tela_cadastro, text='Produtos', font='Arial 16', fg='Blue',bg='#F5F5F5').grid(row=2, column=0, padx=10, pady=10)


        #CONFIGURA A JANELA PARA A BARRA DE MENUS QUE VAI SER USADA
        menu_barra = Menu(tela_cadastro)
        tela_cadastro.configure(menu=menu_barra)


        #CRIANDO E CONFIGURANDO A TREEVIEW
        style = ttk.Style(tela_cadastro)
        treeview = ttk.Treeview(tela_cadastro, style='mystyle.Treeview')

        style.theme_use('default')
        style.configure('mystyle.Treeview', font='Arial 14')
        treeview = ttk.Treeview(tela_cadastro, style='mystyle.Treeview', columns=('ID', 'NomeProduto', 'Descricao', 'Preco'), show='headings', height='20')

        #NO PRIMEIRO CAMPO É O QUE ESTÁ NO BANCO DE DADOS, NO SEGUNDO É COMO O USUÁRIO VAI VER O TITULO
        treeview.heading('ID', text='ID')
        treeview.heading('NomeProduto', text='Nome do Produto')
        treeview.heading('Descricao', text='Descrição do Produto')
        treeview.heading('Preco', text='Preço')

        treeview.column('#0', width=0, stretch=NO)
        treeview.column('ID', width=100)
        treeview.column('NomeProduto', width=300)
        treeview.column('Descricao', width=500)
        treeview.column('Preco', width=200)

        treeview.grid(row=3, column=0, columnspan=10, stick='NSEW')

        #chama a função de listar dados na treeview
        listar_dados()

        def editar_dados(event):
            item_selecionado = treeview.selection()[0]

            #Obtem os valores do item selecionado
            valores_selecionados = treeview.item(item_selecionado)['values']

            janela_edicao = Toplevel(tela_cadastro) 
            janela_edicao.title('Janela de Edição do Produto')
            janela_edicao.configure(bg='#F5F5F5')

            largura_window = 450
            altura_window = 226

            #OBTENDO AS MEDIDAS DA TELA DO COMPUTADOR
            largura_tela = janela_edicao.winfo_screenwidth()
            altura_tela = janela_edicao.winfo_screenheight()

            #DEFINIR A POSIÇÃO INICIAL DA MAIN_WINDOW
            pos_x = (largura_tela // 2) - (largura_window // 2)
            pos_y = (altura_tela // 2) - (altura_window // 2)

            dados = cursor.fetchall()
            for valores in dados:
                treeview.insert('', 'end', values=(valores[0], valores[1], valores[2], valores[3]))

            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_window, altura_window, pos_x, pos_y))

            for i in range(3):
                janela_edicao.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_edicao.grid_columnconfigure(i, weight=1)

        
            estilo_borda = {'borderwidth': 2, 'relief' : 'groove'}
            Label(janela_edicao, text='Nome do produto:', font='Arial 16', bg='#FFFFFF', ).grid(row=0, column=0, padx=10, pady=10, stick='W')
            nome_produto_edicao = Entry(janela_edicao, font='Arial 16', **estilo_borda, bg='#FFFFFF', textvariable=StringVar(value=valores_selecionados[1]))
            nome_produto_edicao.grid(row=0, column=1, padx=10, pady=10)

            Label(janela_edicao, text='Descrição do produto:', font='Arial 16', bg='#FFFFFF', ).grid(row=1, column=0, padx=10, pady=10, stick='W')
            descricao_produto_edicao = Entry(janela_edicao, font='Arial 16', **estilo_borda, bg='#FFFFFF', textvariable=StringVar(value=valores_selecionados[2]))
            descricao_produto_edicao.grid(row=1, column=1, padx=10, pady=10)

            Label(janela_edicao, text='Preço do produto:', font='Arial 16', bg='#FFFFFF', ).grid(row=2, column=0, padx=10, pady=10, stick='W')
            preco_produto_edicao = Entry(janela_edicao, font='Arial 16', **estilo_borda, bg='#FFFFFF', textvariable=StringVar(value=valores_selecionados[3]))
            preco_produto_edicao.grid(row=2, column=1, padx=10, pady=10)



            def salvar_edicao():
                #CRIEI UMA TUPLA COM OS VALORES DE NOME DESCRIÇAO E PREÇO

                novo_produto = nome_produto_edicao.get()
                descricao_nova = descricao_produto_edicao.get()
                preco_novo = preco_produto_edicao.get()

                treeview.item(item_selecionado, values=(valores_selecionados[0], novo_produto, descricao_nova, preco_novo))


                cursor.execute("UPDATE Produtos SET NomeProduto = ?, Descricao = ?, Preco = ? WHERE ID = ? ",
                (novo_produto, descricao_nova, preco_novo, valores_selecionados[0]))

                conexao.commit()
                print('Dados alterados com sucesso')
                janela_edicao.destroy()
                listar_dados()

            botao_salvar_edicao = Button(janela_edicao, text='Salvar Edição', font=('Arial', 12), bg='#00FF00',command=salvar_edicao)
            botao_salvar_edicao.grid(row=4, column=0, padx=20, pady=10)

            def deletar_registro():
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)['values'][0]


                #comando para deletar o item 
                cursor.execute("DELETE FROM Produtos WHERE id = ? ", (id))

                conexao.commit()
                janela_edicao.destroy()

                #ATUALIZA OS DADOS SEM O NOVO REGISTRO
                listar_dados()

            botao_deletar_edicao = Button(janela_edicao, text='Deletar', font=('Arial', 12), bg='#FF0000', command=deletar_registro)
            botao_deletar_edicao.grid(row=4, column=1, columnspan=2, padx=20, pady=10)


        pesquisa_produto.bind('<KeyRelease>', lambda e: filtrar_dados(pesquisa_produto.get(), pesquisa_desc.get()))
        pesquisa_desc.bind('<KeyRelease>', lambda e: filtrar_dados(pesquisa_produto.get(), pesquisa_desc.get()))



        #ao dar 2 cliques na treeview ela será editável
        treeview.bind("<Double-1>", editar_dados)


        #PEGUEI OS CAMPOS DE ENTRY DO "PESQUISA PRODUTO" E "PESQUISA DESC" E VOU APLICAR O COMANDO BIND("<KeyRealese>"), QUE VAI COLETAR OS DADOS INSERIDOS NO CAMPO
        # E VAI EXECUTAR UMA FUNÇÃO LAMBDA, ELA RECEBE UM OBJETO DE EVENTO, ABREVIADO COMO 'E', E DEPOIS DISSO EXECUTA UMA FUNÇÃO, A DE FILTRAR DADOS


        def deletar():
            selected_item = treeview.selection()[0]
            id = treeview.item(selected_item)['values'][0]


            #comando para deletar o item 
            cursor.execute("DELETE FROM Produtos WHERE id = ? ", (id))

            conexao.commit()
            #ATUALIZA OS DADOS SEM O NOVO REGISTRO
            listar_dados()


        botao_deletar_item_selecionado = Button(tela_cadastro, text='Deletar', font='Arial 16' ,bg='#FF0000', command=deletar)
        botao_deletar_item_selecionado.grid(row=7, column=6, columnspan=4, stick='NSEW', pady=10, padx=10)



        #CRIANDO O MENU CHAMADO ARQUIVO
        menu_arquivo = Menu(menu_barra, tearoff=0)
        menu_barra.add_cascade(label='Arquivo', menu=menu_arquivo)

        #CRIA UMA OPÇÃO DENTRO DO MENU "ARQUIVO" QUE SE CHAMA 'Cadastrar'
        menu_arquivo.add_command(label='Cadastrar', command=cadastrar)

        #CRIA UMA OPÇÃO DENTRO DO MENU "ARQUIVO" QUE SE CHAMA 'Sair'
        menu_arquivo.add_command(label='Sair', command=tela_cadastro.destroy)

        def limpa_dados():
            

            #LIMPANDO OS DADOS (LINHA POR LINHA) NA TREEVIEW
            for i in treeview.get_children():
                treeview.delete(i)


        def filtrar_dados(a , b):
            if not pesquisa_produto.get() and not pesquisa_desc.get():

                listar_dados()
                #se estiverem vazios nao vai fazer nada
                return
            sql = "SELECT * From Produtos"
            parametro = []

            if pesquisa_produto.get():
                sql += " WHERE NomeProduto LIKE ?"

                parametro.append('%' + pesquisa_produto.get() + '%')
                
                '''Adiciona um parâmetro de consulta à lista 'parametro'.
                Esse parâmetro é uma string que é composta por três partes concatenadas:
                1 - O caractere curinga '%' no início da string, que representa qualquer
                número de caracteres (ou nenhum) antes do padrão de correspondência de
                texto.
                2 - O valor do campo 'pesquisa_produto' (obtido com o método 'get()' do
                widget de entrada de texto correspondente).
                3 - Outro caractere curinga '%' e no final da string, que representa
                qualquer número de caracteres (ou nenhum) depois do padrão de
                correspondência de texto.

                Essa string será usada como o valor do parâmetro na cláusula 'LIKE'
                da consulta SQL, permitindo que a consulta retorne registros que
                tenham o campo 'NomeProduto' correspondente ao padrão especificado
                pelo usuário na interface do programa. Em resumo, essa linha de
                código está criando um parâmetro de consulta dinamicamente com base
                no texto digitado pelo usuário e adicionando-o à lista de parâmetros
                que serão usados na consulta SQL. '''
            
            if pesquisa_desc.get():
                if pesquisa_produto.get():
                    sql += " AND"
                else:
                    sql += " WHERE"
                sql += " Descricao LIKE ?"
                
                parametro.append('%' + pesquisa_desc.get() + '%')

            cursor.execute(sql, tuple(parametro))
            produtos = cursor.fetchall()

            limpa_dados()

            for dado in produtos:
                treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3]))





        tela_cadastro.mainloop()
        
    else:
        mensagem_de_erro = Label(main_Window, text='Usuário ou senha incorretos', font='Arial 8', fg='Red')
        mensagem_de_erro.grid(row=4, column=0, columnspan=2)




#CRIANDO A JANELA
main_Window = Tk()
main_Window.title("Tela de login")

#DEFININDO UMA COR DE FUNDO PARA A JANELA]
#bg - cor do background
main_Window.configure(bg="#0099CC")

largura_window = 450
altura_window = 300

#OBTENDO AS MEDIDAS DA TELA DO COMPUTADOR
largura_tela = main_Window.winfo_screenwidth()
altura_tela = main_Window.winfo_screenheight()

#DEFINIR A POSIÇÃO INICIAL DA MAIN_WINDOW
pos_x = (largura_tela // 2) - (largura_window // 2)
pos_y = (altura_tela // 2) - (altura_window // 2)

main_Window.geometry('{}x{}+{}+{}'.format(largura_window, altura_window, pos_x, pos_y))

#DEFINIDO A APARENCIA DA NOSSA JANELA 
#font - fonte da letra
#fg - cor da letra
title_lbl = Label(main_Window, text="Faça seu login", font="Arial 20", fg='Black', bg="#0099CC")

#grid - essa função vai seperar a janela de forma que ela fique como uma tabela
#row - é a linha 
#column - é a coluna
#columnspan - é quantas colunas vai ocupar
#pady - espaço que vai ocupar dentro da janela
title_lbl.grid(row=0, column=0, columnspan=3, pady=20)


#CRIANDO A TELA DE LOGIN - nome do usuario
nome_do_usuario_txt = Label(main_Window, text="Nome de usuário:", font="Arial 12 bold", fg='Black', bg="#0099CC")
nome_do_usuario_txt.grid(row=2, column=0, stick='e')

#CRIANDO A TELA DE LOGIN - senha do usuario
senha_do_usuario_txt = Label(main_Window, text='Senha:', font='Arial 12 bold', fg='Black', bg='#0099CC')
senha_do_usuario_txt.grid(row=3, column=0, stick='e')

#CRIANDO O INPUT DO NOME DE USUARIO
nome_do_usuario_entry = Entry(main_Window, font='Arial 12')
nome_do_usuario_entry.grid(row=2, column=1, pady=10)


senha_do_usuario_entry = Entry(main_Window, show='*',font='Arial 12')
senha_do_usuario_entry.grid(row=3, column=1, pady=10)

#CRIANDO O BOTAO DE ENTRAR - VERIFICA SE O USUARUIO ESTA NO BANCO DE DADOS
entry_btn = Button(main_Window, text='Entrar', font='Arial 12', command=verificar_usuario)
entry_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, stick='NSEW')

#CRIANDO O BOTAO DE SAIR DA APLICAÇÃO
sair_btn = Button(main_Window, text='Sair', font='Arial 12', command=main_Window.destroy)
sair_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, stick='NSEW')

for i in range(6):
    main_Window.grid_rowconfigure(i, weight=1)

for i in range(2):
    main_Window.grid_columnconfigure(i, weight=1)

#INICIAR A JANELA
main_Window.mainloop()

