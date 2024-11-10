from pydantic import BaseModel


class Libros(BaseModel):
    titulo: str
    autor: str
    ano_publicacion: int
    categoria: str
    cantidad_disponible: int
