# Registro de Conflictos Git

**Ramas implicadas:** `main` y `feature/interfaz`
**Archivo conflictivo:** `main.py`
**Líneas afectadas:** 16-17 (Título del encabezado del menú)

**Descripción del problema:**
Se provocó un conflicto intencional modificando la misma línea de código en dos ramas distintas. En la rama `main` se cambió el título a `"GAMEVAULT - Mi Colección"`, mientras que en la rama `feature/interfaz` se cambió a `"GAMEVAULT - Consola Interactiva"`. Al intentar fusionar (`git merge feature/interfaz` hacia `main`), Git detuvo el proceso indicando un conflicto de fusión.

**Resolución:**
1. Se abrió el archivo `main.py` en VS Code.
2. Se analizaron las marcas de conflicto (`<<<<<<< HEAD` y `>>>>>>> feature/interfaz`).
3. Se decidió conservar el formato visual de la rama `main` pero integrando el subtítulo sugerido en la rama de feature, quedando como: `"GAMEVAULT - Gestor de Colección Gamer"`.
4. Se eliminaron las marcas residuales de Git.
5. Se guardó el archivo y se finalizó la fusión con los comandos `git add main.py` y `git commit -m "Resuelve conflicto en el título del menú principal"`.
6. Se verificó la integridad ejecutando `python main.py` para asegurar la ausencia de errores de sintaxis.