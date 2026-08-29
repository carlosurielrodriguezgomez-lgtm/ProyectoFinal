import os
from services.videojuego_service import VideojuegoService
from exceptions.custom_exceptions import (
    GameVaultError, 
    RegistroDuplicadoError, 
    VideojuegoNoEncontradoError, 
    ReglaNegocioError
)
from utils.csv_manager import exportar_coleccion_csv

def limpiar_pantalla():
    """Limpia la consola dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado():
    print("\n╔══════════════════════════════════════════╗")
    print("║               GAMEVAULT                  ║")
    print("║       Gestor de Colección Gamer          ║")
    print("╚══════════════════════════════════════════╝")

def mostrar_menu():
    print("\n1. Registrar nuevo videojuego")
    print("2. Ver estadísticas de mi colección")
    print("3. Actualizar progreso de un juego")
    print("4. Exportar colección a CSV")
    print("0. Salir del sistema")
    return input("\nSelecciona una opción: ")

def main():
    # Instanciamos el servicio principal una sola vez
    service = VideojuegoService()
    
    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        opcion = mostrar_menu()
        
        if opcion == '1':
            print("\n--- REGISTRAR VIDEOJUEGO ---")
            try:
                nombre = input("Nombre del juego: ")
                saga_id = int(input("ID de la Saga (ej. 1 para Gears, 2 para Halo): "))
                plataforma = input("Plataforma (PC, Xbox, PS5...): ")
                anio = int(input("Año de lanzamiento: "))
                
                # Pasamos los datos limpios a la capa de servicios
                vj = service.registrar_videojuego(nombre, saga_id, plataforma, anio)
                print(f"\n✓ ÉXITO: '{vj.nombre}' registrado correctamente con ID: {vj.id}")
                
            except ValueError:
                print("\n✗ ERROR: Ingresaste texto donde iba un número (ID o Año).")
            except RegistroDuplicadoError as e:
                print(f"\n✗ ERROR DE NEGOCIO: {e}")
            except GameVaultError as e:
                print(f"\n✗ ERROR DEL SISTEMA: {e}")
            except Exception as e:
                print(f"\n✗ ERROR INESPERADO: Ocurrió un problema con la base de datos.")
                
            input("\nPresiona Enter para continuar...")
            
        elif opcion == '2':
            print("\n--- ESTADÍSTICAS POR SAGA ---")
            try:
                stats = service.repo.estadisticas_por_saga()
                if not stats:
                    print("No hay datos suficientes para generar estadísticas.")
                else:
                    print(f"{'SAGA':<25} | {'TOTAL JUEGOS':<15} | {'PROMEDIO PUNTUACIÓN'}")
                    print("-" * 65)
                    for fila in stats:
                        promedio = fila['promedio_puntuacion'] if fila['promedio_puntuacion'] else "N/A"
                        print(f"{fila['nombre']:<25} | {fila['total_juegos']:<15} | {promedio}")
            except Exception as e:
                print("\n✗ ERROR: No se pudieron cargar las estadísticas.")
            
            input("\nPresiona Enter para continuar...")
            
        elif opcion == '3':
            print("\n--- ACTUALIZAR PROGRESO ---")
            try:
                id_vj = int(input("ID del videojuego a actualizar: "))
                horas = float(input("Total de horas jugadas: "))
                porcentaje = float(input("Porcentaje completado (0 - 100): "))
                
                # Convertimos 'S' o 'N' en un booleano para el servicio
                es_completado = input("¿Juego terminado? (S/N): ").strip().upper() == 'S'
                
                service.actualizar_progreso(id_vj, horas, porcentaje, es_completado)
                print("\n✓ ÉXITO: Progreso actualizado correctamente.")
                
            except ValueError:
                print("\n✗ ERROR: Debes ingresar valores numéricos válidos para ID, horas y porcentaje.")
            except (VideojuegoNoEncontradoError, ReglaNegocioError) as e:
                # Aquí brillan nuestras excepciones personalizadas
                print(f"\n✗ ERROR DE REGLA: {e}")
            except GameVaultError as e:
                print(f"\n✗ ERROR DE NEGOCIO: {e}")
                
            input("\nPresiona Enter para continuar...")
            
        elif opcion == '4':
            print("\n--- EXPORTAR A CSV ---")
            try:
                exito = exportar_coleccion_csv()
                if exito:
                    print("✓ ÉXITO: Colección exportada correctamente en 'data/reportes/videojuegos.csv'.")
                else:
                    print("✗ AVISO: No hay juegos registrados para exportar.")
            except Exception as e:
                print(f"\n✗ ERROR: Falló la exportación. Verifica que la carpeta exista. Detalle: {e}")
                
            input("\nPresiona Enter para continuar...")
            
        elif opcion == '0':
            limpiar_pantalla()
            print("\nCerrando GameVault...")
            print("¡Nos vemos en la próxima partida!\n")
            break
            
        else:
            print("\n✗ Opción no válida. Intenta de nuevo.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()