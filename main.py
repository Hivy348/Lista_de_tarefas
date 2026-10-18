from to_do_list import *

def main():

    lista_de_tarefas = carregar_tarefas()

    while True:

        print('\n=== Lista de Tarefas ===\n')
        print('1. Adicionar tarefa')
        print('2. Listar tarefas')
        print('3. Remover tarefa')
        print('4. Editar tarefa')
        print('5. Sair')

        opcao = input('Digite a opção: ')

        if opcao == '1':
            adicionar_tarefa(lista_de_tarefas)

        elif opcao == '2':
            listar_tarefas(lista_de_tarefas)

        elif opcao == '3':
            remover_tarefa(lista_de_tarefas)

        elif opcao == '4':
            editar_tarefa(lista_de_tarefas)

        elif opcao == '5':
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida. Digite uma opção de 1 a 5.')


if __name__ == "__main__":
    main()