# Nombre de la Aplicación

## Descripción
Breve descripción de la aplicación y su propósito.

## Instalación
1. Clona el repositorio:
    ```bash
    git clone https://github.com/PAU45/lab03.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd repositorio
    ```
3. Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración
1. Crea un archivo `.env` en la raíz del proyecto y añade las siguientes variables de entorno:
    ```env
    SECRET_KEY=tu_secreto
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```
2. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

## Uso
1. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
2. Abre tu navegador y ve a `http://localhost:8000` para ver la aplicación en funcionamiento.

## Contribuir
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
