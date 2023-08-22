from todo import Todo, TodoBook

# Crear una instancia de TodoBook
todo_book = TodoBook()

# Agregar tareas a la lista de todos
todo_id1 = todo_book.add_todo("Tarea 1", "Descripción de la tarea 1")
todo_id2 = todo_book.add_todo("Tarea 2", "Descripción de la tarea 2")

# Marcar una tarea como completada
todo_book.todos[todo_id1].mark_completed()

# Agregar etiquetas a las tareas
todo_book.todos[todo_id1].add_tag("importante")
todo_book.todos[todo_id2].add_tag("urgente")

# Obtener tareas pendientes y completadas
pending_todos = todo_book.pending_todos()
completed_todos = todo_book.completed_todos()

# Obtener el recuento de etiquetas de tareas
tag_count = todo_book.tags_todo_count()

# Imprimir información
for todo in pending_todos:
    print("Pendiente:", todo)

for todo in completed_todos:
    print("Completada:", todo)

print("Recuento de etiquetas:", tag_count)