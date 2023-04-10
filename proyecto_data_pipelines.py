import pandas as pd
import numpy as np
import datetime
import boto3
import psycopg2
import configparser
import random
from faker import Faker

# Identificadores

rdsIdentifier = 'proyecto-db-1'
rdsMySQLIdentifier = 'proyecto-db-2'

# Importacion de archivo config

config = configparser.ConfigParser()
config.read('escec.cfg')

aws_conn = boto3.client('rds', aws_access_key_id=config.get('IAM', 'ACCESS_KEY'),
                    aws_secret_access_key=config.get('IAM', 'SECRET_ACCESS_KEY'),
                    region_name='us-east-1')

# Identificacion de instancias

rdsInstanceIds = []

response = aws_conn.describe_db_instances()
for resp in response['DBInstances']:
    rdsInstanceIds.append(resp['DBInstanceIdentifier'])
    db_instance_status = resp['DBInstanceStatus']

print(f"DBInstanceIds {rdsInstanceIds}")

# Creacion servicio RDS

try:
    response = aws_conn.create_db_instance(
            AllocatedStorage=10,
            DBName=config.get('RDS', 'DB_NAME'),
            DBInstanceIdentifier=rdsIdentifier,
            DBInstanceClass="db.t3.micro",
            Engine="postgres",
            MasterUsername=config.get('RDS', 'DB_USER'),
            MasterUserPassword=config.get('RDS', 'DB_PASSWORD'),
            Port=int(config.get('RDS', 'DB_PORT')),
            VpcSecurityGroupIds=[config.get('VPC', 'SECURITY_GROUP')],
            PubliclyAccessible=True
        )
    print(response)
except aws_conn.exceptions.DBInstanceAlreadyExistsFault as ex:
    print("La Instancia de Base de Datos ya Existe.")

# URL de HOST

try:
     instances = aws_conn.describe_db_instances(DBInstanceIdentifier=rdsIdentifier)
     RDS_HOST = instances.get('DBInstances')[0].get('Endpoint').get('Address')
     print(RDS_HOST)
except Exception as ex:
     print("La instancia de base de datos no existe o aun no se ha terminado de crear.")
     print(ex)

# Conexion a base de datos con python

import DDL_UNO

try:
    db_conn = psycopg2.connect(
        database=config.get('RDS', 'DB_NAME'), 
        user=config.get('RDS', 'DB_USER'),
        password=config.get('RDS', 'DB_PASSWORD'), 
        host=RDS_HOST,
        port=config.get('RDS', 'DB_PORT')
    )

    cursor = db_conn.cursor()
    cursor.execute(DDL_UNO.DDL_T)
    db_conn.commit()
    print("Base de Datos Creada Exitosamente")
except Exception as ex:
    print("ERROR: Error al crear la base de datos.")
    print(ex)

# Insertar a SQL

def insertDataToSQL(data_dict, table_name):
     postgres_driver = f"""postgresql://{config.get('RDS', 'DB_USER')}:{config.get('RDS', 'DB_PASSWORD')}@{RDS_HOST}:{config.get('RDS', 'DB_PORT')}/{config.get('RDS', 'DB_NAME')}"""    
     df_data = pd.DataFrame.from_records(data_dict)
     try:
          response = df_data.to_sql(table_name, postgres_driver, index=False, if_exists='append')
          print(f'Se han insertado {response} nuevos registros.' )
     except Exception as ex:
          print(ex)

# Proceso transaccional

# Leer bucket S3

s3 = boto3.resource(
    service_name = 's3',
    region_name = 'us-east-1',
    aws_access_key_id = config.get('IAM', 'ACCESS_KEY'),
    aws_secret_access_key = config.get('IAM', 'SECRET_ACCESS_KEY')
)

for bucket in s3.buckets.all():
    S3_BUCKET_NAME = bucket.name
    print(bucket.name)

S3_BUCKET_NAME = 'proyecto-data-pipeline-galileo1'

#Obtencion de almacenado en bucket

remoteFileList = []
for objt in s3.Bucket(S3_BUCKET_NAME).objects.all():
    remoteFileList.append(objt.key)

remoteFileList

# Lectura de archivos

import io

df_branch = pd.DataFrame()
df_customer_type = pd.DataFrame()

for remoteFile in remoteFileList:
    try:
        file = s3.Bucket(S3_BUCKET_NAME).Object(remoteFile).get()
        if 'branch.csv' in remoteFile:
            df_branch = pd.read_csv(file['Body'])
        elif 'customer_type.xlsx' in remoteFile:
            data = file['Body'].read()
            df_customer_type = pd.read_excel(io.BytesIO(data), engine='openpyxl')
    except Exception as ex:
        print("No es un archivo.")
        print(ex)

print(df_branch)
print(df_customer_type)

# Convertir archivos a diccionarios

data_dict_branch = df_branch.to_dict('records')
data_dict_customer_type = df_customer_type.to_dict('records')

# Insertar archivos en sql

insertDataToSQL(data_dict_branch, 'branch')
insertDataToSQL(data_dict_customer_type, 'customer_type')

# Tabla City

data_city = [
     {'city_id': 1, 'city_name': 'Mandalay'}, 
     {'city_id': 2, 'city_name': 'Yangon'},
     {'city_id': 3, 'city_name': 'Napypyitaw'}
]

insertDataToSQL(data_city, 'city')

# Tabla Location

data_tiendas_ciudad = []

for ciudad in range(len(data_city)):
    for tienda in range(len(df_branch)):
        
       ciudad_tienda = {
        'location_id': ciudad+1,
        'city_loc_id': data_city[ciudad]['city_id'],
        'branch_loc_id': df_branch.loc[tienda, 'branch_id']
    } 
    
    data_tiendas_ciudad.append(ciudad_tienda)

insertDataToSQL(data_tiendas_ciudad, 'location')


# Tabla Product Line

data_productline = [
     {'product_line_id': 1, 'product_line_name': 'Electronic accessories'}, 
     {'product_line_id': 2, 'product_line_name': 'Fashion accessories'},
     {'product_line_id': 3, 'product_line_name': 'Health and beauty'},
     {'product_line_id': 4, 'product_line_name': 'Food and beverages'},
     {'product_line_id': 5, 'product_line_name': 'Home and lifestyle'},
     {'product_line_id': 6, 'product_line_name': 'Sports and travel'}
]

insertDataToSQL(data_productline, 'product_line')

# Tabla payment

data_payment = [
     {'payment_id': 1, 'payment_type': 'Ewallet'},
     {'payment_id': 2, 'payment_type': 'Cash'},
     {'payment_id': 3, 'payment_type': 'Credit card'} 
]

insertDataToSQL(data_payment, 'payment')

# Tabla Gender

data_gender = [
     {'customergender_id': 1, 'customer_gender': 'Female'},
     {'customergender_id': 2, 'customer_gender': 'Male'}
]

insertDataToSQL(data_gender, 'customer_gender')

# Tabla Customers

cantidad_clientes = np.random.randint(0,1500)
data_clientes = []
nombre_fake = Faker()

for x in range(cantidad_clientes):
    
    gender = random.sample(data_gender, 1)[0]['customergender_id'] # se genera primero el genero para saber si es hombre o mujer y con ello determinar el nombre que generar con Faker
    
    if gender == 1:
        name = nombre_fake.name_female()
    elif gender == 2:
        name = nombre_fake.name_male()
    else:
        name = "Indefinido"

    cliente = {
        'customers_id': x+1,
        'customer_name': name,
        'type_customer_id': random.sample(data_dict_customer_type, 1)[0]['customertype_id'],
        'gender_customer_id': gender,
    } 

    data_clientes.append(cliente)

insertDataToSQL(data_clientes, 'customers')

# Tabla Sale

data_ventas = []
cantidad_ventas = np.random.randint(500,2000)
fecha_fake = Faker() #se volvio a instanciar Faker para comprension y distincion entre "Fakers"

for ventas in range(cantidad_ventas):
    
    unit_price = np.round(np.random.uniform(0,1000),2)
    tax_5 = unit_price*0.05
    quantity = np.random.randint(0,20)
    sale_total = (unit_price + tax_5)*quantity
    sale_gross_income = sale_total * 0.10
    
    venta = {
            'sale_id': ventas+1,
            'sale_location_id': random.sample(data_tiendas_ciudad, 1)[0]['location_id'],
            'sale_payment_type_id': random.sample(data_payment, 1)[0]['payment_id'],
            'sale_product_line_id': random.sample(data_productline, 1)[0]['product_line_id'],
            'sale_costumer_id': random.sample(data_clientes, 1)[0]['customers_id'],
            'sale_date': fecha_fake.date_time_this_year(),
            'sale_quantity': quantity,
            'sale_unitprice': np.round(np.random.uniform(0,10000),2),
            'sale_taxes': tax_5,
            'sale_total': sale_total,
            'sale_gross_income': sale_gross_income
        }
    data_ventas.append(venta)
    
insertDataToSQL(data_ventas,'sales')

