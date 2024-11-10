from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import usuarios_routes, estudiantes_routes, libros_routes, prestamos_routes

app = FastAPI(
    title="PROJECT DATABASE",
    description="ENDPOINTS DE EJEMPLO PARA EL PROYECTO DE LA MATERIA DE BASE DE DATOS",
    version="0.1.0",
    responses={
        404: {"description": "No encontrado"},
        500: {"description": "Error interno del servidor"},
        200: {"description": "Proceso exitoso"}
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_routes.router)
app.include_router(estudiantes_routes.router)
app.include_router(libros_routes.router)
app.include_router(prestamos_routes.router)
