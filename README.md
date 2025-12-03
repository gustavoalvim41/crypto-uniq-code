## GCU

Este projeto tem como objetivo gerar códigos únicos e seguros combinando números sequenciais (1, 2, 3...) com criptografia HMAC encadeada para garantir imprevisibilidade, produzindo identificadores compactos de 12 caracteres.

Evita colisões (paradoxo do aniversário) e elimina a necessidade de consultas ao banco para verificar duplicidade.

## Como Funciona
1. **Número sequencial** convertido para Base36
2. **HMAC encadeado com chave secreta** cada HMAC depende do anterior, garantindo que os códigos futuros não possam ser previstos a partir dos anteriores.
3. **Resultado final**: código de 12 caracteres seguro e único.

O `SEQUENTIAL_NUMBER` deve ser obtido do banco de dados na aplicação real.
