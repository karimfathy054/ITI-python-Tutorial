use python;

create table employee (
    id int auto_increment primary key,
    first_name varchar(255),
    last_name varchar(255),
    age int,
    department varchar(255),
    salary int
);

alter table employee
add managed_department varchar(255) default null;