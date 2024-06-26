def anadirPartidos(conexion):

	partidos=[["Champions", "Final", "2019-06-22","21:00", "ATM", "5-0", "Madrid", 12345, "Calderon", "Cod1", "Cod2"],
			["Champions", "Final", "2020-06-22","21:00", "ATM", "5-0", "Madrid", 12345, "Calderon", "Cod1", "Cod2"],
			["Champions", "Final", "2019-07-22","21:00", "ATM", "5-0", "Madrid", 12345, "Calderon", "Cod1", "Cod2"],
			["Champions", "Final", "2019-06-22","21:00", "ATM", "5-0", "Madrid", 12345, "Calderon", "Cod1", "Cod2"],
			["Champions", "Final", "2023-06-22","21:00", "ATM", "5-0", "Madrid", 12345, "Calderon", "Cod1", "Cod2"],
			["Champions", "Final", "2022-06-13","21:00", "ATM", "5-0", "Madrid", 12345, "Calderon", "Cod1", "Cod2"],
			["Champions", "Final", "2019-06-22","21:00", "ATM", "5-0", "Madrid", 12345, "Calderon", "Cod1", "Cod2"],]

	for partido in partidos:

		conexion.c.execute("""INSERT INTO partidos (competicion, ronda, fecha, hora,
								local, marcador, visitante, publico, sede, codequipo1, codequipo2)
								VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
								tuple(partido))

		conexion.confirmar()

def test_tabla_partidos_vacia_inicio(conexion):

	conexion.c.execute("SELECT * FROM partidos")

	assert not conexion.c.fetchall()

def test_tabla_partidos_llena(conexion):

	assert conexion.tabla_partidos_vacia()

def test_obtener_partidos_no_existen(conexion):

	assert conexion.obtenerPartidosFecha("2019-06-22") is None

def test_obtener_partidos_existen(conexion):

	anadirPartidos(conexion)

	partidos_obtenidos=conexion.obtenerPartidosFecha("2019-06-22")

	assert len(partidos_obtenidos)==3

	for partido in partidos_obtenidos:

		assert partido[5]=="22-06-2019"

def test_partido_existe_no_existe(conexion):

	assert not conexion.partido_existe(0)

def test_partido_existe(conexion):

	anadirPartidos(conexion)

	partidos_obtenidos=conexion.obtenerPartidosFecha("2019-06-22")

	id_partido=partidos_obtenidos[0][-1]

	assert conexion.partido_existe(id_partido)

def test_detalle_partido_no_existe(conexion):

	assert not conexion.detalle_partido(0)

def test_detalle_partido(conexion):

	anadirPartidos(conexion)

	partidos_obtenidos=conexion.obtenerPartidosFecha("2019-06-22")

	id_partido=partidos_obtenidos[0][-1]

	datos_partido=conexion.detalle_partido(id_partido)

	assert len(datos_partido)==11

	conexion.c.execute("DELETE FROM partidos")

	conexion.confirmar()