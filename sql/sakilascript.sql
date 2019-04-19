use sakila;
show tables;
select * from actor;
select first_name, last_name from actor;
select upper(concat(first_name," ",last_name)) "Actor Name" from actor;
select actor_id,first_name,last_name from actor where first_name = "Joe";
select * from actor where instr(last_name,'gen');
select * from actor where instr(last_name,'li') order by last_name, first_name;
select country_id,country from country where country in ("afghanistan","bangladesh","china");
alter table actor add column description blob;
alter table actor drop column description;
select last_name, count(last_name) from actor group by last_name;
select last_name, count(last_name) from actor group by last_name having count(last_name) > 1;
update actor set first_name = 'HARPO' where last_name ='Williams' and first_name = "Harpo";
update actor set first_name = 'GROUCHO' where last_name ='Williams' and first_name = "HARPO";
show create table address;
select first_name, last_name, a.address from staff s join address a on s.address_id = a.address_id;
select first_name, last_name, sum(p.amount) 'total amt' from staff s 
join payment p on s.staff_id = p.staff_id 
where monthname(payment_date) = 'august' and year(payment_date) = 2005
group by last_name, first_name;
select title, count(actor_id) from film f 
inner join film_actor fa on f.film_id = fa.film_id;
select title, count(i.film_id) from film f join inventory i on f.film_id = i.film_id
where title = 'Hunchback Impossible';
select first_name, last_name, sum(amount) from customer c join payment p on c.customer_id = p.customer_id group by last_name;
select title from film where film_id in (select film_id from film where title like'q%' or title like 'k%')
and language_id in (select language_id from language where name = 'english'); 
select first_name, last_name from actor a where actor_id in (select actor_id from film_actor where film_id in (select film_id from film where title = 'alone trip'));