"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2


def start():
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="kirova7574"
    )

    data_customers = '''COPY customers(customer_id,company_name,contact_name)
    FROM 'C:/Users/Since1925/PycharmProjects/postgres-homeworks/homework-1/north_data/customers_data.csv'
    DELIMITER ','
    CSV HEADER;'''

    data_employees = '''COPY employees(employee_id,first_name,last_name,title,birth_date,notes)
    FROM 'C:/Users/Since1925/PycharmProjects/postgres-homeworks/homework-1/north_data/employees_data.csv'
    DELIMITER ','
    CSV HEADER;'''

    data_orders = '''COPY orders(order_id,customer,employee,order_date,ship_city)
    FROM 'C:/Users/Since1925/PycharmProjects/postgres-homeworks/homework-1/north_data/orders_data.csv'
    DELIMITER ','
    CSV HEADER;'''

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(data_customers)
                cur.execute(data_employees)
                cur.execute(data_orders)
    finally:
        conn.close()


if __name__ == '__main__':
    start()
