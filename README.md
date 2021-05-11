# Proyecto FP Andrés

## Arrancar la wea

1. Realizar en la carpeta del repositorio mediante git: `docker-compose up -d`
3. Cuando empiece a correr el Compose, ir a [Grafana](http://localhost:3000)
   - User: `admin`
   - Pass: `admin`
4. Usar este link para [Añadir datasource de Prometheus](http://localhost:3000/datasources/new)
   - Campo HTTP URL: `http://prom:9090`
5. Crear y añadir Dashboards al gusto, añadiendo las graficas que veas pertinentes.
6. Organizar dichas graficas y darles nombres mediante Edit.
