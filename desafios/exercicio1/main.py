from event_validator import handler
import json

def main():
    """
    Carrega o schema e um evento de teste, e chama a função handler para processá-lo.
    """
    # Carregar o schema JSON
    with open('schema.json', 'r') as file:
        schema = json.load(file)

    # Definir um evento de teste
    event = {
         "eid": "12345",
    "documentNumber": "67890",
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "Main St",
        "number": 100,
        "mailAddress": True
    },
    "extraField": "unexpected" 
        }
    

    # Chamar a função handler com o evento e o schema
    handler(event, schema)

if __name__ == "__main__":
    main()

