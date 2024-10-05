class ListaDeTareas:
    def __init__(self):
        self.__lista_tareas = []

    def agregarTarea(self, tarea):
        if tarea in self.__lista_tareas:
            print("La tarea no fue agregada a la lista")
        else:
            self.__lista_tareas.append(tarea)
            print("Tarea agregada correctamente a la lista")

    def quitarTarea(self, tarea):
        if tarea in self.__lista_tareas:
            self.__lista_tareas.remove(tarea)
            print("Tarea eliminada correctamente de la lista")
        else:
            print("La tarea no fue eliminada de la lista")

    def mostrarTareas(self):
        return self.__lista_tareas

tareas = ListaDeTareas()
tareas.agregarTarea("Estudiar")
tareas.agregarTarea("Trabajar")
print(tareas.mostrarTareas())
tareas.quitarTarea("Estudiar")
print(tareas.mostrarTareas())