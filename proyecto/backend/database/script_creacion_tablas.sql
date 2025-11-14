CREATE DATABASE gestion_salas;

USE gestion_salas;

-- Tabla: login
CREATE TABLE login (
    correo VARCHAR(255) PRIMARY KEY,
    contrasena VARCHAR(255) NOT NULL
);

-- Tabla: participante
CREATE TABLE participante (
    ci VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Tabla: facultad
CREATE TABLE facultad (
    id_facultad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Tabla: programa_academico
CREATE TABLE programa_academico (
    nombre_programa VARCHAR(255) PRIMARY KEY,
    id_facultad INT,
    tipo ENUM('grado', 'posgrado') NOT NULL,
    FOREIGN KEY (id_facultad) REFERENCES facultad(id_facultad)
);

-- Tabla: participante_programa_academico
CREATE TABLE participante_programa_academico (
    id_alumno_programa INT AUTO_INCREMENT PRIMARY KEY,
    ci_participante VARCHAR(20),
    nombre_programa VARCHAR(255),
    rol ENUM('alumno', 'docente') NOT NULL,
    FOREIGN KEY (ci_participante) REFERENCES participante(ci),
    FOREIGN KEY (nombre_programa) REFERENCES programa_academico(nombre_programa)
);

-- Tabla: edificio
CREATE TABLE edificio (
    nombre_edificio VARCHAR(255) PRIMARY KEY,
    direccion VARCHAR(255) NOT NULL,
    departamento VARCHAR(255) NOT NULL
);

-- Tabla: sala
CREATE TABLE sala (
    nombre_sala VARCHAR(255),
    edificio VARCHAR(255),
    capacidad INT NOT NULL,
    tipo_sala ENUM('libre', 'posgrado', 'docente') NOT NULL,
    PRIMARY KEY (nombre_sala, edificio),
    FOREIGN KEY (edificio) REFERENCES edificio(nombre_edificio)
);

-- Tabla: turno
CREATE TABLE turno (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL
);

-- Tabla: reserva
CREATE TABLE reserva (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    nombre_sala VARCHAR(255),
    edificio VARCHAR(255),
    fecha DATE NOT NULL,
    id_turno INT,
    estado ENUM('activa', 'cancelada', 'sin_asistencia', 'finalizada') NOT NULL,
    FOREIGN KEY (nombre_sala, edificio) REFERENCES sala(nombre_sala, edificio),
    FOREIGN KEY (id_turno) REFERENCES turno(id_turno)
);

-- Tabla: reserva_participante
CREATE TABLE reserva_participante (
    ci_participante VARCHAR(20),
    id_reserva INT,
    fecha_solicitud_reserva DATETIME NOT NULL,
    asistencia BOOLEAN NOT NULL,
    PRIMARY KEY (ci_participante, id_reserva),
    FOREIGN KEY (ci_participante) REFERENCES participante(ci),
    FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva)
);

-- Tabla: sancion_participante
CREATE TABLE sancion_participante (
    ci_participante VARCHAR(20),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    PRIMARY KEY (ci_participante, fecha_inicio, fecha_fin),
    FOREIGN KEY (ci_participante) REFERENCES participante(ci)
);

-- Tabla: login (es para probar, después haremos lo de hashing)
INSERT INTO login (correo, contrasena) VALUES
('ana@ucu.edu.uy', 'claveAna123'),
('juan@ucu.edu.uy', 'claveJuan456'),
('maria@ucu.edu.uy', 'claveMaria789');

-- Tabla: participante
INSERT INTO participante (ci, nombre, apellido, email) VALUES
('11111111', 'Ana', 'Pérez', 'ana@ucu.edu.uy'),
('22222222', 'Juan', 'Rodríguez', 'juan@ucu.edu.uy'),
('33333333', 'María', 'Fernández', 'maria@ucu.edu.uy');

-- Tabla: facultad
INSERT INTO facultad (nombre) VALUES
('Facultad de Ingeniería'),
('Facultad de Ciencias Empresariales'),
('Facultad de Ciencias de la Salud');

-- Tabla: programa_academico
INSERT INTO programa_academico (nombre_programa, id_facultad, tipo) VALUES
('Ingeniería en Informática', 1, 'grado'),
('Dirección de Empresas', 2, 'grado'),
('Maestría en Rehabilitación Oral', 3, 'posgrado');

-- Tabla: participante_programa_academico
INSERT INTO participante_programa_academico (ci_participante, nombre_programa, rol) VALUES
('11111111', 'Ingeniería en Informática', 'alumno'),
('22222222', 'Dirección de Empresas', 'alumno'),
('33333333', 'Maestría en Rehabilitación Oral', 'docente');

-- Tabla: edificio
INSERT INTO edificio (nombre_edificio, direccion, departamento) VALUES
('Edificio Central', 'Av. 8 de Octubre 2738', 'Montevideo'),
('Edificio Mullin', 'Comandante Braga 2745', 'Montevideo'),
('Edificio Semprún', 'Estero Bellaco 2771', 'Montevideo');

-- Tabla: sala
INSERT INTO sala (nombre_sala, edificio, capacidad, tipo_sala) VALUES
('Sala 101', 'Edificio Central', 20, 'libre'),
('Sala 202', 'Edificio Mullin', 15, 'posgrado'),
('Sala 303', 'Edificio Central', 10, 'docente');

-- Tabla: turno
INSERT INTO turno (hora_inicio, hora_fin) VALUES
('08:00:00', '09:00:00'),
('10:00:00', '11:00:00'),
('14:00:00', '15:00:00');

-- Tabla: reserva
INSERT INTO reserva (nombre_sala, edificio, fecha, id_turno, estado) VALUES
('Sala 101', 'Edificio Central', '2025-11-10', 1, 'activa'),
('Sala 202', 'Edificio Mullin', '2025-11-11', 2, 'finalizada'),
('Sala 303', 'Edificio Central', '2025-11-12', 3, 'cancelada');

-- Tabla: reserva_participante
INSERT INTO reserva_participante (ci_participante, id_reserva, fecha_solicitud_reserva, asistencia) VALUES
('11111111', 1, '2025-11-09 10:00:00', TRUE),
('22222222', 2, '2025-11-10 11:00:00', FALSE),
('33333333', 3, '2025-11-11 12:00:00', TRUE);

-- Tabla: sancion_participante
INSERT INTO sancion_participante (ci_participante, fecha_inicio, fecha_fin) VALUES
('11111111', '2025-11-01', '2025-11-15'),
('22222222', '2025-11-05', '2025-11-20'),
('33333333', '2025-11-10', '2025-11-25');

