class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.left = None
        self.right = None
        self.pai = None

    def getInfo(self):
        return self.dado

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getFather(self):
        return self.pai

    def isLeft(self):
        q = self.getFather()
        # se não tem pai, é a raiz
        if q is None:
            return False
        # se o filho esquerdo do pai for este nó, então é True
        if q.getLeft() == self: 
            return True
        return False

    def isRight(self):
        q = self.getFather()

        if q is None:
            return False

        if q.getRight() == self:
            return True
        return False

    def getBrother(self):
        q = self.getFather()

        if q is None:
            return None

        if self.isLeft():
            return q.getRight()
        return q.getLeft()

class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def inOrderTreeWalk(self, x):
        if x is not None:
            self.inOrderTreeWalk(x.left)   # sub-arvore esquerda
            print(x.getInfo(), end=" ")       # raiz
            self.inOrderTreeWalk(x.right)    # sub-arvore direita

    def preOrderTreeWalk(self, x):
        if x is not None:
            print(x.getInfo(), end=" ")    # raiz
            self.preOrderTreeWalk(x.left)   # sub-arvore esquerda
            self.preOrderTreeWalk(x.right)    # sub-arvore direita

    def postOrderTreeWalk(self, x):
        if x is not None:
            self.postOrderTreeWalk(x.left)   # sub-arvore esquerda
            self.postOrderTreeWalk(x.right)    # sub-arvore direita
            print(x.getInfo(), end=" ")    # raiz

    def treeSearch(self, x, k):
        if x is None or k == x.dado:
            return x
        if k < x.dado:
            return self.treeSearch(x.left, k)
        else: return self.treeSearch(x.right, k)

    def iterativeTreeSearch(self, x, k):
        while x is not None and k is not x.dado:
            if k < x.dado:
                x = x.left
            else: x = x.right
        return x

    def treeMinimun(self, x):
        while x.left is not None:
            x = x.left
        return x

    def treeMaximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def treeSuccessor(self, x):
        if x.right is not None:
            return self.treeMinimun(x.right)
        y = x.pai
        while y is not None and x == y.right:
            x = y
            y = y.pai
        return y

    def treePredecesor(self, x):
        if x.left is not None:
            return self.treeMaximum(x.left)
        y = x.pai
        while y is not None and x == y.left:
            x = y
            y = y.pai
        return y

    def treeInsert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.dado < x.dado:
                x = x.left
            else:
                x = x.right
        z.pai = y
        if y is None:
            self.root = z    # árvore vazia
        elif z.dado < y.dado:
            y.left = z
        else:
            y.right = z





if __name__ == '__main__':
    arvore = ArvoreBinaria()

    valores = [12, 5, 18, 2, 9, 15, 19, 17]
    # Árvore resultante esperada:
    #            12
    #          /    \
    #         5      18
    #        / \    /  \
    #       2   9  15   19
    #               \
    #                17

    print("=== INSERINDO ELEMENTOS ===")
    for v in valores:
        arvore.treeInsert(Nodo(v))
        print(f"Inserido: {v}")

    print("\n--- 1. Teste de Ordenação (In-Order) ---")
    # Se a inserção BST estiver correta, a saída DEVE ser estritamente crescente
    print("Esperado: 2 5 9 12 15 17 18 19")
    print("Obtido:  ", end=" ")
    arvore.inOrderTreeWalk(arvore.root)
    print("\n")