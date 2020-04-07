def convert_to_json(**kargs):
    result = {}
    for key, value in kargs.items():
        if value:
            result[key] = value
    return result
