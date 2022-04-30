# Busca de Notícias do Mercado Financeiro

Projeto de web scraping completo, incluindo a construção dos "robôs" de forma flexível e escalável, integração com Banco de Dados e Agendamento de execução.  

## Spiders
Spider construídos utilizando a biblioteca [**Scrapy**](https://docs.scrapy.org/en/latest/).

Os spiders estão localizados em */scrapper/spiders*.

Novos spiders podem ser adicionados conforme a necessidade. (Necessário configurar um spider para cada website)

O arquivo TEMPLATE.py apresenta uma estrutura que pode ser utilizada para construção de novos Spiders.

## Banco de Dados
O PostgreSQL está definido como banco de dados padrão. Basta configurar um server PostgreSQL, criar um database e atualizar as variáveis de ambiente no arquivo .env ou no próprio OS (como preferir).

Caso deseje utilizar o MySQL, incluir a variável de ambiente *DATABASE="mysql"*

Não é preciso criar a tabela, pois a mesma será criada automaticamente na primeira execução.

## Schedule
Ao iniciar o serviço, ele ficará em standby e será executado nos horários agendados. O agendamento é feito configurando a variável de ambiente *CRAWL_SCHEDULE* utilizando expressão CRON [Saiba Mais](https://crontab.guru/).

Caso deseje, a execução pode ser iniciada imediatamente utilizando o argumento *--now* ao inicializar o arquivo *main.py*.

---

Outros projetos de web scraping podem ser facilmente desenvolvidos utilizando o conteúdo desse repositório como referência.

Fique a vontade para criar seu *fork*!