from pydantic import BaseModel
from typing import Optional


class Usuarios(BaseModel):
    id_rol: int
    nombres: str
    paterno: str
    materno: str
    cedula: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    correo: Optional[str] = None
    avatar: Optional[str] = None
    usuario: str
    contrasenia: str
