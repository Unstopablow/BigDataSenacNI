use vendas_online;

CREATE TABLE clientes (
 id_cliente INT PRIMARY KEY,
 nome VARCHAR(255),
 email VARCHAR(255)
);

CREATE TABLE pedidos (
 id_pedido INT PRIMARY KEY,
 data_pedido DATE,
 valor_total DECIMAL(10, 2),
 id_cliente INT,
 id_produto INT,
 quantidade INT,
 FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
 FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);