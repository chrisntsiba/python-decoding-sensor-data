import snowflake.connector

un = "cntsiba"
pw = "zW0fL@qp!"
acnt = "xp15959.east-us-2.azure"

context = snowflake.connector.connect(user=un, password=pw, account=acnt)
cursor = context.cursor()

try:
    cursor.execute("use role accountadmin")

    cursor.execute("use warehouse demo_wh")
    cursor.execute("use database demo_db")
    cursor.execute("use schema public")
    cursor.execute('select top 10 * from "DEMO_DB"."PUBLIC"."airports_postgres"')

    for i in cursor.fetchall():
        print(i)
finally:
    cursor.close()
context.close()

