from sqlalchemy import Column, Integer, String
from database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    director = Column(String(100), nullable=False)
    genero = Column(String(50), nullable=False)
    duracion = Column(Integer, nullable=False)      
    anio_estreno = Column(Integer, nullable=False)
    clasificacion = Column(String(20), nullable=False)
