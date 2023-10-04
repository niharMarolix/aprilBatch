import psycopg2

db_params = {
    "host":"localhost",
    "port":5432,
    "database" : "connectDb",
    "user":"postgres",
    "password":"uuuu1111"
}

try:
    connection = psycopg2.connect(**db_params)

    curser = connection.cursor()

    dataToAdd = {
        "name" : "KC",
        "email":"kc@gmail.com",
        "age":28
    }

    insert_query = "INSERT INTO `EMPDATA` (`name`, `email`, `age`) VALUES ('KC', 'kc@gmail.com', 28)";

    curser.execute(insert_query, dataToAdd)

    connection.commit()

    print("data inserted successfully")

except:
    if connection:
        curser.close()
        connection.close()
        print("connection failed")


