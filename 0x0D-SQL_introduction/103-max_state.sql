-- 103-max_state.sql

USE hbtn_0c_0;

SELECT state, MAX(temperature) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

