# Busca de Notícias do Mercado Financeiro

## Spiders
Spider construídos utilizando a biblioteca [**Scrapy**](https://docs.scrapy.org/en/latest/).

Os spiders estão localizados em */scrapper/spiders*.

Novos spiders podem ser adicionados conforme a necessidade. (Necessário configurar um spider para cada website)

## Banco de Dados
As notícias estão sendo salvas em um tabela no PostgreSQL. Basta configurar um server PostgreSQL como preferir e atualizar as variáveis de ambiente no arquivo .env ou no próprio OS (como preferir). 

Não é preciso criar a tabela, pois a mesma será criada automaticamente na primeira execução.
