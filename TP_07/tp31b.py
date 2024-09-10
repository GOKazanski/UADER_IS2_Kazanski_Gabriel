import networkx as nx
import matplotlib.pyplot as plt

# Crear un gráfico dirigido
G = nx.DiGraph()

# Añadir las tareas y sus dependencias (ID, Duración)
tasks = {
    'A': 5,   # Requerimientos
    'B': 3,   # Arquitectura, depende de A
    'C': 10,  # Diseño, depende de A
    'D': 20,  # Test cases, depende de A
    'E': 5,   # Programa 1, depende de B, C
    'F': 6,   # Programa 2, depende de B, C
    'G': 7,   # Programa 3, depende de B, C
    'H': 10,  # Test F1, depende de E, F, D
    'I': 9,   # Test F2, depende de G, D
    'J': 12,  # System test, depende de H, I
}

# Definir las dependencias entre tareas
dependencies = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('B', 'E'),
    ('C', 'E'),
    ('B', 'F'),
    ('C', 'F'),
    ('B', 'G'),
    ('C', 'G'),
    ('E', 'H'),
    ('F', 'H'),
    ('D', 'H'),
    ('G', 'I'),
    ('D', 'I'),
    ('H', 'J'),
    ('I', 'J'),
]

# Añadir las tareas y las dependencias al gráfico
for task, duration in tasks.items():
    G.add_node(task, duration=duration, start_time=None, end_time=None)

for dep in dependencies:
    G.add_edge(dep[0], dep[1])

# Función para calcular la duración total del proyecto con 2 personas
def calculate_project_duration_two_people():
    person_1_tasks = ['A', 'B', 'C', 'F', 'G', 'I']
    person_2_tasks = ['D', 'E', 'H', 'J']
    
    person_1_time = 0
    person_2_time = 0
    
    # Simulación de ejecución de tareas para la persona 1
    for task in person_1_tasks:
        pred = list(G.predecessors(task))
        if pred:
            max_pred_time = max([G.nodes[p]['end_time'] for p in pred if G.nodes[p]['end_time'] is not None])
        else:
            max_pred_time = 0
        G.nodes[task]['start_time'] = max(person_1_time, max_pred_time)
        G.nodes[task]['end_time'] = G.nodes[task]['start_time'] + G.nodes[task]['duration']
        person_1_time = G.nodes[task]['end_time']
    
    # Simulación de ejecución de tareas para la persona 2
    for task in person_2_tasks:
        pred = list(G.predecessors(task))
        if pred:
            max_pred_time = max([G.nodes[p]['end_time'] for p in pred if G.nodes[p]['end_time'] is not None])
        else:
            max_pred_time = 0
        G.nodes[task]['start_time'] = max(person_2_time, max_pred_time)
        G.nodes[task]['end_time'] = G.nodes[task]['start_time'] + G.nodes[task]['duration']
        person_2_time = G.nodes[task]['end_time']
    
    # El proyecto termina cuando la última tarea de ambas personas se completa
    project_duration = max(person_1_time, person_2_time)
    
    return project_duration

# Calcular la duración del proyecto
project_duration = calculate_project_duration_two_people()
print(f"La duración total del proyecto con 2 personas es de {project_duration} días.")

# Visualizar la red de tareas y dependencias
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
labels = {task: f"{task} ({G.nodes[task]['duration']})" for task in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels)
plt.show()
