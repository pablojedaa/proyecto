BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Manager" (
	"id_manager"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"edad"	INTEGER NOT NULL,
	PRIMARY KEY("id_manager")
);
CREATE TABLE IF NOT EXISTS "Marca" (
	"id_marca"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"dinero"	INTEGER NOT NULL,
	PRIMARY KEY("id_marca")
);
CREATE TABLE IF NOT EXISTS "Jugadores" (
	"id_jugador"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"edad"	INTEGER NOT NULL,
	"id_manager"	INTEGER NOT NULL,
	"id_marca"	INTEGER NOT NULL,
	FOREIGN KEY("id_marca") REFERENCES "Marca"("id_marca"),
	PRIMARY KEY("id_jugador"),
	FOREIGN KEY("id_manager") REFERENCES "Manager"("id_manager")
);
COMMIT;
