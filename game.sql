USE gamevault;

-- 1. Insertar Sagas
INSERT INTO sagas (id, nombre, desarrollador, genero_principal, descripcion) VALUES
(1, 'Gears of War', 'The Coalition', 'Shooter en Tercera Persona', 'Franquicia de guerra entre la humanidad y la horda Locust.'),
(2, 'Halo', '343 Industries', 'Shooter en Primera Persona', 'Saga épica del Jefe Maestro y la lucha contra el Covenant.'),
(3, 'Resident Evil', 'Capcom', 'Survival Horror', 'Pioneros del género de terror, supervivencia y armas biológicas.'),
(4, 'Persona', 'Atlus', 'JRPG', 'Juegos de rol que combinan vida escolar y exploración de mazmorras.'),
(5, 'Hades', 'Supergiant Games', 'Roguelike', 'Acción frenética en el inframundo de la mitología griega.'),
(6, 'Grand Theft Auto', 'Rockstar Games', 'Mundo Abierto', 'Saga icónica de crimen, libertad y sátira social.'),
(7, 'Apex Legends', 'Respawn Entertainment', 'Battle Royale', 'Juego de disparos competitivo basado en héroes en el universo Titanfall.'),
(8, 'Lies of P', 'Neowiz Games', 'Soulslike', 'Oscura reimaginación de la historia de Pinocho con combate desafiante.'),
(9, 'Dark Souls', 'FromSoftware', 'Action RPG', 'Franquicia legendaria por su dificultad, diseño de niveles y narrativa.');

-- 2. Insertar Videojuegos
-- El ID se generará automáticamente. Los saga_id corresponden a los números de arriba.
INSERT INTO videojuegos (nombre, saga_id, plataforma, anio_lanzamiento, estado, puntuacion_personal, favorito) VALUES
-- Gears of War (Saga 1)
('Gears of War', 1, 'Xbox', 2006, 'COMPLETADO', 9.5, TRUE),
('Gears of War 2', 1, 'Xbox', 2008, 'COMPLETADO', 10.0, TRUE),
-- Halo (Saga 2)
('Halo: Combat Evolved', 2, 'PC', 2001, 'COMPLETADO', 9.0, FALSE),
('Halo 2', 2, 'PC', 2004, 'COMPLETADO', 9.5, TRUE),
-- Resident Evil (Saga 3)
('Resident Evil 2', 3, 'PC', 2019, 'COMPLETADO', 9.0, FALSE),
('Resident Evil 4', 3, 'PC', 2023, 'JUGANDO', NULL, FALSE),
-- Persona (Saga 4)
('Persona 5 Royal', 4, 'PC', 2020, 'COMPLETADO', 10.0, TRUE),
('Persona 3 Reload', 4, 'PC', 2024, 'PENDIENTE', NULL, FALSE),
-- Hades (Saga 5)
('Hades', 5, 'PC', 2020, 'COMPLETADO', 9.5, TRUE),
('Hades II', 5, 'PC', 2024, 'JUGANDO', NULL, FALSE),
-- GTA (Saga 6)
('Grand Theft Auto V', 6, 'PC', 2013, 'COMPLETADO', 9.0, FALSE),
('Grand Theft Auto: San Andreas', 6, 'PC', 2004, 'COMPLETADO', 9.5, TRUE),
-- Apex (Saga 7)
('Apex Legends', 7, 'PC', 2019, 'JUGANDO', 8.5, FALSE),
-- Lies of P (Saga 8)
('Lies of P', 8, 'PC', 2023, 'PENDIENTE', NULL, FALSE),
-- Dark Souls (Saga 9)
('Dark Souls Remastered', 9, 'PC', 2018, 'COMPLETADO', 9.5, TRUE),
('Dark Souls III', 9, 'PC', 2016, 'COMPLETADO', 10.0, TRUE);