import json

def send_event_to_queue(event, queue_name):
    #Simula o envio do evento para a fila especificada.
    print(
        f"Evento válido. Enviado para a fila {queue_name}: {json.dumps(event)}")

#converter tipos de dados especificados em um esquema JSON para seus equivalentes em Python
def json_type_to_python_type(json_type):#json_type é o tipo de dado json que quero converter
    """
    Mapeia tipos de JSON para tipos de dados/python equivalentes.
    Este dicionário mapeia strings representando tipos de dados JSON para os tipos de dados correspondentes em Python
    """
    types = {
        'string': str,
        'integer': int,
        'boolean': bool,
        'object': dict,  # Este será um indicador para validação recursiva
    }
    #Se o json_type existir no dicionário types, o tipo Python equivalente é retornado. 
    #Se não, None é retornado, o que significa que o tipo JSON fornecido não tem um mapeamento direto conhecido ou válido no dicionário types.
    return types.get(json_type, None)


def validate_event(event, schema):
    """
    Valida um evento com base no schema JSON fornecido de forma recursiva.
    Retorna um booleano indicando a validade e uma mensagem explicativa.
    """
    # Verificar por campos obrigatórios e tipo correto
    for field in schema['required']:
        if field not in event:
            return False, f"Falta o campo obrigatório: {field}"
        expected_type_str = schema['properties'][field]['type']
        expected_type = json_type_to_python_type(expected_type_str)

        # Se o campo for um objeto, fazer a validação recursiva
        if expected_type is dict:
            if not isinstance(event[field], dict):
                return False, f"Tipo incorreto para o campo '{field}'.Esperado: objeto, encontrado: {type(event[field]).__name__}"
            # Chamada recursiva para validar o objeto aninhado
            is_valid, message = validate_event(
                event[field], schema['properties'][field])
            if not is_valid:
                return False, f"No campo '{field}': {message}"
        elif not isinstance(event[field], expected_type):
            return False, f"Tipo incorreto para o campo '{field}'. Esperado: {expected_type_str}, encontrado: {type(event[field]).__name__}"

    # Verificar por campos extras não definidos no schema
    extra_fields = [
        field for field in event if field not in schema['properties']]
    if extra_fields:
        return False, f"Campo(s) não esperado(s): {', '.join(extra_fields)}"

    return True, "Evento válido"

#funcao handler é estimulada sempre que um novo evento cai na fila
#funcao handler recebe eventos, valida-os conforme o schema definido, e entao decide se um evento 
def handler(event, schema):
    """
    Processa e valida eventos. Inclui logs específicos para detalhar a validação.
    """
    is_valid, message = validate_event(event, schema)
    if is_valid:
        # Simplificado para imprimir apenas após a ação de enviar para a fila
        send_event_to_queue(event, 'valid-events-queue')
    else:
        print(f"Evento inválido. Não enviado. Motivo: {message}")
