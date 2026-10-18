import json
import os

Arquivo = 'tarefas.json'

# Carregar tarefas
def carregar_tarefas():
    if not os.path.exists(Arquivo):
        return []

    with open(Arquivo, 'r', encoding='UTF-8') as arquivo:
        return json.load(arquivo)


# Salvar tarefas
def salvar_tarefas(tarefas):
    with open(Arquivo, 'w', encoding='UTF-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


# Adicionar tarefa
def adicionar_tarefa(lista_de_tarefas):

    descricao = input('Digite sua tarefa: ')

    print('\nPrioridade:')
    print('1 - Alta')
    print('2 - Média')
    print('3 - Baixa')

    opcao_prioridade = input('Digite a prioridade: ')

    prioridades = {
        '1': 'Alta',
        '2': 'Média',
        '3': 'Baixa'
    }

    prioridade = prioridades.get(opcao_prioridade, 'Média')

    tarefa = {
        "descrição": descricao,
        "concluida": False,
        "prioridade": prioridade
    }

    lista_de_tarefas.append(tarefa)
    salvar_tarefas(lista_de_tarefas)

    print('Sua tarefa foi adicionada com sucesso!')


# Listar tarefas
def listar_tarefas(lista_de_tarefas):

    if not lista_de_tarefas:
        print('Não existe nenhuma tarefa cadastrada no momento.')
        return

    for i, tarefa in enumerate(lista_de_tarefas, start=1):
        status = '✅' if tarefa["concluida"] else '⬜'

        print(
            f"{i}. {status} {tarefa["descrição"]} "
            f"[Prioridade: {tarefa["prioridade"]}]"
        )


# Remover tarefa
def remover_tarefa(lista_de_tarefas):

    if not lista_de_tarefas:
        print('Não existe nenhuma tarefa para remover.')
        return

    listar_tarefas(lista_de_tarefas)

    try:
        numero_tarefa = int(input('Digite o número da tarefa: '))

        if 1 <= numero_tarefa <= len(lista_de_tarefas):
            lista_de_tarefas.pop(numero_tarefa - 1)

            salvar_tarefas(lista_de_tarefas)

            print('Tarefa removida da lista.')
        else:
            print('Número da tarefa inválido.')

    except ValueError:
        print('Digite apenas números.')


# Editar tarefa
def editar_tarefa(lista_de_tarefas):

    if not lista_de_tarefas:
        print('Não existe nenhuma tarefa para editar.')
        return

    listar_tarefas(lista_de_tarefas)

    try:
        numero_tarefa = int(
            input('Digite o número da tarefa que deseja editar: ')
        )

        if 1 <= numero_tarefa <= len(lista_de_tarefas):

            tarefa = lista_de_tarefas[numero_tarefa - 1]

            print('\nO que deseja editar?')
            print('1 - Descrição')
            print('2 - Prioridade')

            opcao_editar = input('Escolha uma opção: ')

            if opcao_editar == '1':

                nova_descricao = input(
                    'Digite a nova descrição: '
                )

                tarefa['descrição'] = nova_descricao

                salvar_tarefas(lista_de_tarefas)

                print('Descrição alterada com sucesso!')

            elif opcao_editar == '2':

                print('\nNova prioridade')
                print('1 - Alta')
                print('2 - Média')
                print('3 - Baixa')

                prioridade = input(
                    'Escolha a prioridade: '
                )

                prioridades = {
                    '1': 'Alta',
                    '2': 'Média',
                    '3': 'Baixa'
                }

                if prioridade in prioridades:

                    tarefa['prioridade'] = prioridades[prioridade]
                    salvar_tarefas(lista_de_tarefas)
                    
                    print('Prioridade alterada com sucesso!')

                else:
                    print('Prioridade inválida!')

            else:
                print('Opção inválida.')
                salvar_tarefas()

        else:
            print('Número da tarefa inválido.')

    except ValueError:
        print('Digite apenas números.')
