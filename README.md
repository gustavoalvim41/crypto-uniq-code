# GCU
Gerador de Códigos Únicos

## Objetivo
Gerar códigos únicos sequenciais que contornam o paradoxo do aniversário através de criptografia, criando identificadores curtos, seguros e não previsíveis.

## Características Principais
- **Sequencial**: Baseado em números sequenciais (1, 2, 3...)
- **Seguro**: Usa HMAC para garantir imprevisibilidade
- **Compacto**: Códigos de apenas 10 caracteres
- **Único**: Elimina riscos de colisão (paradoxo do aniversário)
- **Criptografado**: Transformação irreversível para segurança

## Como Funciona
1. **Número sequencial** convertido para Base36
2. **HMAC com chave secreta** para segurança e imprevisibilidade
3. **Resultado final**: código de 10 caracteres seguro
## Como Rodar
```
1. Crie um arquivo `.env`
SECRET_KEY=

2. Instale as dependências
pip install -r requirements.txt

3. Execute o script
python main.py
```

## Observação
O valor `SEQUENTIAL_NUMBER` deve ser buscado do banco de dados na aplicação real. Aqui ele está fixo apenas para demonstração.
