#Задание №1
SELECT login, 
       COUNT(o.id) 
FROM "Couriers" AS c 
LEFT OUTER JOIN "Orders" AS o ON c.id=o."courierId" 
WHERE o."inDelivery" = TRUE 
GROUP BY login;

#Задание №2
SELECT track, 
       CASE 
           WHEN finished = TRUE THEN 2 
           WHEN cancelled = TRUE THEN -1 
           WHEN "inDelivery" = TRUE THEN 1 
           ELSE 0 
       END AS status 
FROM "Orders";