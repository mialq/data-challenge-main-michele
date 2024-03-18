# expandir a função handler em json_schema_to_hive.py
# para incluir a lógica de leitura do schema e geração da query SQL
import json

def json_schema_to_hive_type(json_type):
    mapping = {
        "string": "STRING",
        "integer": "INT",
        "boolean": "BOOLEAN",
        "object": "struct<{}>",  # Requer tratamento especial para campos aninhados.
    }
    return mapping.get(json_type, "STRING")

def schema_to_athena_ddl(schema, table_name="my_table_name"):
    ddl_parts = []
    for field, props in schema["properties"].items():
        hive_type = json_schema_to_hive_type(props["type"])
        if props["type"] == "object":
            nested_fields = ", ".join([f"{sub_field}: {json_schema_to_hive_type(sub_props['type'])}" for sub_field, sub_props in props["properties"].items()])
            hive_type = hive_type.format(nested_fields)
        ddl_parts.append(f"{field} {hive_type}")

    ddl_query = f"CREATE EXTERNAL TABLE IF NOT EXISTS {table_name} ({', '.join(ddl_parts)}) STORED AS PARQUET LOCATION 's3://your-data-bucket/path/to/data/'"
    return ddl_query

def create_hive_table_with_athena(query):
    print(f"Executing Query: {query}")
    # Em um cenário real, aqui eu usaria _ATHENA_CLIENT.start_query_execution(QueryString=query)

def handler():
    schema_path = 'schema.json'  
    with open(schema_path, 'r') as file:
        schema = json.load(file)
    query = schema_to_athena_ddl(schema)
    create_hive_table_with_athena(query)

