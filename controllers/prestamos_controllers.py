from sqlalchemy.orm import Session
from sqlalchemy import text
from schema.responses_schema import standar_response, server_error
from datetime import date, datetime


def add_loan(model, db: Session):
    try:
        query = """
            INSERT INTO prestamos(id_usuario, id_estudiante, id_libro, fecha_devolucion, estado_prestamo)
            VALUES(:id_usuario, :id_estudiante, :id_libro, :fecha_devolucion, :estado_prestamo)
        """
        values = {
            "id_usuario": model.id_usuario,
            "id_estudiante": model.id_estudiante,
            "id_libro": model.id_libro,
            "fecha_devolucion": model.fecha_devolucion,
            "estado_prestamo": model.estado_prestamo
        }

        db.execute(text(query), values)

        update_query = """
            UPDATE libros
            SET cantidad_disponible = cantidad_disponible - 1
            WHERE id_libro = :id_libro AND cantidad_disponible > 0
        """

        update_values = {"id_libro": model.id_libro}
        db.execute(text(update_query), update_values)
        db.commit()

        return standar_response(message="Prestamo registrado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def list_loan(db: Session):
    try:
        query = "SELECT * FROM prestamos WHERE estado_prestamo = 1"
        result = db.execute(text(query))
        column_names = result.keys()
        serializer_data = [
            {col: (str(value) if isinstance(value, (date, datetime)) else value)
             for col, value in zip(column_names, row)}
            for row in result
        ]
        return standar_response(message="Listado de prestamos", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def sel_loan(id_loan, db: Session):
    try:
        query = f"SELECT * FROM prestamos WHERE id_prestamo = {id_loan} AND estado = 1"
        serializer_data = {}
        result = db.execute(text(query))
        for i in result:
            serializer_data = {
                "id_prestamo": i[0],
                "id_usuario": i[1],
                "id_estudiante": i[2],
                "id_libro": i[3],
                "fecha_devolucion": i[5].strftime("%Y-%m-%d"),
                "estado_prestamo": i[6]
            }
        return standar_response(message="Listado de prestamos", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def edit_loan(id_loan, model, db: Session):
    try:
        query = """
            UPDATE prestamos
            SET id_usuario = :id_usuario, id_estudiante = :id_estudiante, id_libro = :id_libro, 
                fecha_devolucion = :fecha_devolucion, estado_prestamo = :estado_prestamo
            WHERE id_prestamo = :id_prestamo
        """
        values = {
            "id_usuario": model.id_usuario,
            "id_estudiante": model.id_estudiante,
            "id_libro": model.id_libro,
            "fecha_devolucion": model.fecha_devolucion,
            "estado_prestamo": model.estado_prestamo,
            "id_prestamo": id_loan
        }

        db.execute(text(query), values)
        db.commit()
        return standar_response(message="Prestamo editado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def remove_loan(id_loan, id_libro, db: Session):
    try:
        query = """
            UPDATE prestamos
            SET estado = 0
            WHERE id_prestamo = :id_prestamo
        """
        values = {
            "id_prestamo": id_loan,
        }
        db.execute(text(query), values)
        update_query = """
            UPDATE libros
            SET cantidad_disponible = cantidad_disponible + 1
            WHERE id_libro = :id_libro
        """
        update_values = {"id_libro": id_libro}
        db.execute(text(update_query), update_values)
        db.commit()
        return standar_response(message="Devolución registrado exitosamente", data=id_loan)
    except Exception as e:
        print(e)
        return server_error()
