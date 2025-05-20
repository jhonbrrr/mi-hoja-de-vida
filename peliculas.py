#Jhon Alexander Linares__Parcial practico corteII

class Pelicula:
    def __init__(self, isbn=0, titulo="", duracion=0, autor="", prestado=False):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__duracion = duracion
        self.__autor = autor
        self.__prestado = prestado

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def get_numero_paginas(self):
        return self.__duracion

    def get_autor(self):
        return self.__autor

    def is_prestado(self):
        return self.__prestado

    # Setters
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def set_autor(self, autor):
        self.__autor = autor

    def set_prestado(self, prestado):
        self.__prestado = prestado

    # Métodos
    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            return "La pelicula  ha sido prestada."
        else:
            return "La pelicula ya estaba prestada."

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            return "La pelicula ha sido devuelta."
        else:
            return "La pelicula no estaba prestada."

    def imprimir(self, coste_por_minuto):
        coste_total = self.__duracion * coste_por_minuto
        return f"El costo de imprimir La pelicula es: ${coste_total:.2f}"

    def __str__(self):
        estado = "está prestada" if self.__prestado else "no está prestada"
        return (f"La pelicula {self.__isbn} con titulo {self.__titulo} y autor {self.__autor} "
                f"tiene {self.__duracion} minutos de duración y {estado}")

    def __eq__(self, otro_libro):
        if isinstance(otro_libro, Pelicula):
            return self.__isbn == otro_libro.get_isbn()
        return False


if __name__ == "__main__":
    pelicula1 = Pelicula(1244, "La era de hielo", 92, "Chris Wedge")
    pelicula2 = Pelicula(3456, "Las 50 sombras de Grey", 98, "Samantha Louise Taylor")
    pelicula3 = Pelicula(2688, "Chiquito pero peligroso", 74, "Keenen Ivory Wayans")

