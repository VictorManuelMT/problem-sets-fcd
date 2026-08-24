#%%
# 1

import pandas as pd

# Ruta de los dataframes filtrados de la sección anterior
ruta_datos = (
    r"C:\Users\Victor Manuel\Desktop\INEI - CLASES"
    r"\FUNDAMENTOS\ProblemSet1\Resultados"
)

# Leer los dataframes filtrados de 2024 y 2025
df_2024 = pd.read_csv(
    ruta_datos + r"\Enaho01-2024-100_filtrado.csv",
    encoding="utf-8-sig"
)

df_2025 = pd.read_csv(
    ruta_datos + r"\Enaho01-2025-100_filtrado.csv",
    encoding="utf-8-sig"
)

# Nombres de las columnas estén en minúscula
df_2024.columns = df_2024.columns.str.lower()
df_2025.columns = df_2025.columns.str.lower()


# Crear la variable dicotómica target
# 0 = Respuesta: encuesta completa o incompleta
# 1 = No respuesta: cualquier otro resultado

df_2024["target"] = 0
df_2024.loc[~df_2024["result"].isin([1, 2]), "target"] = 1

df_2025["target"] = 0
df_2025.loc[~df_2025["result"].isin([1, 2]), "target"] = 1


# Verificación
print("2024 - Result y Target:")
print(
    df_2024
    .groupby(["result", "target"])
    .size()
)

print("\n2025 - Result y Target:")
print(
    df_2025
    .groupby(["result", "target"])
    .size()
)

print("\nFrecuencia del target 2024:")
print(df_2024["target"].value_counts().sort_index())

print("\nFrecuencia del target 2025:")
print(df_2025["target"].value_counts().sort_index())





#%%
# 2

# Convertir ubigeo a texto y completar con ceros a la izquierda
df_2024["ubigeo"] = df_2024["ubigeo"].astype(str).str.zfill(6)
df_2025["ubigeo"] = df_2025["ubigeo"].astype(str).str.zfill(6)


# Crear departamento y provincia a partir de ubigeo
df_2024["departamento"] = df_2024["ubigeo"].str[:2]
df_2024["provincia"] = df_2024["ubigeo"].str[:4]

df_2025["departamento"] = df_2025["ubigeo"].str[:2]
df_2025["provincia"] = df_2025["ubigeo"].str[:4]


# Verificación
print("2024:")
print(
    df_2024[
        ["ubigeo", "departamento", "provincia"]
    ].head(10)
)

print("\n2025:")
print(
    df_2025[
        ["ubigeo", "departamento", "provincia"]
    ].head(10)
)

print("\nCantidad de departamentos 2024:")
print(df_2024["departamento"].nunique())

print("\nCantidad de provincias 2024:")
print(df_2024["provincia"].nunique())

print("\nCantidad de departamentos 2025:")
print(df_2025["departamento"].nunique())

print("\nCantidad de provincias 2025:")
print(df_2025["provincia"].nunique())













#%%
# 3

# Crear la variable área a partir de estrato
df_2024["area"] = ""
df_2024.loc[df_2024["estrato"] <= 5, "area"] = "Urbano"
df_2024.loc[df_2024["estrato"] >= 6, "area"] = "Rural"

df_2025["area"] = ""
df_2025.loc[df_2025["estrato"] <= 5, "area"] = "Urbano"
df_2025.loc[df_2025["estrato"] >= 6, "area"] = "Rural"


# Verificación
print("2024 - Distribución por área:")
print(df_2024["area"].value_counts())

print("\n2025 - Distribución por área:")
print(df_2025["area"].value_counts())


print("\n2024 - Estrato y área:")
print(
    df_2024[
        ["estrato", "area"]
    ].drop_duplicates().sort_values("estrato")
)

print("\n2025 - Estrato y área:")
print(
    df_2025[
        ["estrato", "area"]
    ].drop_duplicates().sort_values("estrato")
)







#%%
# 4

# Crear la variable región natural a partir de dominio
df_2024["region_natural"] = ""
df_2024.loc[df_2024["dominio"].isin([1, 2, 3]), "region_natural"] = "Costa"
df_2024.loc[df_2024["dominio"].isin([4, 5, 6]), "region_natural"] = "Sierra"
df_2024.loc[df_2024["dominio"] == 7, "region_natural"] = "Selva"
df_2024.loc[df_2024["dominio"] == 8, "region_natural"] = "Lima Metropolitana"

df_2025["region_natural"] = ""
df_2025.loc[df_2025["dominio"].isin([1, 2, 3]), "region_natural"] = "Costa"
df_2025.loc[df_2025["dominio"].isin([4, 5, 6]), "region_natural"] = "Sierra"
df_2025.loc[df_2025["dominio"] == 7, "region_natural"] = "Selva"
df_2025.loc[df_2025["dominio"] == 8, "region_natural"] = "Lima Metropolitana"


# Verificación
print("2024 - Distribución por región natural:")
print(df_2024["region_natural"].value_counts())

print("\n2025 - Distribución por región natural:")
print(df_2025["region_natural"].value_counts())


print("\n2024 - Dominio y región natural:")
print(
    df_2024[
        ["dominio", "region_natural"]
    ].drop_duplicates().sort_values("dominio")
)

print("\n2025 - Dominio y región natural:")
print(
    df_2025[
        ["dominio", "region_natural"]
    ].drop_duplicates().sort_values("dominio")
)



#%%
# 5

# Crear trimestre a partir del mes
df_2024["trimestre"] = pd.cut(
    df_2024["mes"],
    bins=[0, 3, 6, 9, 12],
    labels=[1, 2, 3, 4]
)

df_2025["trimestre"] = pd.cut(
    df_2025["mes"],
    bins=[0, 3, 6, 9, 12],
    labels=[1, 2, 3, 4]
)


# Crear variables discretas para mes
mes_2024 = pd.get_dummies(
    df_2024["mes"],
    prefix="mes",
    dtype=int
)

mes_2025 = pd.get_dummies(
    df_2025["mes"],
    prefix="mes",
    dtype=int
)


# Crear variables discretas para trimestre
trimestre_2024 = pd.get_dummies(
    df_2024["trimestre"],
    prefix="trimestre",
    dtype=int
)

trimestre_2025 = pd.get_dummies(
    df_2025["trimestre"],
    prefix="trimestre",
    dtype=int
)


# Crear variables discretas para departamento
departamento_2024 = pd.get_dummies(
    df_2024["departamento"],
    prefix="departamento",
    dtype=int
)

departamento_2025 = pd.get_dummies(
    df_2025["departamento"],
    prefix="departamento",
    dtype=int
)


# Crear variables discretas para provincia
provincia_2024 = pd.get_dummies(
    df_2024["provincia"],
    prefix="provincia",
    dtype=int
)

provincia_2025 = pd.get_dummies(
    df_2025["provincia"],
    prefix="provincia",
    dtype=int
)


# Crear variables discretas para urbano y rural
area_2024 = pd.get_dummies(
    df_2024["area"],
    dtype=int
)

area_2025 = pd.get_dummies(
    df_2025["area"],
    dtype=int
)

area_2024.columns = area_2024.columns.str.lower()
area_2025.columns = area_2025.columns.str.lower()


# Crear variables discretas para región natural
region_2024 = pd.get_dummies(
    df_2024["region_natural"],
    prefix="region",
    dtype=int
)

region_2025 = pd.get_dummies(
    df_2025["region_natural"],
    prefix="region",
    dtype=int
)


# Crear variables discretas para dominio
dominio_2024 = pd.get_dummies(
    df_2024["dominio"],
    prefix="dominio",
    dtype=int
)

dominio_2025 = pd.get_dummies(
    df_2025["dominio"],
    prefix="dominio",
    dtype=int
)


# Agregar las nuevas variables a los dataframes
df_2024 = pd.concat(
    [
        df_2024,
        mes_2024,
        trimestre_2024,
        departamento_2024,
        provincia_2024,
        area_2024,
        region_2024,
        dominio_2024
    ],
    axis=1
)

df_2025 = pd.concat(
    [
        df_2025,
        mes_2025,
        trimestre_2025,
        departamento_2025,
        provincia_2025,
        area_2025,
        region_2025,
        dominio_2025
    ],
    axis=1
)


# Verificación
print("Dimensión del dataframe 2024 después de crear variables discretas:")
print(df_2024.shape)

print("\nDimensión del dataframe 2025 después de crear variables discretas:")
print(df_2025.shape)


print("\nVariables de mes creadas en 2024:")
print(mes_2024.columns.tolist())

print("\nVariables de trimestre creadas en 2024:")
print(trimestre_2024.columns.tolist())

print("\nVariables de área creadas en 2024:")
print(area_2024.columns.tolist())

print("\nVariables de región natural creadas en 2024:")
print(region_2024.columns.tolist())

print("\nVariables de dominio creadas en 2024:")
print(dominio_2024.columns.tolist())


print("\nEjemplo de las variables discretas de área:")
print(
    df_2024[
        ["area", "urbano", "rural"]
    ].head(10)
)

print("\nEjemplo de mes y trimestre:")
print(
    df_2024[
        ["mes", "trimestre", "mes_1", "mes_2", "mes_3",
         "trimestre_1", "trimestre_2", "trimestre_3", "trimestre_4"]
    ].head(10)
)






#%%
# 6

# Función para obtener porcentajes de respuesta y no respuesta
def estadisticas_target(df, variable, anio):

    tabla = (
        df
        .groupby(variable)["target"]
        .agg(["count", "mean"])
        .reset_index()
    )

    # Como target = 1 representa no respuesta,
    # su media equivale a la proporción de no respuesta
    tabla["no_respuesta"] = (tabla["mean"] * 100).round(2)

    # El porcentaje restante corresponde a respuesta
    tabla["respuesta"] = (100 - tabla["no_respuesta"]).round(2)

    tabla = tabla[
        [variable, "count", "respuesta", "no_respuesta"]
    ]

    tabla = tabla.rename(
        columns={
            "count": "hogares_" + str(anio),
            "respuesta": "respuesta_" + str(anio),
            "no_respuesta": "no_respuesta_" + str(anio)
        }
    )

    return tabla


# Estadísticas por mes
mes_2024_est = estadisticas_target(df_2024, "mes", 2024)
mes_2025_est = estadisticas_target(df_2025, "mes", 2025)

comparacion_mes = pd.merge(
    mes_2024_est,
    mes_2025_est,
    on="mes",
    how="outer"
)


# Estadísticas por trimestre
trimestre_2024_est = estadisticas_target(
    df_2024, "trimestre", 2024
)

trimestre_2025_est = estadisticas_target(
    df_2025, "trimestre", 2025
)

comparacion_trimestre = pd.merge(
    trimestre_2024_est,
    trimestre_2025_est,
    on="trimestre",
    how="outer"
)


# Estadísticas por departamento
departamento_2024_est = estadisticas_target(
    df_2024, "departamento", 2024
)

departamento_2025_est = estadisticas_target(
    df_2025, "departamento", 2025
)

comparacion_departamento = pd.merge(
    departamento_2024_est,
    departamento_2025_est,
    on="departamento",
    how="outer"
)


# Estadísticas por provincia
provincia_2024_est = estadisticas_target(
    df_2024, "provincia", 2024
)

provincia_2025_est = estadisticas_target(
    df_2025, "provincia", 2025
)

comparacion_provincia = pd.merge(
    provincia_2024_est,
    provincia_2025_est,
    on="provincia",
    how="outer"
)


# Estadísticas por urbano y rural
area_2024_est = estadisticas_target(
    df_2024, "area", 2024
)

area_2025_est = estadisticas_target(
    df_2025, "area", 2025
)

comparacion_area = pd.merge(
    area_2024_est,
    area_2025_est,
    on="area",
    how="outer"
)


# Estadísticas por región natural
region_2024_est = estadisticas_target(
    df_2024, "region_natural", 2024
)

region_2025_est = estadisticas_target(
    df_2025, "region_natural", 2025
)

comparacion_region = pd.merge(
    region_2024_est,
    region_2025_est,
    on="region_natural",
    how="outer"
)


# Estadísticas por dominio
dominio_2024_est = estadisticas_target(
    df_2024, "dominio", 2024
)

dominio_2025_est = estadisticas_target(
    df_2025, "dominio", 2025
)

comparacion_dominio = pd.merge(
    dominio_2024_est,
    dominio_2025_est,
    on="dominio",
    how="outer"
)


# Mostrar resultados
print("Comparación por mes:")
print(comparacion_mes)

print("\nComparación por trimestre:")
print(comparacion_trimestre)

print("\nComparación por área:")
print(comparacion_area)

print("\nComparación por región natural:")
print(comparacion_region)

print("\nComparación por dominio:")
print(comparacion_dominio)

print("\nComparación por departamento:")
print(comparacion_departamento)

print("\nPrimeras 20 provincias:")
print(comparacion_provincia.head(20))




#%%
# 6

print("Comparación por trimestre:")
print(comparacion_trimestre.to_string(index=False))

print("\nComparación por área:")
print(comparacion_area.to_string(index=False))

print("\nComparación por región natural:")
print(comparacion_region.to_string(index=False))

print("\nComparación por dominio:")
print(comparacion_dominio.to_string(index=False))

print("\nComparación por departamento:")
print(comparacion_departamento.to_string(index=False))





#%%
# 7

# Ruta donde se guardarán los dataframes transformados
ruta_salida = (
    r"C:\Users\Victor Manuel\Desktop\INEI - CLASES"
    r"\FUNDAMENTOS\ProblemSet1\Resultados"
)

# Guardar dataframe 2024
df_2024.to_csv(
    ruta_salida + r"\Enaho01-2024-100_transformado.csv",
    index=False,
    encoding="utf-8-sig"
)

# Guardar dataframe 2025
df_2025.to_csv(
    ruta_salida + r"\Enaho01-2025-100_transformado.csv",
    index=False,
    encoding="utf-8-sig"
)

# Verificación
print("Dataframe 2024 guardado:")
print(df_2024.shape)

print("\nDataframe 2025 guardado:")
print(df_2025.shape)

print("\nArchivos guardados correctamente en:")
print(ruta_salida)