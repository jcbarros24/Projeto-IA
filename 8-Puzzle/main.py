
from iddfs_copy import iddfs_copy
from iddfs_inplace import iddfs_inplace

initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

max_depth = 10

print("Rodando IDDFS com cópia do estado")
if iddfs_copy(initial_state, max_depth):
    print("Solução encontrada com a cópia do estado!")
else:
    print("Nenhuma solução encontrada com a cópia do estado.")

print("Executando IDDFS com modificação in-place...")
if iddfs_inplace(initial_state, max_depth):
    print("Solução encontrada com modificação in-place!")
else:
    print("Nenhuma solução encontrada com modificação in-place.")
