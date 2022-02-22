'''
Program written by Yasharth Yadav (yasharthby@gmail.com)
Python script to generate the poset complex induced by a hypergraph.

Input files:-
arg1 -> nodelist of hypergraph
arg2 -> hyperedges of the hypergraph

Output files:-
arg3 -> each line contains the ID of a node in the poset complex
arg4 -> 1-skeleton of the poset complex (in adjacency list format)
arg5 -> 2-skeleton of the poset complex (in edgelist format)
arg6 -> cardinalities of nodes
arg7 -> triangular faces in the 2-skeleton
'''

import time
import sys
start = time.time()

output1 = open(sys.argv[3],'w')
output2 = open(sys.argv[4],'w')
output3 = open(sys.argv[5],'w')
output4 = open(sys.argv[6],'w')
output5 = open(sys.argv[7],'w')


#create dictionaries of new nodes (old hyperedges) and their cardinalities, each node indexed by whole numbers
print(sys.argv[2])
print('%fs\tReading hyperedge files'%(0))
nodes = {}
k_values = {}
with open(sys.argv[1],'r') as f:
  count = 0
  for line in f:
    nodes[count] = {int(line.strip())}
    k_values[count] = 1
    output1.write(str(count)+'\n')
    output4.write(str(k_values[count])+'\n')
    count+=1
with open(sys.argv[2],'r') as f:
  for line in f:
    nodes[count] = set(map(int,line.split()))
    k_values[count] = len(nodes[count])
    output1.write(str(count)+'\n')
    output4.write(str(k_values[count])+'\n')
    count+=1

print('%fs\tGenerating poset complex'%(time.time()-start))
'''
partition the hyperedges based on their cardinality
hyperedges[k] = set of hyperedges with cardinality k
'''
k_max = max(k_values.values())
hyperedges = {k:[i for i,j in k_values.items() if j == k] for k in range(1,k_max+1)}

'''
For a hyperedge assigned an index i
parent[i] --> set of direct parents of i
initialize to empyt sets and update throughout the process of finding the poset
'''
parent = [set()  for i in nodes]
print('%fs\tSize of parent list: %dbytes'%(time.time()-start,sys.getsizeof(parent)))

'''
Compute the poset:
Start with highest cardinality hyperedges and compare with all lower cardinality hyperedges
Let A = set of parents of i
  B = set of parents if j
If j is a subset of i,
  1) add i to B
  2) B <- B-A
'''
for k in range(k_max,1,-1):
  for i in hyperedges[k]:
    for d in range(1,k):
      temp = [j for j in hyperedges[k-d] if nodes[j].issubset(nodes[i])]
      for j in temp:
        parent[j].add(i)
        parent[j]=parent[j].difference(parent[i])

print('%fs\tPoset generated. Writing to output files'%(time.time()-start))
#print to output2, output3 and output5
for i,val in enumerate(parent):
  output2.write(str(i)+'\t')
  new_edges = set()
  faces = set()
  for j in val:
    output2.write(str(j)+'\t')
    output3.write(str(i)+'\t'+str(j)+'\n')
    for k in parent[j]:
        new_edges.add((i,k))
        faces.add((i,j,k))
  for item in new_edges: output3.write(str(item[0])+'\t'+str(item[1])+'\n')
  for item in faces: output5.write(str(item[0])+'\t'+str(item[1])+ '\t' + str(item[2])+'\n')
  output2.write('\n')

output1.close()
output2.close()
output3.close()
output4.close()
output5.close()

end = time.time()
print('%fs\tDone'%(end-start))
print('=======================================================')
