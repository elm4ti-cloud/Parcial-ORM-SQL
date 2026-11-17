# Sistema de Inventario de Zapatos — SQLAlchemy ORM

## 1. Información del proyecto

| Información | Descripción |
|---|---|
| Estudiante | Matias Villero |
| Asignatura | DESARROLLO DE APLICACIONES CON ACCESO A DATOS |
| Docente | Eduardo Pimienta |
| Fecha | 17/11/26 |
| Lenguaje de programación | Python |
| ORM utilizado | SQLAlchemy |
| Base de datos | SQLite |

## 2. Descripción del proyecto

**¿En qué consiste el programa?**

El programa consiste en un sistema de gestión de inventario para una tienda de zapatos
que opera directamente desde la consola interactiva. Su Proposito principal es permitir
la administración persistente de los productos de la tienda, ofreciendo operaciones para
registrar nuevos modelos, consultar el listado completo, buscar por identificador único,
actualizar precios y eliminar registros de manera eficiente mediante el uso de un ORM.

**¿Qué funcionalidades tiene?**

Describe brevemente las operaciones que permite realizar el sistema:

- Registrar zapatos: Registrar zapatos indicando modelo talla y precio.
- Consultar el inventario: Consulta todo el inventario disponible.
- Buscar zapatos por ID: Buscar un zapato específico por su ID.
- Actualizar precios: Actualizar el precio de un modelo existente.
- Eliminar zapatos: Eliminar un zapato del sistema.

## 3. Estructura del proyecto

Presenta la estructura de archivos de tu aplicación.

```text
tienda_zapatos/
├── main.py
├── datos.py
├── requirements.txt
├── README.md
└── evidencias/
```

**Explicación de los archivos:**

| Archivo | ¿Cuál es su responsabilidad? |
|---|---|
| `main.py` | Contiene el menú interactivo, la captura de datos por consola y la lógica de la interacción con el usuario |
| `datos.py` | Implementa la capa de persistente utilizando SQLAlchemy, configurando la conexión, el modelo de datos y las funciones CRUD. |
| `requirements.txt` | Especifica las depencias externas necesarias para ejecutar la aplicación |
| `zapateria.db` | Archivo de base de datos de SQLite generando automaticamente al iniciar la aplicación |

## 4. Instalación y ejecución

Explica los pasos para ejecutar el proyecto en otro computador.

**Paso 1. Requisitos**

Tener Instalado python y pip

**Paso 2. Instalación de dependencias**

```bash
python -m pip install -r requirements.txt
```

**Paso 3. Ejecución**

```bash
python main.py
```

**Paso 4. Resultado esperado**

Se desplegará el menú interactivo en la consola con las opciones desponibles para administrar el inventario
de la tienda de zapatos

---

# 5. Documentación técnica — Preguntas obligatorias

Responde las siguientes preguntas utilizando tu implementación. Cuando sea necesario, incluye fragmentos de tu código para explicar el funcionamiento.

### Pregunta 1. Modelo y tabla

¿Qué clase de Python representa la tabla de la base de datos? Explica cómo SQLAlchemy identifica el nombre de la tabla y sus columnas.

**Respuesta:**

La tabla está representada por la clase Zapato. SQLAlchemy identifica el nombre con __tablename__ = "zapatos" y las columnas utilizando Mapped y mapped_column().

### Pregunta 2. Creación de la base de datos

¿Qué ocurre cuando ejecutas el programa por primera vez? Explica cómo se crea la base de datos `zapateria.db` y la tabla `zapatos`.

**Respuesta:**

Al ejecutarse por primera vez, inicializar_bd() invoca Base.metadata.create_all(engine). Si zapateria.db no existe, SQLite lo crea automáticamente junto con la estructura de la tabla zapatos.

### Pregunta 3. Registro de zapatos

Cuando seleccionas la opción de registrar un zapato, ¿qué recorrido siguen los datos desde el menú hasta quedar almacenados en SQLite? Identifica las funciones utilizadas.

**Respuesta:**

1. El usuario ingresa los datos en el menú (main.py).
2. Se llama a datos.crear_zapato(modelo, talla, precio).
3. Se abre una sesión, se instancia Zapato, se añade con session.add() y se persiste con session.commit().

### Pregunta 4. Sesiones y transacciones

¿Para qué se utiliza una sesión de SQLAlchemy? ¿Qué ocurriría si agregas o modificas un objeto, pero no confirmas la transacción con `commit()`?

**Respuesta:**

La sesión (Session) administra el espacio de trabajo temporal y las transacciones. Si se omite session.commit(), los cambios se quedan en memoria y no se guardan de forma permanente en SQLite.

### Pregunta 5. Búsqueda por ID

¿Cómo funciona la búsqueda de zapatos por ID? Explica qué devuelve tu función cuando encuentra el registro y qué devuelve cuando no existe.

**Respuesta:**

Utiliza session.get(Zapato, id_zapato). Si encuentra el registro, devuelve el objeto Zapato; de lo contrario, retorna None.

### Pregunta 6. Actualización de precios

¿Cómo se actualiza el precio de un zapato mediante el ORM? Explica cómo se obtiene el objeto, cómo se modifica su atributo y cómo se guarda el cambio.

**Respuesta:**

Se obtiene el objeto con session.get(), se modifica el atributo precio directamente y se confirman los cambios con session.commit().

### Pregunta 7. Eliminación de registros

¿Qué ocurre cuando eliminas un zapato? Explica cómo compruebas que el registro ya no existe en la base de datos.

**Respuesta:**

Se busca el objeto por ID, se elimina con session.delete(zapato) y se confirma con session.commit(). Se comprueba que ya no existe al intentar buscarlo nuevamente y obtener None.

### Pregunta 8. Persistencia de datos

¿Qué sucede con los zapatos registrados cuando cierras y vuelves a ejecutar el programa? Explica por qué permanecen almacenados.

**Respuesta:**

Los zapatos permanecen guardados porque se utiliza una base de datos basada en un archivo físico (zapateria.db), por lo que los cambios confirmados con commit() se escriben permanentemente en disco.

---

## 6. Pruebas de funcionamiento y evidencias

Debes ejecutar el programa y demostrar el funcionamiento de cada una de las operaciones.

### Prueba 1. Registrar zapatos

- **Acción realizada:** registrar dos zapatos.
- **Datos utilizados:** [Indicar modelo, talla y precio].
- **Resultado obtenido:** [Explicar qué ocurrió].

**Evidencia:**

![Registro de zapatos](evidencias/registro.png)

### Prueba 2. Listar inventario

- **Acción realizada:** consultar todos los zapatos.
- **Resultado obtenido:** [Explicar qué mostró el programa].

**Evidencia:**

![Listado de zapatos](evidencias/listado.png)

### Prueba 3. Buscar por ID

- **ID utilizado:** [Indicar ID].
- **Resultado obtenido:** [Explicar qué ocurrió].

**Evidencia:**

![Búsqueda de zapatos](evidencias/busqueda.png)

### Prueba 4. Actualizar precio

- **Zapato seleccionado:** [Indicar].
- **Precio anterior:** [Indicar].
- **Precio nuevo:** [Indicar].
- **Resultado obtenido:** [Explicar qué ocurrió].

**Evidencia:**

![Actualización de precio](evidencias/actualizacion.png)

### Prueba 5. Eliminar zapato

- **ID eliminado:** [Indicar ID].
- **Resultado obtenido:** [Explicar cómo verificaste la eliminación].

**Evidencia:**

![Eliminación de zapato](evidencias/eliminacion.png)

### Prueba 6. Comprobar persistencia

- **Acción realizada:** cerrar y ejecutar nuevamente el programa.
- **Resultado obtenido:** [Explicar cuáles registros permanecieron guardados].

**Evidencia:**

![Persistencia de datos](evidencias/persistencia.png)

### Pruebas con registros inexistentes

Ejecuta las operaciones de buscar, actualizar y eliminar utilizando un ID que no exista.

| Operación | ¿Qué sucedió? |
|---|---|
| Buscar ID inexistente | [Respuesta] |
| Actualizar ID inexistente | [Respuesta] |
| Eliminar ID inexistente | [Respuesta] |

## 7. Conclusiones

Responde brevemente:

1. ¿Qué aprendiste al implementar las operaciones CRUD utilizando SQLAlchemy?
2. ¿Qué diferencia identificaste entre trabajar con objetos Python y escribir sentencias SQL directamente?
3. ¿Cuál fue la principal dificultad durante el desarrollo y cómo la solucionaste?


## Indicaciones de documentación

- Responde las ocho preguntas con tus propias palabras.
- Relaciona tus explicaciones con el código que implementaste.
- Incluye fragmentos de código únicamente cuando ayuden a explicar tu respuesta.
- Todas las evidencias deben corresponder a ejecuciones reales del programa.
- Guarda las capturas dentro de la carpeta `evidencias/` utilizando los nombres indicados o actualiza las rutas del README.
- Verifica que las imágenes se visualicen correctamente en GitHub.
- Elimina los textos entre corchetes y reemplázalos con tus respuestas antes de entregar.
- La documentación debe permitir que otra persona comprenda cómo instalar, ejecutar y utilizar tu aplicación.
