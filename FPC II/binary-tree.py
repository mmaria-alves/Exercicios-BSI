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

    def treeDelete(self, z):
        if z.left is None or z.right is None:
            y = z
        else:
            y = self.treeSuccessor(z)

        if y.left is not None:
            x = y.left
        else: 
            x = y.right

        if x is not None:
            x.pai = y.pai

        if y.pai is None:
            self.root = x
        elif y == y.pai.left:
            y.pai.left = x
        else:
            y.pai.right = x

        if y != z:
            z.dado = y.dado

        return y

class NodoAVL(Nodo):
    def __init__(self, dado):
        super().__init__(dado)
        self.altura = 1

class ArvoreAVL(ArvoreBinaria):
    def __init__(self):
        super().__init__()

    def nodeHeight(self, x):
        if x is None:
            return 0
        return getattr(x, 'altura', 1)

    def balanceFactor(self, x):
        if x is None:
            return 0
        return self.nodeHeight(x.left) - self.nodeHeight(x.right)

    def updateHeight(self, x):
        if x is not None:
            x.altura = 1 + max(self.nodeHeight(x.left), self.nodeHeight(x.right))

    def leftRotate(self, x):
        y = x.right
        x.right = y.left

        if y.left is not None:
            y.left.pai = x

        y.pai = x.pai

        if x.pai is None:
            self.root = y
        elif x == x.pai.left:
            x.pai.left = y
        else:
            x.pai.right = y

        x.left = x
        x.pai = y

        self.updateHeight(x)
        self.updateHeight(y)

    def rightRotate(self, y):
        x = y.left
        y.right = x.left

        if x.right is not None:
            x.right.pai = y

        x.pai = y.pai

        if y.pai is None:
            self.root = x
        elif y == y.pai.right:
            y.pai.right = x
        else:
            y.pai.left = x

        x.right = y
        y.pai = x

        self.updateHeight(y)
        self.updateHeight(x)

    def treeRebalancing(self, z):
        self.updateHeight(z)
        bf = self.balanceFactor(z)

        # Caso 1 - rotação simples a direita
        if bf > 1 and self.balanceFactor(z.left) >=0:
            self.rightRotate(z)

        # Caso 2- rotação dupla a direita
        if bf > 1 and self.balanceFactor(z.left) < 0:
            self.leftRotate(z.left)
            self.rightRotate(z)

        # Caso 3 - rotação simples a esquerda
        if bf < -1 and self.balanceFactor(z.right) <= 0:
            self.leftRotate(z)

        # Caso 4 - rotação dupla a esquerda
        if bf < -1 and self.balanceFactor(z.right) > 0:
            self.rightRotate(z.right)
            self.leftRotate(z)

    def insertAVl(self, z):
        self.treeInsert(z)

        atual = z.pai
        while atual is not None:
            pai_aux = atual.pai
            self.treeRebalancing(atual)
            atual = pai_aux

class NodoRB(Nodo):
    def __init__(self, dado, color="RED"):
        super().__init__(dado)
        self.color = color
        self.dado = dado
        self.pai = None
        self.left = None
        self.right = None

class ArvoreRB(ArvoreBinaria):
    def __init__(self):
        super().__init__()
        self.root = None

    def getColor(self, nodo):
        if nodo is None:
            return "BLACK"
        return nodo.color

    def leftRotate(self, x):
        y = x.right
        x.right = y.left

        if y.left is not None:
            y.left.pai = x

        y.pai = x.pai

        if x.pai is None:
            self.root = y
        elif x == x.pai.left:
            x.pai.left = y
        else:
            x.pai.right = y
        y.left = x
        x.pai = y
    

    def rightRotate(self, y):
        x = y.left
        y.left = x.right

        if x.right is not None:
            x.right.pai = y

        x.pai = y.pai

        if y.pai is None:
            self.root = x
        elif y == y.pai.right:
            y.pai.right = x
        else:
            y.pai.left = x

        x.right = y
        x.pai = x

    def RBInsert(self, z):
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
            self.root = z
        elif z.dado < y.dado:
            y.left = z
        else:
            y.right = z

        z.left = None
        z.right = None
        z.color = "RED"
        self.RBInsertFixup(z)

    def RBInsertFixup(self, z):
        while z.pai is not None and z.pai.color == "RED":
            if z.pai.pai is None:
                break

            # tio de Z
            if z.pai == z.pai.pai.left:
                y = z.pai.pai.right

                # Caso 1: tio vermelho
                if self.getColor(y) == "RED":
                    z.pai.color = "BLACK"
                    if y is not None:
                        y.color = "BLACK"
                    z.pai.pai.color = "RED"
                    z = z.pai.pai
                # Caso 2 e caso 3: tio é preto
                else: 
                    
                    if z == z.pai.right:
                        z = z.pai
                        self.leftRotate(z)
                    
                    if z.pai is not None and z.pai.pai is not None:
                        z.pai.color = "BLACK"
                        z.pai.pai.color = "RED"
                        self.rightRotate(z.pai.pai)
            else:
                # tio do lado oposto
                y = z.pai.pai.left
                # Caso 1 
                if self.getColor(y) == "RED":
                    z.pai.color = "BLACK"
                    if y is not None:
                        y.color = "BLACK"
                    z.pai.pai.color = "RED"
                    z = z.pai.pai
                else:
                    # z é filho esquerdo
                    if z == z.pai.left:
                        z = z.pai
                        self.rightRotate(z)

                    if z.pai is not None and z.pai.pai is not None:
                        z.pai.color = "BLACK"
                        z.pai.pai.color = "RED"
                        self.leftRotate(z.pai.pai)

        self.root.color = "BLACK"



if __name__ == '__main__':
    rb = ArvoreRB()

    for v in [10, 20, 30, 15, 25]:
        rb.RBInsert(NodoRB(v))

    print("Raiz:", rb.root.dado, "| Cor:", rb.root.color)          # Esperado: 20 | BLACK
    print("Esquerda:", rb.root.left.dado, "| Cor:", rb.root.left.color)  # Esperado: 10 | BLACK
    print("Direita:", rb.root.right.dado, "| Cor:", rb.root.right.color) # Esperado: 30 | BLACK