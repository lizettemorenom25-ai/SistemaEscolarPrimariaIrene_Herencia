
# SISTEMA ESCOLAR PRIMARIA IRENE
# Proyecto de Programacion Orientada a Objetos
# Aplicacion del concepto de herencia


# ==========================================
# 1. CLASE BASE: PERSONA
# ==========================================

class Persona:
    def __init__(self, nombre, edad):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")

        if not isinstance(edad, int) or isinstance(edad, bool) or edad <= 0:
            raise ValueError("La edad debe ser un entero mayor que cero.")

        self.nombre = nombre.strip()
        self.edad = edad

    # Metodo heredable para mostrar informacion
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


# ==========================================
# 2. CLASE DERIVADA: ESTUDIANTE
# ==========================================

class Estudiante(Persona):

    def __init__(self, matricula, nombre, edad, grado):
        # Reutiliza el constructor de Persona
        super().__init__(nombre, edad)

        if not isinstance(matricula, str) or not matricula.strip():
            raise ValueError("La matricula no puede estar vacia.")

        if not isinstance(grado, str) or not grado.strip():
            raise ValueError("El grado no puede estar vacio.")

        self.matricula = matricula.strip()
        self.grado = grado.strip()

    # Sobrescribe el metodo heredado y agrega datos propios
    def mostrar_info(self):
        print(f"Matricula: {self.matricula}")
        super().mostrar_info()
        print(f"Grado: {self.grado}")
        print("-" * 35)


# ==========================================
# 3. CLASE DERIVADA: PROFESOR
# ==========================================

class Profesor(Persona):

    def __init__(self, numero_empleado, nombre, edad, asignatura):
        # Reutiliza los atributos de Persona
        super().__init__(nombre, edad)

        if not isinstance(numero_empleado, str) or not numero_empleado.strip():
            raise ValueError("El numero de empleado no puede estar vacio.")

        if not isinstance(asignatura, str) or not asignatura.strip():
            raise ValueError("La asignatura no puede estar vacia.")

        self.numero_empleado = numero_empleado.strip()
        self.asignatura = asignatura.strip()

    # Sobrescribe el metodo heredado
    def mostrar_info(self):
        print(f"Numero de empleado: {self.numero_empleado}")
        super().mostrar_info()
        print(f"Asignatura: {self.asignatura}")
        print("-" * 35)


# ==========================================
# 4. CLASE ESCUELA
# ==========================================

class Escuela:

    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
        self.profesores = []

    # Agregar estudiante
    def agregar_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            print("Error: el registro no es un estudiante.")
            return False

        if self.buscar_estudiante(estudiante.matricula):
            print("Error: la matricula ya esta registrada.")
            return False

        self.estudiantes.append(estudiante)
        print("Estudiante agregado correctamente.")
        return True

    # Buscar estudiante por matricula
    def buscar_estudiante(self, matricula):
        matricula = matricula.strip().casefold()

        for estudiante in self.estudiantes:
            if estudiante.matricula.casefold() == matricula:
                return estudiante

        return None

    # Mostrar estudiantes
    def mostrar_estudiantes(self):
        print(f"\nESTUDIANTES DE {self.nombre.upper()}")

        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return

        for estudiante in self.estudiantes:
            estudiante.mostrar_info()

    # Consultar estudiante
    def consultar_estudiante(self):
        matricula = input("Ingresa la matricula: ").strip()

        if not matricula:
            print("Debes ingresar una matricula.")
            return

        estudiante = self.buscar_estudiante(matricula)

        if estudiante:
            print("\nEstudiante encontrado:")
            estudiante.mostrar_info()
        else:
            print("No se encontro el estudiante.")

    # Editar estudiante
    def editar_estudiante(self):
        matricula = input("Matricula del estudiante: ").strip()

        if not matricula:
            print("Debes ingresar una matricula.")
            return

        estudiante = self.buscar_estudiante(matricula)

        if not estudiante:
            print("No se encontro el estudiante.")
            return

        print("\nDatos actuales:")
        estudiante.mostrar_info()

        print("Deja vacio un campo para conservar su valor.")

        nombre = input("Nuevo nombre: ").strip()
        edad_texto = input("Nueva edad: ").strip()
        grado = input("Nuevo grado: ").strip()

        nueva_edad = estudiante.edad

        if edad_texto:
            try:
                nueva_edad = int(edad_texto)

                if nueva_edad <= 0:
                    print("La edad debe ser mayor que cero.")
                    return

            except ValueError:
                print("La edad debe ser un numero entero.")
                return

        # Aplicar los cambios
        if nombre:
            estudiante.nombre = nombre

        estudiante.edad = nueva_edad

        if grado:
            estudiante.grado = grado

        print("\nEstudiante actualizado correctamente.")
        estudiante.mostrar_info()

    # Agregar profesor
    def agregar_profesor(self, profesor):
        if not isinstance(profesor, Profesor):
            print("Error: el registro no es un profesor.")
            return False

        for existente in self.profesores:
            if existente.numero_empleado.casefold() == profesor.numero_empleado.casefold():
                print("Error: el numero de empleado ya existe.")
                return False

        self.profesores.append(profesor)
        print("Profesor agregado correctamente.")
        return True

    # Mostrar profesores
    def mostrar_profesores(self):
        print(f"\nPROFESORES DE {self.nombre.upper()}")

        if not self.profesores:
            print("No hay profesores registrados.")
            return

        for profesor in self.profesores:
            profesor.mostrar_info()


# ==========================================
# 5. PROGRAMA PRINCIPAL
# ==========================================

def main():

    escuela = Escuela("Primaria Irene")

    # Registros de ejemplo
    try:
        escuela.agregar_estudiante(
            Estudiante("PI001", "Ana", 10, "5to")
        )

        escuela.agregar_estudiante(
            Estudiante("PI002", "Luis", 11, "5to")
        )

        escuela.agregar_profesor(
            Profesor("PR001", "Maria", 35, "Matematicas")
        )

    except ValueError as error:
        print(f"Error al registrar: {error}")
        return

    # Menu principal
    while True:

        print(f"\n===== SISTEMA ESCOLAR: {escuela.nombre} =====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Editar estudiante")
        print("5. Agregar profesor")
        print("6. Mostrar profesores")
        print("7. Salir")

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            try:
                matricula = input("Matricula: ")
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                grado = input("Grado escolar: ")

                estudiante = Estudiante(
                    matricula, nombre, edad, grado
                )

                escuela.agregar_estudiante(estudiante)

            except ValueError as error:
                print(f"Error en los datos: {error}")

        elif opcion == "2":
            escuela.mostrar_estudiantes()

        elif opcion == "3":
            escuela.consultar_estudiante()

        elif opcion == "4":
            escuela.editar_estudiante()

        elif opcion == "5":
            try:
                numero = input("Numero de empleado: ")
                nombre = input("Nombre del profesor: ")
                edad = int(input("Edad: "))
                asignatura = input("Asignatura: ")

                profesor = Profesor(
                    numero, nombre, edad, asignatura
                )

                escuela.agregar_profesor(profesor)

            except ValueError as error:
                print(f"Error en los datos: {error}")

        elif opcion == "6":
            escuela.mostrar_profesores()

        elif opcion == "7":
            print("Gracias por utilizar el sistema escolar.")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()