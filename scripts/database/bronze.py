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

def crear_staging_tabla(conexion):
    tabla = """
        CREATE TABLE IF NOT EXISTS stg_minerales(
        sk SERIAL PRIMARY KEY,
        anio DECIMAL,
        mineral TEXT,
        country TEXT,
        is_rare_earth DECIMAL,
        end_use TEXT,
        mine_production_tonnes DECIMAL,
        production_share_pct DECIMAL,
        reserves_tonnes DECIMAL,
        years_of_reservers DECIMAL,
        refined_share_pct DECIMAL,
        price_usd_per_tonne DECIMAL,
        demand_growth_pct DECIMAL,
        export_control_active DECIMAL,
        hhi DECIMAL,
        top_country_share_pct DECIMAL,
        supply_risk_score DECIMAL,
        high_supply_risk DECIMAL,
        disruption DECIMAL,
        disruption_next_year DECIMAL
        );
    """

    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(tabla)
        conexion.commit()
    except (Exception, TimeoutError) as error:
        if conexion:
            conexion.rollback()
            print("Ha ocurrido un error, los cambios no se han registrado")
    finally:
        cursor.close()

