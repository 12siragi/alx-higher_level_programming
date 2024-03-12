-- 102-top_city.sql

USE hbtn_0c_0;

SELECT city, AVG((temperature - 32) * 5 / 9) as avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

