class GameVaultError(Exception):
    """Excepción base para el dominio de GameVault"""
    pass

class RegistroDuplicadoError(GameVaultError):
    pass

class VideojuegoNoEncontradoError(GameVaultError):
    pass

class ReglaNegocioError(GameVaultError):
    pass