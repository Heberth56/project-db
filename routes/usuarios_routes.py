from fastapi import APIRouter, Depends
from config.config import get_db
from models.usuarios_models import Usuarios
from controllers.usuarios_controllers import add_user, edit_user, list_users, sel_user, remove_user
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/usuarios",
    tags=["CRUD USUARIOS DB"]
)


@router.get("/list")
async def list_users_router(db: Session = Depends(get_db)):
    return list_users(db)


@router.get("/list/{id_user}")
async def sel_user_router(id_user: int, db: Session = Depends(get_db)):
    return sel_user(id_user, db)


@router.post("/add")
async def add_user_router(model: Usuarios, db: Session = Depends(get_db)):
    return add_user(model, db)


@router.put("/edit/{id_user}")
async def edit_user_router(id_user: int, model: Usuarios, db: Session = Depends(get_db)):
    return edit_user(id_user, model, db)


@router.delete("/remove/{id_user}")
async def remove_user_router(id_user: int, db: Session = Depends(get_db)):
    return remove_user(id_user, db)
