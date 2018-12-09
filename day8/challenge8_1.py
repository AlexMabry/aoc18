numbers = list(map(lambda n: int(n), open('input.txt', 'r').read().split()))
current = 0


def process_node():
    global current
    num_kids = numbers[current]
    meta_length = numbers[current+1]
    current += 2
    node = {'kids': [process_node() for _ in range(num_kids)], 'meta': numbers[current:current + meta_length], }
    node['value'] = sum(node['meta']) + sum([n['value'] for n in node['kids']])
    current += meta_length
    return node


root = process_node()
print(root['value'])
