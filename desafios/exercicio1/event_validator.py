import json

def send_event_to_queue(event, queue_name):
    """
    Simula o envio do evento para a fila especificada.
    """
    print(f"Evento válido. Enviado para a fila {queue_name}: {json.dumps(event)}")

def json_type_to_python_type(json_type):
    """
    Mapeia tipos de JSON para tipos de Python equivalentes.
    """
    types = {
        'string': str,
        'integer': int,
        'boolean': bool,
        'object': dict,
    }
    return types.get(json_type, None)

def validate_event(event, schema):
    """
    Valida um evento com base no schema JSON fornecido.
    Retorna um booleano indicando a validade e uma mensagem explicativa.
    """
    # Verificar por campos obrigatórios e tipo correto
    for field in schema['required']:
        if field not in event:
            return False, f"Falta o campo obrigatório: {field}"
        expected_type_str = schema['properties'][field]['type']
        expected_type = json_type_to_python_type(expected_type_str)
        if not isinstance(event[field], expected_type):
            return False, f"Tipo incorreto para o campo '{field}'. Esperado: {expected_type_str}, encontrado: {type(event[field]).__name__}"

    # Verificar por campos extras não definidos no schema
    extra_fields = [field for field in event if field not in schema['properties']]
    if extra_fields:
        return False, f"Campo(s) não esperado(s) : {', '.join(extra_fields)}"

    return True, "Evento válido"

def handler(event, schema):
    """
    Processa e valida eventos. Inclui logs específicos para detalhar a validação.
    """
    is_valid, message = validate_event(event, schema)
    if is_valid:
        print(message + f" Enviando para a fila. Evento: {json.dumps(event)}")
        send_event_to_queue(event, 'valid-events-queue')
    else:
        print(f"Evento inválido. Não enviado. Motivo: {message}")




