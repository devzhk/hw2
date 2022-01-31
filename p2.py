#%%
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#%%
raw = np.loadtxt('gr_qc_coauthorships.txt', delimiter=' ')
edges = raw.astype(int)
# %%
G = nx.Graph()
G.add_edges_from(edges)
# %%
hist = nx.degree_histogram(G)
degrees = list(range(len(hist)))
# %%
plt.plot(degrees, hist)
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('Degree', fontsize=15)
plt.savefig('figs/p2-hist.pdf', bbox_inches='tight', dpi=200)
plt.show()
# %%
cum_sum = np.cumsum(hist)
ccdf = 1 - cum_sum / cum_sum[-1]
# %%
plt.plot(degrees, ccdf)
plt.ylabel('Probability', fontsize=15)
plt.xlabel('Degree', fontsize=15)
plt.savefig('figs/p2-ccdf.pdf', bbox_inches='tight', dpi=200)
plt.show()
# %%
T_dict = nx.triangles(G)
T = sum([value for key, value in T_dict.items()])
print(f'Number of triangles is {T / 3}')
# %%
avg_cluster = nx.average_clustering(G)
overall_cluster = nx.transitivity(G)
print(
    f'Average clustering coefficient: {avg_cluster}; \nOverall clustering coefficient: {overall_cluster}')

max_diameter = nx.diameter(G)
avg_dimater = nx.average_shortest_path_length(G)
print(
    f'Max diameter: {max_diameter}; Average diameter: {avg_dimater}')

# %%
