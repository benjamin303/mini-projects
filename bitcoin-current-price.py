import requests
import schedule
import time
import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.103",
    user="benjamin",
    password="benjamin",
    database="learning"
)

mycursor = mydb.cursor()

def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS bitcoin_price (id INT AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), eur_price VARCHAR(255), usd_price VARCHAR(255))")
    print("Table created successfully.")

create_table()

last_price = None

def job():
    global last_price

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    if response.status_code == 200:
        data = response.json()
        bpi_time = data["time"]["updated"]
        eur_price = data["bpi"]["EUR"]["rate"]
        usd_price = data["bpi"]["USD"]["rate"]

        print("Current time is:", bpi_time)
        print("Current Bitcoin price in EUR is:", eur_price)
        print("Current Bitcoin price in USD is:", usd_price)

        if last_price is None or last_price != eur_price:
            sql = "INSERT INTO bitcoin_price (time, eur_price, usd_price) VALUES (%s, %s, %s)"
            val = (bpi_time, eur_price, usd_price)
            mycursor.execute(sql, val)
            mydb.commit()
            last_price = eur_price
            print("Price has changed. Data saved.")
        else:
            print("Price has not changed. Skipping data save.")
    else:
        print("Failed to retrieve data.")

# schedule.every().hour.do(job)
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

