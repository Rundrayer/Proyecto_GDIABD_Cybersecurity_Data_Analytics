# Guía de Ejecución General y Estructura del Proyecto

**Proyecto Integrador: Cybersecurity Data Analytics**

---

## Apreciaciones

El proyecto está diseñado como un **pipeline modular y secuencial** compuesto por **10 notebooks numerados**. Cada etapa transforma los datos y genera artefactos persistentes que sirven de insumo obligatorio para la siguiente fase:

>**Datasets Iniciales:** Los unicos archivos impresindibles para su uso especifico, son los 3 datasets externos que le brindan al proyecto su fuente de datos, y que deben acoplacerse en la carpeta Recursos la cual reconocera automaticamente la estructura del proyecto. (link de drive con estos 3 artefactos: )
- **Ejecución estrictamente secuencial:** No ejecute notebooks aislados sin haber corrido previamente las etapas anteriores, ya que fallarán al buscar los archivos `.parquet`, `.pkl` o `.joblib` intermedios.
- **Recursos de cómputo:** Las etapas de PySpark, la validación cruzada de la Guía 9 y la búsqueda en grilla de la Guía 10 hacen uso intensivo de procesador y RAM; se recomienda cerrar aplicaciones innecesarias durante el entrenamiento.
- **Integridad de artefactos:** No renombre ni edite manualmente los artefactos generados en la ejecución de los notebooks ni las carpetas iniciales; el código verifica esquemas de columnas y firmas para garantizar reproducibilidad.

---

## Conectores y herramientas

### 1. `Configuracion.py`

El archivo `Configuracion.py` actúa como la **única fuente de verdad** para la configuración del entorno en todo el proyecto. Su propósito es evitar rutas absolutas escritas a mano dentro de los 10 notebooks.

- **Gestión automática de rutas:** Define automáticamente la raíz del proyecto y construye las rutas relativas hacia las carpetas de datos crudos, capas Parquet procesadas, resultados analíticos, reportes y modelos serializados.
- **Configuración de Spark y Hadoop:** Centraliza la referencia a `HADOOP_HOME`, específicamente la dirección de ruta de los binarios necesarios para ejecutar en Windows de no contar con estas como variables de entorno, esenciales como parámetros base de inicialización de sesiones de Spark.

> **Nota de uso:** Antes de correr la Guía 1 por primera vez, abre `Configuracion.py` y verifica que la ruta base del proyecto y la variable de entorno de Hadoop coincidan con la ubicación real en tu computadora, o clona el repositorio y ejecútalo desde ese punto con el entorno de ejecución a elección.

### 2. `.gitignore`

Los archivos de tráfico de red y las capas intermedias de Spark ocupan cientos de megabytes o gigabytes, superando el límite de tamaño de archivo de GitHub (100 MB). Archivos como `datos_split_guia8.pkl` o `modelo_optimizado_guia10.joblib` son binarios generados automáticamente por el código y se excluyen del control de versiones porque pueden reconstruirse de forma determinista ejecutando los notebooks.

Ayudo al equipo impidiendo que se subieran por accidente datasets crudos o tablas intermedias con direcciones IP sin anonimizar antes de pasar por los procesos de agregación y garantizó que en GitHub quedara exclusivamente el código fuente, la configuración centralizada, las plantillas y los resultados analíticos ligeros necesarios para auditar el proyecto.

### 3. `Descarga_Librerias.txt`

El archivo `Descarga_Librerias.txt` funciona como la **guía de preparación y alistamiento del entorno técnico** antes de ejecutar cualquiera de los 10 notebooks.

- **Descripción:** Detalla los requisitos de software base (versión de Python, JDK de Java y binarios de Hadoop para ejecución local en Windows) junto con el listado completo de librerías necesarias para cada fase del pipeline (procesamiento con PySpark y Pandas, visualización y reportería con Plotly/Jinja2, y modelado con scikit-learn y Joblib).
- **Uso:** Antes de iniciar la ejecución del proyecto en una máquina nueva, el usuario debe consultar este archivo, instalar las dependencias mediante el comando `pip` sugerido y validar las variables de entorno (`JAVA_HOME` y `HADOOP_HOME`) para asegurar que todas las guías corran sin errores de importación ni incompatibilidades.


## Estructura del Proyecto Ejecutado

A continuación se detalla la organización de directorios y archivos principales del proyecto

El repositorio tiene las mismas marcas para replicar este resultado, pero no contempla archivos demasiado pesados por razones de almacenamiento.

```text
Proyecto_GDIABD_Cybersecurity_Data_Analytics/
├── Datos/                                             # Capas de datos, salidas analíticas y artefactos del pipeline
│   ├── Analiticos/                                    # Tablas agregadas y métricas listas para consumo analítico 
|   |   ├── Parquet/                                   # Parquet Procesado, enriquecido y de modelado para reproducibilidad
|   |   |   └──[dataset_crudo_limpio_final.parquet, 
|   |   |        dataset_enriquecido_final.parquet,
|   |   |        dataset_modelado_guia08.parquet]      # Muestra estratificada limpia (21 variables) previa al split de ML
│   │   └── Resultados/                                #Reporte de calidad y de estrcutura para dataset Analitico
|   |       └──[REPORTE_ARQUITECTURA_BLOQUE3.md, 
|   |           Reporte_calidad_de_datos_df_Bloque2.xlsx]
|   |
│   ├── CSV_Generados/                                 # Vistas analíticas anonimizadas y gobernadas listas para distribución (Guia 4)
│   │   ├── dataset_publicable_redes.csv               # Versión CSV anonimizada y minimizada para consumo externo o Power BI
│   │   └── dataset_publicable_redes.parquet           # Versión Parquet comprimida del dataset gobernado
|   |
│   ├── Cargados/                                      # Ingesta inicial de fuentes crudas y descompresión del dataset original
│   │   ├── GeneratedLabelledFlows/                    # Flujos etiquetados descomprimidos (contiene parte de los 9 CSV de tráfico)
|   |       └──[CSVS De registros de trafico] 
│   │   ├── MachineLearningCSV/                        # Datos de tráfico descomprimidos (completa los 9 CSV de fuentes de red)
|   |       └──[CSVS De registros de trafico] 
│   │   ├── cybersecurity_intrusion_data.csv           #Resumen sintentico proveniente de el origen crudo
│   │   ├── GeneratedLabelledFlows.zip
│   │   └── MachineLearningCSV.zip
|   |
│   ├── Geoanalisis/                                   # Capas geoespaciales anonimizadas para ArcGIS (Guía 6)
│   │   ├── capa_ataques.csv                           # Distribución geográfica agregada por tipo de ataque
│   │   ├── capa_ciudades.csv                          # Tráfico de red agrupado por ciudad 
│   │   ├── capa_organizaciones.csv                    # Flujos agregados por organización
│   │   ├── Link_Mapa_ARCGIS.txt                       # Enlaces a las vistas publicadas en ARCGIS
│   │   ├── Mapa_Ataques_Registrados.png
│   │   ├── Mapa_Capa_Ciudades.png
│   │   └── Mapa_Capa_Organizaciones.png
|   |
│   ├── Implementacion_Gobernanza/                     # Artefactos normativos, clasificación y gestión de riesgos de datos (Guía 4)
│   │   ├── clasificacion_datos_redes.xlsx             # Catálogo de sensibilidad de variables
│   │   ├── matriz_riesgos_redes.xlsx                  # Evaluación de riesgos de exposición, privacidad e impacto
│   │   └── politica_gobernanza_redes.md               # Lineamientos de anonimización, retención y acceso seguro
|   |
│   ├── Modelos/                                         # Particiones, pipelines serializados, modelos de manera persistente
│   │   ├── datos_split_guia8.pkl                        # Particiones estratificadas (train, val, test) y variables 
│   │   ├── validacion_cruzada_guia09.csv                # Resultados de validación cruzada estratificada entre modelos 
│   │   ├── comparacion_modelos_guia09.csv               # Tabla comparativa de métricas (F1, Recall, Precision, AUC) 
│   │   ├── ranking_variables_guia09.csv                 # Importancia y ranking de las 21 variables predictoras 
│   │   ├── modelo_candidato_guia09.joblib               # Pipeline serializado del modelo candidato Random Forest 
│   │   ├── ficha_modelo_guia09.json                     # Metadatos, parámetros y huella SHA-256 del modelo candidato 
│   │   ├── guia09_comparativa_sobreajuste.png           # Gráfico de diagnóstico de overfitting entre train y validación 
│   │   ├── guia09_curva_de_discriminacion_modelos.png # Curvas ROC/PR comparativas de discriminación de modelos 
│   │   ├── guia09_top_variables_rd.png                  # Gráfico de barras de las variables más influyentes del RF 
│   │   ├── gridsearch_resultados_guia10.csv             # Resultados completos de las 36 combinaciones (144 fits) de GridSearchCV 
│   │   ├── comparacion_antes_despues_guia10.csv         # Comparativa de rendimiento antes y después de optimizar 
│   │   ├── predicciones_modelo_optimizado_guia10.csv    # Predicciones y probabilidades finales sobre el conjunto de prueba 
│   │   └── modelo_optimizado_guia10.joblib              # Pipeline definitivo de Random Forest reentrenado con mejores parámetros 
|   |
│   ├── Procesados/                                    #Consolidación inicial de fuentes unificadas en Parquet, previo a limpieza guia1
│   │   ├── dataset_crudo_unificado.parquet            # Unificación inicial de los flujos de red crudos en formato Parquet
│   │   └── dataset_ml_unificado.parquet               # Unificación inicial de los registros orientados a ML en formato Parquet
|   |
│   ├── Reporteria/                                    # Informes automatizados en HTML, PDF, DOCX y gráficos (Guía 7)
│   │   ├── datos/                                     # Insumos tabulares procesados para el reporte
│   │   │   └── agregados/                             # Tablas agregadas anónimas sin IPs (resumen_general.csv, etc.)
│   │   ├── documentos/                                # Informes ejecutivos generados (v1.0 en HTML, PDF y DOCX)
│   │   ├── evidencias/                                # Recursos visuales del informe
│   │   │   └── reporte/                               # Siete gráficos analíticos exportados con Plotly
│   │   ├── exportaciones/                             # Archivos de metadatos y trazabilidad de cada versión
│   │   └── templates/                                 # Plantilla Jinja2 utilizada para renderizar el reporte
|   |
│   └── ReportesPowerBI/                               # Dashboards (.pbix) y reportes visuales de Power BI (Guía 5)
│       ├── Dashboard_Cybersecurity_Gerencia.pbix.zip    # Archivo empaquetado del tablero gerencial en Power BI
│       ├── Dashboard_Cybersecurity_POWERBI.pbix.zip     # Archivo empaquetado del tablero operativo en Power BI
│       ├── Links_Vistas_PUblicadas_POWERBI.txt          # Enlaces a las vistas publicadas en Power BI Service
│       ├── VIsta_Modelo_Estrella.jpg                   
│       ├── Vista_Reporte_Estados.png                    
│       └── Vista_Reporte_Gerencial.png                  
│
|
├── Documentacion/                                     # Documentos de entrega técnica del proyecto académico
│   └── [Contiene informes técnicos, bitácoras y entregables academicos]
│
├── Notebook/                                          # Código fuente secuencial del pipeline y configuración central
│   ├── 01_CargaDeDatos.ipynb                          # Ingesta de fuentes heterogéneas
│   ├── 02_Limpieza_Normalizacion.ipynb                # Limpieza e ingeniería de características
│   ├── 03_ArquitecturaBigData_Spark.ipynb             # Procesamiento distribuido por capas en PySpark
│   ├── 04_Implementacion_Gobernanza.ipynb             # Gobernanza ética, anonimización y calidad de datos
│   ├── 06_Analisis_Geoespacial.ipynb                  # Geolocalización IP con DB-IP y preparación para ArcGIS
│   ├── 07_Reporteria_Automatizada.ipynb               # Generación automática de reportes (Plotly + Jinja2)
│   ├── 08_Fundamentos_IA_RandomForest.ipynb           # Modelado inicial de clasificación con Random Forest
│   ├── 08_Fundamentos_IA_RegresionLogistica.ipynb     # Modelo base de clasificación con Regresión Logística
│   ├── 09_Entrenamiento_Modelos_ML.ipynb              # Evaluación rigurosa, validación cruzada y selección de modelo
│   ├── 10_Optimizacion_Hiperparametros.ipynb          # Ajuste con GridSearchCV, análisis de errores y pipeline final
│   ├── Configuracion.py                               # Archivo centralizado de rutas y entorno Spark/Hadoop
│   └── Descarga_Librerias.txt                         # Guía de dependencias y preparación del entorno
│
├── Recursos/                                          # Insumos externos y datasets base originales (solo lectura)
│   ├── cybersecurity_intrusion_data.zip               # Dataset base de tráfico de red e intrusiones
│   ├── dbip-asn-lite-2026-10.csv.gz                   # Base de referencia DB-IP por organización/ASN
│   └── dbip-city-lite-2026-10.csv.gz                  # Base de referencia DB-IP por ciudad/ubicación
│
├── .gitignore                                                  # Reglas de exclusión de archivos pesados, binarios y temporales
├── Guía de Ejecución General y Estructura del Proyecto.md      # Guía de ejecución general y estructura del proyecto
└── README.md                                                   # Documentación principal y resumen ejecutivo del repositorio
```