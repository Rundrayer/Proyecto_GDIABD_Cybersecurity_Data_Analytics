# Reportería automatizada — Cybersecurity Data Analytics
Notebook `Reporte_Automatizado.ipynb`: parquet enriquecido -> agregados anónimos -> KPIs -> Plotly -> Jinja2 -> HTML/PDF/DOCX + metadata JSON.
- `datos/agregados/`: CSV anónimos (se suben a GitHub). El parquet completo NO se sube.
- `templates/informe.html.j2`: plantilla. `exportaciones/`: informes. `evidencias/reporte/`: gráficos.
- Local: abrir el notebook y ejecutar todo (busca el parquet vía Configuracion.py). GitHub: Actions > Run workflow.
Gobernanza: sin IP, flow_id ni puertos de origen. Fuente: CICIDS2017 - https://www.unb.ca/cic/datasets/ids-2017.html
