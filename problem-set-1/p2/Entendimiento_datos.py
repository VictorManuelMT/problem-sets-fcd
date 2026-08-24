
#%%
import pandas as pd

#%%
# 1. RUTAS DE LOS ARCHIVOS

ruta_modulo_100 = r"C:\Users\Victor Manuel\Desktop\INEI - CLASES\FUNDAMENTOS\ProblemSet1\BD_ENAHO\Enaho01-2024-100.csv"
ruta_modulo_200 = r"C:\Users\Victor Manuel\Desktop\INEI - CLASES\FUNDAMENTOS\ProblemSet1\BD_ENAHO\Enaho01-2024-200.csv"

#%%
# 2. LECTURA DE LOS ARCHIVOS

df_100 = pd.read_csv(
    ruta_modulo_100,
    encoding="latin-1",
    na_values=[" "]
)

df_200 = pd.read_csv(
    ruta_modulo_200,
    encoding="latin-1",
    na_values=[" "]
)

#%%
# 3. NOMBRES DE LAS COLUMNAS EN MINÚSCULA

df_100.columns = df_100.columns.str.lower()
df_200.columns = df_200.columns.str.lower()

#%%
# 4. EXPLORACIÓN INICIAL

print("Dimensión del módulo 100:")
print(df_100.shape)

print("\nDimensión del módulo 200:")
print(df_200.shape)

print("\nFrecuencia de la variable result:")
print(df_100["result"].value_counts(dropna=False).sort_index())

#%%
# 5. REVISIÓN DE VALORES FALTANTES SEGÚN RESULT

variables_revision = [
    "mes",
    "ubigeo",
    "dominio",
    "estrato",
    "periodo",
    "tipenc",
    "panel",
    "p22",
    "p24a",
    "p24b",
    "p101",
    "p102",
    "p103",
    "p104",
    "p105a"
]

faltantes_por_result = (
    df_100
    .groupby("result")[variables_revision]
    .agg(lambda x: x.isna().mean() * 100)
    .round(2)
)

print("\nPorcentaje de valores faltantes según result:")
print(faltantes_por_result)

#%%

# 6. COMPARACIÓN: VARIABLES DISPONIBLES ANTES DE LA ENTREVISTA
#    VS. VARIABLES OBTENIDAS DURANTE LA ENTREVISTA

variables_base = [
    "mes",
    "ubigeo",
    "dominio",
    "estrato",
    "periodo",
    "tipenc"
]

variables_entrevista = [
    "p22",
    "p24a",
    "p24b",
    "p101",
    "p102",
    "p103",
    "p104",
    "p105a"
]

# Casos considerados como no respuesta:
# result diferente de 1 (Completa) y 2 (Incompleta)
df_no_respuesta = df_100[~df_100["result"].isin([1, 2])]

print("\nValores faltantes en variables base para casos de no respuesta:")
print(
    (df_no_respuesta[variables_base].isna().mean() * 100)
    .round(2)
)

print("\nValores faltantes en variables obtenidas durante la entrevista:")
print(
    (df_no_respuesta[variables_entrevista].isna().mean() * 100)
    .round(2)
)

#%%
# 7. VARIABLES QUE PODRÍAN UTILIZARSE COMO PREDICTORES

variables_predictoras = [
    "mes",
    "ubigeo",
    "dominio",
    "estrato",
    "periodo",
    "tipenc"
]

print("\nVariables potencialmente utilizables como predictoras:")
print(variables_predictoras)

print("\nValores faltantes de estas variables:")
print(df_100[variables_predictoras].isna().sum())

#%%
# 8. EVALUACIÓN DEL MÓDULO 200

# Variables que identifican a cada hogar en ambos módulos
llaves_hogar = [
    "año",
    "conglome",
    "vivienda",
    "hogar"
]

# Resultado de la entrevista por hogar
resultado_hogar = (
    df_100[llaves_hogar + ["result"]]
    .drop_duplicates()
)

# Hogares que aparecen en el módulo 200
hogares_modulo_200 = (
    df_200[llaves_hogar]
    .drop_duplicates()
)

# Unimos los hogares del módulo 200 con su resultado
comparacion_modulo_200 = pd.merge(
    hogares_modulo_200,
    resultado_hogar,
    on=llaves_hogar,
    how="left"
)

print("\nResultados de los hogares que aparecen en el módulo 200:")
print(
    comparacion_modulo_200["result"]
    .value_counts(dropna=False)
    .sort_index()
)
#%%
# 3. Después de la reflexión de 2, filtra sólo estas variables.

variables_filtradas = [
    "año",
    "mes",
    "conglome",
    "vivienda",
    "hogar",
    "ubigeo",
    "dominio",
    "estrato",
    "periodo",
    "tipenc",
    "result"
]

df_100_filtrado = df_100[variables_filtradas].copy()

print("Dimensión del dataframe original:")
print(df_100.shape)

print("\nDimensión del dataframe filtrado:")
print(df_100_filtrado.shape)

print("\nVariables conservadas:")
print(df_100_filtrado.columns.tolist())

print("\nPrimeras filas del dataframe filtrado:")
print(df_100_filtrado.head())


#%%
# 4

# Ruta donde se encuentran los archivos CSV
ruta_datos = r"C:\Users\Victor Manuel\Desktop\INEI - CLASES\FUNDAMENTOS\ProblemSet1\BD_ENAHO"

# Lectura del módulo 100 para cada año
df_2019 = pd.read_csv(ruta_datos + r"\Enaho01-2019-100.csv",
                      encoding="latin-1",
                      na_values=[" "])

df_2020 = pd.read_csv(ruta_datos + r"\Enaho01-2020-100.csv",
                      encoding="latin-1",
                      na_values=[" "])

df_2021 = pd.read_csv(ruta_datos + r"\Enaho01-2021-100.csv",
                      encoding="latin-1",
                      na_values=[" "])

df_2022 = pd.read_csv(ruta_datos + r"\Enaho01-2022-100.csv",
                      encoding="latin-1",
                      na_values=[" "])

df_2023 = pd.read_csv(ruta_datos + r"\Enaho01-2023-100.csv",
                      encoding="latin-1",
                      na_values=[" "])

df_2024 = pd.read_csv(ruta_datos + r"\Enaho01-2024-100.csv",
                      encoding="latin-1",
                      na_values=[" "])

df_2025 = pd.read_csv(ruta_datos + r"\Enaho01-2025-100.csv",
                      encoding="latin-1",
                      sep=";",
                      na_values=[" "])


# Nombres de columnas en minúscula
df_2019.columns = df_2019.columns.str.lower()
df_2020.columns = df_2020.columns.str.lower()
df_2021.columns = df_2021.columns.str.lower()
df_2022.columns = df_2022.columns.str.lower()
df_2023.columns = df_2023.columns.str.lower()
df_2024.columns = df_2024.columns.str.lower()
df_2025.columns = df_2025.columns.str.lower()


# Conservamos solamente año y result para este análisis
df_result = pd.concat(
    [
        df_2019[["año", "result"]],
        df_2020[["año", "result"]],
        df_2021[["año", "result"]],
        df_2022[["año", "result"]],
        df_2023[["año", "result"]],
        df_2024[["año", "result"]],
        df_2025[["año", "result"]]
    ],
    ignore_index=True
)


# Número de hogares según año y categoría de result
tabla_result = (
    df_result
    .groupby(["año", "result"])
    .size()
    .reset_index(name="hogares")
)


# Total de hogares por año
total_anual = (
    tabla_result
    .groupby("año")["hogares"]
    .sum()
    .reset_index(name="total_hogares")
)


# Agregamos el total anual a cada categoría
tabla_result = pd.merge(
    tabla_result,
    total_anual,
    on="año",
    how="left"
)


# Calculamos el porcentaje de hogares
tabla_result["porcentaje"] = (
    tabla_result["hogares"] /
    tabla_result["total_hogares"] *
    100
)


# Cuadro final: años en filas y categorías de result en columnas
tabla_porcentajes = pd.pivot_table(
    tabla_result,
    values="porcentaje",
    index="año",
    columns="result",
    aggfunc="sum",
    fill_value=0
).round(2)


# Nombres de las categorías
tabla_porcentajes = tabla_porcentajes.rename(
    columns={
        1: "Completa",
        2: "Incompleta",
        3: "Rechazo",
        4: "Ausente",
        5: "Vivienda Desocupada",
        6: "No se Inició la Entrevista",
        7: "Otro"
    }
)


# Año vuelve a ser una columna
tabla_porcentajes = tabla_porcentajes.reset_index()


print("Porcentaje de hogares según resultado de la encuesta por año:")
print(tabla_porcentajes)


# Guardar el resultado como CSV
ruta_salida = (
    r"C:\Users\Victor Manuel\Desktop\INEI - CLASES"
    r"\FUNDAMENTOS\ProblemSet1\Resultados"
    r"\porcentaje_result_2019_2025.csv"
)

tabla_porcentajes.to_csv(
    ruta_salida,
    index=False,
    encoding="utf-8-sig"
)

print("\nArchivo guardado correctamente en:")
print(ruta_salida)





#%%
#%%
# 5

variables_filtradas = [
    "año",
    "mes",
    "conglome",
    "vivienda",
    "hogar",
    "ubigeo",
    "dominio",
    "estrato",
    "periodo",
    "tipenc",
    "result"
]

variables_filtradas_200 = [
    "año",
    "mes",
    "conglome",
    "vivienda",
    "hogar",
    "codperso",
    "ubigeo",
    "dominio",
    "estrato"
]


# Filtrar las variables del módulo 100
df_2019_filtrado = df_2019[variables_filtradas].copy()
df_2020_filtrado = df_2020[variables_filtradas].copy()
df_2021_filtrado = df_2021[variables_filtradas].copy()
df_2022_filtrado = df_2022[variables_filtradas].copy()
df_2023_filtrado = df_2023[variables_filtradas].copy()
df_2024_filtrado = df_2024[variables_filtradas].copy()
df_2025_filtrado = df_2025[variables_filtradas].copy()


# Filtrar el módulo 200 de 2024
df_200_filtrado = df_200[variables_filtradas_200].copy()


# Ruta donde se guardarán los dataframes filtrados
ruta_salida_filtrados = (
    r"C:\Users\Victor Manuel\Desktop\INEI - CLASES"
    r"\FUNDAMENTOS\ProblemSet1\Resultados"
)


# Guardar los módulos 100
df_2019_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2019-100_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)

df_2020_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2020-100_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)

df_2021_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2021-100_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)

df_2022_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2022-100_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)

df_2023_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2023-100_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)

df_2024_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2024-100_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)

df_2025_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2025-100_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)


# Guardar el módulo 200 de 2024
df_200_filtrado.to_csv(
    ruta_salida_filtrados + r"\Enaho01-2024-200_filtrado.csv",
    index=False,
    encoding="utf-8-sig"
)


# Verificación
print("Dimensiones de los dataframes filtrados:")

print("2019 - Módulo 100:", df_2019_filtrado.shape)
print("2020 - Módulo 100:", df_2020_filtrado.shape)
print("2021 - Módulo 100:", df_2021_filtrado.shape)
print("2022 - Módulo 100:", df_2022_filtrado.shape)
print("2023 - Módulo 100:", df_2023_filtrado.shape)
print("2024 - Módulo 100:", df_2024_filtrado.shape)
print("2024 - Módulo 200:", df_200_filtrado.shape)
print("2025 - Módulo 100:", df_2025_filtrado.shape)

print("\nVariables conservadas del módulo 100:")
print(variables_filtradas)

print("\nVariables conservadas del módulo 200:")
print(variables_filtradas_200)

print("\nDataframes filtrados guardados correctamente en:")
print(ruta_salida_filtrados)

# %%
