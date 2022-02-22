'''
Program written by Yasharth Yadav (yasharthby@gmail.com)
Python script to compute the Forman-Ricci curvatures, scalar curvatures and the Euler characteristic of a poset complex induced by a hypergraph.

INPUTS:
argv1 -> List of nodes in the poset complex
argv2 -> List of edges in the poset complex
argv3 -> List of triangles in the poset complex

OUTPUTS:
argv4 -> Euler chaarcteristic appended to a text file
argv5 -> Ricci curvature of edges
argv6 -> Scalar curvature of nodes computed using edge Ricci curvatures

argv7 -> filename of the hypergraph
'''

import networkx as nx
import itertools as it
import sys

G = nx.Graph()
#Create a node and edge weighted graph using list of nodes and edges.
#The weights represent the number of traingles in which the edge/node belongs. Initialize all weights to 0
with open(sys.argv[1]) as f:
  for line in f:
    G.add_node(int(line.strip()), triangles = 0)
with open(sys.argv[2]) as f:
  for line in f:
    temp = line.strip().split()
    G.add_edge(int(temp[0]),int(temp[1]),triangles = 0)

#read triangles and update node and edge weights
with open(sys.argv[3]) as f:
  count = 0
  for line in f:
    temp = list(map(int,line.strip().split()))
    for i in temp:
      G.nodes[i]['triangles'] = G.nodes[i]['triangles'] + 1
    for i,j in it.combinations(temp,2):
      G.edges[i,j]['triangles'] = G.edges[i,j]['triangles'] + 1
    count+=1

#Compute Euler characteristic
EulerX = G.number_of_nodes() - G.number_of_edges() + count
output1 = open(sys.argv[4],'a')
output1.write(str(sys.argv[7])+'\t'+ str(EulerX) +'\n')
output1.close()

#Compute Ricci curvatures and write to output
output2 = open(sys.argv[5],'w')
for u,v in G.edges():
  temp = 4 - G.degree(u) - G.degree(v) + 3*G.edges[u,v]['triangles']
  G.edges[u,v]['RicE'] = temp
  output2.write(str(u) + '\t' + str(v) + '\t' + str(temp) + '\n')
output2.close()

#Compute node curvatures and write to output
output3 = open(sys.argv[6],'w')
for i in [node for node in G.nodes() if G.degree(node)>0]:
  scalar_curvature = 0
  for u,v in G.edges(i):
    scalar_curvature = scalar_curvature + G.edges[u,v]['RicE']
  output3.write(str(i) + '\t' + str(scalar_curvature) + '\t' +str(scalar_curvature/G.degree(i)) +'\n')
output3.close()
