import pandas as pd

#Leyendo los datos de asistencias
asistenciaDataFrame=pd.read_csv("../data/asistencia_estudiantes_completo.csv")
#print(asistenciaDataFrame)

#Obteniendo informacion basica del dataframe
#print(asistenciaDataFrame.info())

#Obtener los primeros 20 registros
#print(asistenciaDataFrame.head(20))

#Obtener los ultimops 20 registros
#print(asistenciaDataFrame.tail(20))

#Obtener resumen estadistico
#print(asistenciaDataFrame.describe())

#cuenta los valores vacíos en cada columna.
#print(asistenciaDataFrame.isnull().sum())

#Selecciona una columna del DataFrame llamada estado,devuelve todos los valores de esa columna
#print(asistenciaDataFrame['estado'])

#Cuenta cuántas veces se repite cada valor distinto en esa columna.
#print(asistenciaDataFrame['estado'].value_counts())

#Cuenta cuántas veces aparece cada estrato en la tabla.
#print(asistenciaDataFrame['estrato'].value_counts())

#.value_counts().head(2) → Muestra los 2 valores más repetidos en la columna.
#.head(2)                 → Muestra las 2 primeras filas reales (sin contar repeticiones).
#print(asistenciaDataFrame['estrato'].value_counts().head(2))

#Tarea: Filtros o consultas detalladas
#1. Encontrar los estudiantes que si asistieron
estudiantesQueAsistieron=asistenciaDataFrame.query('estado=="asistio"')
print(estudiantesQueAsistieron)

#2. Encontrar los estudiantes que faltaron
#estudiantesQueFaltaron=asistenciaDataFrame.query('estado=="inasistencia"')
#print(estudiantesQueFaltaron)

#3. Encontrar los estudiantes que llegaron tarde(justificaron la inaxistencia)
#justificado=asistenciaDataFrame.query('estado=="justificado"')
#print(justificado)

#4. Encontrar los estudiantes de estrato 1
#estudiantesEstratoUno=asistenciaDataFrame.query('estrato==1')
#print(estudiantesEstratoUno)

#5. Encontrar los estudiantes de estratos altos(5 y 6)
#estrato5y6=asistenciaDataFrame.query('estrato in[5,6]')
#print(estrato5y6)

#6. Encontrar los estudiantes que llegan en metro
#estudiantesMetro=asistenciaDataFrame.query('medio_transporte=="metro"')
#print(estudiantesMetro)

#7. Encontrar los estudiantes que llegaron en bicicleta
#bicicleta=asistenciaDataFrame.query('medio_transporte=="bicicleta"')
#print(bicicleta)

#8. Encontrar todos los estudiantes menos los que llegaron a pie
#estudiantesQueNoCaminan=asistenciaDataFrame.query('medio_transporte!="a pie"')
#print(estudiantesQueNoCaminan)
#print(asistenciaDataFrame["medio_transporte"].unique())

#9. Encontrar todos los registros de asistencia de junio
#asistenciajunio=asistenciaDataFrame[asistenciaDataFrame["fecha"].str.contains("-06-")]
#print(asistenciajunio)

#10.Encontrar todos los estudiantes que usan transportes ecologicos
#transporte_ecologico=asistenciaDataFrame.query('medio_transporte==["bicicleta","a pie"]')
#print(transporte_ecologico)

#11.Encontrar los estudiantes q usan bus y son de estrato alto 
#estudiantes = asistenciaDataFrame.query('medio_transporte=="bus" and estrato==6')
#print(estudiantes)

#12.Encontrar los estudiantes q usan bus y son de estrato bajo
#estudiantes = asistenciaDataFrame.query('medio_transporte=="bus" and estrato < 3')
#print(estudiantes)

#13.Encontrar estudiantes que caminan para llegar a clases
#Caminan =asistenciaDataFrame.query('medio_transporte=="a pie"')
#print(Caminan)

#Conteo por agrupaciones

#1.Conteo de registros por estado de asistencia
#conteo=asistenciaDataFrame.groupby('estado').size()
#print(conteo)

#2.Obtener el numero de registros por estrato
#conteo_estrato=asistenciaDataFrame.groupby('estrato').size()
#print(conteo_estrato)

#3.Cantidad de estudiantes por medio de transporte
#conteoMedioTransporte=asistenciaDataFrame.groupby('medio_transporte').size()
#print(conteoMedioTransporte)

#4.Promedio de estrato por estado de asistencia
#promedioAsistenciaPorEstrato=asistenciaDataFrame.groupby('estado')['estrato'].mean()
#print(promedioAsistenciaPorEstrato)

#5.Maximo estrato por estado
#maximo=asistenciaDataFrame.groupby('estado')['estrato'].max()
#print(maximo)

#6.Minimo estrato por estado
#minimo=asistenciaDataFrame.groupby('estado')['estrato'].min()
#print(minimo)

#7.Conteo de asistencias por grupo y estado
#conteo=asistenciaDataFrame.groupby(['id_grupo','estado']).size()
#print(conteo)
