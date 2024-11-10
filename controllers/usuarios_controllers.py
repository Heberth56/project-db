from sqlalchemy.orm import Session
from sqlalchemy import text
from schema.responses_schema import standar_response, value_error, server_error


def add_user(model, db: Session):
    try:
        query = """
            INSERT INTO usuarios(id_rol, nombres, paterno, materno, cedula, telefono, direccion, correo, avatar, usuario, contrasenia)
            VALUES(:id_rol, :nombres, :paterno, :materno, :cedula, :telefono, :direccion, :correo, :avatar, :usuario, :contrasenia)
        """
        values = {
            "id_rol": model.id_rol,
            "nombres": model.nombres,
            "paterno": model.paterno,
            "materno": model.materno,
            "cedula": model.cedula,
            "telefono": model.telefono,
            "direccion": model.direccion,
            "correo": model.correo,
            "avatar": model.avatar,
            "usuario": model.usuario,
            "contrasenia": model.contrasenia
        }

        db.execute(text(query), values)
        db.commit()

        return standar_response(message="Usuario registrado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def list_users(db: Session):
    try:
        query = "SELECT * FROM usuarios WHERE estado = 1"
        result = db.execute(text(query))
        column_names = result.keys()
        serializer_data = [dict(zip(column_names, row)) for row in result]
        return standar_response(message="Listado de usuarios", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def sel_user(id_user, db: Session):
    try:
        query = f"SELECT * FROM usuarios WHERE id_usuario = {id_user} AND estado = 1"
        serializer_data = {}
        result = db.execute(text(query))
        for i in result:
            serializer_data = {
                "id_usuario": i[0],
                "id_rol": i[1],
                "nombres": i[2],
                "paterno": i[3],
                "materno": i[4],
                "cedula": i[5],
                "telefono": i[6],
                "direccion": i[7],
                "correo": i[8],
                "avatar": i[9],
                "usuario": i[10],
                "contrasenia": i[11]
            }
        return standar_response(message="Listado de usuarios", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def edit_user(id_user, model, db: Session):
    try:
        query = """
            UPDATE usuarios
            SET id_rol = :id_rol, nombres = :nombres, paterno = :paterno, materno = :materno, 
                cedula = :cedula, telefono = :telefono, direccion = :direccion, correo = :correo, 
                avatar = :avatar, usuario = :usuario, contrasenia = :contrasenia
            WHERE id_usuario = :id_usuario
        """
        values = {
            "id_rol": model.id_rol,
            "nombres": model.nombres,
            "paterno": model.paterno,
            "materno": model.materno,
            "cedula": model.cedula,
            "telefono": model.telefono,
            "direccion": model.direccion,
            "correo": model.correo,
            "avatar": model.avatar,
            "usuario": model.usuario,
            "contrasenia": model.contrasenia,
            "id_usuario": id_user
        }

        db.execute(text(query), values)
        db.commit()
        return standar_response(message="Usuario editado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def remove_user(id_user, db: Session):
    try:
        query = """
            UPDATE usuarios
            SET estado = 0
            WHERE id_usuario = :id_usuario
        """
        values = {
            "id_usuario": id_user,
        }
        db.execute(text(query), values)
        db.commit()
        return standar_response(message="Usuario eliminado exitosamente", data=id_user)
    except Exception as e:
        print(e)
        return server_error()
