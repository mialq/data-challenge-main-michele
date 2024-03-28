#Exemplos de testes para validacao da funcao validate_event.

#1 - EVENTO VALIDO
event = {
    "eid": "12345",
    "documentNumber": "67890",
    "name": "Renata",
    "age": 30,
    "address": {
        "street": "Rua da Alegria",
        "number": 100,
        "mailAddress": True
    }
}

#2 - EVENTO INVALIDO - FALTA CAMPO OBRIGATORIO - NUMBER
event = {
    "eid": "54321",
    "documentNumber": "09876",
    "name": "Marcos",
    "age": 35,
    "address": {
        "street": "Av. Solidariedade",
        # "number" está faltando
        "mailAddress": False
    }
}

# Definir um evento de teste onde 'address' tem um tipo incorreto, nao é dicionario
event = {
        "eid": "12345",
        "documentNumber": "67890",
        "name": "Renata",
        "age": 30,
        "address": "I am a string, not an object"
    }

#Evento Inválido com Tipo Incorreto em address
event = {
    "eid": "67890",
    "documentNumber": "12345",
    "name": "Gabriela",
    "age": 28,
    "address": {
        "street": "Rodovia BR 118",
        "number": "Deveria ser um inteiro",
        "mailAddress": True
    }
}

# Definir um evento de teste com erro no campo 'mailAddress' do objeto 'address'
event = {
        "eid": "12345",
        "documentNumber": "67890",
        "name": "Renata",
        "age": 30,
        "address": {
            "street": "Main St",
            "number": 100,
            "mailAddress": "yes"  # Este deveria ser um booleano, mas é uma string
        }
    }

# Evento Válido com Campo Adicional em address
event = {
    "eid": "98765",
    "documentNumber": "43210",
    "name": "Thiago",
    "age": 34,
    "address": {
        "street": "Fourth St",
        "number": 200,
        "mailAddress": True,
        "apartment": "1B"  # Campo adicional não definido no schema
    }
}

#VALIDAR CAMPO EXTRA
# Definir um evento de teste adicionando campos não esperados pelo schema
event = {
        "eid": "12345",
        "documentNumber": "67890",
        "name": "Renata",
        "age": 30,
        "address": {
            "street": "Main St",
            "number": 100,
            "mailAddress": True
        },
        "type": "string",
        "title": "the name schema"
    }