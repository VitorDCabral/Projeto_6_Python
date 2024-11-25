def add_task(tasks, task, description, category, priority=3):
    tasks.append({'task': task, 'description': description, 'category': category, 'priority': priority, 'completed': False})

def show_tasks(tasks):
    non_completed_tasks = [task for task in tasks if not task['completed']]
    if non_completed_tasks:
        for i, task in enumerate(non_completed_tasks):
            print(f"{i + 1}. {task['task']} (Prioridade: {task['priority']}, Categoria: {task['category']})\n   Descrição: {task['description']}")
    else:
        print("Nenhuma tarefa disponível.\n")

def show_completed_tasks(completed_tasks):
    if completed_tasks:
        for i, task in enumerate(completed_tasks):
            print(f"{i + 1}. {task['task']} (Categoria: {task['category']})\n   Descrição: {task['description']}")
    else:
        print("Nenhuma tarefa concluída ainda.\n")

def prioritize(tasks, task_index, new_priority):
    if 0 <= task_index < len(tasks) and not tasks[task_index]['completed']:
        if 1 <= new_priority <= 5:
            tasks[task_index]['priority'] = new_priority
            print("Prioridade atualizada!\n")
        else:
            print("Prioridade inválida. Verifique se está entre 1 e 5.")
    else:
        print("Dados inválidos. Verifique se o índice está correto e se a tarefa não está concluída.")

def complete_task(tasks, completed_tasks, task_index):
    if 0 <= task_index < len(tasks) and not tasks[task_index]['completed']:
        tasks[task_index]['completed'] = True
        completed_tasks.append(tasks[task_index])
        print("Tarefa concluída!\n")
    else:
        print("Índice de tarefa inválido ou tarefa já concluída.")

def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks) and not tasks[task_index]['completed']:
        tasks.pop(task_index)
        print("Tarefa removida!\n")
    else:
        print("Índice de tarefa inválido ou tarefa já concluída.")

def filter_tasks(tasks):
    filter_type = input("Deseja filtrar por Categoria ou Prioridade? (Digite 'C' para Categoria ou 'P' para Prioridade): ").strip().upper()

    if filter_type == 'C':
        categories = get_categories(tasks)
        print("\nCategorias disponíveis:")
        for category in categories:
            print(f"- {category}")
        category = input("\nDigite a categoria para filtrar: ")
        filtered_tasks = [task for task in tasks if task['category'] == category]
        print(f"\nTarefas na Categoria '{category}':")
        show_filtered_tasks(filtered_tasks)
    
    elif filter_type == 'P':
        priorities = get_priorities(tasks)
        print("\nPrioridades disponíveis:")
        for priority in priorities:
            print(f"- {priority}")
        priority = int(input("\nDigite a prioridade para filtrar (1-5): "))
        filtered_tasks = [task for task in tasks if task['priority'] == priority]
        print(f"\nTarefas com Prioridade '{priority}':")
        show_filtered_tasks(filtered_tasks)

    else:
        print("Opção inválida. Tente novamente.\n")

def show_filtered_tasks(filtered_tasks):
    for i, task in enumerate(filtered_tasks):
        if not task['completed']:
            print(f"{i + 1}. {task['task']} (Prioridade: {task['priority']}, Categoria: {task['category']})\n   Descrição: {task['description']}")

def get_categories(tasks):
    categories = set(task['category'] for task in tasks)
    return categories

def get_priorities(tasks):
    priorities = set(task['priority'] for task in tasks)
    return priorities

def main():
    tasks = []
    completed_tasks = []
    print("Bem-vindo à sua Lista de Tarefas!\n")

    while True:
        print("1. Adicionar Tarefa")
        print("2. Mostrar Tarefas")
        if tasks:  # Só mostrar essas opções se houver tarefas adicionadas
            print("3. Priorizar Tarefa")
            print("4. Concluir Tarefa")
            print("5. Remover Tarefa")
        if completed_tasks:  # Mostrar a opção de ver tarefas concluídas se houver alguma
            print("6. Mostrar Tarefas Concluídas")
        if tasks:
            print("7. Filtrar Tarefas")
        print("8. Sair")
        
        choice = input("Escolha uma opção: ")

        if choice == '1':
            while True:
                task = input("Digite a descrição da tarefa: ").strip()
                if task:
                    break
                else:
                    print("A descrição da tarefa não pode estar vazia. Por favor, digite novamente.")
            while True:
                description = input("Digite a descrição do que precisa ser feito: ").strip()
                if description:
                    break
                else:
                    print("A descrição não pode estar vazia. Por favor, digite novamente.")
            while True:
                category = input("Digite a categoria da tarefa: ").strip()
                if category:
                    break
                else:
                    print("A categoria não pode estar vazia. Por favor, digite novamente.")
            while True:
                try:
                    priority = int(input("Digite a prioridade da tarefa (1-5): "))
                    if 1 <= priority <= 5:
                        break
                    else:
                        print("Por favor, insira uma prioridade entre 1 e 5.")
                except ValueError:
                    print("Por favor, insira um número válido.")
            add_task(tasks, task, description, category, priority)
            print("Tarefa adicionada!\n")

        elif choice == '2':
            if tasks and any(not task['completed'] for task in tasks):
                print("\nLista de Tarefas:")
                show_tasks(tasks)
                print()
            else:
                print("Nenhuma tarefa disponível.\n")

        elif choice == '3' and tasks:
            if any(not task['completed'] for task in tasks):
                show_tasks(tasks)
                while True:
                    try:
                        task_index = int(input("Digite o número da tarefa que deseja priorizar: ")) - 1
                        new_priority = int(input("Digite a nova prioridade (1-5): "))
                        if 0 <= task_index < len(tasks) and 1 <= new_priority <= 5:
                            prioritize(tasks, task_index, new_priority)
                            break
                        else:
                            print("Por favor, insira um índice e prioridade válidos.")
                    except ValueError:
                        print("Por favor, insira um número válido.")
            else:
                print("Nenhuma tarefa disponível para priorizar.\n")

        elif choice == '4' and tasks:
            if any(not task['completed'] for task in tasks):
                show_tasks(tasks)
                while True:
                    try:
                        task_index = int(input("Digite o número da tarefa que deseja concluir: ")) - 1
                        if 0 <= task_index < len(tasks):
                            complete_task(tasks, completed_tasks, task_index)
                            break
                        else:
                            print("Por favor, insira um índice válido.")
                    except ValueError:
                        print("Por favor, insira um número válido.")
            else:
                print("Nenhuma tarefa disponível para concluir.\n")
        
        elif choice == '5' and tasks:
            if any(not task['completed'] for task in tasks):
                show_tasks(tasks)
                while True:
                    try:
                        task_index = int(input("Digite o número da tarefa que deseja remover: ")) - 1
                        if 0 <= task_index < len(tasks):
                            remove_task(tasks, task_index)
                            break
                        else:
                            print("Por favor, insira um índice válido.")
                    except ValueError:
                        print("Por favor, insira um número válido.")
            else:
                print("Nenhuma tarefa disponível para remover.\n")

        elif choice == '6' and completed_tasks:
            print("\nTarefas Concluídas:")
            show_completed_tasks(completed_tasks)
            print()

        elif choice == '7' and tasks:
            filter_tasks(tasks)
            print()

        elif choice == '8':
            print("Saindo...")
            break

        else:
            print("Opção inválida ou nenhuma tarefa adicionada ainda. Tente novamente.\n")

if __name__ == "__main__":
    main()
