
```                     
  _ __ ___  _   _  ___| |__   __ _ _ __   _ __  _   _ 
 | '_ ` _ \| | | |/ __| '_ \ / _` | '__| | '_ \| | | |
 | | | | | | |_| | (__| | | | (_| | |    | |_) | |_| |
 |_| |_| |_|\__, |\___|_| |_|\__,_|_|    | .__/ \__, |
             |___/                        |_|    |___/ 

```

```
       ██████████            
      ██          ██          
      ██            ██        
    ██  ██      ██  ██        
    ██  ██      ██    ██      
    ██░░░░      ░░░░  ██      
      ██            ██        
        ██████████████        
    ████    ██      ████      
  ██      ██        ██  ██    
██    ██          ██      ██  
██      ██████████      ██  ██
██                      ██  ██
  ██                  ████  ██
    ██████████████████    ██  

```

# mychar 🐍 La palabra más larga

> Proyecto desarrollado como parte del **Curso de Especialización en Ciberseguridad**  
> Módulo: *Puesta en Producción Segura* · C.P.I.F.P. Alan Turing, Granada · 2025-2026
> Unidad 1 Guiada: Prueba de aplicaciones web y para dispositivos móviles
> Tarea: Evaluación de software
---

## Descripción del software

### `mychar.py` · Lógica principal

El núcleo del proyecto es la función `cadena_mas_larga(lista)`, que recibe una lista de cadenas y devuelve la más larga aplicando las siguientes reglas:

- Si dos cadenas tienen la misma longitud, gana la que va antes alfabéticamente, ignorando las mayúsculas.
- Si hay un empate exacto incluso en minúsculas, se conserva la primera aparición en la lista.
- Los espacios a los lados no cuentan para la longitud y se eliminan del resultado.
- Los espacios internos sí cuentan.
- Si la lista está vacía, devuelve `""`.

La función también valida la entrada antes de procesar:

- Si el argumento no es una lista → lanza `TypeError`
- Si algún elemento no es una cadena de texto → lanza `ValueError`

La función `main()` gestiona la interacción con el usuario: solicita 5 palabras una a una, rechaza entradas con números o símbolos y llama a `cadena_mas_larga()` para mostrar el resultado.

### `testingCrearemos.py` · Suite de pruebas unitarias

Las pruebas están organizadas en **4 bloques** que cubren desde el uso normal hasta el abuso de la función.

**Bloque 1: Entradas normales**

| Caso | ¿Qué se prueba? |
|---|---|
| **Caso 1** | Lista con dos palabras empatadas en longitud → devuelve la menor alfabéticamente (`"abcd"` sobre `"dddd"`) |
| **Caso 2** | Lista donde todos los elementos tienen la misma longitud → comprueba que el desempate alfabético ignora mayúsculas |
| **Caso 3** | Empate exacto incluso en minúsculas (ej: `"Kafka"` / `"kafka"`) → conserva la primera aparición |
| **Caso 4** | Cadenas con espacios internos → los espacios cuentan como parte de la longitud |
| **Caso 5** | Cadenas con espacios laterales → no cuentan para la longitud y no aparecen en el resultado |

**Bloque 2: Lista vacía y elementos en blanco**

| Caso | ¿Qué se prueba?  |
|---|---|
| **Caso 6** | Lista completamente vacía → devuelve `""` |
| **Caso 7** | Lista con solo espacios en blanco o cadenas vacías → devuelve `""` |

**Bloque 3: Caracteres del español**

| Caso | ¿Qué se prueba?  |
|---|---|
| **Caso 8** | Palabras con acentos, ñ y diéresis → el desempate respeta el orden Unicode (ej: `"pingüin"` antes que `"pingüín"`) |

**Bloque 4: Mal uso**

| Caso | ¿Qué se prueba?  |
|---|---|
| **Caso 9** | Argumento que no es una lista (ej: un string o una tupla) → lanza `TypeError` |
| **Caso 10** | Lista con elementos que no son strings (ej: enteros o `None`) → lanza `ValueError` |

---

## Tecnologías

| Elemento | Detalle |
|---|---|
| Lenguaje | Python 3.12 |
| Librería de testing | `unittest` (incluida en la librería estándar) |
| Entorno recomendado | Ubuntu 24.04 / WSL2 |
| Control de versiones | Git 2.47.3 |
| Editor | Visual Studio Code |

---

## Estructura del proyecto

```
PPS1/
├── mychar.py               # Lógica principal e interacción con usuario
├── testingCrearemos.py     # Suite de pruebas unitarias 
├── README.md               # Descripción del proyecto
└── .gitignore              # Exclusiones de seguridad e higiene del repo
```

---

## Guía de despliegue

### 1. Prepara el entorno

```bash
python3 -m venv venv
source venv/bin/activate  # En Linux
```

### 2. Clona el repositorio

```bash
git clone git@github.com:mlramos308-pps/PPS1.git
cd PPS1
```

### 3. Ejecuta el programa

```bash
python3 mychar.py
```

```
---------------------------------------------
           La palabra más larga
---------------------------------------------
  A continuación introduce 5 palabras y te diré cuál es la más larga:

Ingresa la palabra 1: Dewback
Ingresa la palabra 2: Nexu
Ingresa la palabra 3: Tauntaun
Ingresa la palabra 4: Varactyl
Ingresa la palabra 5: Reek

La palabra más larga es: Varactyl
```

### 4. Ejecuta los tests

```bash
python3 -m unittest -v testingCrearemos.py
```

---

## Historial de versiones

## Historial de versiones

| Versión | Fecha | Descripción del cambio |
|---|---|---|
| 0.1.0 | 2026-03-22 | Inicialización del repositorio y migración de código base desde la Unidad 1 |
| 0.1.1 | 2026-05-03 | Incorporación de README.md técnico y checklist de seguridad |
| 0.1.2 | 2026-05-03 | Configuración de higiene del repositorio en el .gitignore |
| 0.2.0 | 2026-05-04 | Actual: Implementación de identidad verificada mediante firmado GPG |

---

## Checklist de seguridad  `.gitignore`

Archivos y carpetas excluidos del repositorio y por qué:

| Excluido | Razón técnica |
|---|---|
| `__pycache__/` · `*.pyc` | Bytecode compilado automáticamente por Python. No es portable entre versiones del intérprete y puede revelar la versión exacta utilizada. |
| `.venv/` · `env/` · `venv/` | Entornos virtuales con dependencias locales. Son reproducibles con `pip install` y no deben versionarse. |
| `*.log` | Los ficheros de registro pueden exponer trazas de ejecución, rutas del sistema o entradas del usuario. |
| `.env` · `secrets.env` | Variables de entorno con claves o tokens. Exponerlos en un repositorio es un riesgo crítico difícil de revertir una vez publicado. |

> La higiene del repositorio no es opcional. Es el primer paso para una puesta en producción segura.

---

## Autora

**Laura Ramos Granados**  
SysAdmin
