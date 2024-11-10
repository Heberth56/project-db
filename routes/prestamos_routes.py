from fastapi import APIRouter, Depends
from config.config import get_db
from models.prestamos_models import Prestamo
from controllers.prestamos_controllers import add_loan, edit_loan, list_loan, sel_loan, remove_loan
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/prestamos",
    tags=["CRUD PRESTAMOS DB"]
)


@router.get("/list")
async def list_loan_router(db: Session = Depends(get_db)):
    return list_loan(db)


@router.get("/list/{id_loan}")
async def sel_loan_router(id_loan: int, db: Session = Depends(get_db)):
    return sel_loan(id_loan, db)


@router.post("/add")
async def add_loan_router(model: Prestamo, db: Session = Depends(get_db)):
    return add_loan(model, db)


@router.put("/edit/{id_loan}")
async def edit_loan_router(id_loan: int, model: Prestamo, db: Session = Depends(get_db)):
    return edit_loan(id_loan, model, db)


@router.delete("/remove/{id_loan}/{id_book}")
async def remove_loan_router(id_loan: int, id_book: int, db: Session = Depends(get_db)):
    return remove_loan(id_loan, id_book, db)
