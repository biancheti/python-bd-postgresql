from cadastro_categoria import menu_categoria
from cadastro_produto import menu_produto
from cadastro_cliente import menu_cliente
from conexao import conecta_db

def login(conexao) -> None:
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')

    cursor = conexao.cursor()
    cursor.execute('select id, login, senha from usuario '  + 
                   'where login = %s and senha = %s', (login, senha))
    registro = cursor.fetchone()

    if registro is None:
        print('Usuario e senha invalida.')
    else:
        menu_principal()



def menu_principal():
    print('------------------------------')
    print('        MENU PROGRAMA         ')
    print('------------------------------')
    print('    1 - Categoria             ')
    print('    2 - Produto               ')
    print('    3 - Cliente               ')
    print('    4 - Venda                 ')
    print('    5 - Sair do Sistema       ')
    print('------------------------------')

    while True:
        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            menu_categoria(opcao)
        elif opcao == "2":
            menu_produto(opcao)
        elif opcao == "3":
            menu_cliente(opcao)
        elif opcao == "4":
           print('Ainda não foi implementado')
        elif opcao == "5":
            break
        else:
            print('Opção inválida, tente novamente.')


if __name__ == "__main__":
    conexao = conecta_db()
    login(conexao)