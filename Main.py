# Jhon_Alexander Linares

from peliculas import Pelicula  # Importa la clase desde el otro archivo

# Crear películas
pelicula1 = Pelicula(1244, "La era de hielo", 92, "Chris Wedge")
pelicula2 = Pelicula(3456, "Las 50 sombras de Grey", 98, "Samantha Louise Taylor")
pelicula3 = Pelicula(2688, "Chiquito pero peligroso", 74, "Keenen Ivory Wayans")

# Mostrar información
print("Información de las películas:")
print(pelicula1)
print(pelicula2)
print(pelicula3)

print("\nPréstamos:")
print("Pelicula 1:", pelicula1.prestar())
print("Pelicula 2:", pelicula2.prestar())
print("Pelicula 3:", pelicula3.devolver())  # No estaba prestada

print("\nCosto de reproducción:")
print(pelicula1.imprimir(34))  # 34 es la tarifa por minuto

print("\n¿Son iguales?")
print("¿Pelicula 1 y Pelicula 3 tienen el mismo ISBN?", pelicula1 == pelicula3)
