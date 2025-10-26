

tasks_list = []

def add_task():
    task_data = input('Enter task details or type q to quit')
    if task_data != 'q':
        task = {
            'data' : task_data,
            'completed' : False,
        }
        tasks_list.append(task)
        print('Task is added.')
    else:
        flag = False

def view_tasks():
    num = 1
    for task in tasks_list:
        print(f'Task {num}:')
        print('Task Details:')
        print(task['data'])
        print('Task Status:')
        print('completed' if task['completed'] else 'not completed')
        num += 1

def mark_complete():
    task_num = input('Enter task number or type q to quit')
    if task_num != 'q':
        task_num = int(task_num)
        to_change = tasks_list[task_num - 1]
        to_change['completed'] = True
        print(f'task number {task_num} is marked as complete.')
    else:
        flag = False

def delete_task():
    task_num = input('Enter task number or type q to quit')
    if task_num != 'q':
        task_num = int(task_num)
        del tasks_list[task_num - 1]
        print(f'task number {task_num} is deleted.')
    else:
        flag = False

def start():
    print('Welcome to To-do-list')
    choices = {1: add_task, 2: view_tasks, 3: mark_complete, 4: delete_task}
    global flag
    flag = True
    while flag:
        print('Type q to quit anytime.\nAvailable tasks: Enter the corresponding number.')
        print('1: add task,\n2: view all tasks\n3: Mark a task completed'
            '\n4: Delete the task')
        n = input()
        if n != 'q':
            n = int(n)
            choices[n]()
        else:
            flag = False
