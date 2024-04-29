"""
5. Modifique el programa IS2_taller_memory.py para que la clase tenga la
capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar los
mismos en cualquier orden de ser necesario. El método undo deberá tener un
argumento adicional indicando si se desea recuperar el inmediato anterior (0) y
los anteriores a el (1,2,3).
"""
import os

#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo con capacidad de almacenar hasta 4 estados
#*-------------------------------------------------------------------
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def __init__(self):
        self.mementos = []

    def save(self, writer):
        if len(self.mementos) >= 4:
            self.mementos.pop(0)  # Elimina el estado más antiguo si ya hay 4
        self.mementos.append(writer.save())

    def undo(self, writer, index):
        if 0 <= index < len(self.mementos):
            writer.undo(self.mementos[index])

if __name__ == '__main__':
    os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones I\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional V")
    writer.write("Material adicional de la clase de patrones V\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se muestra el estado actual")
    print(writer.content + "\n")

    print("Se invoca al <undo> para recuperar el estado más reciente")
    caretaker.undo(writer, 2)  # Recupera el estado con índice 2

    print("Se muestra el estado actual")
    print(writer.content + "\n")

    ind_undo= int(input("Ingrese el numero de indice a recuperar: "))
    caretaker.undo(writer, ind_undo)

    print("Se muestra el estado actual")
    print(writer.content + "\n")