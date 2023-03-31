# Análisis

Se puede agregar un campo a la tabla de empleados llamado "Centro de trabajo" donde defina en qué centro de trabajo está laborando. Este será una llave foránea a la tabla de centros de trabajo en donde describirá a mayor detalle el centro de trabajo incluyendo el código del centro, dirección y teléfono.

En caso se requiera un histórico se puede crear una tabla "Asignaciones" que podrá tener la fecha de la asignación (será mensual) el código del empleado y el código del centro de trabajo donde deberá presentarse. También se debe tomar en cuenta otra tabla con la información de la asistencia. Esta tabla mostrará la asistencia diara que tendrá un empleado en un centro de trabajo.

**Tabla de asignaciones**
|FECHA | CÓDIGO EMPLEADO | CÓDIGO CENTRO DE TRABAJO |
|---| --------------  | ------------------------ |
|ABR-2021|   EMP-0001      | CT-1243                 |
|ABR-2021|   EMP-002     |  CT-9932                  |

**Tabla de Centros de trabajo**
|CODIGO | NOMBRE | DIRECCIÓN | TELEFONO |
|---|---|---|---|
|CT-12433|CENTRO ALTAMIRA|SOLOLA|12345678|
|CT-9932|CENTRO PACIFICO|ESCUINTLA|87654321|

**Tabla de asistencia**
| CÓDIGO EMPLEADO | FECHA | ASISTENCIA |
| --- | --- | --- |
| EMP-0001 | 01-04-2021 | 0 |
| EMP-0002 | 01-04-2021 | 0 |

Además, cada mes se podrá ejecutar un script el cuál puede asignar de manera aleatoria a los empleados en los diferentes centros. En la base de datos será una actualización al campo "Centro de trabajo" para cada empleado de la tabla de empleados.

#### Preguntas
- ¿Existe límite de capacidad en los centros de trabajo?
- ¿Se puede realizar la asignación de manera aleatoria?

#### Suposiciones

- Existe una persona que realizará la asignación cada mes
- Se cuenta con la información de todos los centros de trabajo
- En la tabla de asistencias no se toma en cuenta el centro pues se asume que cada mes este es asignado sin modificación

