CREATE DATABASE databases;
    create table users (
    id int primary key AUTO_INCREMENT,
    username VARCHAR(20) not null,
    PASSWORD VARCHAR(20) not null
);