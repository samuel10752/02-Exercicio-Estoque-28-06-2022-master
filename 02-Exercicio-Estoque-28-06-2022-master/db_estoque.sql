create database estoque;
use estoque;

create table Produtos(
id int auto_increment,
nome varchar(70) not null,
fabricante varchar(35) not null,
quantidade int,
primary key (id)
);