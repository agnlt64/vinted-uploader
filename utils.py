TYPES = {
    'jean': 'J',
    'polo': 'P',
    'teeshirt': 'T',
    'chemise': 'C',
    'bermuda': 'B',
    'sous_pull': 'S',
    'pyjama': 'Y',
    'bermuda': 'B',
    'jogging': 'G',
}

BRANDS = {
    'atlas': 'A',
    'kiabi': 'K',
    'tissaia': 'T',
    'decathlon': 'D',
    'puma': 'P',
    'lh': 'L',
    'kaporal': 'C',
    'nike': 'N'
}

COLORS = {
    'bleu': 'B',
    'noir': 'N',
    'orange': 'O',
    'rouge': 'R',
    'vert': 'V',
    'jaune': 'J',
    'gris': 'G',
    'blanc': 'C',
    'marron': 'M'
}

QUALITY = {
    'excellent': 'EE',
    'bon': 'BE',
    'mauvais': 'ME'
}

def parse_type(type: str) -> str:
    if type == '': return ''
    type_split = type.split(' ')
    if len(type_split) == 1:
        type_split = type.split('-')
        return ''.join(type_split).lower()
    else:
        final = ''
        for word in type_split:
            if word != type_split[-1]:
                final += word.lower() + '_'
            else:
                final += word.lower()
        return final

def parse_brand(brand: str) -> str:
    if brand == '': return ''
    brand = brand.split(' ')
    final = ''
    for word in brand:
        if word != brand[-1]:
            final += word.lower() + '_'
        else:
            final += word.lower()
    return final

def parse_quality(quality: str) -> str:
    return '' if quality == '' else quality.lower()

def generate_folder_name(type: str, color: str, size: str | int, brand: str, quality: str) -> str:
    return f'{type}_{color}_{str(size)}_{brand}_{quality}'

def generate_code(folder_name: str) -> str:
    folder_name = folder_name.split('_')
    return f'{TYPES[folder_name[0]]}{COLORS[folder_name[1]]}{folder_name[2]}{BRANDS[folder_name[3]]}{QUALITY[folder_name[-1]]}'
