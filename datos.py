from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)


# =====================================
# TODO ORM 1 - CONFIGURAR LA CONEXION
# =====================================
# Crear el engine para conectar con una base SQLite llamada zapateria.db
engine = create_engine("sqlite:///zapateria.db", echo=False)


# =====================================
# TODO ORM 2 - CREAR LA CLASE BASE
# =====================================
# Crear la clase Base utilizando DeclarativeBase.
class Base(DeclarativeBase):
    pass


# =====================================
# TODO ORM 3 - CREAR EL MODELO ZAPATO
# =====================================
class Zapato(Base):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    modelo: Mapped[str] = mapped_column(String(100), nullable=False)
    talla: Mapped[int] = mapped_column(nullable=False)
    precio: Mapped[float] = mapped_column(nullable=False)


# =====================================
# TODO ORM 4 - CREAR LA TABLA
# =====================================
def inicializar_bd():
    # Crear las tablas del modelo utilizando el engine.
    Base.metadata.create_all(engine)


# =====================================
# TODO ORM 5 - REGISTRAR ZAPATO
# =====================================
def crear_zapato(modelo, talla, precio):
    try:
        with Session(engine) as session:
            nuevo_zapato = Zapato(modelo=modelo, talla=talla, precio=precio)
            session.add(nuevo_zapato)
            session.commit()
            return True
    except Exception as e:
        print(f"Error al registrar el zapato: {e}")
        return False


# =====================================
# TODO ORM 6 - LISTAR ZAPATOS
# =====================================
def listar_zapatos():
    try:
        with Session(engine) as session:
            stmt = select(Zapato)
            zapatos = session.scalars(stmt).all()
            return zapatos
    except Exception as e:
        print(f"Error al listar los zapatos: {e}")
        return []


# =====================================
# TODO ORM 7 - BUSCAR POR ID
# =====================================
def buscar_zapato(id_zapato):
    try:
        with Session(engine) as session:
            return session.get(Zapato, id_zapato)
    except Exception as e:
        print(f"Error al buscar el zapato: {e}")
        return None


# =====================================
# TODO ORM 8 - ACTUALIZAR PRECIO
# =====================================
def actualizar_precio(id_zapato, nuevo_precio):
    try:
        with Session(engine) as session:
            zapato = session.get(Zapato, id_zapato)
            if zapato:
                zapato.precio = nuevo_precio
                session.commit()
                return True
            return False
    except Exception as e:
        print(f"Error al actualizar el precio: {e}")
        return False


# =====================================
# TODO ORM 9 - ELIMINAR ZAPATO
# =====================================
def eliminar_zapato(id_zapato):
    try:
        with Session(engine) as session:
            zapato = session.get(Zapato, id_zapato)
            if zapato:
                session.delete(zapato)
                session.commit()
                return True
            return False
    except Exception as e:
        print(f"Error al eliminar el zapato: {e}")
        return False