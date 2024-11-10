from pydantic import BaseModel
from typing import Optional


class Estudiantes(BaseModel):
    nombre: str
    apellido: str
    matricula: str
    correo: Optional[str] = None
    telefono: Optional[str] = None
