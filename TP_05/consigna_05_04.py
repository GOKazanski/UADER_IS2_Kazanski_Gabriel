"""
4. Modifique el programa IS2_taller_scanner.py para que además la secuencia de
barrido de radios que tiene incluya la sintonía de una serie de frecuencias
memorizadas tanto de AM como de FM. Las frecuencias estarán etiquetadas
como M1, M2, M3 y M4. Cada memoria podrá corresponder a una radio de AM
o de FM en sus respectivas frecuencias específicas. En cada ciclo de barrido se
barrerán las cuatro memorias.
"""

import os

class State:
    def scan(self):
        pass

    def toggle_amfm(self):
        pass

    def toggle_memory(self):
        pass

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["590", "630", "1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def scan(self):
        print(f"Sintonizando... Estación {self.stations[self.pos]} AM")
        self.pos = (self.pos + 1) % len(self.stations)

    def toggle_amfm(self):
        print("- Cambiando a FM\n")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def scan(self):
        print(f"Sintonizando... Estación {self.stations[self.pos]} FM")
        self.pos = (self.pos + 1) % len(self.stations)

    def toggle_amfm(self):
        print("- Cambiando a AM\n")
        self.radio.state = self.radio.amstate

class MemoryStateFM(State):
    def __init__(self, radio):
        self.radio = radio
        self.memories = {
            'M1': '88.8',
            'M2': '99.9',
            'M3': '102.3',
            'M4': '103.7'
        }
        self.pos = 0
        self.name = "Memoria FM"

    def scan(self):
        keys = list(self.memories.keys())
        self.pos = (self.pos + 1) % len(self.memories)
        key = keys[self.pos]
        memory = self.memories[key]
        print("Sintonizando memoria FM... Estación {} {}".format(memory, key))

    def toggle_memory(self):
        print("- Cambiando a memoria AM\n")
        self.radio.state = self.radio.memorystateam

class MemoryStateAM(State):
    def __init__(self, radio):
        self.radio = radio
        self.memories = {
            'M1': '590',
            'M2': '630',
            'M3': '900',
            'M4': '1100'
        }
        self.pos = 0
        self.name = "Memoria AM"

    def scan(self):
        keys = list(self.memories.keys())
        self.pos = (self.pos + 1) % len(self.memories)
        key = keys[self.pos]
        memory = self.memories[key]
        print("Sintonizando memoria AM... Estación {} {}".format(memory, key))

    def toggle_memory(self):
        print("- Cambiando a memoria FM\n")
        self.radio.state = self.radio.memorystatefm

class Radio:
    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.memorystatefm = MemoryStateFM(self)
        self.memorystateam = MemoryStateAM(self)
        self.state = self.fmstate  # Initial state

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def toggle_memory(self):
        if self.state in [self.amstate, self.fmstate]:
            print("- Cambiado al estado de memoria FM\n")
            self.state = self.memorystatefm
        else:
            self.state.toggle_memory()

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")
    radio = Radio()
    actions = [radio.scan] * 4 + [radio.toggle_amfm] + [radio.scan] * 4 + [radio.toggle_memory] + [radio.scan] * 4 + [radio.toggle_memory] + [radio.scan] * 4
    for action in actions:
        action()
