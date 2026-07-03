def filter_by_state(data:list[dict], state = 'EXECUTED') -> list[dict]:
    result = []
    for item in data:
        if item.get('state') == state:
            result.append(item)
    return result

