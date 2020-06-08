from arborescences import *
from routing import *

#graph sehen
g = init_k_graph(10,11)
print(g.nodes())
print(g.edges())

#als bild polen
nx.draw(g)
plt.savefig("simple_path.png")
plt.show()