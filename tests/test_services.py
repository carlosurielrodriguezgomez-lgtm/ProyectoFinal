import pytest
from services.videojuego_service import VideojuegoService
from exceptions.custom_exceptions import ReglaNegocioError

def test_juego_completado_exige_100_porciento():
    service = VideojuegoService()
    # Asume que el juego con ID 1 existe en la base de datos de prueba
    with pytest.raises(ReglaNegocioError) as context:
        service.actualizar_progreso(id_vj=1, horas=40, porcentaje=90, completado=True)
    
    assert "Un juego completado debe tener el 100%" in str(context.value)