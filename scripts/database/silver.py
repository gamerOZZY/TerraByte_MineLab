import psycopg2 as psy

def crear_conexion():
    conexion = psy.connect(
                database = "bd",
                user = "gamerOZZY",
                password = "123",
                host = "postgres",
                port = 5432
            )
    print("Conectado")
    return conexion

