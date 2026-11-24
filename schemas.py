from pydantic import BaseModel, Field, ConfigDict

class MovieCreate(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    director: str = Field(min_length=2, max_length=100)
    genero: str = Field(min_length=2, max_length=50)
    duracion: int = Field(gt=0, description="Duración en minutos")
    anio_estreno: int = Field(ge=1888, le=2100)
    clasificacion: str = Field(min_length=1, max_length=20)

class MovieResponse(MovieCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
