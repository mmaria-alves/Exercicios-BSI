def PrintAllPairsShortestPath(pi, i, j):
    if i == j:
        print(i, end=" ")
    elif pi[i][j] is None:
        print(f"no path from {i} to {j} exists", end=" ")
    else:
        PrintAllPairsShortestPath(pi, i, pi[i][j])
        print(j, end=" ")

# Matriz de predecessores fictícia
pi_matrix = [
    [None, 0, 3, 4, 0],
    [3, None, 3, 1, 1],
    [3, 2, None, 3, 3],
    [3, 0, 3, None, 0],
    [3, 0, 3, 4, None]
]

print("Caminho de 1 até 4: ", end="")
PrintAllPairsShortestPath(pi_matrix, 3, 1)
print() # quebra de linha