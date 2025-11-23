-- Creación de base de datos
CREATE DATABASE gestion_salas
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- Creación de tablas
USE gestion_salas;

-- Tabla: participante
CREATE TABLE participante (
  ci VARCHAR(20) PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: login
CREATE TABLE login (
  correo VARCHAR(255) PRIMARY KEY,
  contrasena VARCHAR(255) NOT NULL,
  FOREIGN KEY (correo) REFERENCES participante(email) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: facultad
CREATE TABLE facultad (
  id_facultad INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: programa_academico
CREATE TABLE programa_academico (
  nombre_programa VARCHAR(255) PRIMARY KEY,
  id_facultad INT,
  tipo ENUM('grado', 'posgrado') NOT NULL,
  FOREIGN KEY (id_facultad) REFERENCES facultad(id_facultad)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: participante_programa_academico
CREATE TABLE participante_programa_academico (
  id_alumno_programa INT AUTO_INCREMENT PRIMARY KEY,
  ci_participante VARCHAR(20),
  nombre_programa VARCHAR(255),
  rol ENUM('alumno', 'docente', 'admin') NOT NULL,
  FOREIGN KEY (ci_participante) REFERENCES participante(ci) ON DELETE CASCADE,
  FOREIGN KEY (nombre_programa) REFERENCES programa_academico(nombre_programa)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: edificio
CREATE TABLE edificio (
  nombre_edificio VARCHAR(255) PRIMARY KEY,
  direccion VARCHAR(255) NOT NULL,
  departamento VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: sala
CREATE TABLE sala (
  nombre_sala VARCHAR(255),
  edificio VARCHAR(255),
  capacidad INT NOT NULL,
  tipo_sala ENUM('libre', 'posgrado', 'docente') NOT NULL,
  PRIMARY KEY (nombre_sala, edificio),
  FOREIGN KEY (edificio) REFERENCES edificio(nombre_edificio)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: turno
CREATE TABLE turno (
  id_turno INT AUTO_INCREMENT PRIMARY KEY,
  hora_inicio TIME NOT NULL,
  hora_fin TIME NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

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
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: reserva_participante
CREATE TABLE reserva_participante (
  ci_participante VARCHAR(20),
  id_reserva INT,
  fecha_solicitud_reserva DATETIME NOT NULL,
  asistencia BOOLEAN NOT NULL,
  PRIMARY KEY (ci_participante, id_reserva),
  FOREIGN KEY (ci_participante) REFERENCES participante(ci) ON DELETE RESTRICT,
  FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Tabla: sancion_participante
CREATE TABLE sancion_participante (
  ci_participante VARCHAR(20),
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  PRIMARY KEY (ci_participante, fecha_inicio, fecha_fin),
  FOREIGN KEY (ci_participante) REFERENCES participante(ci) ON DELETE RESTRICT
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Inserción de datos

-- Inserción de participante
INSERT INTO participante (ci, nombre, apellido, email) VALUES
('000000000', 'Admin', 'Admin', 'admin@ucu.edu.uy'),
('11111111', 'Ana', 'Pérez', 'ana@correo.ucu.edu.uy'),
('22222222', 'Juan', 'Rodríguez', 'juan@correo.ucu.edu.uy'),
('33333333', 'María', 'Fernández', 'maria@ucu.edu.uy'),
('44444444', 'Sofía', 'López', 'sofia@correo.ucu.edu.uy'),
('55555555', 'Martín', 'Santos', 'martin@correo.ucu.edu.uy'),
('66666666', 'Laura', 'Bermúdez', 'laura@ucu.edu.uy'),
('77777777', 'Carlos', 'Vega', 'carlos@correo.ucu.edu.uy'),
('88888888', 'Valeria', 'Nuñez', 'valeria@ucu.edu.uy'),
('99999999', 'Diego', 'Silva', 'diego@correo.ucu.edu.uy'),
('10101010', 'Paula', 'García', 'paula@correo.ucu.edu.uy'),
('12121212', 'Andrés', 'Méndez', 'andres@correo.ucu.edu.uy'),
('13131313', 'Lucía', 'Torres', 'lucia@ucu.edu.uy'),
('14141414', 'Fernando', 'Suárez', 'fernando@correo.ucu.edu.uy'),
('15151515', 'Camila', 'Martínez', 'camila@correo.ucu.edu.uy'),
('16161616', 'Ricardo', 'Pereira', 'ricardo@ucu.edu.uy'),
('17171717', 'Julieta', 'Costa', 'julieta@correo.ucu.edu.uy'),
('18181818', 'Sebastián', 'Ramos', 'sebastian@ucu.edu.uy'),
('19191919', 'Florencia', 'Gómez', 'florencia@correo.ucu.edu.uy'),
('20202020', 'Gabriel', 'Domínguez', 'gabriel@ucu.edu.uy'),
('21212121', 'Micaela', 'Pintos', 'micaela@correo.ucu.edu.uy'),
('22222223', 'Rodrigo', 'Álvarez', 'rodrigo@ucu.edu.uy'),
('23232323', 'Natalia', 'Figueroa', 'natalia@correo.ucu.edu.uy'),
('24242424', 'Pablo', 'Sosa', 'pablo@ucu.edu.uy'),
('25252525', 'Carolina', 'Ferreira', 'carolina@correo.ucu.edu.uy'),
('26262626', 'Ignacio', 'Barrios', 'ignacio@ucu.edu.uy'),
('27272727', 'Verónica', 'Acosta', 'veronica@correo.ucu.edu.uy'),
('28282828', 'Agustín', 'Morales', 'agustin@ucu.edu.uy'),
('29292929', 'Daniela', 'Rossi', 'daniela@correo.ucu.edu.uy');

-- Inserción de login
INSERT INTO login (correo, contrasena) VALUES
('admin@ucu.edu.uy', '$2b$12$7o4obBRWKL8unImYUJi6uunnd.MmSltbGLFD82q1rJxqTYO6/jvzK'), -- admin123
('ana@correo.ucu.edu.uy', '$2b$12$czflrJn.B3W7iwMOlfK9.eUNqnMf2RtePDn9d/y7q5BX1dYwhUYdu'), -- Ana123
('juan@correo.ucu.edu.uy', '$2b$12$OOllyQAnMkD8/Uu6EPrSfeifYV.ihVNv2AxEMHmoSk7S5hf937xTW'), -- Juan456
('maria@ucu.edu.uy', '$2b$12$HoMYjvWHt785VSrYQT3pse3yfLSZV18e3JYgkfN3X3s4X6cSlHP9q'), -- Maria789
('sofia@correo.ucu.edu.uy', '$2b$12$Z3GiuzZed2mzYl71wlMttO60ztCg4m1tbq363.8V/ylgsLsQNhr.K'), -- Sofia123
('martin@correo.ucu.edu.uy', '$2b$12$U/y41mBoJ/n22VgKWplFg.8hqGqfCuJCe2sA7DTv7B3GczWbTBQQK'), -- Martin456
('laura@ucu.edu.uy', '$2b$12$5CHuXwr4dHZQytw7ud62nukhr473RjzQ/B8a8/zIyUJlYzgsEjbAK'), -- Laura789
('carlos@correo.ucu.edu.uy', '$2b$12$Uy7S5Xc4rZF7FptLSzRp0O8AxuBkKHkN3zjvAJZCt2hlR7ubNwyou'), -- Carlos321
('valeria@ucu.edu.uy', '$2b$12$K9dtoF0wlrejSxtzZ0.R5OzVItBFoE1h0TW0Q8Vlw5/y.FjhAVAAK'), -- Valeria654
('diego@correo.ucu.edu.uy', '$2b$12$vHOqThGIvJTIQznmWGzM6eRL15cvMeYBjQARxqhY0dhnkyzctdVIO'), -- Diego111
('paula@correo.ucu.edu.uy', '$2b$12$TEt7NJJ1LgWxjUGz5k3fteFCH4agWCgQrQaD25wYWjnlBt5cDpLm6'), -- Paula222
('andres@correo.ucu.edu.uy', '$2b$12$gem2W.3O4sINQit7Jq7xIeymEuw.b72UuuFGFl6Z85FYj.d5etwIm'), -- Andres333
('lucia@ucu.edu.uy', '$2b$12$bkq9/.OBx3cZlKEATr8Mpeiw7vi9shIc8bMKg1g2nYO/JnDxnh3m.'), -- Lucia444
('fernando@correo.ucu.edu.uy', '$2b$12$nnpVs8zc6YPQahrXErhaZuRxXGaNLYhWnRW7/g5CQTZVhk3jKBawG'), -- Fernando555
('camila@correo.ucu.edu.uy', '$2b$12$Ai.FO8lpgqxT63toKq2dYeF8XFX/q8uIN6NvKxL.1bATEqh4zLzoi'), -- Camila666
('ricardo@ucu.edu.uy', '$2b$12$clGRHGvNqY0yIQgvF3hIb..yB/5KQsEKRZcGTVo7r2tAIZ6I9qooS'), -- Ricardo777
('julieta@correo.ucu.edu.uy', '$2b$12$X5xGqKCwtw54VMBvz8jKjeGqimi3duxfF4tGW/6M7Kt/EJ8Ze7SaG'), -- Julieta888
('sebastian@ucu.edu.uy', '$2b$12$id81WzsNewzxG/bljIHU5eNiqTYBqKNwLEXzGo4p9K1T6sNtS2z1K'), -- Sebastian999
('florencia@correo.ucu.edu.uy', '$2b$12$7nIzqek5cWfNDwzNoLXd7Ozl0xLgTDQCrd4uFy/icha32eYTwjalG'), -- Florencia000
('gabriel@ucu.edu.uy', '$2b$12$uscsAD38YhvDVe41CZ.gJeY2a90ArGgEgom8YfGK3/NOk3Cu3PqOG'), -- Gabriel123
('micaela@correo.ucu.edu.uy', '$2b$12$gH7i5YIL2kC0r0H8vLs13ezGwm5JdMM8mhn0EhhfKA5.buYsl9QQa'), -- Micaela234
('rodrigo@ucu.edu.uy', '$2b$12$YCwu/C6BpSidfAVfchbxeeONi7uHxL9z2IuqDkzX2m8rkcA0vJIkq'), -- Rodrigo345
('natalia@correo.ucu.edu.uy', '$2b$12$3DugcNgNFbShJC9kk31aHuwI4r7FjdwtIiH.L8sdld6FP8hiGOWD.'), -- Natalia456
('pablo@ucu.edu.uy', '$2b$12$boam.yR63xWSXLQFS11aouP.ro9crU6K1FDzpFrU8Sny7XWa96Huy'), -- Pablo567
('carolina@correo.ucu.edu.uy', '$2b$12$On/il1kCetLq.GrsIBtcDuNaEDqsITKoxDjOyCYfmPOl0LQAYw2s.'), -- Carolina678
('ignacio@ucu.edu.uy', '$2b$12$vPBNYVIFPjZy7XTfv/AZo.tx7XpnXS5z2tYz88lQyI0nk2qISeX2e'), -- Ignacio789
('veronica@correo.ucu.edu.uy', '$2b$12$0bSFgtyDN18yn2kgWv7tPu2LwqURmbl6Y3ze7Mj0ypI5O77gZk0n2'), -- Veronica890
('agustin@ucu.edu.uy', '$2b$12$8nExwdpYr2a2H9KsbDpaiOoWsQoDn6Xxab3xMrz6ldW4ucyQdo9te'), -- Agustin901
('daniela@correo.ucu.edu.uy', '$2b$12$4YakFxuNkO4kOyyWRsT7/O.4Mv0zrPTYd8IYsm5O6l85/JVhTV59O'); -- Daniela012

-- Inserción de facultad
INSERT INTO facultad (nombre) VALUES
('Facultad de Ingeniería y Tecnologías'),
('Facultad de Ciencias Empresariales'),
('Facultad de Ciencias de la Salud'),
('Facultad de Derecho y Ciencias Humanas');

-- Inserción de programa_académico
INSERT INTO programa_academico (nombre_programa, id_facultad, tipo) VALUES
('Ingeniería en Informática', 1, 'grado'),
('Ingeniería Artificial y Ciencia de Datos', 1, 'grado'),
('Maestría en Ciencia de Datos', 1, 'posgrado'),
('Contador Público', 2, 'grado'),
('Dirección de Empresas', 2, 'grado'),
('Maestría en Políticas Públicas', 2, 'posgrado'),
('Medicina', 3, 'grado'),
('Odontología', 3, 'grado'),
('Maestría en Rehabilitación Oral', 3, 'posgrado'),
('Abogacía', 4, 'grado'),
('Comunicación', 4, 'grado'),
('Maestría en Comunicación Organizacional', 4, 'posgrado');

-- Inserción de participante_programa_academico
INSERT INTO participante_programa_academico (ci_participante, nombre_programa, rol) VALUES
('000000000', 'Ingeniería en Informática', 'admin'),
('11111111', 'Ingeniería en Informática', 'alumno'),
('99999999', 'Ingeniería Artificial y Ciencia de Datos', 'alumno'),
('13131313', 'Ingeniería Artificial y Ciencia de Datos', 'docente'),
('20202020', 'Maestría en Ciencia de Datos', 'alumno'),
('16161616', 'Maestría en Ciencia de Datos', 'docente'),
('44444444', 'Ingeniería en Informática', 'alumno'),
('22222222', 'Dirección de Empresas', 'alumno'),
('10101010', 'Dirección de Empresas', 'docente'),
('21212121', 'Maestría en Políticas Públicas', 'docente'),
('28282828', 'Contador Público', 'alumno'),
('55555555', 'Contador Público', 'alumno'),
('26262626', 'Contador Público', 'docente'),
('33333333', 'Maestría en Rehabilitación Oral', 'docente'),
('19191919', 'Maestría en Rehabilitación Oral', 'alumno'),
('14141414', 'Odontología', 'alumno'),
('15151515', 'Medicina', 'alumno'),
('18181818', 'Medicina', 'docente'),
('66666666', 'Comunicación', 'docente'),
('77777777', 'Comunicación', 'alumno'),
('88888888', 'Maestría en Comunicación Organizacional', 'docente'),
('17171717', 'Maestría en Comunicación Organizacional', 'alumno'),
('23232323', 'Abogacía', 'alumno'),
('24242424', 'Abogacía', 'docente'),
('29292929', 'Comunicación', 'docente'),
('27272727', 'Abogacía', 'alumno'),
('14141414', 'Comunicación', 'alumno');

-- Inserción de edificios
INSERT INTO edificio (nombre_edificio, direccion, departamento) VALUES
('Edificio Central', 'Av. 8 de Octubre 2738', 'Montevideo'),
('Edificio San Ignacio', 'Cornelio Cantera 2733', 'Montevideo'),
('Edificio Athanasius', 'Gral. Urquiza 2871', 'Montevideo'),
('Edificio Mullin', 'Comandante Braga 2715', 'Montevideo'),
('Edificio Semprún', 'Estero Bellaco 2771', 'Montevideo'),
('Edificio San José', 'Av. 8 de Octubre 2733', 'Montevideo'),
('Edificio Sacré Coeur', 'Av. 8 de Octubre 2738', 'Montevideo'),
('Edificio Madre Marta', 'Av. Garibaldi 2831', 'Montevideo'),
('Casa Xalambrí', 'Cornelio Cantera 2728', 'Montevideo');

-- Inserción de salas
INSERT INTO sala (nombre_sala, edificio, capacidad, tipo_sala) VALUES
('Sala 101', 'Edificio Central', 5, 'libre'),
('Sala 102', 'Edificio Central', 25, 'posgrado'),
('Sala 103', 'Edificio Central', 15, 'docente'),
('Sala 104', 'Edificio Central', 30, 'libre'),
('Sala 201', 'Edificio San Ignacio', 20, 'libre'),
('Sala 202', 'Edificio San Ignacio', 18, 'posgrado'),
('Sala 203', 'Edificio San Ignacio', 6, 'docente'),
('Sala 301', 'Edificio Athanasius', 25, 'libre'),
('Sala 302', 'Edificio Athanasius', 20, 'posgrado'),
('Sala 303', 'Edificio Athanasius', 10, 'docente'),
('Sala 202', 'Edificio Mullin', 15, 'posgrado'),
('Sala 203', 'Edificio Mullin', 20, 'libre'),
('Sala 204', 'Edificio Mullin', 12, 'docente'),
('Sala 401', 'Edificio Semprún', 22, 'libre'),
('Sala 402', 'Edificio Semprún', 18, 'posgrado'),
('Sala 403', 'Edificio Semprún', 10, 'docente'),
('Sala 201', 'Edificio San José', 25, 'libre'),
('Sala 202', 'Edificio San José', 30, 'posgrado'),
('Sala 203', 'Edificio San José', 5, 'docente'),
('Sala 300', 'Edificio Sacré Coeur', 20, 'docente'),
('Sala 301', 'Edificio Sacré Coeur', 15, 'libre'),
('Sala 302', 'Edificio Sacré Coeur', 3, 'posgrado'),
('Sala 100', 'Edificio Madre Marta', 18, 'posgrado'),
('Sala 101', 'Edificio Madre Marta', 20, 'libre'),
('Sala 102', 'Edificio Madre Marta', 12, 'docente'),
('Sala 501', 'Casa Xalambrí', 15, 'libre'),
('Sala 502', 'Casa Xalambrí', 5, 'posgrado'),
('Sala 503', 'Casa Xalambrí', 2, 'docente');

-- Inserción de turnos
INSERT INTO turno (hora_inicio, hora_fin) VALUES
('08:00:00', '09:00:00'),
('09:00:00', '10:00:00'),
('10:00:00', '11:00:00'),
('11:00:00', '12:00:00'),
('12:00:00', '13:00:00'),
('13:00:00', '14:00:00'),
('14:00:00', '15:00:00'),
('15:00:00', '16:00:00'),
('16:00:00', '17:00:00'),
('17:00:00', '18:00:00'),
('18:00:00', '19:00:00'),
('19:00:00', '20:00:00'),
('20:00:00', '21:00:00'),
('21:00:00', '22:00:00'),
('22:00:00', '23:00:00');

-- Inserción de reservas
INSERT INTO reserva (nombre_sala, edificio, fecha, id_turno, estado) VALUES
('Sala 101', 'Edificio Central', '2025-11-10', 1, 'activa'),
('Sala 202', 'Edificio Mullin', '2025-11-11', 2, 'finalizada'),
('Sala 303', 'Edificio Athanasius', '2025-11-12', 3, 'cancelada'),
('Sala 201', 'Edificio San José', '2025-11-15', 4, 'activa'),
('Sala 202', 'Edificio San José', '2025-11-16', 5, 'finalizada'),
('Sala 300', 'Edificio Sacré Coeur', '2025-11-17', 6, 'activa'),
('Sala 301', 'Edificio Sacré Coeur', '2025-11-18', 7, 'cancelada'),
('Sala 100', 'Edificio Madre Marta', '2025-11-19', 8, 'sin_asistencia'),
('Sala 201', 'Edificio San Ignacio', '2025-11-20', 9, 'finalizada'),
('Sala 302', 'Edificio Athanasius', '2025-11-21', 10, 'activa'),
('Sala 401', 'Edificio Semprún', '2025-11-22', 11, 'finalizada'),
('Sala 501', 'Casa Xalambrí', '2025-11-23', 12, 'activa'),
('Sala 104', 'Edificio Central', '2025-11-24', 13, 'finalizada'),
('Sala 202', 'Edificio San Ignacio', '2025-11-25', 14, 'finalizada'),
('Sala 301', 'Edificio Athanasius', '2025-11-26', 15, 'finalizada'),
('Sala 402', 'Edificio Semprún', '2025-11-27', 1, 'finalizada'),
('Sala 302', 'Edificio Sacré Coeur', '2025-11-28', 2, 'finalizada'),
('Sala 101', 'Edificio Madre Marta', '2025-11-29', 3, 'finalizada'),
('Sala 502', 'Casa Xalambrí', '2025-11-30', 4, 'finalizada');

-- Inserción de reserva_participante
INSERT INTO reserva_participante (ci_participante, id_reserva, fecha_solicitud_reserva, asistencia) VALUES
('11111111', 1, '2025-11-09 10:00:00', TRUE),
('22222222', 2, '2025-11-10 11:00:00', FALSE),
('33333333', 3, '2025-11-11 12:00:00', TRUE),
('44444444', 4, '2025-11-14 10:30:00', TRUE),
('55555555', 5, '2025-11-15 09:45:00', TRUE),
('66666666', 6, '2025-11-16 08:20:00', FALSE),
('77777777', 7, '2025-11-17 16:00:00', TRUE),
('88888888', 8, '2025-11-18 12:10:00', FALSE),
('99999999', 9, '2025-11-19 09:00:00', TRUE),
('10101010', 9, '2025-11-19 09:15:00', TRUE),
('12121212', 10, '2025-11-20 08:45:00', FALSE),
('13131313', 10, '2025-11-20 09:00:00', TRUE),
('14141414', 11, '2025-11-21 10:00:00', TRUE),
('15151515', 11, '2025-11-21 10:10:00', TRUE),
('16161616', 12, '2025-11-22 11:00:00', FALSE),
('17171717', 12, '2025-11-22 11:15:00', TRUE),
('18181818', 12, '2025-11-22 11:20:00', TRUE),
('11111111', 13, '2025-11-23 09:00:00', TRUE),
('22222222', 13, '2025-11-23 09:05:00', TRUE),
('33333333', 13, '2025-11-23 09:10:00', TRUE),
('44444444', 13, '2025-11-23 09:15:00', TRUE),
('55555555', 13, '2025-11-23 09:20:00', TRUE),
('66666666', 13, '2025-11-23 09:25:00', TRUE),
('77777777', 13, '2025-11-23 09:30:00', TRUE),
('88888888', 13, '2025-11-23 09:35:00', TRUE),
('99999999', 13, '2025-11-23 09:40:00', TRUE),
('10101010', 13, '2025-11-23 09:45:00', TRUE),
('12121212', 13, '2025-11-23 09:50:00', TRUE),
('13131313', 13, '2025-11-23 09:55:00', TRUE),
('14141414', 13, '2025-11-23 10:00:00', TRUE),
('15151515', 13, '2025-11-23 10:05:00', TRUE),
('16161616', 13, '2025-11-23 10:10:00', TRUE),
('17171717', 13, '2025-11-23 10:15:00', TRUE),
('18181818', 13, '2025-11-23 10:20:00', TRUE),
('19191919', 13, '2025-11-23 10:25:00', TRUE),
('20202020', 13, '2025-11-23 10:30:00', TRUE),
('21212121', 13, '2025-11-23 10:35:00', TRUE),
('22222223', 13, '2025-11-23 10:40:00', TRUE),
('23232323', 13, '2025-11-23 10:45:00', TRUE),
('24242424', 13, '2025-11-23 10:50:00', TRUE),
('25252525', 13, '2025-11-23 10:55:00', TRUE),
('26262626', 13, '2025-11-23 11:00:00', TRUE),
('27272727', 13, '2025-11-23 11:05:00', TRUE),
('28282828', 13, '2025-11-23 11:10:00', TRUE),
('29292929', 13, '2025-11-23 11:15:00', TRUE);

-- Inserción de sancion_participante
INSERT INTO sancion_participante (ci_participante, fecha_inicio, fecha_fin) VALUES
('11111111', '2025-07-01', '2025-09-01'),
('22222222', '2025-11-05', '2026-01-05'),
('33333333', '2025-11-10', '2026-01-10'),
('44444444', '2026-01-01', '2026-03-01'),
('55555555', '2026-01-05', '2026-03-05'),
('99999999', '2025-12-01', '2026-02-01'),
('10101010', '2025-12-05', '2026-02-05'),
('12121212', '2026-02-01', '2026-04-01'),
('14141414', '2026-03-01', '2026-05-01'),
('17171717', '2026-04-01', '2026-06-01');


SELECT *
FROM sancion_participante
WHERE ci_participante = '14141414';
