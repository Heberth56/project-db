from pydantic import BaseModel
from typing import Optional


class Prestamo(BaseModel):
    id_usuario: int
    id_estudiante: int
    id_libro: int
    fecha_devolucion: str
    estado_prestamo: int
