# PyTextAnalyzer

### to run tests
run: ```pytest```

### to run app
run: ```python3 main.py```

## to retrieve info from reddit
create a ```secrets.json``` and add your credentials there

# Características

PyTextAnalyzer es una clase en Python diseñada para el análisis y manipulación básica de texto. Sus funcionalidades principales incluyen:

Procesamiento de texto: Tokeniza el texto de entrada eliminando signos de puntuación y dividiéndolo en palabras.
    Conteo de palabras: Calcula el número de palabras en el texto procesado.

Manipulación de palabras:

```Map:``` Aplica una función a cada palabra (por ejemplo, convertir a mayúsculas o minúsculas).

```Filter:``` Elimina palabras basadas en una condición (por ejemplo, longitud de la palabra).

```Reduce:``` Agrega palabras en un solo valor usando una función personalizada (por ejemplo, concatenación).

```Encadenamiento de métodos:``` Interfaz fluida para encadenar operaciones (por ejemplo, process().map().filter()).

# Uso
## Inicializar el Analizador

```analyzer = PyTextAnalyzer()```

## Procesar Texto

```analyzer.process("Tu texto de entrada aquí.")```

## Ejemplo de Flujo de Trabajo
```
result = (
    analyzer.process("¡Hola, mundo! Esto es una prueba.")
    .map_words(lambda word: word.upper())
    .filter_words(lambda word: len(word) > 3)
    .reduce_words(lambda acc, word: f"{acc} {word}", "Resultado:")
)

print(result.get())           # Salida: "Resultado: HOLA MUNDO ESTO PRUEBA"
print(result.get_words_list()) # Salida: ['HOLA', 'MUNDO', 'ESTO', 'PRUEBA']
print(result.words_count())    # Salida: 4
```
## Métodos Públicos
### ```process(text: str) -> PyTextAnalyzer```

```Descripción:``` Procesa el texto de entrada (tokeniza y cuenta las palabras).

```Parámetros:```

```text:``` Cadena de texto a analizar.
    
```Retorna:``` self para permitir encadenamiento de métodos.

### ```get_words_list() -> list[str]```

```Descripción:``` Retorna la lista de palabras tokenizadas.

```Lanza:``` ValueError si no se ha procesado ningún texto.

### ```get() -> str```

```Descripción:``` Retorna el texto procesado como una cadena.

```Lanza:``` ValueError si no hay texto disponible.

### ```map_words(fn: Callable[[str], str]) -> PyTextAnalyzer```

```Descripción:``` Aplica fn a cada palabra y actualiza el texto.

```Parámetros:```

```fn:``` Función para transformar palabras (por ejemplo, lambda word: word.lower()).

```Retorna:``` self para permitir encadenamiento de métodos.

### ```filter_words(condition: Callable[[str], bool]) -> PyTextAnalyzer```

```Descripción:``` Filtra palabras basadas en condition.

```Parámetros:```

```condition:``` Función que retorna True/False para cada palabra (por ejemplo, lambda word: len(word) > 2).

```Retorna:``` self para permitir encadenamiento de métodos.

### ```reduce_words(fn: Callable[[str, str], str], acc: str = "") -> PyTextAnalyzer```

```Descripción:``` Reduce las palabras a un solo valor usando fn y actualiza el texto.

```Parámetros:```

```fn:``` Función de agregación (por ejemplo, lambda acc, word: acc + word).

```acc:``` Valor inicial del acumulador (por defecto: "").

```Retorna:``` self para permitir encadenamiento de métodos.

### ```words_count() -> int```

```Descripción:``` Retorna el número de palabras en el texto procesado.
