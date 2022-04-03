

CREATE TABLE PERSONA(
   ID INT NOT NULL AUTO_INCREMENT,
   IDENTIFICACION VARCHAR(100) NOT NULL,
   NOMBRE VARCHAR(40) NOT NULL,
   APELLIDO VARCHAR(40),
   PRIMARY KEY (ID )
);

CREATE TABLE TIPO_REVISION(
   ID INT NOT NULL AUTO_INCREMENT,
   NOMBRE_TIPO VARCHAR(50) NOT NULL,
   PRIMARY KEY (ID )
);


CREATE TABLE VEHICULO(
   ID INT NOT NULL AUTO_INCREMENT,
   MARCA VARCHAR(50) NOT NULL,
   MODELO VARCHAR(50) NOT NULL,
   PATENTE VARCHAR(50) NOT NULL,
   A�O VARCHAR(50) NOT NULL,
   PERSONA_ID INT NOT NULL
   PRIMARY KEY (ID ),
   FOREIGN KEY (PERSONA_ID) REFERENCES PERSONA(ID)
);

CREATE TABLE REVISION(
   ID INT NOT NULL AUTO_INCREMENT,
   VEHICULO_ID INT NOT NULL,
   APROBADO BIT,
   OBSERVACIONES VARCHAR(50),
   PRESONA ID INT NOT NULL,
   FECHA_REVISION DATE NOT NULL,
   PRIMARY KEY (ID ),
   FOREIGN KEY (PERSONA_ID) REFERENCES PERSONA(ID),
   FOREIGN KEY (VEHICULO_ID) REFERENCES VEHICULO(ID)
);


CREATE TABLE INSPECCION(
   ID INT NOT NULL AUTO_INCREMENT,
   REVISION_ID INT NOT NULL,
   TIPO_INSPECCION INT,
   OBSERVACIONES VARCHAR(50),
   ESTADO VARCHAR(10),
   PRESONA ID INT NOT NULL,
   PRIMARY KEY (ID ),
   FOREIGN KEY (PERSONA_ID) REFERENCES PERSONA(ID),
   FOREIGN KEY (TIPO_INSPECCION) REFERENCES TIPO_REVISION(ID),
   FOREIGN KEY (REVISION_ID) REFERENCES REVISION(ID),

);