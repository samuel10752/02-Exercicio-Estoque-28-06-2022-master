create database estoque;
use estoque;

create table Produtos(
id int auto_increment,
nome varchar(70) not null,
fabricante varchar(35) not null,
quantidade int,
primary key (id)
);

create table Fabricante(
id int auto_increment,
nome varchar(70) not null,
primary key (id)
);

create table Compras(
id int auto_increment,
quantidade varchar(70) not null,
primary key (id)
);

create table Vendas(
id int auto_increment,
quantidade varchar(70) not null,
primary key (id)
);

select * from Produtos;
select * from Fabricante;
select * from Compras;
select * from Vendas

