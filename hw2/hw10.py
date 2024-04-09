def parse(str):
    pairs = str.split('&')
    result = {}

    for pair in pairs:
        key, value = pair.split('=')
        result[key] = value

    return result

str = 'led=on&motor=off&switch=off'
result = parse(str)
print(result)