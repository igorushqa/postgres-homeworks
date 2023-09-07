"""Скрипт для заполнения данными таблиц в БД Postgres."""
from csv import DictReader
import psycopg2
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def read_csv(filename: str) -> list[tuple]:
    path_csv = Path.joinpath(ROOT_PATH, 'north_data', filename)
    with open(path_csv, 'r', encoding='windows-1251') as csv:
        data = DictReader(csv)
        temp_list = []
        temp_list1 = []
        result_list_tuple = []
        for item in data:
            temp_list.append(item)
        for ini_dict in temp_list:
            for vol in ini_dict.values():
                temp_list1.append(vol)
            result_list_tuple.append(tuple(temp_list1))
            temp_list1 = []
    return result_list_tuple


def record_table(database: str, filename: str, postgres_command: str):
    conn = psycopg2.connect(
        host="localhost",
        database=database,
        user="postgres",
        password="kirova7574"
    )
    data = read_csv(filename)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(postgres_command, data)
    finally:
        conn.close()


if __name__ == '__main__':
    record_table("north", "customers_data.csv", """INSERT INTO customers (customer_id, company_name, contact_name)
    VALUES (%s,%s,%s)""")
    record_table("north", "employees_data.csv", """INSERT INTO employees (employee_id, first_name, last_name, title,
    birth_date, notes) VALUES (%s,%s,%s,%s,%s,%s)""")
    record_table("north", "orders_data.csv", """INSERT INTO orders (order_id, customer_id, employee_id, order_date,
    ship_city) VALUES (%s,%s,%s,%s,%s)""")
