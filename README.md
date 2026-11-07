# Sistema Escolar Primaria Irene - Herencia

## Descripción
Este proyecto consiste en un sistema escolar básico desarrollado en Python mediante Programación Orientada a Objetos, incorporando el concepto de herencia.

## Objetivo
Aplicar la herencia mediante una clase base y clases derivadas para reutilizar atributos y métodos, mejorar la organización del código y facilitar su mantenimiento.

## Clases principales
- **Persona:** clase base que contiene los atributos nombre y edad.
- **Estudiante:** clase derivada que hereda de Persona y agrega matrícula y grado.
- **Profesor:** clase derivada que hereda de Persona y agrega número de empleado y asignatura.
- **Escuela:** administra los registros de estudiantes y profesores.

## Funcionalidades
- Registrar estudiantes.
- Mostrar estudiantes registrados.
- Buscar estudiantes por matrícula.
- Editar información de estudiantes.
- Registrar profesores.
- Mostrar profesores registrados.

## Tecnologías utilizadas
- Python.
- Visual Studio Code.
- Git.
- GitHub.

## Conceptos aplicados
- Programación Orientada a Objetos.
- Clases y objetos.
- Herencia.
- Reutilización de código.
- Método `super()`.
- Sobrescritura de métodos.

## Ejecución
Abrir la terminal en la carpeta del proyecto y ejecutar:

```bash
python sistema_escolar_herencia.py
```

## Nota
Los registros se almacenan temporalmente en listas, por lo que la información se pierde al cerrar el programa.

## Autora
Proyecto académico desarrollado como práctica de Programación Orientada a Objetos.
