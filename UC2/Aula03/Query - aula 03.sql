CREATE DATABASE vendas_online;
 use vendas_online;

CREATE TABLE produtos (
 id_produto INT PRIMARY KEY,
 nome VARCHAR(255),
 categoria VARCHAR(100),
 preco DECIMAL(10, 2),
 estoque INT
);

select categoria, preco <1000

from produtos;

select *

from produtos
where preco < 1000;

select nome, categoria
from produtos
where categoria = 'escritório';
