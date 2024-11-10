from fastapi import APIRouter, Depends
from config.config import get_db
from models.estudiantes_models import Estudiantes
from controllers.estudiantes_controllers import add_student, edit_student, list_student, sel_student, remove_student
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/estudiantes",
    tags=["CRUD ESTUDIANTES DB"]
)


@router.get("/list")
async def list_student_router(db: Session = Depends(get_db)):
    return list_student(db)


@router.get("/list/{id_student}")
async def sel_student_router(id_student: int, db: Session = Depends(get_db)):
    return sel_student(id_student, db)


@router.post("/add")
async def add_student_router(model: Estudiantes, db: Session = Depends(get_db)):
    return add_student(model, db)


@router.put("/edit/{id_student}")
async def edit_student_router(id_student: int, model: Estudiantes, db: Session = Depends(get_db)):
    return edit_student(id_student, model, db)


@router.delete("/remove/{id_student}")
async def remove_student_router(id_student: int, db: Session = Depends(get_db)):
    return remove_student(id_student, db)
