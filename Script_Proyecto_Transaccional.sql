CREATE TABLE branch(
branch_id INT PRIMARY KEY,
branch VARCHAR(2)
);

CREATE TABLE city(
city_id INT PRIMARY KEY,
city_name VARCHAR(32)
);

CREATE TABLE location (
    location_id SERIAL PRIMARY KEY,
    branch_loc_id INT NOT NULL,
    city_loc_id INT NOT NULL,
    FOREIGN KEY (branch_loc_id) REFERENCES branch(branch_id),
    FOREIGN KEY (city_loc_id) REFERENCES city(city_id),
    UNIQUE (branch_loc_id, city_loc_id) -- Permite que una ciudad tenga solo un tipo de Branch, por ejemplo la ciudad "Yangon" solo puede tener una unica tienda del branch A, una B y una C.
);


CREATE TABLE product_line(
	product_line_id INT PRIMARY KEY,
    product_line_name VARCHAR(60)
    );

CREATE TABLE payment (
    payment_id INT PRIMARY KEY,
    payment_type VARCHAR(50) NOT NULL UNIQUE
);



CREATE TABLE customer_gender (
    customergender_id INT PRIMARY KEY,
    customer_gender VARCHAR(20) NOT NULL
);

CREATE TABLE customer_type (
    customertype_id INT PRIMARY KEY,
    customer_type VARCHAR(20) NOT NULL
);

CREATE TABLE customers (
    customers_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(120),
    type_customer_id INT NOT NULL,
    gender_customer_id INT NOT NULL,
    FOREIGN KEY (type_customer_id) REFERENCES customer_type(customertype_id),
    FOREIGN KEY (gender_customer_id) REFERENCES customer_gender(customergender_id),
);


CREATE TABLE sales (

    sale_id SERIAL PRIMARY KEY,
    sale_location_id INT NOT NULL,
    sale_payment_type_id INT NOT NULL,
    sale_product_line_id INT NOT NULL,
    sale_date TIMESTAMP NOT NULL,
    sale_quantity INT NOT NULL,
    sale_unitprice DOUBLE PRECISION NOT NULL,
    sale_taxes DOUBLE PRECISION NOT NULL,
    sale_total DOUBLE PRECISION NOT NULL,
    sale_gross_income DOUBLE PRECISION NOT NULL,
    
    FOREIGN KEY (sale_location_id) REFERENCES location(location_id),
    FOREIGN KEY (sale_payment_type_id) REFERENCES payment(payment_id),
    FOREIGN KEY (sale_product_line_id) REFERENCES product_line(product_line_id)
);







