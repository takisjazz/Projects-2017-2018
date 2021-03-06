####
## graph-visual1.py
## Simple Graph Visualization
####

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import pause
from random import shuffle

graph = {
0: [1,5],
1: [0,2,5,6],
2: [1,4,6],
3: [4,5,6],
4: [2,3,5,6],
5: [0,1,3,4,],
6: [1,2,3,4]
}


## extract nodes from graph
nodes = [node for node in graph]
edges = [graph[node] for node in graph]
# print("Per Node Edges List:",edges)

labels = {}
edge_colors = []

## create networkx graph
G=nx.Graph()
## add nodes
for node in nodes:

    # numOfNeigbors = len(graph[node])
    # print("Neighbors of node",node,":", end=" ")
    # print(edges[node])
    G.add_node(node)
    # Add label to each node
    labels[node] = node

    ## add edges
    for n in edges[node]:
        # print(node,"-->",n)
        G.add_edge(node,n,  edge_color='lightgrey')

## Update edge colors
edge_colors = [e[2]['edge_color'] for e in G.edges(data=True)]

# print(labels)
print(G.nodes())
print(G.edges())
# print(edge_colors)

    #### Print Initial Edge colors
    # for e in G.edges(data=True):
    # print(e, e[2]['edge_color'] )

## positions for all nodes
pos = nx.shell_layout(G)
## nodes
nx.draw_networkx_nodes(G, pos, node_size=400)
## edges
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, edgelist=G.edges(), width=2)
## labels
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')

## show graph
plt.ioff()

plt.axis('off')
plt.title("Simple Graph Visualization")
plt.draw()
pause(2.5)
# plt.show()

########### DFS iteratively ##############
def dfs_iteratively(graph, root):

    global edge_colors, visited, nodes_not_visited

    visited = []
    stack = [root]
    nodes_not_visited = []

    while stack:

        # Pop the LAST item in stack
        node = stack.pop()
        print("Popping Node:", node)

        # node.node_color = '#A0CBE2'
        if node not in visited:
            visited.append(node)
            print("Visited Nodes:",visited)
            print("Neighbors of Node",node,":",list( G.neighbors(node)))

            geitones = list( G.neighbors(node))
            ## Shuffle list of neighbors
#            print("Geitones", geitones)
#            shuffle(geitones)
#            print("Shuffled Geitones", geitones)

#            geitones.reverse()

            # For all Neighbors of the node
            for x in geitones :
                if (x not in visited) and (x not in stack) :
                    # Add NOT visited Neighbors to the stack
                    stack.append(x)
                else:
                    print("From Nodes", list( G.neighbors(node)) ,"Already VISITED:",x)
                    G.add_edge(node,x, edge_color='red')
                ## Update edge colors
                # edge_colors = [e[2]['edge_color'] for e in G.edges(data=True)]
                # for e in G.edges(data=True):
                # print(e, e[2]['edge_color'] )

        print("Stack:",stack)
        ## Get list of nodes not yet visited, to draw in original color
        nodes_not_visited = list(set(nodes).difference(visited))
        # print("Not_Visited yet:",nodes_not_visited)

        ## positions for all nodes
        pos = nx.shell_layout(G)

        ## nodes
        ## if node in visited , draw in othet color :
        nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='green', node_size=700)
        nx.draw_networkx_nodes(G, pos, nodelist=nodes_not_visited,  node_color="red", node_size=400)

        ## edges
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, edgelist=G.edges(data=True), width=2)
        ## labels
        nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')

        ## show graph
        plt.axis('off')
        plt.title("Simple Graph Visualization\n"+"Visiting node:"+str(node) )
        ## Redraw figure with changes

        plt.draw()
        pause(2.5)

    print("Stack is EMPTY. We have visited ALL nodes !")
    return visited
################################################

#----- Main program -------------#
print("DFS iteratively: ",dfs_iteratively(graph,5))

### Print ONLY the DFS path  ###
dfs_path = []
edge_colors = []

G = G.to_directed()

for n in visited:
    if(visited.index(n)+1 < len(visited)):
        # print(n, visited[visited.index(n)+1] )
        dfs_path.append((n, visited[visited.index(n)+1]))
        G.add_edge(n, visited[visited.index(n)+1] , edge_color='red')

# print(dfs_path)
# print(edge_colors)

## positions for all nodes
pos = nx.shell_layout(G)

## nodes
## if node in visited , draw in othet color :
nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='green', node_size=700)


for n in visited:
    if(visited.index(n)+1 < len(visited)):
        # print(n, visited[visited.index(n)+1] )
        dfs_path.append((n, visited[visited.index(n)+1]))
        G.add_edge(n, visited[visited.index(n)+1] , edge_color='red')
        edge_colors.append('red')
        edge_colors.append('red')

#print(edge_colors)
## edges
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, edgelist=dfs_path, arrows='True', width=2, style='dashed')
## labels
nx.draw_networkx_labels(G, pos, font_size=16, font_color='white', font_family='sans-serif' )

## show graph
plt.axis('off')
t = str(visited)
plt.title("FINAL DFS PATH : "+t[1:-1])
plt.draw()
plt.show()