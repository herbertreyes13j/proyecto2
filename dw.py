#Importar Librerias

import pandas as pd
import numpy as np
import datetime
import boto3
import psycopg2
import configparser
import random
from faker import Faker

# Archivo de configuracion y establecimiento de instancias
rdsIdentifier = 'proyecto-db-1'
rdsMySQLIdentifier = 'proyecto-db-2'
config = configparser.ConfigParser()
config.read('escec.cfg')


# Creacion instancia RDS

aws_conn = boto3.client('rds', aws_access_key_id=config.get('IAM', 'ACCESS_KEY'),
                    aws_secret_access_key=config.get('IAM', 'SECRET_ACCESS_KEY'),
                    region_name='us-east-1')

# Verificar instancias disponibles

rdsInstanceIds = []

response = aws_conn.describe_db_instances()
for resp in response['DBInstances']:
    rdsInstanceIds.append(resp['DBInstanceIdentifier'])
    db_instance_status = resp['DBInstanceStatus']

print(f"DBInstanceIds {rdsInstanceIds}")


# Obtencion de URL de HOSTS
try:
     instances = aws_conn.describe_db_instances(DBInstanceIdentifier=rdsIdentifier)
     RDS_HOST = instances.get('DBInstances')[0].get('Endpoint').get('Address')
     instances = aws_conn.describe_db_instances(DBInstanceIdentifier=rdsMySQLIdentifier)
     RDS_HOSTMySQL = instances.get('DBInstances')[0].get('Endpoint').get('Address')
     print(RDS_HOST)
     print(RDS_HOSTMySQL)
except Exception as ex:
     print("La instancia de base de datos no existe o aun no se ha terminado de crear.")
     print(ex)

    
# URL a Postgres

postgres_driver = f"""postgresql://{config.get('RDS', 'DB_USER')}:{config.get('RDS', 'DB_PASSWORD')}@{RDS_HOST}:{config.get('RDS', 'DB_PORT')}/{config.get('RDS', 'DB_NAME')}"""  

#Obtencion y limpieza de dimensiones

sql_query = 'SELECT * FROM branch;'
df_branch = pd.read_sql(sql_query, postgres_driver)
df_branch.head()

sql_query = 'SELECT * FROM city;'
df_city = pd.read_sql(sql_query, postgres_driver)
df_city.head()

sql_query = 'SELECT * FROM location;'
df_location = pd.read_sql(sql_query, postgres_driver)
df_location.head()

df_location = df_location.merge(df_branch, left_on='branch_loc_id',right_on='branch_id', how='inner')
df_location

df_location = df_location.merge(df_city, left_on='city_loc_id',right_on='city_id', how='inner')
df_location

df_location = df_location.drop(labels=['branch_loc_id','city_loc_id','branch_id','city_id'],axis=1)
df_location

sql_query = 'SELECT * FROM customer_type;'
df_customer_type = pd.read_sql(sql_query, postgres_driver)
df_customer_type.head()

sql_query = 'SELECT * FROM customer_gender;'
df_customer_gender = pd.read_sql(sql_query, postgres_driver)
df_customer_gender.head()

sql_query = 'SELECT * FROM customers;'
df_customers = pd.read_sql(sql_query, postgres_driver)
df_customers.head()

df_customers = df_customers.merge(df_customer_type, left_on='type_customer_id',right_on='customertype_id', how='inner')
df_customers


df_customers = df_customers.merge(df_customer_gender, left_on='gender_customer_id',right_on='customergender_id', how='inner')
df_customers

df_customers =df_customers.drop(labels=['type_customer_id','gender_customer_id','customertype_id','customergender_id'],axis=1)
df_customers

sql_query = 'SELECT * FROM payment;'
df_payment = pd.read_sql(sql_query, postgres_driver)
df_payment.head()

sql_query = 'SELECT * FROM product_line;'
df_product_line = pd.read_sql(sql_query, postgres_driver)
df_product_line.head()

sql_query = 'SELECT * FROM sales;'
df_sales = pd.read_sql(sql_query, postgres_driver)
df_sales.head()

#Conectando con MySQL

try:
    response = aws_conn.create_db_instance(
            AllocatedStorage=10,
            DBName=config.get('RDS_MYSQL', 'DB_NAME'),
            DBInstanceIdentifier=rdsMySQLIdentifier,
            DBInstanceClass="db.t3.micro",
            Engine="mysql",
            MasterUsername=config.get('RDS_MYSQL', 'DB_USER'),
            MasterUserPassword=config.get('RDS_MYSQL', 'DB_PASSWORD'),
            Port=int(config.get('RDS_MYSQL', 'DB_PORT')),
            VpcSecurityGroupIds=[config.get('VPC', 'SECURITY_GROUP')],
            PubliclyAccessible=True
        )
    print(response)
except aws_conn.exceptions.DBInstanceAlreadyExistsFault as ex:
    print("La Instancia de Base de Datos ya Existe.")

#Creacion de DW
import DDL_DOS
import mysql.connector as mysqlC

try:
    myDw = mysqlC.connect(
    host=RDS_HOSTMySQL, 
    user=config.get('RDS_MYSQL', 'DB_USER'),
    password=config.get('RDS_MYSQL', 'DB_PASSWORD'),
    database=config.get('RDS_MYSQL', 'DB_NAME')
    )
    mycursor = myDw.cursor()
    mycursor.execute(DDL_DOS.DDL_T, multi=True)
    myDw.commit()
    print("Data Warehouse Creado Exitosamente")
except Exception as ex:
    print("ERROR: Error al crear la base de datos.")
    print(ex)

#Insertando en MySQL

mysql_driver = f"""mysql+pymysql://{config.get('RDS_MYSQL', 'DB_USER')}:{config.get('RDS_MYSQL', 'DB_PASSWORD')}@{RDS_HOSTMySQL}:{config.get('RDS_MYSQL', 'DB_PORT')}/{config.get('RDS_MYSQL', 'DB_NAME')}""" 

df_location.to_sql('dim_location',mysql_driver,index=False,if_exists='append')

df_product_line.to_sql('dim_product_line',mysql_driver,index=False,if_exists='append')

df_payment.to_sql('dim_payment',mysql_driver,index=False,if_exists='append')

df_customers.to_sql('dim_customers',mysql_driver,index=False,if_exists='append')

df_sales.to_sql('fact_sales',mysql_driver,index=False,if_exists='append')





