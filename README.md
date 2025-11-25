## GCU
Este projeto tem como objetivo gerar códigos únicos e seguros combinando números sequenciais (1, 2, 3...) com criptografia HMAC para garantir imprevisibilidade, produzindo identificadores compactos de 10 chars. 

Evita colisões (paradoxo do aniversário) e elimina a necessidade de consultas ao banco para verificar duplicidade.

## Como Funciona
1. **Número sequencial** convertido para Base36
2. **HMAC com chave secreta** garante segurança e imprevisibilidade
3. **Resultado final**: código de 10 chars seguro

O `SEQUENTIAL_NUMBER` deve ser obtido do banco de dados na aplicação real.
