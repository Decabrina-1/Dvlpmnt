import tkinter as tk
from datetime import datetime

def add_task():
    task = task_entry.get("1.0", tk.END).strip()  # Изменено для Text
    if task:
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
        task_with_time = f"{timestamp} - {task}"
        task_listbox.insert(tk.END, task_with_time)
        task_entry.delete("1.0", tk.END)  # Очистка Text

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task[0])

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task[0], bg="azure4")

def on_entry_key(event):
    # Запрет переноса строки
    if event.keysym == "Return":
        return "break"

root = tk.Tk()
root.title("Блок учета задач")
root.configure(background="bisque3")

# Настройка растягивания
root.columnconfigure(0, weight=1)
root.rowconfigure(4, weight=1)

label_style = {'bg': 'bisque3', 'anchor': 'w', 'padx': 10}
entry_style = {
    'bg': 'beige',
    'bd': 2,
    'relief': 'groove',
    'wrap': 'none'  # Запрет переноса строк
}
button_style = {
    'width': 25,
    'bg': 'bisque4',
    'fg': 'white',
    'activebackground': 'bisque2',
    'activeforeground': 'black',
    'relief': 'raised'
}

# Интерфейс
tk.Label(root, text="Введите вашу задачу:", **label_style).grid(row=0, column=0, sticky='ew', pady=(10, 5))

# Фрейм для поля ввода с прокруткой
entry_frame = tk.Frame(root)
entry_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=5)

task_entry = tk.Text(
    entry_frame,
    height=1,
    **entry_style
)
scroll_entry_x = tk.Scrollbar(
    entry_frame,
    orient=tk.HORIZONTAL,
    command=task_entry.xview
)
task_entry.configure(xscrollcommand=scroll_entry_x.set)

# Привязка запрета переноса строк
task_entry.bind("<KeyPress>", on_entry_key)

task_entry.pack(side=tk.TOP, fill=tk.X)
scroll_entry_x.pack(side=tk.BOTTOM, fill=tk.X)

buttons_frame = tk.Frame(root, bg='bisque3')
buttons_frame.grid(row=2, column=0, sticky='w', padx=10, pady=5)
tk.Button(buttons_frame, text="Добавить задачу", command=add_task, **button_style).pack(side='left', padx=5)
tk.Button(buttons_frame, text="Удалить задачу", command=delete_task, **button_style).pack(side='left', padx=5)
tk.Button(buttons_frame, text="Отметить выполненную", command=mark_task, **button_style).pack(side='left', padx=5)

tk.Label(root, text="Список задач:", **label_style).grid(row=3, column=0, sticky='ew', pady=(10, 5))

# Фрейм для списка с двойной прокруткой
list_frame = tk.Frame(root)
list_frame.grid(row=4, column=0, sticky='nsew', padx=10, pady=(0, 10))

# Вертикальная и горизонтальная прокрутки
scrollbar_y = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar_x = tk.Scrollbar(list_frame, orient=tk.HORIZONTAL)

task_listbox = tk.Listbox(
    list_frame,
    bg='beige',
    bd=2,
    relief='groove',
    yscrollcommand=scrollbar_y.set,
    xscrollcommand=scrollbar_x.set,
    font=('Courier New', 10)
)

scrollbar_y.config(command=task_listbox.yview)
scrollbar_x.config(command=task_listbox.xview)

# Размещение элементов в grid
task_listbox.grid(row=0, column=0, sticky="nsew")
scrollbar_y.grid(row=0, column=1, sticky="ns")
scrollbar_x.grid(row=1, column=0, sticky="ew")

# Настройка растягивания
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

root.mainloop()