import psycopg2 as psy
import time

conexion = psy.connect(
            database = "bd",
            user = "gamerOZZY",
            password = "123",
            host = "mi_postgres",
            port = 5432
        )
print("Conectado...")