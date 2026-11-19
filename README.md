# Proyecto: Cybersecurity Data Analytics.

Se busca con este proyecto contribuir al avance de sistemas de detección de anomalías por medio de modelos IA, con un papeline de análisis de datos que integre e interrelacione toda la información de un tráfico de red con el comportamiento normal de los usuarios utilizando de base el datset distribuido por Canadian Institute for Cybersecurity (CIC), específicamente al conocido CICIDS2017.

---

# Analítica de Ciberseguridad: Construcción de Pipeline integral de analítica de datos y Machine Learning, diseñado para procesar, gobernar, visualizar y aprender por medio de modelos del tráfico de red a gran escala.

## Descripción Detallada por Etapa

### 1. Ingesta y Unificación de Datos
* Descompresión automatizada del archivo fuente (`cybersecurity_intrusion_data.zip`).
* Consolidación de los múltiples archivos CSV de tráfico de red hacia almacenamiento columnar en formato **Parquet** para optimizar el rendimiento de lectura:
  * `dataset_crudo_unificado.parquet`: conserva las direcciones IP y metadatos originales para auditoría y cruce geoespacial.
  * `dataset_ml_unificado.parquet`: estructura consolidada orientada a los flujos de modelado predictivo.

### 2. Limpieza y Control de Calidad en PySpark
* Procesamiento distribuido de **3,119,345 registros crudos**, preservando las direcciones IP para etapas posteriores.
* Eliminación de columnas redundantes (como el atributo duplicado `fwd_header_length_1`).
* Normalización de marcas de tiempo (*timestamps*), conversión estricta de contadores enteros y depuración de registros nulos o duplicados.
* Generación del reporte de calidad de datos y exportación de `dataset_crudo_limpio_final.parquet`.

### 3. Enriquecimiento y Particionamiento (PySpark & Spark SQL)
* Filtrado de consistencia sobre el tráfico depurado, reteniendo **2,827,562 flujos válidos**.
* Cálculo de variables derivadas de comportamiento de red:
  * `ratio_fwd_bwd_bytes`: proporción entre bytes enviados (*forward*) y recibidos (*backward*) para detectar asimetrías o posibles exfiltraciones de datos.
  * `total_flags_activadas`: conteo acumulado de banderas TCP activas por sesión.
  * `categoria_duracion`: clasificación discreta de los flujos según su duración temporal.
* Ejecución de agregaciones analíticas mediante **Spark SQL** y escritura de `dataset_enriquecido_final.parquet` particionado físicamente por `anio` y `mes`.

### 4. Gobernanza y Privacidad de Datos
* Aplicación de controles de privacidad y minimización antes de habilitar el consumo analítico externo:
  * **Seudonimización:** generación de identificadores únicos `flow_token` mediante hashing **SHA-256 con sal (*salt*)**.
  * **Enmascaramiento y generalización:** ofuscación de direcciones IP y puertos de origen, junto con generalización de duraciones de flujo.
* Exportación de la vista segura y minimizada (`dataset_publicable_redes.parquet` y `dataset_publicable_redes.csv`).
* Generación de artefactos documentales en Markdown con las **matrices de clasificación de datos**, **matrices de riesgos** y **políticas de gobernanza**.

### 5. Dashboard Ejecutivo en Power BI
* Diseño y construcción de un tablero interactivo en **Power BI** utilizando exactamente los mismos **KPIs, métricas y reglas de negocio** definidos en el módulo de reportería automatizada.
* Implementación de medidas en **DAX** para el monitoreo operativo y ejecutivo de volumen de flujos, tasa de tráfico malicioso frente a benigno, distribución por tipo de ataque, concentración de banderas TCP (`total_flags_activadas`), comportamiento del `ratio_fwd_bwd_bytes` y evolución temporal por año y mes.

### 6. Geolocalización e Inteligencia Espacial en PySpark
* Extracción y depuración de **19,035 direcciones IP públicas únicas** provenientes del tráfico analizado.
* Cruce distribuido contra las bases de datos **DB-IP** (`dbip-city-lite` y `dbip-asn-lite`) optimizado mediante bloques de red **`/16`**.
* Exportación de tres capas geográficas agregadas y completamente anonimizadas (sin exposición de direcciones IP) listas para análisis espacial:
  * `capa_ciudades.csv`: distribución de eventos por ciudad y país.
  * `capa_ataques.csv`: concentración geográfica por tipología de intrusión.
  * `capa_organizaciones.csv`: atribución de tráfico por Sistema Autónomo (ASN) y organización.

### 7. Reportería Automatizada
* Desarrollo de un flujo automatizado en Python para generar informes periódicos manteniendo consistencia total con los KPIs y métricas del dashboard de Power BI.
* Renderizado de visualizaciones estadísticas de alta resolución mediante **Plotly** y **Kaleido**, junto con el ensamblaje dinámico de documentos formales en **Word (`.docx`)** con `python-docx` y **PDF (`.pdf`)** con `WeasyPrint`.

### 8. Preparación y Preprocesamiento para Machine Learning
* Acondicionamiento del conjunto consolidado (`dataset_ml_unificado.parquet`) para aprendizaje supervisado.
* Selección, limpieza y transformación de variables predictoras (escalamiento numérico y codificación de atributos categóricos), junto con la partición estratificada en conjuntos de entrenamiento y prueba (**84,915 registros** reservados para validación final).

### 9. Entrenamiento y Evaluación de Modelos Base
* Implementación y comparación de algoritmos de clasificación supervisada (como **Regresión Logística** y **Random Forest**) para la detección de intrusiones de red.
* Evaluación comparativa mediante métricas clave de ciberseguridad (**Recall**, **Precision**, **F1-Score** y **ROC-AUC**), priorizando una alta tasa de detección de amenazas reales mientras se minimizan las alertas por falsos positivos.

### 10. Optimización de Hiperparámetros y Auditoría del Modelo Final
* Ajuste fino del modelo seleccionado mediante un `Pipeline` de `scikit-learn` con `RandomForestClassifier` y `GridSearchCV`, evaluando **36 combinaciones** bajo validación cruzada de **4 folds**.
* Validación sobre el conjunto de prueba aislado (**84,915 registros**), alcanzando un **F1-Score de 0.9942** y un **ROC-AUC de 0.9999**, complementado con el análisis de falsos positivos/negativos y el ranking de importancia de características 

---

Este proyecto demuestra cómo articular una arquitectura de datos moderna capaz de transformar millones de registros crudos de red en inteligencia accionable bajo estándares estrictos de privacidad y gobernanza. Al combinar procesamiento distribuido en PySpark, visualización homologada entre Power BI y reportes automatizados, enriquecimiento geoespacial sin exposición de datos sensibles y modelos de clasificación de alta precisión, la solución establece una base sólida, auditable y escalable para la detección temprana de amenazas y la toma de decisiones en ciberseguridad.
