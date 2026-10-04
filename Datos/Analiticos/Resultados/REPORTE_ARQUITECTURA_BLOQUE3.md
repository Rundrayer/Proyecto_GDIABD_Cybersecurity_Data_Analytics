# Reporte de Arquitectura Big Data  - BLOQUE 3

---

## [INFRAESTRUCTURA Y ENTORNO]
* **Motor de Procesamiento:** Apache Spark (v3.5.3)
* **Estrategia de Persistencia:** Apache Parquet (Compresión columnar / Snappy)
* **Particionamiento Físico:** `.partitionBy('anio', 'mes')` (Organización por carpetas de atributos)

## [MÉTRICAS DE VOLUMETRÍA]
* **Registros Totales Procesados:** 2,827,562
* **Dimensionalidad Inicial (Features Base):** 90
* **Dimensionalidad Final (Enriquecida):** 93

## [OPTIMIZACIÓN DE CLÚSTER]
* **Paralelismo Inicial (RDD):** 12
* **Paralelismo Final (Optimizado):** 8

## [LOCALIZACIÓN DEL DATASET ENRIQUECIDO]
* **Ruta de Salida:** `C:\Users\galle\Desktop\IA Datos\Jupyter\Proyecto_GDIABD_Cybersecurity_Data_Analytics\Datos\Analiticos\Parquet\dataset_enriquecido_final.parquet`
* **Formato:** Parquet particionado jerárquicamente
