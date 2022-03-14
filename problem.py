class Hamiltonian:
  def __init__(self, start):
    #start (& end) city
    self.start = start

    #list to store the route path
    self.route = []

    #varibale to mark if graph has the route
    self.hasroute = False

  #method to inititate the search of route
  def findRoute(self):
    # add starting city to the list
    self.route.append(self.start)

    #start the search of the hamiltonian cycle of city
    self.solve(self.start)

  #recursive function to implement backtracking
  def solve(self, city):
    #Base condition: if the city is the start city
    #and all nodes have been visited (start city twice)
    if city == self.start and len(self.route) == N+1:
      self.hasroute = True

      #output the route
      self.displayRoute()

      #return to explore more route
      return

    #iterate through the neighbor cities
    for i in range(len(cities)):
      if adjacencyM[city][i] != 0 and visited[i] == 0:
        nbr = i
        #visit and add city to the route
        visited[nbr] = adjacencyM[city][i]
        self.route.append(nbr)

        #traverse the neighbor city to find the route
        self.solve(nbr)

        #Backtrack
        visited[nbr] = 0
        self.route.pop()

  #function to display the hamiltonian class
  def displayRoute(self):
    names = []
    dis = []  
    for v in self.route:
      names.append(cities[v])
      dis.append(visited[v])
    print('path :',names ,'total Distance:',sum(dis))

    

if __name__ == '__main__':
  cities =     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T']
  adjacencyM = [[0, 1063, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 2656, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1352, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1841, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 61, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1634, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 285, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 380, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2547, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2524, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6999, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 105, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 244, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 502],
                [30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  #list mapping of cities  to mark city visited
  visited = [0 for x in range(len(cities))]

  #number of cities  in the graph
  N = 20
  
  #Driver code
  hamiltonian = Hamiltonian(0)
  hamiltonian.findRoute()

  #if the graph doesn't have any Hamiltonian Cycle of city
  if not hamiltonian.hasroute:
    print("No Hamiltonian Cycle of city")