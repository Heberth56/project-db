from sqlalchemy.orm import Session
from sqlalchemy import text
from schema.responses_schema import standar_response, server_error


def add_student(model, db: Session):
    try:
        query = """
            INSERT INTO estudiantes(nombre, apellido, matricula, correo, telefono)
            VALUES(:nombre, :apellido, :matricula, :correo, :telefono)
        """
        values = {
            "nombre": model.nombre,
            "apellido": model.apellido,
            "matricula": model.matricula,
            "correo": model.correo,
            "telefono": model.telefono
        }

        db.execute(text(query), values)
        db.commit()

        return standar_response(message="Estudiante registrado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def list_student(db: Session):
    try:
        query = "SELECT * FROM estudiantes WHERE estado = 1"
        result = db.execute(text(query))
        column_names = result.keys()
        serializer_data = [dict(zip(column_names, row)) for row in result]
        return standar_response(message="Listado de estudiantes", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def sel_student(id_student, db: Session):
    try:
        query = f"SELECT * FROM estudiantes WHERE id_estudiante = {id_student} AND estado = 1"
        serializer_data = {}
        result = db.execute(text(query))
        for i in result:
            serializer_data = {
                "id_usuario": i[0],
                "nombre": i[1],
                "apellido": i[2],
                "matricula": i[3],
                "correo": i[4],
                "telefono": i[5]
            }
        return standar_response(message="Listado de estudiantes", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def edit_student(id_student, model, db: Session):
    try:
        query = """
            UPDATE estudiantes
            SET nombre = :nombre, apellido = :apellido, matricula = :matricula, 
                correo = :correo, telefono = :telefono
            WHERE id_estudiante = :id_estudiante
        """
        values = {
            "nombre": model.nombre,
            "apellido": model.apellido,
            "matricula": model.matricula,
            "correo": model.correo,
            "telefono": model.telefono,
            "id_estudiante": id_student
        }

        db.execute(text(query), values)
        db.commit()
        return standar_response(message="Estudiante editado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def remove_student(id_student, db: Session):
    try:
        query = """
            UPDATE estudiantes
            SET estado = 0
            WHERE id_student = :id_student
        """
        values = {
            "id_estudiante": id_student,
        }
        db.execute(text(query), values)
        db.commit()
        return standar_response(message="Estudiante eliminado exitosamente", data=id_student)
    except Exception as e:
        print(e)
        return server_error()
