numbers = list(map(lambda n: int(n), open('input.txt', 'r').read().split()))
current = 0


def advance(length):
    global current
    current += length
    return numbers[current - length:current]


def process_node():
    num_kids = advance(1)[0]
    meta_length = advance(1)[0]
    node = {
        'kids': [process_node() for _ in range(num_kids)],
        'meta': advance(meta_length)
    }

    node['value'] = sum(node['meta']) + sum([n['value'] for n in node['kids']])

    return node


root = process_node()
print(root['value'])
