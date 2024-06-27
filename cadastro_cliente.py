from conexao import conecta_db

def consultar(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id, nome from cliente")
    registros = cursor.fetchall()
    print('------------------------------------------------')
    print('| ID        |Descrição|                         ')
    print('------------------------------------------------')
    for registro in registros:
        print(f'|  {registro[0]}  | {registro[1]}  |')
    print('-------------------------------')

def inserir(conexao):
    cursor = conexao.cursor()
    nome =    str(input('Digite o nome do cliente: '))

    sql_insert = "insert into cliente (nome) values ('"+ nome +  "')"
    cursor.execute(sql_insert)
    conexao.commit()

def alterar(conexao):
    cursor = conexao.cursor()
    id =        input('Digite o ID: ')
    nome = input('Digite o nome: ')

    sql_update = "update cliente set nome = %s where id = %s"
    dados = (nome, id)
    cursor.execute(sql_update, dados)
    conexao.commit()

def deletar(conexao):
    cursor = conexao.cursor()
    id = input('Digite o ID: ')

    sql_delete = "delete from cliente where id =" + id
    cursor.execute(sql_delete)
    conexao.commit()

def menu_cliente(opcao):

    print('------------------------------')
    print('         MENU Cliente         ')
    print('------------------------------')
    print('    1 - Consultar Cliente     ')
    print('    2 - Inserir Nome          ')
    print('    3 - Alterar Nome          ')
    print('    4 - Deletar Nome          ')
    print('    5 - Sair do Sistema       ')
    print('------------------------------')

    conexao = conecta_db()

    while True:
        
        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
        elif opcao == "3":
            alterar(conexao)
        elif opcao == "4":
            deletar(conexao)
        elif opcao == "5":
            break
        else:
            print('Opção inválida, tente novamente.')