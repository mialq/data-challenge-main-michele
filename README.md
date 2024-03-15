# data-challenge-main-michele
Documentaçao Projeto Desafio de Dados.
-------------------------------------

Documentação do Desafio de Dados
Visão Geral
Este projeto consiste em criar uma plataforma de dados para uma empresa financeira utilizando serviços AWS. O objetivo é construir um fluxo de ingestão de dados robusto, implementar validação de dados com um módulo de Data Quality e automatizar a criação de tabelas no AWS Athena para análises exploratórias.

Tecnologias Utilizadas
AWS Kinesis
AWS Lambda
Amazon S3
AWS Glue
AWS Athena
AWS CloudWatch
Exercício 1: Validação de Eventos
Descrição
Construção de um módulo em Python para validar eventos de acordo com um JSON Schema, enviando eventos válidos para uma fila específica.

Instalação e Uso
Nenhuma instalação específica é necessária. Execute python main.py no diretório exercicio1 para simular o processo de validação.

Código
python
Copy code
# Sumário do código para validar eventos
def validate_event(event, schema):
    # lógica de validação
Exercício 2: Automação de Tabelas no Athena
Descrição
Módulo Python para automatizar a criação de tabelas no AWS Athena a partir do JSON Schema utilizado no módulo de Data Quality.

Instalação e Uso
Execute python main.py no diretório exercicio2 para simular a criação de tabelas no Athena.

Código
python
Copy code
# Sumário do código para criação de tabelas
def schema_to_athena_ddl(schema):
    # gera a query DDL a partir do schema
Arquitetura da Solução
A solução proposta envolve a ingestão de dados via AWS Kinesis, validação desses dados através de um Lambda, armazenamento em um Data Lake no Amazon S3, transformação e catalogação via AWS Glue, análises ad hoc com AWS Athena, e monitoramento com AWS CloudWatch.
