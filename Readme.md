# Jhon Alexander Linares.

# Proposito del codigo 
Este código define una clase llamada Pelicula que simula el manejo de películas en una biblioteca o sistema de préstamo. Permite almacenar información sobre cada película, controlar su estado de préstamo y calcular costos 
asociados a su impresión.

#  Descripción de la clase Pelicula
__isbn: Número único que identifica la película (similar a un código de barras).

__titulo: Título de la película.

__duracion: Duración en minutos de la película.

__autor: Director o creador de la película.

__prestado: Estado de préstamo de la película (True si está prestada, False si no lo está).

Métodos de acceso (Getters y Setters)
Getters: Permiten obtener el valor de los atributos privados.

get_isbn(), get_titulo(), get_numero_paginas(), get_autor(), is_prestado()

Setters: Permiten modificar el valor de los atributos privados.

set_isbn(), set_titulo(), set_duracion(), set_autor(), set_prestado()

# ¿Para qué sirve?
Este código es útil para:

Gestión de inventarios: Mantener un registro de las películas disponibles en una biblioteca o sistema de préstamo.

Control de préstamos: Verificar si una película está disponible para ser prestada o si ya está en préstamo.

Cálculo de costos: Determinar el costo asociado a la impresión o reproducción de una película basándose en su duración.

# Instrucciones de uso
Instalación: No requiere instalación adicional. Solo necesitas tener Python instalado en tu sistema.

Ejecución: Guarda el código en un archivo con extensión .py (por ejemplo, peliculas.py) y ejecútalo desde la terminal o un entorno de desarrollo integrado (IDE) como PyCharm o VSCode.

Interacción: Puedes modificar los valores al crear instancias de la clase Pelicula para adaptarlos a tus necesidades. Luego, utiliza los métodos disponibles para interactuar con las películas.
