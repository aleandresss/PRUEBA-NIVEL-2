class Node:
    def __init__ (self,valor)
    self.valor = valor 
    self.izq = None
    self.der = None 

    def insert(self,valor)
    #izquierda (valores mas pequeños)
    if val < self.valor:        
            if self.izq is None:
                self.izq = Node(valor)
            else:
                self.izq.insert(valor)
    #derecha (valores mas mayores)
        else:
            if self.der is None:
                self.der = Node(valor)
            else:
                self.der.insert(valor)

#determinar si un número está cargado en el árbol o no;

    def arbol(numeros):
    raiz = Node(numeros[0])
    for i in range(1, len(numeros)): #1000
        raiz.insert(numbers[i])
    return raiz

#preorden --- raíz, subárbol izquierdo, subárbol derecho.
def preorder_traversal(node):
    if node is None:
        return []
    traversal = [valor_node]
    traversal += preorder_traversal(node.izq)
    traversal += preorder_traversal(node.der)
    return traversal

#inorden ---- subárbol izquierdo,raíz ,subárbol derecho.
def inorder_traversal(node):
    if node is None:
        return []
    traversal = inorder_traversal(node.izq)
    traversal += [valor_node]
    traversal += inorder_traversal(node.der)
    return traversal

#postorden ---- subárbol izquierdo, subárbol derecho, raiz
def postorder_traversal(node):
    if node is None:
        return []
    traversal = postorder_traversal(node.izq)
    traversal += postorder_traversal(node.der)
    traversal += [valor_node]
    return traversal

#nivel
from collections import deque

def nivel_traversal(node):
    if node is None:
        return []
    traversal = []
    queue = deque([node])
    while queue:
        curr_node = queue.popleft()
        traversal.append(curr_valor_node)
        if curr_node.izq:
            queue.append(curr_node.izq)
        if curr_node.der:
            queue.append(curr_node.der)
    return traversal

#eliminar tres valores del árbol;
def delete (node, valor):
    if node is None
    return None
    if valor < valor_node
        node.izq = delete(node.izq,valor)
    elif valor > valor_node
         node.der = delete(node.der,valor)
    elif valor == valor_node
        if node.izq is None:
            return node.der
        elif node.der is None:
            return node.izq


#determinar si un número está cargado en el árbol o no;
def search(node,valor):
    if node is None: 
    return false

# determinar la altura del subárbol izquierdo y del subárbol derecho;
#La altura de un subárbol es la altura máxima de sus nodos hoja.
def altura_arbol(node):
  if node is None:
    return 0
  return 1 + max(altura(node.izq), altura(node.der))

def altura_izq(node):
  if node is None or node.izq is None:
    return 0
  return 1 + altura(node.izq)

def altura_der (node):
  if node is None or node.der is None:
    return 0
  return 1 + altura(node.der)

# contar cuántos números pares e impares hay en el árbol.
def pares_impares(arbol):
  if arbol is None:
    return 0, 0
  
  pares_izq, impares_izq = contar_pares_impares(arbol.izq)
  pares_derecha, impares_derecha = contar_pares_impares(arbol.der)
  
  if valor_node % 2 == 0:
    pares = pares_izquierda + pares_derecha + 1
    impares = impares_izquierda + impares_derecha
  else:
    pares = pares_izq + pares_der
    impares = impares_izq + impares_der+ 1
  
  return pares, impares

