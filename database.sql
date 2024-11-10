create database project_db;
use project_db;

create table roles (
    id_rol serial primary key, 
    nombre_rol varchar(100) not null,
    estado int default 1
);

insert into roles(nombre_rol)
values ('SuperAdmin'), ('Administrador'), ('Encargado');

create table usuarios (
    id_usuario serial primary key, 
    id_rol int not null,
    nombres varchar(100) not null,
    paterno varchar(100) not null,
    materno varchar(100) not null,
    cedula varchar(10) not null,
    telefono varchar(8) null,
    direccion varchar(255),
    correo varchar(255),   
    avatar text,
    usuario varchar(100) not null,
    contrasenia text not null,
    estado int default 1,
    constraint fk_id_usuario foreign key (id_rol) references roles(id_rol) on delete cascade
);

insert into usuarios(id_rol, nombres, paterno, materno, cedula, telefono, direccion, correo, avatar, usuario, contrasenia)
values(1, 'Jhon', 'Bon', 'Doe', '11547958', '69325698', 'El Alto', 'jhon@gmail.com', '', 'admin', 'libre');

create table mensaje (
    id_mensaje serial primary key,
    id_usuario int not null,
    titulo varchar(255) not null,
    estado int default 1,
    constraint fk_id_usuario_mensaje foreign key (id_usuario) references usuarios(id_usuario) on delete cascade
);


create table historial (
    id_historial serial primary key,
    id_mensaje int not null,
    pregunta text,
    respuesta text,
    estado int default 1,
    constraint fk_id_mensaje_historial foreign key (id_mensaje) references mensaje(id_mensaje) on delete cascade
);


create table estudiantes (
    id_estudiante serial primary key,
    nombre varchar(100) not null,
    apellido varchar(100) not null,
    matricula varchar(50) unique not null,  
    correo varchar(255),
    telefono varchar(15),
    estado int default 1
);


create table libros (
    id_libro serial primary key,
    titulo varchar(255) not null,
    autor varchar(255),
    ano_publicacion int,
    categoria varchar(100),
    cantidad_disponible int default 1,  
    estado int default 1
);

create table prestamos (
    id_prestamo serial primary key,
    id_usuario int not null,
    id_estudiante int not null,
    id_libro int not null,
    fecha_prestamo date default current_timestamp,
    fecha_devolucion date,
    estado_prestamo int default 1,
    estado int default 1,
    constraint fk_usuario_pestamo foreign key (id_usuario) references usuarios(id_usuario) on delete cascade,
    constraint fk_estudiante_prestamo foreign key (id_estudiante) references estudiantes(id_estudiante) on delete cascade,
    constraint fk_libro_prestamo foreign key (id_libro) references libros(id_libro) on delete cascade
);


