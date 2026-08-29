# GameVault — Gestor de Colección y Progreso de Videojuegos

## Descripción
GameVault es un sistema backend en Python que resuelve el problema de administrar el progreso, estado y estadísticas de una colección personal de videojuegos. Evita la pérdida de seguimiento en títulos pendientes y genera reportes valiosos de los hábitos de juego.

## Características
* **Persistencia Relacional:** Uso de MySQL con relaciones `1:N` (Sagas -> Videojuegos).
* **Arquitectura de Software:** Código dividido en `models`, `repositories`, `services` y `main` (Controlador).
* **Reglas de Negocio Estrictas:** Excepciones personalizadas para evitar duplicados y validar porcentajes lógicos (100% exigido para juegos completados).
* **Estadísticas Avanzadas:** Consultas SQL utilizando `JOIN`, `GROUP BY` y `AVG`.
* **Exportación y Auditoría:** Generación de archivos `.csv` para reportes externos y `.json` para logs de operaciones.

## Instalación y Ejecución
1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el script `BD.sql` en tu gestor MySQL local para crear la base de datos `gamevault`.
4. Ajusta tus credenciales locales en `repositories/db.py`.
5. Ejecuta el sistema:
   ```bash
   python main.py