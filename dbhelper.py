import mysql.connector

class DB:
    def __init__(self):

        # connect to database
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="flights"
            )
            self.mycursor = self.conn.cursor()
            print("Connection Establish")
        except:
            print("Connection Error ")
    def fetch_city_names(self):

        city=[]
        self.mycursor.execute("""
        SELECT DISTINCT source FROM flights.flights
        UNION 
        SELECT DISTINCT destination FROM flights.flights
        """)
        data= self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flight(self,source,destination):
        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price FROM flights 
         WHERE source="{}" and destination ="{}"
        """.format(source,destination))

        data= self.mycursor.fetchall()

        return data
    def fetch_airline_frequency(self):
        airline=[]
        frequency =[]

        self.mycursor.execute("""
        SELECT Airline,count(*) AS "frequency" FROM flights
        GROUP BY Airline
        """)

        data= self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency
    def busy_airport(self):
        city=[]
        frequency =[]
        self.mycursor.execute("""SELECT source, count(*) FROM (SELECT source FROM flights
                             UNION ALL 
                             SELECT destination FROM flights) t
                             GROUP BY t.source 
                             ORDER BY count(*) DESC""")
        data= self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city,frequency

    def dily_frequency(self):
        date=[]
        frequency =[]
        self.mycursor.execute("""SELECT Date_of_Journey, COUNT(*) FROM flights
                           GROUP BY Date_of_Journey """)
        data= self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date,frequency


