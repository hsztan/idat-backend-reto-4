from json import load, decoder, dump
from time import sleep
from uuid import uuid4

data = {
    "alumnos": [],
    "docentes": []
}


class Alumnos():
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
        self.id = str(uuid4())
        self.promedio = sum(notas)/len(notas)
        self.nota_max = max(notas)
        self.nota_min = min(notas)
        data["alumnos"].append({
            "id": self.id,
            "nombre": self.nombre,
            "notas": self.notas,
            "promedio": self.promedio,
            "max_nota": self.nota_max,
            "min_nota": self.nota_min
        })

    @staticmethod
    def cargar_alumnos():
        try:
            archivo = open("alumnos.json", "r")
            data["alumnos"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando JSON de Alumnos")
            sleep(1)
            archivo = open("alumnos.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\nNo hay alumnos creados, se puede crear desde ahora")

    @classmethod
    def guardar_alumnos(cls):
        archivo = open("alumnos.json", "w")
        dump(data["alumnos"], archivo, indent=4)
        archivo.close()

    @classmethod
    def visualizar_alumnos(cls):
        if len(data["alumnos"]) == 0:
            print("No se han cargado alumnos")
        else:
            for alumno in data["alumnos"]:
                print("==================")
                for key, value in alumno.items():
                    print(key, value)
                print("==================")


class Docentes():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.id = str(uuid4())
        data["docentes"].append({
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "dni": self.dni
        })

    @staticmethod
    def cargar_docentes():
        try:
            archivo = open("docentes.json", "r")
            data["docentes"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando JSON de Docentes")
            sleep(1)
            archivo = open("docentes.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\nNo hay docentes creados, se puede crear desde ahora")

    @classmethod
    def guardar_docentes(cls):
        archivo = open("docentes.json", "w")
        dump(data["docentes"], archivo, indent=4)
        archivo.close()

    @classmethod
    def visualizar_docentes(cls):
        if len(data["docentes"]) == 0:
            print("No se han cargado docentes")
        else:
            for docente in data["docentes"]:
                print("==================")
                for key, value in docente.items():
                    print(key, value)
                print("==================")


class Coleapp():
    def __init__(self):
        Alumnos.cargar_alumnos()
        Docentes.cargar_docentes()
        self.interfaz_general()

    def interfaz_general(self):
        while True:
            print('''
                Bienvenido al colegio YourLifeIsAHack : 
                ¿Que desea gestionar?
                1) Alumnos
                2) Docentes
                3) Salir y guardar\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.interfaz_alumnos()
            if opcion == "2":
                self.interfaz_docentes()
            else:
                self.salir_guardar()

    def interfaz_alumnos(self):
        while True:
            print('''
                Escoga una opción:
                1) Agregar Alumno
                2) Visualizar Alumnos
                3) Regresar al menu anterior
                4) Salir y guardar\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.ingresar_alumnos()
            elif opcion == "2":
                Alumnos.visualizar_alumnos()
                sleep(1)
            elif opcion == "3":
                self.interfaz_general()
            else:
                self.salir_guardar()

    def interfaz_docentes(self):
        while True:
            print('''
                Escoga una opción:
                1) Agregar Docentes
                2) Visualizar Docentes
                3) Regresar al menu anterior
                4) Salir y guardar\n
            ''')
            opcion = input("> ")
            if opcion == "1":
                self.ingresar_docentes()
            elif opcion == "2":
                Docentes.visualizar_docentes()
            elif opcion == "3":
                self.interfaz_general()
            else:
                self.salir_guardar()

    def ingresar_docentes(self):
        print('''
            INGRESO DE DATOS DEL DOCENTE:
        ''')
        nombre = input("Ingrese nombre del docente:\n>")
        while True:
            try:
                edad = int(input("Ingrese la edad del docente:\n>"))
                break
            except:
                print("Ingrese una edad válida")
        dni = input("Ingrese el número de DNI del docente:\n>")
        Docentes(nombre, edad, dni)

    def ingresar_alumnos(self):
        print('''
            INGRESO DE DATOS DE ALUMNO:\n
            Ingrese nombre de alumno:
        ''')
        nombre = input("> ")
        notas = []
        num_notas = 0
        while num_notas < 4:
            print('''
                Cúantas notas desea ingresar del alumno
                mínimo deben ser 4:
            ''')
            try:
                num_notas = int(input("> "))
            except:
                print("Error, escriba un número")
        for i in range(num_notas):
            while True:
                try:
                    nota = float(
                        input(f'Ingrese nota { i + 1 } de { num_notas }:\n>'))
                    if (not nota or nota < 0 or nota > 20):
                        raise Exception
                    notas.append(nota)
                    break
                except:
                    print("Ingrese una nota de 0 - 20")
        Alumnos(nombre, notas)

    def salir_guardar(self):
        Alumnos.guardar_alumnos()
        Docentes.guardar_docentes()
        print("-------- Gracias por usar nuestro CLI -------")
        exit()


Coleapp()
