
class vertice:
    def __init__(self,nombre,s_indice):
        self.nombre=nombre
        self.indice=indice 

class grafo:
    def __init__(self):
        self.vertices= []
        self.matrizadyacente = []

    def añadir_vertice(self,vertice):
        self.vertice.append(vertice)
        self.matrizadyacente.append([0]*len(self.vertices))

    def añadir_eje (self,u,v,peso):
        self.matrizadyacente[u][v] = peso
        self.matrizadyacente[v][u] = peso

    def max_extension(self,s_indice):
        pass

    def maxepisodios (self):
        pass
    def n_episodios(self,n):
        pass

    def max_extension(self,s_indice): 
        h= [(0,s_indice)]
        vi = set()
        arbol =[]

        while h: 
            peso, u = heapq.heappop(heap)
            if u is in vi: 
                continue
            
            vi.add(u)
            arbol.append(self.vertices[u])

            for v in range(len(self.vertices)):
                if self.matrizadyacente[v][u] > 0 and v not in visited:
                    heapq.heappush(heap, (self.adjacency_matrix[u][v], v))
        return tree

    def vermax_episodios(self):
        maxepisodios = 0 



