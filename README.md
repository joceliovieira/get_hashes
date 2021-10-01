# Projeto: get_hashes

Projeto desenvolvido com o objetivo de coletar hashes do tipo MD5 de documentos de Inteiro Teor das proposições apresentadas nos últimos 3 dias na Câmara dos Deputados.

## Usando a API

Para usar a API, basta hospedar a aplicação em um servidor, executar o arquivo main.py e acessar o endereço da mesma.

Ao acessar a aplicação, será disposta uma página solicitando os tipos de proposições a serem consultadas. As mesmas devem ser do tipo PL, PLP ou PEC, e devem ser escritas em letras maiúsculas separadas por vírgula.

Após submeter os tipos de interesse, o sistema irá retornar uma lista de dicionários contendo: HashMD5, ID da proposição e tipo da mesma (PL, PLP ou PEC).

### Referências
https://dadosabertos.camara.leg.br/swagger/api.html
