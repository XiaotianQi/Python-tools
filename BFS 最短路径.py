# _*_coding:utf-8_*_

gragh = {
    'A':['B', 'C'],
    'B':['A', 'C', 'D'],
    'C':['A', 'B', 'D', 'E'],
    'D':['B', 'C', 'E', 'F'],
    'E':['C', 'D'],
    'F':['D']
}

def pathBfs(gragh, node):
    queue = []
    queue.append(node)
    seen = set()
    seen.add(node)
    parent = {node : None}
    while len(queue)>0:
        vertex = queue.pop(0)
        nodes = gragh[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
        # print(vertex)
    return parent

if __name__ == '__main__':
    parent = pathBfs(gragh, 'A')
    node = 'E'
    while node != None:
        print(node)
        node = parent[node]