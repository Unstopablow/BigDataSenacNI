SELECT c.nome, p.data_pedido
FROM clientes c
JOIN pedidos p ON c.id_cliente = p.id_cliente;
