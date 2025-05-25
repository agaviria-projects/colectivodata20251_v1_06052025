import pandas as pd

# Cargar archivo Excel desde carpeta 'data'
usuarioDataFrame = pd.read_excel("../data/usuarios_sistema_completo.xlsx")

# Mostrar primeras filas
print(usuarioDataFrame.head())

# Conteo de tipo de usuario
print("\nConteo de tipos de usuario:")
print(usuarioDataFrame["tipo_usuario"].value_counts())

# Valores únicos para validar errores de escritura
print("\nValores únicos en tipo_usuario:")
print(usuarioDataFrame["tipo_usuario"].unique())

# Verificar columnas con valores faltantes
print("\nColumnas con valores faltantes:")
print(usuarioDataFrame.isnull().sum())

#print(usuarioDataFrame.isnull().sum)

#1. Necesito una tabla con aprendices o estudiantes
#aprendices_o_estudiantes = usuarioDataFrame.query('tipo_usuario == "aprendiz" or tipo_usuario == "estudiante"')
#print(aprendices_o_estudiantes)

#2. Listado de instructores o profesores
#instructores_o_profesores = usuarioDataFrame.query('tipo_usuario == "instructor" or tipo_usuario == "profesor"')
#print(instructores_o_profesores)

#3. Listado de especialistas en especialidad de desarrollo web o sistemas
#usuariosWebSistemas = usuarioDataFrame.query('especialidad == "desarrollo web" or especialidad == "sistemas"')
#print(usuariosWebSistemas)

#4. Listado de solo usuarios con direcciones en Medellin
#usuariosMedellin = usuarioDataFrame.query('direccion == "Medellin"')
#print(usuariosMedellin)

#5. Listado de usuarios cuya direcciones terminen en sur
#usuariosSur = usuarioDataFrame[usuarioDataFrame["direccion"].str.endswith("sur")]
#print(usuariosSur)

#6. Listado de especialistas o profesores que contengan la palabra datos
#resultado = usuarioDataFrame[
    #(usuarioDataFrame["tipo_usuario"] == "especialista") |
    #(usuarioDataFrame["tipo_usuario"] == "profesor")
#]

#resultado = resultado[resultado["especialidad"].str.contains("datos")]
#print(resultado)

#7. Necesito docentes de Itagui
#docentes_itagui = usuarioDataFrame[
    #(usuarioDataFrame["tipo_usuario"] == "docente") &
    #(usuarioDataFrame["direccion"] == "Itagui")
#]
#print(docentes_itagui)

#8. Necesito lista de nacidos del 90 o anteriores
# Convertir la columna a tipo fecha (si no lo está)
#usuarioDataFrame["fecha_nacimiento"] = pd.to_datetime(usuarioDataFrame["fecha_nacimiento"])
# Filtrar nacidos hasta el 31 de diciembre de 1990
#nacidos_90_o_antes = usuarioDataFrame[usuarioDataFrame["fecha_nacimiento"] <= "1990-12-31"]
#print(nacidos_90_o_antes)

#9. Necesito listado instructores o profesores mayores
# Convertimos la fecha a formato fecha (si no lo hemos hecho)
#usuarioDataFrame["fecha_nacimiento"] = pd.to_datetime(usuarioDataFrame["fecha_nacimiento"])

# Calculamos la edad
#usuarioDataFrame["edad"] = (pd.to_datetime("today") - usuarioDataFrame["fecha_nacimiento"]).dt.days // 365

# Filtramos instructores o profesores mayores de 50
#docentes_mayores = usuarioDataFrame[
    #((usuarioDataFrame["tipo_usuario"] == "instructor") | 
     #(usuarioDataFrame["tipo_usuario"] == "profesor")) &
    #(usuarioDataFrame["edad"] > 50)
#]
#print(docentes_mayores)


#10. Necesito de profesores y estudiantes nacidos en el nuevo milenium
# Asegurarse de que la fecha esté en formato fecha
#usuarioDataFrame["fecha_nacimiento"] = pd.to_datetime(usuarioDataFrame["fecha_nacimiento"])

# Filtrar profesores y estudiantes nacidos desde el año 2000
#nuevomilenio = usuarioDataFrame[
    #((usuarioDataFrame["tipo_usuario"] == "profesor") |
     #(usuarioDataFrame["tipo_usuario"] == "estudiante")) &
    #(usuarioDataFrame["fecha_nacimiento"] >= "2000-01-01")
#]
#print(nuevomilenio)


