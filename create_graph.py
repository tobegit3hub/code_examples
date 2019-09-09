import dgl

g = dgl.DGLGraph()
g.add_nodes(10)
for i in range(1, 4):
        g.add_edge(i, 0)
        src = list(range(5, 8)); dst = [0]*3
        g.add_edges(src, dst)
