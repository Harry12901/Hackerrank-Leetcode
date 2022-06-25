/*
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
The STATION table is described as follows:
+-------------+------------+
| Field       |   Type     |
+-------------+------------+
| ID          | INTEGER    |
| CITY        | VARCHAR(21)|
| STATE       | VARCHAR(2) |
| LAT_N       | NUMERIC    |
| LONG_W      | NUMERIC    |
+-------------+------------+
where LAT_N is the northern latitude and LONG_W is the western longitude.
*/
SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTRING(CITY,1,1) NOT IN ('a','e','i','o','u') OR SUBSTRING(CITY,-1,1) NOT IN ('a','e','i','o','u');
