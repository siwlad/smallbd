import csv
import psycopg2
from decimal import Decimal

conn = psycopg2.connect(
    host="localhost",
    database="cars",
    user="students",
    password="qwerty"
)

cur = conn.cursor()

with open('region25.csv', 'r') as f:
    reader = csv.DictReader(f)
    next(reader)
    for row in reader: 
        for key in row.keys():
            if row[key] == "":
                row[key] = None
            elif key == 'price':
                row[key] = Decimal(row[key])
        cur.execute(
            "INSERT INTO cars (brand, car_name, bodytype, color, fuelType, price, car_location) "
            "VALUES (%(brand)s, %(name)s, %(bodyType)s, %(color)s, %(fuelType)s, %(price)s, %(location)s)",
            row
        )
        
        print(row)

        conn.commit()
    cur.close()     
    conn.close()
