from services.videojuego_service import VideojuegoService
from exceptions.custom_exceptions import GameVaultError
from utils.csv_manager import exportar_coleccion_csv

def mostrar_menu():
    print("\n╔══════════════════════════════════════════╗")
    print("║              GAMEVAULT                   ║")
    print("║      Gestor de Colección Gamer           ║")
    print("╚══════════════════════════════════════════╝")
    print("1. Registrar videojuego")
    print("2. Ver estadísticas de Sagas")
    print("3. Exportar a CSV")
    print("0. Salir")

def main():
    service = VideojuegoService()
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            try:
                saga_id = int(input("ID de la Saga: "))
                plataforma = input("Plataforma (Ej. Steam, Xbox): ")
                anio = int(input("Año de lanzamiento: "))
                
                # Llamada al servicio
                vj = service.registrar_videojuego(nombre, saga_id, plataforma, anio)
                print(f"\n✓ Videojuego registrado correctamente con ID: {vj.id}")
                
            except ValueError:
                print("\n✗ Error: Debes ingresar un valor numérico válido.")
            except GameVaultError as e:
                # Captura excepciones específicas del dominio
                print(f"\n✗ Error de Negocio: {e}")
            except Exception as e:
                # Fallback genérico para errores críticos (ej. Base de datos caída)
                print(f"\n✗ Error inesperado: {e}")
                
        elif opcion == '2':
            # Llamarías a service.obtener_estadisticas()
            print("\n--- Estadísticas ---")
            
        elif opcion == '3':
            if exportar_coleccion_csv():
                print("\n✓ Colección exportada a CSV exitosamente.")
            else:
                print("\n✗ No hay datos para exportar.")
                
        elif opcion == '0':
            print("\nSaliendo de GameVault... ¡Sigue jugando!")
            break
        else:
            print("\nOpción no válida.")

if __name__ == "__main__":
    main()