SELECT * FROM flights.flights;
SELECT DISTINCT source FROM flights.flights
UNION 
SELECT DISTINCT destination FROM flights.flights

SELECT * FROM flights 
WHERE source="banglore" and destination ="delhi"

SELECT Airline,count(*) AS "frequency" FROM flights
GROUP BY Airline

-- busiest airport 
SELECT source, count(*) FROM (SELECT source FROM flights
                             UNION ALL 
                             SELECT destination FROM flights) t
GROUP BY t.source 
ORDER BY count(*) DESC

SELECT * FROM flights

SELECT Date_of_Journey, COUNT(*) FROM flights
GROUP BY Date_of_Journey 