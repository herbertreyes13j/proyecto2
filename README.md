# Proyecto Data Pipelines 

## Integrantes: 
- Herbert Reyes
- Carlos Yong
- Rodrigo Aragon

## Descripcion:

Para este proyecto usted deberá desarrollar un pipeline de ingeniería utilizando Python, SQL y AWS como herramientas de desarrollo, su proyecto debe contar con los siguientes componentes:
• Scope: Scope del Proyecto y descripción de fuentes de información,
• Exploración: Exploración de la data para definir el modelo de datos,
• Modelo de datos: Deberá definer el modelo de datos que usará para su Proyecto ya sea un DW o un DL,
• Procesamiento: deberá definer todos su Código como un conjunto de scripts en Python, los cuales extraigan, transofrmen y cargen la data.
• Analitica: Deberá plantear al menos 5 preguntas de análisis que puedan ser resueltas con la estructura que definio.
• Reporte: Un documento de Markdown el cual incluya todos los elementos solicitados anteriormente.

Se elaboro el proyecto en base al dataset llamado "Supermarket Sales" obtenido en Kaggle (https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales). Se desarrollaron 2 partes. 

Una transaccional en donde se consumen 2 archivos cargados en el servicio de S3 de AWS por medio del uso de boto3, y estos se utilizan para la carga de data a una instancia creada en RDS. Como DB engine de la instancia se utilizo PostgreSQL y para la creacion de las tablas de la DB se utilizo un archivo .py con una variable la cual contenia un string con el DDL necesario para la creacion de tablas y relaciones. 

La segunda parte consiste en la elaboracion de las dimensiones y la tabla de hechos del DataWarehouse, en el caso del dataset utilizado se buscó la manera de representar de la mejor manera y ejemplificar el proceso de elaboracion de un DW, siempre manteniendo la escencia de los conceptos aprendidos y del uso de python para la manipulacion de data e interaccion con los servicios de AWS. 

## Entregables 

En nuestro zip puede encontrar dos partes 
1. proyecto_datapipelines.ipynb Parte 1 [Haz clic aquí](https://github.com/herbertreyes13j/proyecto2/blob/main/proyecto_data_pipelines.py)
se explica en el siguiente link: VIDEO [Haz clic aquí](https://drive.google.com/file/d/1TYe0RUGOzP_pEr1R4huYLJ65kU61BRph/view?usp=sharing)
2. dw.ipynb Parte 2 [Haz clic aquí](https://github.com/herbertreyes13j/proyecto2/blob/main/dw.py)
se explica en el siguiente link: VIDEO [Haz clic aquí](https://drive.google.com/drive/folders/1urW117AeYEP5z8b7Seww-XBh4UJ4iNfn?usp=sharing)



