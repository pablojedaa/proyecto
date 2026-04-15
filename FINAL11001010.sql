BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Manager" (
	"id_manager"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"edad"	INTEGER NOT NULL,
	PRIMARY KEY("id_manager" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Marca" (
	"id_marca"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"dinero"	INTEGER NOT NULL,
	PRIMARY KEY("id_marca" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Jugadores" (
	"id_jugador"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"edad"	INTEGER NOT NULL,
	"id_manager"	INTEGER NOT NULL,
	"id_marca"	INTEGER NOT NULL,
	FOREIGN KEY("id_manager") REFERENCES "Manager"("id_manager"),
	PRIMARY KEY("id_jugador" AUTOINCREMENT),
	FOREIGN KEY("id_marca") REFERENCES "Marca"("id_marca")
);
INSERT INTO "Manager" VALUES (1,'Pellegrini',72);
INSERT INTO "Manager" VALUES (2,'Pepe Mel',63);
INSERT INTO "Manager" VALUES (3,'Setién',67);
INSERT INTO "Marca" VALUES (1,'Kappa',30000000);
INSERT INTO "Marca" VALUES (2,'Macron',9000000);
INSERT INTO "Marca" VALUES (3,'Adidas',50000000);
INSERT INTO "Jugadores" VALUES (1,'Joaquín',44,1,1);
INSERT INTO "Jugadores" VALUES (2,'Ruben Castro',43,2,2);
INSERT INTO "Jugadores" VALUES (3,'Fabián',28,3,3);
COMMIT;
