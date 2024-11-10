from fastapi import APIRouter, Depends
from config.config import get_db
from models.libros_modes import Libros
from controllers.libros_controllers import add_book, edit_book, list_book, sel_book, remove_book
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/libros",
    tags=["CRUD LIBROS DB"]
)


@router.get("/list")
async def list_book_router(db: Session = Depends(get_db)):
    return list_book(db)


@router.get("/list/{id_book}")
async def sel_book_router(id_book: int, db: Session = Depends(get_db)):
    return sel_book(id_book, db)


@router.post("/add")
async def add_book_router(model: Libros, db: Session = Depends(get_db)):
    return add_book(model, db)


@router.put("/edit/{id_book}")
async def edit_book_router(id_book: int, model: Libros, db: Session = Depends(get_db)):
    return edit_book(id_book, model, db)


@router.delete("/remove/{id_book}")
async def remove_book_router(id_book: int, db: Session = Depends(get_db)):
    return remove_book(id_book, db)
