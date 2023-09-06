-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title text,
	birth_date varchar(25) NOT NULL,
	notes varchar(100) NOT NULL
);

CREATE TABLE customers
(
	customer_id varchar(25) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer varchar(25) REFERENCES customers(customer_id) NOT NULL,
	employee int REFERENCES employees(employee_id) NOT NULL,
	order_date varchar(100) NOT NULL,
	ship_city varchar(100) NOT NULL
)