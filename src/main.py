"""
TaskTracker - Aplicação de linha de comando (CLI) para gerenciamento de tarefas.

Bootcamp II - Fase 2 (Entrega Intermediária)
Implementa a lógica planejada na Fase 1: cadastro, listagem e validação
das regras de negócio (título obrigatório e prioridade restrita).
"""

PRIORIDADES_VALIDAS = {"alta": "Alta", "media": "Média", "média": "Média", "baixa": "Baixa"}


def validar_titulo():
    """Pede o título da tarefa até que um valor não vazio seja informado."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("⚠️  O título não pode ser vazio. Tente novamente.\n")


def validar_prioridade():
    """Pede a prioridade até que um valor válido (Alta, Média ou Baixa) seja informado."""
    while True:
        prioridade = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if prioridade in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[prioridade]
        print("⚠️  Prioridade inválida. Use apenas: Alta, Média ou Baixa.\n")


def cadastrar_tarefa(tarefas):
    """Cadastra uma nova tarefa na lista, aplicando as validações obrigatórias."""
    print("\n--- Cadastro de Nova Tarefa ---")
    titulo = validar_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA ou deixe em branco): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não definida",
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"\n✅ Tarefa '{titulo}' cadastrada com sucesso!\n")


def visualizar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas, ou uma mensagem caso a lista esteja vazia."""
    print("\n--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.\n")
        return

    ordem_prioridade = {"Alta": 0, "Média": 1, "Baixa": 2}
    tarefas_ordenadas = sorted(tarefas, key=lambda t: ordem_prioridade[t["prioridade"]])

    for i, tarefa in enumerate(tarefas_ordenadas, start=1):
        print(f"\nTarefa {i}")
        print(f"  Título      : {tarefa['titulo']}")
        print(f"  Descrição   : {tarefa['descricao'] or 'Sem descrição'}")
        print(f"  Prioridade  : {tarefa['prioridade']}")
        print(f"  Data limite : {tarefa['data_limite']}")
        print(f"  Status      : {tarefa['status']}")

    pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    concluidas = sum(1 for t in tarefas if t["status"] == "Concluída")
    print(f"\nTotal: {pendentes} pendente(s) | {concluidas} concluída(s)\n")


def exibir_menu():
    print("=" * 40)
    print("           TASKTRACKER - MENU")
    print("=" * 40)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=" * 40)


def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("\n⚠️  Opção inválida. Escolha 1, 2 ou 3.\n")


if __name__ == "__main__":
    main()
