# 🎬 Ejercicio 11: API para gestión de películas

**Aprendiz:** Frank Smith Hurtado Hurtado  
**Tecnologías:** Python · FastAPI · SQLAlchemy · Pydantic · PostgreSQL (Neon) · Render

## 🌐 Enlace en producción (Swagger UI)
👉 **[Probar la API en vivo aquí](https://onrender.com/docs)**

*(Nota: Al estar alojada en el plan gratuito de Render, si la API lleva más de 15 minutos sin actividad, la primera petición puede tardar unos 40–50 segundos mientras el servidor se reactiva).*

## 📌 Endpoints implementados

| Método | Endpoint | Actividad |
| :--- | :--- | :--- |
| `POST` | `/movies` | 1. Registrar una película |
| `GET` | `/movies` | 2. Consultar todas las películas |
| `GET` | `/movies/{movie_id}` | 3. Consultar una película por ID |
| `PUT` | `/movies/{movie_id}` | 4. Actualizar la información de una película |
| `GET` | `/movies?genero=...` | 5. Filtrar películas según su género |
| `DELETE` | `/movies/{movie_id}` | 6. Eliminar una película |
