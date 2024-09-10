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

# Función para calcular el camino crítico y la duración del proyecto con recursos infinitos
def calculate_project_duration_infinite_resources():
    # Inicializar tiempos de inicio y fin
    for task in G.nodes():
        G.nodes[task]['start_time'] = 0
        G.nodes[task]['end_time'] = 0

    # Calcular los tiempos más tempranos para todas las tareas
    for task in nx.topological_sort(G):  # Ordenación topológica para respetar dependencias
        pred = list(G.predecessors(task))
        if pred:
            max_pred_time = max([G.nodes[p]['end_time'] for p in pred])
        else:
            max_pred_time = 0
        G.nodes[task]['start_time'] = max_pred_time
        G.nodes[task]['end_time'] = G.nodes[task]['start_time'] + G.nodes[task]['duration']

    # La duración total del proyecto será el fin de la última tarea
    project_duration = max([G.nodes[task]['end_time'] for task in G.nodes()])
    
    # Obtener el camino crítico
    critical_path = nx.dag_longest_path(G, weight='duration')

    return project_duration, critical_path

# Calcular la duración del proyecto con recursos infinitos
project_duration, critical_path = calculate_project_duration_infinite_resources()

# Mostrar los resultados
print(f"a) Duración total del proyecto (sin restricciones): {project_duration} días")
print(f"a) Camino crítico: {' -> '.join(critical_path)}")

# Visualizar la red de tareas y dependencias
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
labels = {task: f"{task} ({G.nodes[task]['duration']})" for task in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels)
plt.show()
