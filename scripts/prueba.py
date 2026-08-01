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

def crear_tabla(cursor):
    tabla = """
          CREATE TABLE IF NOT EXISTS minerales(
            sk SERIAL PRIMARY KEY,
            anio INT,
            mineral VARCHAR(30),
            country VARCHAR(30),
            is_rare_earth INT,
            end_use VARCHAR(30),
            mine_production_tonnes NUMERIC(10,1),
            production_share_pct NUMERIC(5,2),
            rese
          )  
    """


