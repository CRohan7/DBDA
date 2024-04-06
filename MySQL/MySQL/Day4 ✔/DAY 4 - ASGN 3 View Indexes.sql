DAY 4 - ASGN 3 View Indexes


Q4
------------------------------
select c.cname , v.vname,s.sname,  concat (round(((v.price-cv.buy_price)/v.price)*100,2),"%")  discount  from
cust_vehicle cv inner join customer c on cv.custid= c.custid

inner join salesman s on s.sid=cv.sid

inner join vehicle v on v.vid= cv.vid;

-------------------------------------------------
Q5
select s.sname ,c.cname  , v.vname , s.sname  from 

cust_vehicle cv inner join customer c on cv.custid=c.custid

inner join vehicle v on v.vid =cv.vid 

inner join salesman s on s.sid=cv.sid


where s.address="Pune";

-----------------------------------------------
Q6
select c.cname,v.vname from 

cust_vehicle cv inner join customer c on cv.custid=c.custid

inner join vehicle v on v.vid =cv.vid 



where v.vname="Motor Bike";
















