DDL_T ='''
CREATE TABLE dim_location (
    location_id INT PRIMARY KEY,
    branch VARCHAR(2),
    city_name VARCHAR(32)
);

CREATE TABLE dim_product_line (
    product_line_id INT PRIMARY KEY,
    product_line_name VARCHAR(60)
);

CREATE TABLE dim_payment (
    payment_id INT PRIMARY KEY,
    payment_type VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE dim_customers (
    customers_id int PRIMARY KEY,
    customer_name VARCHAR(120),
    customer_type VARCHAR(20) NOT NULL,
    customer_gender VARCHAR(20) NOT NULL
);

CREATE TABLE fact_sales (
    sale_id SERIAL PRIMARY KEY,
    sale_location_id INT NOT NULL,
    sale_payment_type_id INT NOT NULL,
    sale_product_line_id INT NOT NULL,
    sale_costumer_id int not null,
    sale_date TIMESTAMP NOT NULL,
    sale_quantity INT NOT NULL,
    sale_unitprice DOUBLE PRECISION NOT NULL,
    sale_taxes DOUBLE PRECISION NOT NULL,
    sale_total DOUBLE PRECISION NOT NULL,
    sale_gross_income DOUBLE PRECISION NOT NULL,
    FOREIGN KEY (sale_location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (sale_payment_type_id) REFERENCES dim_payment(payment_id),
    FOREIGN KEY (sale_product_line_id) REFERENCES dim_product_line(product_line_id),
    FOREIGN KEY (sale_costumer_id) REFERENCES dim_customers(customers_id)
);
'''