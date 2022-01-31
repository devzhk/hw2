#%%
import networkx as nx
import matplotlib.pyplot as plt

#%%
G = nx.binomial_graph(n=30, p=0.2)
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig('figs/p4-a.pdf', bbox_inches='tight')
# %%
sizes = [10, 10, 10]
probs = [[0.7, 0.1, 0.1], 
         [0.1, 0.7, 0.1], 
         [0.1, 0.1, 0.7]]
G = nx.stochastic_block_model(sizes, probs)
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig('figs/p4-b.pdf', bbox_inches='tight')
# %%
