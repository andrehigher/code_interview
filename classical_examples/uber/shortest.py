def bfs(graph, source):
  queue = []
  visited = []

  queue.insert(0, source)
  while len(queue) > 0:
    current = queue.pop()
    if current not in visited:
      visited.append(current)
    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.insert(0, neighbor)

  print(visited)


def shortest_path(graph, source, target):
  queue = [(source, [source])]
  while queue:
    (vertex, path) = queue.pop(0)
    for next in graph[vertex] - set(path):
      if next == target:
        yield path + [next]
      else:
        queue.append((next, path + [next]))


graph = {
  'a': ['b', 'c', 'e'],
  'b': ['a', 'c'],
  'c': ['a', 'b', 'd', 'e'],
  'd': ['c'],
  'e': ['c', 'a']
}

bfs(graph, 'a')
shortest_path(graph, 'a', 'd')