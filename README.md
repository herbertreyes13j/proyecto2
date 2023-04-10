# Proyecto Data Pipelines 

## Integrantes: 
- Herbert Reyes
- Carlos Yong
- Rodrigo Aragon

## Descripcion:

Se elaboro el proyecto en base al dataset llamado "Supermarket Sales" obtenido en Kaggle (https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales). Se desarrollaron 2 partes. 

Una transaccional en donde se consumen 2 archivos cargados en el servicio de S3 de AWS por medio del uso de boto3, y estos se utilizan para la carga de data a una instancia creada en RDS. Como DB engine de la instancia se utilizo PostgreSQL y para la creacion de las tablas de la DB se utilizo un archivo .py con una variable la cual contenia un string con el DDL necesario para la creacion de tablas y relaciones. 

La segunda parte consiste en la elaboracion de las dimensiones y la tabla de hechos del DataWarehouse, en el caso del dataset utilizado se buscó la manera de representar de la mejor manera y ejemplificar el proceso de elaboracion de un DW, siempre manteniendo la escencia de los conceptos aprendidos y del uso de python para la manipulacion de data e interaccion con los servicios de AWS. 
