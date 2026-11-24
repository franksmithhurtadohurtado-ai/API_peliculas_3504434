from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import engine, Base, get_db
from models import Movie
from schemas import MovieCreate, MovieResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movies API")


@app.post("/movies", response_model=MovieResponse, status_code=201)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    nueva_pelicula = Movie(**movie.model_dump())
    db.add(nueva_pelicula)
    db.commit()
    db.refresh(nueva_pelicula)
    return nueva_pelicula

@app.get("/movies", response_model=List[MovieResponse])
def get_movies(genero: Optional[str] = None, db: Session = Depends(get_db)):
    if genero:
      
        return db.query(Movie).filter(Movie.genero.ilike(f"%{genero}%")).all()
    return db.query(Movie).all()


@app.get("/movies/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    pelicula = db.query(Movie).filter(Movie.id == movie_id).first()
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return pelicula


@app.put("/movies/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, movie_data: MovieCreate, db: Session = Depends(get_db)):
    pelicula = db.query(Movie).filter(Movie.id == movie_id).first()
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    for key, value in movie_data.model_dump().items():
        setattr(pelicula, key, value)

    db.commit()
    db.refresh(pelicula)
    return pelicula


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    pelicula = db.query(Movie).filter(Movie.id == movie_id).first()
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    db.delete(pelicula)
    db.commit()
    return {"message": "Película eliminada correctamente"}
