# Usar la imagen base de Python
FROM python:3.10-slim

# Instalar dependencias
RUN pip install --no-cache-dir streamlit

# Copiar los archivos del proyecto
WORKDIR /app
COPY . .

# Puerto por defecto de Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]

