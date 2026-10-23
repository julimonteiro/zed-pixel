-- Abra example.csv e execute a tarefa "CSV: SELECT com DuckDB".
-- No terminal DuckDB, execute:
SELECT nome, quantidade, preco FROM csv WHERE quantidade > 1 ORDER BY preco DESC;
SELECT categoria, sum(quantidade * preco) AS total FROM csv GROUP BY categoria;
-- Para sair: .quit
