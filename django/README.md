# WeatherApp

Una aplicación Django que muestra la información del clima utilizando la Weather API.

## API Utilizada

**Weather API**: Utilicé la [Weather API](https://www.weatherapi.com/) para obtener datos meteorológicos en tiempo real.

- **API Key**: `88ee208bd0104304ad4110850240706`

## Cómo Utilizamos la API

1. **Consulta de la API**:
   Use la Weather API para obtener información del clima de una ciudad específica. La API nos proporciona datos como la temperatura, humedad y condición climática.

2. **Integración con Django**:
   En el archivo `views.py` de la aplicación Django, hacemos una solicitud GET a la API usando la biblioteca `requests` de Python. Filtramos los datos relevantes que necesitamos, como la temperatura y la humedad.

3. **Renderización de los Datos**:
   Los datos obtenidos se pasan al template `index.html` donde se muestran en una tabla HTML. Use Bootstrap para estilizar la tabla y hacer que se vea bien visualmente.
