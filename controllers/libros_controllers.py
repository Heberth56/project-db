from sqlalchemy.orm import Session
from sqlalchemy import text
from schema.responses_schema import standar_response, server_error


def add_book(model, db: Session):
    try:
        query = """
            INSERT INTO libros(titulo, autor, ano_publicacion, categoria, cantidad_disponible)
            VALUES(:titulo, :autor, :ano_publicacion, :categoria, :cantidad_disponible)
        """
        values = {
            "titulo": model.titulo,
            "autor": model.autor,
            "ano_publicacion": model.ano_publicacion,
            "categoria": model.categoria,
            "cantidad_disponible": model.cantidad_disponible
        }

        db.execute(text(query), values)
        db.commit()

        return standar_response(message="Libro registrado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def list_book(db: Session):
    try:
        query = "SELECT * FROM libros WHERE estado = 1 AND cantidad_disponible > 0"
        result = db.execute(text(query))
        column_names = result.keys()
        serializer_data = [dict(zip(column_names, row)) for row in result]
        return standar_response(message="Listado de libros", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def sel_book(id_book, db: Session):
    try:
        query = f"SELECT * FROM libros WHERE id_libro = {id_book} AND estado = 1"
        serializer_data = {}
        result = db.execute(text(query))
        for i in result:
            serializer_data = {
                "id_libro": i[0],
                "titulo": i[1],
                "autor": i[2],
                "ano_publicacion": i[3],
                "categoria": i[4],
                "cantidad_disponible": i[5]
            }
        return standar_response(message="Listado de libros", data=serializer_data)
    except Exception as e:
        print(e)
        return server_error()


def edit_book(id_book, model, db: Session):
    try:
        query = """
            UPDATE libros
            SET titulo = :titulo, autor = :autor, ano_publicacion = :ano_publicacion, 
                categoria = :categoria, cantidad_disponible = :cantidad_disponible
            WHERE id_libro = :id_libro
        """
        values = {
            "titulo": model.titulo,
            "autor": model.autor,
            "ano_publicacion": model.ano_publicacion,
            "categoria": model.categoria,
            "cantidad_disponible": model.cantidad_disponible,
            "id_libro": id_book
        }

        db.execute(text(query), values)
        db.commit()
        return standar_response(message="Libro editado exitosamente", data=values)
    except Exception as e:
        print(e)
        return server_error()


def remove_book(id_book, db: Session):
    try:
        query = """
            UPDATE libros
            SET estado = 0
            WHERE id_libro = :id_libro
        """
        values = {
            "id_libro": id_book,
        }
        db.execute(text(query), values)
        db.commit()
        return standar_response(message="Libro eliminado exitosamente", data=id_book)
    except Exception as e:
        print(e)
        return server_error()
