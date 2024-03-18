
# Documentação do Projeto Data Challenge – Michele Teixeira

## Introdução

Este documento descreve minha jornada ao abordar os exercícios 1, 2 e 3 do Projeto Data Challenge. O foco está na construção de um módulo de Data Quality, automação da criação de tabelas no AWS Athena, e a proposta de uma arquitetura de dados robusta.

### Exercício 1: Módulo de Data Quality

Iniciei o projeto definindo a estrutura básica dentro do diretório `exercicio1/`, concentrando-me em dois arquivos principais: `event_validator.py` e `schema.json`. O `schema.json` serviu como a base para validar a estrutura dos eventos de dados, garantindo sua qualidade.

**Desenvolvimento:**

Implementei a função `validate_event(event, schema)` no arquivo `event_validator.py`. Essa função verifica se cada evento corresponde ao schema definido, atentando especialmente para dois aspectos:

- Asseguro que o tipo de cada campo do evento coincide com o especificado no schema.
- Verifico que o evento não inclua campos não listados no schema.

**Execução:**

Para testar minha implementação, executei `python main.py`, que simula o processo de validação de eventos, assegurando que eles atendam aos critérios definidos.

### Exercício 2: Automação de Criação de Tabelas no AWS Athena

Avancei para o `exercicio2/`, onde meu objetivo era automatizar a criação de tabelas no AWS Athena. Utilizei o mesmo `schema.json` do Exercício 1 como fundamento.

**Desenvolvimento:**

No arquivo `json_schema_to_athena.py`, desenvolvi uma função que traduz o `schema.json` em uma query SQL de criação de tabela para o Athena. Este passo exigiu uma compreensão profunda da documentação do AWS Athena, especialmente no que se refere à sintaxe de criação de tabelas.

**Execução:**

Após implementar a função, executei `python main.py` para testar a automação, verificando se a query SQL gerada estava correta e alinhada com as especificações do Athena.

### Exercício 3: Proposta de Arquitetura de Dados

Finalmente, dediquei-me ao desafio de propor uma arquitetura de dados completa. Meu objetivo era abordar soluções de ingestão, pipeline ETL, soluções de armazenamento, e o catálogo de dados.

**Desenvolvimento:**

Utilizei ferramentas de desenho como Draw.io para esboçar a arquitetura, fazendo escolhas conscientes sobre cada componente:

- **Solução de Ingestão:** Defini como os dados seriam coletados e importados para o sistema.
- **Pipeline ETL:** Projetei o processo de transformação dos dados para prepará-los para análise.
- **Soluções de Armazenamento:** Especifiquei onde os dados seriam armazenados, considerando escalabilidade e acesso.
- **Catálogo de Dados:** Desenvolvi uma estratégia para gerenciar metadados e facilitar a descoberta de dados.

**Documentação:**

Para cada componente da arquitetura, providenciei uma descrição detalhada, explicando sua função e contribuição para os objetivos gerais de negócios e dados.

## Considerações Finais

Espero que este documento ofereça uma visão clara da minha abordagem aos desafios propostos, refletindo as decisões, implementações e aprendizados ao longo deste projeto.

---

# ARQUITETURA DO PROJETO – Módulo Data Quality

(imagem.png)

A arquitetura parece estar bem alinhada com os requisitos do desafio de criar um sistema que possa validar eventos de dados e, em seguida, disponibilizá-los para análise. 
Aqui está um resumo coerente de cada etapa baseado no desenho fornecido:

1. **Coleta de Dados:** Os eventos são gerados por fontes internas e externas e disponibilizados em formato JSON.
2. **Enfileiramento de Eventos:** Os eventos em JSON são colocados em uma fila de mensagens AWS SQS, que serve como um buffer intermediário e ajuda a gerenciar o fluxo de dados.
3. **Validação de Dados (AWS Lambda):** Os eventos são consumidos da fila SQS e passam por uma função AWS Lambda que os valida contra um esquema predefinido (`schema.json`). Este é o núcleo do módulo Data Quality, garantindo que apenas dados corretos e completos avancem no pipeline.
4. **Armazenamento de Dados Validados (Amazon DynamoDB):** Após a validação, os dados são armazenados no Amazon DynamoDB, que oferece armazenamento rápido e flexível, adequado para acesso e consulta de alta performance.
5. **Catalogação de Dados (AWS Glue):** Os metadados dos dados validados são gerenciados pelo AWS Glue, que cria um catálogo de dados para facilitar a organização, a descoberta e o acesso aos dados.
6. **Consulta e Análise de Dados (Amazon Athena):** O Amazon Athena é utilizado para realizar consultas diretamente sobre os dados armazenados no Amazon S3. Isso permite análises complexas e a execução de consultas SQL sem a necessidade de mover os dados para outro sistema.
7. **Interpretação de Dados (Usuário Final):** Os analistas e usuários de negócios acessam os insights e relatórios gerados pelo Athena, provavelmente usando ferramentas de Business Intelligence (BI) ou outras interfaces analíticas.
