
# Política de Gobernanza - Cybersecurity Data Analytics

## 1. Propósito
Establecer las directrices operativas y principios éticos para la gestión, protección, uso analítico y conservación de los registros de
tráfico de red procesados para el desarrollo de modelos de Detección de Intrusos (IDS).

## 2. Alcance
Aplica a todos los archivos de captura y logs de red crudos (`.parquet`, `.csv`), vistas analíticas minimizadas, scripts de Python/PySpark,
cuadernos de Jupyter y documentación generada en el proyecto.

## 3. Clasificación de datos
- Público: Puertos de destino estándar (`destination_port`), protocolo de red (`protocol`) y la etiqueta final de tráfico (`label`, ej. BENIGN, DoS, PortScan).
- Interno: Métricas cuantitativas de comportamiento de red (`flow_duration`, `min_seg_size_forward`, `active_mean`, `idle_mean`, `total_fwd_packets`).
- Confidencial: Direcciones IP de origen y destino (`source_ip`, `destination_ip`), puerto de origen (`source_port`) e identificadores únicos de flujo (`flow_id`).
- Restringido: Claves secretas de salado (`SALT`), logs crudos con payloads completos de red y credenciales de infraestructura.

## 4. Acceso
- Administrador / Ing. de Datos: Acceso total a los datasets crudos y gestión de las claves de salado para los procesos de anonimización.
- Científico de Datos / Analista: Acceso exclusivo a la vista protegida y minimizada para el diseño y entrenamiento de modelos predictivos.
- Auditor de Seguridad: Acceso en modo lectura a las matrices de riesgo, registros de validación y evidencias de cumplimiento.

## 5. Minimización y Protección de Datos
1. Queda estrictamente prohibida la inclusión de direcciones IP reales sin enmascarar en la vista analítica final.
2. Todo identificador de flujo (`flow_id`) debe convertirse a un token unidireccional utilizando SHA-256 junto con una sal (`SALT`).
3. Se aplicará enmascaramiento parcial a los puertos de origen y generalización por rangos *binning* a la duración de los flujos e intervalos
de reposo para evitar la reidentificación por *fingerprinting*.

## 6. Retención y Depuración
- Datos Crudos: Se mantendrán únicamente en el entorno de almacenamiento temporal durante la etapa de procesamiento y limpieza.
- Vista Analítica Protegida: Se conservará mientras dure el desarrollo del proyecto académico.
- Cierre del Proyecto: Todos los archivos temporales y copias locales de datos crudos deberán ser eliminados al finalizar el ciclo de evaluación, conservando únicamente los scripts de código y modelos entrenados.

## 7. Uso Ético y Responsable
1. Los datos procesados se utilizarán con la única finalidad de investigar y entrenar modelos de detección de amenazas cibernéticas.
2. Se prohíbe explícitamente cualquier intento de desanonimizar direcciones IP, rastrear hosts específicos en la red o realizar escaneos de vulnerabilidad
no autorizados sobre la infraestructura de origen.
3. El equipo deberá evaluar la presencia de sesgos o desbalance severo en las clases de ataques (`label`) para evitar falsos positivos o falsos negativos
en la detección de tráfico malicioso.

## 8. Registro de Evidencias
Cualquier transformación sobre los datos (aplicación de hash, máscaras de IP, filtrado de atributos) debe estar documentada y ser ejecutable
mediante scripts de código reproducibles en el repositorio.
