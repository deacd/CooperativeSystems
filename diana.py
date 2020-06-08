import networkx
from routing import *
import arborescences
import objective_function_experiments
import infocom2019_experiments
import srds2019_experiments
import dsn2019_experiments


"""----------------------------------------------------------------------------------------Section1
#gweichtete Kanten u. shortest path mit Dijkstra

G = networkx.Graph()
G.add_edge('A','B', weight=2 )
G.add_edge('B','D', weight=4 )
G.add_edge('A','C', weight=3 )
G.add_edge('C','D', weight=1 )

print(G.nodes())
print(G.edges())

print(networkx.shortest_path(G,'A','D', weight='weight', method="dijkstra"))

networkx.draw(G)
plt.savefig("simple_path.png")
plt.show()
"""

"""--------------------------------------------------------------------------------------Section2
#erzeugt in diesem fall 3 .png

graph1 = arborescences.init_k_graph(2, 7)
arborescences.drawArborescences(graph1, "weighted_graph.png")
"""

"""--------------------------------------------------------------------------------------Section3
#write graph 0 with default paramenters (see objective_function_experiments.py)
#to run it, you have to create a simple file in the projekt, as it is explained in the write_graph method: example experiment-objective-function1_graph_10_0.txt
       
objective_function_experiments.write_graphs()
objective_function_experiments.rep +=1
"""

"""----------------------------------------------------------------------------------------Section4
#write graph 1 with default paramenters (see objective_function_experiments.py)
#to run it, you have to create a simple file in the projekt, as it is explained in the write_graph method: example experiment-objective-function1_graph_10_1.txt
          
graph1 = arborescences.init_k_graph(2, 7)
objective_function_experiments.write_graphs()
graph1 = objective_function_experiments.read_graph(1)


#given graph1 returns a list of its arborescences
arboList = arborescences.get_arborescence_list(graph1)
print(arboList)

#.is_arvorescence_decomposition - i took this test from Robert
if (arborescences.is_arborescence_decomposition(graph1)):
    print("Graph1 is decomposed acyclicly")
else:
    print("Graph1 is not decomposed acyclicly")
"""

"""----------------------------------------------------------------------------------------Section5
#examplic run of an experiment - Robert

dsn2019_experiments.run_regular(2, 20, 10)

#if connectivity k>2, failure scenarios in results folder
dsn2019_experiments.run_regular(3, 20, 10)
"""












