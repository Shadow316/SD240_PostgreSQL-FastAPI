# La clase base de las clases modelos
# los modelos o clases modelo son las clases que mapean a las tablas
from orm.config import BaseClass
# Importar de SQLAlchemy los tipos de datos que usan las tablas
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
# Para calcular la hora actual (datetime)
import datetime

class Usuario(BaseClass):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column (Integer)
    domicilio = Column (String(100))
    email = Column("email", String(100))
    password = Column(String(100))
    fecha_registro = Column(DateTime(timezone=True), default=datetime.datetime.now)

class Compra(BaseClass):
    __tablename__ = "compras"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer)
    producto = Column(String(100))
    precio = Column(Float)
    id_usuario = Column(Integer, ForeignKey(Usuario.id))

class Foto(BaseClass):
    __tablename__ = "fotos"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer)
    titulo = Column(String(100))
    descripcion = Column(String(100))
    ruta = Column(String(50))
    id_usuario = Column(Integer, ForeignKey(Usuario.id))