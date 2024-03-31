# expandir a função handler em json_schema_to_hive.py
# para incluir a lógica de leitura do schema e geração da query SQL
import json

"""
A função -json_schema_to_hive_type, recebe um parâmetro json_type, que é uma string representando 
o tipo de dado em um schema JSON (por exemplo, 'string', 'integer', 'boolean', 'object')
"""
def json_schema_to_hive_type(json_type):
    #Mapeia os tipos de dados do JSON para os tipos de dados equivalentes no Hive
    #que sao usados em consulta SQL no Athena
#Este dicionário mapeia os tipos de dados JSON (chaves) para os tipos de dados correspondentes no Hive (valores)
    mapping = {
        "string": "STRING",
        "integer": "INT",
        "boolean": "BOOLEAN",
        "object": "struct<{}>",  # Requer tratamento especial para campos aninhados.
    }
    #Retorna o tipo de dado Hive correspondente ao tipo de dado JSON fornecido, se nao encontrar retorna string.
    return mapping.get(json_type, "STRING")

#criar uma tabela hive, baseada no schema json
def schema_to_athena_ddl(schema, table_name="data_quality_module"):
    ddl_parts = []
    for field, props in schema["properties"].items():#itera sobre os campos properties do esquema json.
        hive_type = json_schema_to_hive_type(props["type"])
        if props["type"] == "object":
            nested_fields = ", ".join([f"{sub_field}: {json_schema_to_hive_type(sub_props['type'])}" for sub_field, sub_props in props["properties"].items()])
            hive_type = hive_type.format(nested_fields)
        ddl_parts.append(f"{field} {hive_type}")

    ddl_query = f"CREATE EXTERNAL TABLE IF NOT EXISTS {table_name} ({', '.join(ddl_parts)}) PARTITIONED BY (year INT, month INT, day INT) STORED AS PARQUET LOCATION 's3://your-data-bucket/path/to/data/'"
    return ddl_query

#Simula a execução da query DDL no Amazon Athena
def create_hive_table_with_athena(query):
    print(f"Executing Query: {query}")
    # Em um cenário real, essa funcao usaria um cliente do ATHENA_CLIENT.start_query_execution(QueryString=query)


#Função principal carrega o esquema JSON, gera a query DDL usando o esquema e 
#simula a execução dessa query para criar a tabela no Athena.
def handler():
    schema_path = 'schema.json'  # Assegure-se de ajustar para o caminho correto do seu schema.json
    with open(schema_path, 'r') as file:
        schema = json.load(file)
    query = schema_to_athena_ddl(schema)
    create_hive_table_with_athena(query)

# Isto assumirá que o _ATHENA_CLIENT tenha sido configurado corretamente.
