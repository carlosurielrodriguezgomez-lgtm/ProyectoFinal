CREATE DATABASE IF NOT EXISTS gamevault;
USE gamevault;

CREATE TABLE IF NOT EXISTS sagas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    desarrollador VARCHAR(100) NOT NULL,
    genero_principal VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS videojuegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    saga_id INT NOT NULL,
    plataforma VARCHAR(50) NOT NULL,
    anio_lanzamiento INT,
    estado ENUM('PENDIENTE', 'JUGANDO', 'COMPLETADO', 'ABANDONADO') DEFAULT 'PENDIENTE',
    puntuacion_personal DECIMAL(3,1),
    fecha_inicio DATE,
    fecha_finalizacion DATE,
    favorito BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (saga_id) REFERENCES sagas(id) ON DELETE CASCADE,
    UNIQUE(nombre, saga_id)
);

CREATE TABLE IF NOT EXISTS progresos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    videojuego_id INT NOT NULL,
    porcentaje_completado DECIMAL(5,2) NOT NULL,
    horas_jugadas DECIMAL(7,2) NOT NULL,
    fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    notas TEXT,
    FOREIGN KEY (videojuego_id) REFERENCES videojuegos(id) ON DELETE CASCADE
);