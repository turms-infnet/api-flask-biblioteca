def validate_fields(data, fields):
    result = {}

    for field in fields:
        if field not in fields:
            result.update({field: 'O campo é obrigatório'})

    hasKeys = len(result.keys()) > 0

    return hasKeys, result