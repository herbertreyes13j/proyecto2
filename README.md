# Proyecto Data Pipelines 

## Integrantes: 
- Herbert Reyes
- Carlos Yong
- Rodrigo Aragon

## Scope:

Para este proyecto usted deberá desarrollar un pipeline de ingeniería utilizando Python, SQL y AWS como herramientas de desarrollo, su proyecto debe contar con los siguientes componentes:
- Scope: Scope del Proyecto y descripción de fuentes de información,
- Exploración: Exploración de la data para definir el modelo de datos,
- Modelo de datos: Deberá definer el modelo de datos que usará para su Proyecto ya sea un DW o un DL,
- Procesamiento: deberá definer todos su Código como un conjunto de scripts en Python, los cuales extraigan, transofrmen y cargen la data.
- Analitica: Deberá plantear al menos 5 preguntas de análisis que puedan ser resueltas con la estructura que definio.
- Reporte: Un documento de Markdown el cual incluya todos los elementos solicitados anteriormente.

### Fuentes 

Se elaboro el proyecto en base al dataset llamado "Supermarket Sales" obtenido en Kaggle (https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales). Se desarrollaron 2 partes. 

### Descripcion 

Una transaccional en donde se consumen 2 archivos cargados en el servicio de S3 de AWS por medio del uso de boto3, y estos se utilizan para la carga de data a una instancia creada en RDS. Como DB engine de la instancia se utilizo PostgreSQL y para la creacion de las tablas de la DB se utilizo un archivo .py con una variable la cual contenia un string con el DDL necesario para la creacion de tablas y relaciones. 

La segunda parte consiste en la elaboracion de las dimensiones y la tabla de hechos del DataWarehouse, en el caso del dataset utilizado se buscó la manera de representar de la mejor manera y ejemplificar el proceso de elaboracion de un DW, siempre manteniendo la escencia de los conceptos aprendidos y del uso de python para la manipulacion de data e interaccion con los servicios de AWS. 

## Exploracion

## Modelo de datos

## Procesamiento

El proyecto fue realizado en 2 partes. 
#### Parte 1 
La fase en toda la exploracion y transformacion de la informacion, ubicado en el archivo [proyecto_datapipelines.py](https://github.com/herbertreyes13j/proyecto2/blob/main/proyecto_data_pipelines.py) donde podemos observar toda la primera fase, desde la obtencion de la informacion desde diversas fuentes, y el procesamiento del archivo. 
Para obtener una explicacion mas detallada se puede ver en el siguiente [VIDEO](https://drive.google.com/file/d/1TYe0RUGOzP_pEr1R4huYLJ65kU61BRph/view?usp=sharing)
#### Parte 2
La parte 2 es la construccion del DW desde la primera base de datos en postgres. Esta ya fue realizada en mysql y se construye en base a la transformacion de las tablas de la base anterior. En el archivo [dw.py](https://github.com/herbertreyes13j/proyecto2/blob/main/dw.py) se puede ver a detalle todo el script de esta fase y para la explicacion en el siguiente [VIDEO](https://drive.google.com/drive/folders/1urW117AeYEP5z8b7Seww-XBh4UJ4iNfn?usp=sharing)

## Analitica






