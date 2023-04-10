# Proyecto Data Pipelines 

## Integrantes: 
- Herbert Reyes
- Carlos Rivera Yong
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

Se realizaron dos Notebooks:

Primer Notebook: https://github.com/herbertreyes13j/proyecto2/blob/main/DDL_UNO.py
Este notebook contiene un script de SQL que crea o define una estructura de base de datos relacional. La estructura de la base de datos está compuesta por 8 tablas, cada una con sus respectivos campos y relaciones con otras tablas.
###Las tablas creadas son:
1. branch: que tiene dos campos (branch_id y branch) y es utilizada para almacenar información sobre sucursales.
2. city: que tiene dos campos (city_id y city_name) y almacena información sobre ciudades.
3. location: que tiene tres campos (location_id, branch_loc_id y city_loc_id) y es utilizada para relacionar sucursales con ciudades.
4. product_line: que tiene dos campos (product_line_id y product_line_name) y almacena información sobre líneas de productos.
5. payment: que tiene dos campos (payment_id y payment_type) y es utilizada para almacenar información sobre tipos de pago.
6. customer_gender: que tiene dos campos (customergender_id y customer_gender) y almacena información sobre género de los clientes.
7. customer_type: que tiene dos campos (customertype_id y customer_type) y almacena información sobre el tipo de cliente.
8. customers: que tiene cuatro campos (customers_id, customer_name, type_customer_id y gender_customer_id) y es utilizada para almacenar información sobre los clientes y su género y tipo.
9. sales: que tiene once campos (sale_id, sale_location_id, sale_payment_type_id, sale_product_line_id, sale_costumer_id, sale_date, sale_quantity, sale_unitprice, sale_taxes, sale_total y sale_gross_income) y es utilizada para almacenar información sobre las ventas realizadas, incluyendo la ubicación, el tipo de pago, la línea de producto, el cliente y otros detalles.

Segundo Notebook: https://github.com/herbertreyes13j/proyecto2/blob/main/DDL_DOS.py

El segundo notebook contiene un script de SQL que define una estructura de base de datos relacional. Esta estructura de base de datos está diseñada siguiendo el patrón de diseño dimensional, en el que se separan los datos en dimensiones y hechos.

Las tablas definidas son:

1. dim_location: que tiene tres campos (location_id, branch y city_name) y almacena información sobre la ubicación de las ventas, separando la información de sucursal y ciudad.
2. dim_product_line: que tiene dos campos (product_line_id y product_line_name) y almacena información sobre las líneas de productos.
3. dim_payment: que tiene dos campos (payment_id y payment_type) y almacena información sobre los tipos de pago.
4. dim_customers: que tiene cuatro campos (customers_id, customer_name, customer_type y customer_gender) y almacena información sobre los clientes, separando su tipo y género.
5. fact_sales: que tiene once campos (sale_id, sale_location_id, sale_payment_type_id, sale_product_line_id, sale_costumer_id, sale_date, sale_quantity, 6. sale_unitprice, sale_taxes, sale_total y sale_gross_income) y almacena información sobre las ventas realizadas.

Diagrama Entidad Relacion

https://github.com/herbertreyes13j/proyecto2/blob/main/DiagramaER.jpg

## Modelo de datos

Se obtuvo el siguiente diagrama definiendo el DW:
https://github.com/herbertreyes13j/proyecto2/blob/main/DiagramaDW.png


## Procesamiento

El proyecto fue realizado en 2 partes. 
#### Parte 1 
La fase en toda la exploracion y transformacion de la informacion, ubicado en el archivo [proyecto_datapipelines.py](https://github.com/herbertreyes13j/proyecto2/blob/main/proyecto_data_pipelines.py) donde podemos observar toda la primera fase, desde la obtencion de la informacion desde diversas fuentes, y el procesamiento del archivo. 
Para obtener una explicacion mas detallada se puede ver en el siguiente [VIDEO](https://drive.google.com/drive/folders/1urW117AeYEP5z8b7Seww-XBh4UJ4iNfn?usp=sharing)
#### Parte 2
La parte 2 es la construccion del DW desde la primera base de datos en postgres. Esta ya fue realizada en mysql y se construye en base a la transformacion de las tablas de la base anterior. En el archivo [dw.py](https://github.com/herbertreyes13j/proyecto2/blob/main/dw.py) se puede ver a detalle todo el script de esta fase y para la explicacion en el siguiente [VIDEO](https://drive.google.com/file/d/1TYe0RUGOzP_pEr1R4huYLJ65kU61BRph/view?usp=sharing)

## Analitica

1. ¿Cómo se relacionan las tablas "fact_sales" y "dim_customers" con las tablas de dimensiones "dim_location" y "dim_payment"?
2. ¿Qué información adicional se almacena en la tabla "dim_customers" en comparación con la tabla "customers" del primer notebook?
3. ¿Cómo se obtiene la URL de HOSTS para PostgreSQL y MySQL?
4. ¿Qué tablas se obtienen y limpian de la base de datos de PostgreSQL?
5. ¿Qué servicios de AWS se utilizan en el script?






