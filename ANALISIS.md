# Análisis

Se puede agregar un campo a la tabla de empleados llamado "Centro de trabajo" donde defina en qué centro de trabajo está laborando. Este será una llave foránea a la tabla de centros de trabajo en donde describirá a mayor detalle el centro de trabajo incluyendo el código del centro, dirección y teléfono.

En caso se requiera un histórico se puede crear una tabla "Asignaciones" que podrá tener la fecha de la asignación (será mensual) el código del empleado y el código del centro de trabajo donde deberá presentarse.

Además, cada mes se podrá ejecutar un script el cuál puede asignar de manera aleatoria a los empleados en los diferentes centros. En la base de datos será una actualización al campo "Centro de trabajo" para cada empleado de la tabla de empleados.

Preguntas:

- ¿Existe límite de capacidad en los centros de trabajo?

- ¿Se puede realizar la asignación de manera aleatoria?
