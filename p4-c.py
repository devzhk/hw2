from fetcher3 import fetch_links
import matplotlib.pyplot as plt
from collections import Counter, deque
import networkx as nx
import os
os.environ['PYDEVD_WARN_EVALUATION_TIMEOUT'] = '100.0'


def filt_add(links, key, deq, graph=None, source=None):
    '''
    1. Filter out the urls that are not in caltech domain
    2. Add edge for the remaining urls
    '''
    for link in links:
        if key in link:
            deq.append(link)
            if graph and source:
                graph.add_node(link)
                graph.add_edge(link, source)
    return deq


def add_edge(graph, source, links, key):
    for link in links:
        if key in link:
            graph.add_edge(link, source)


if __name__ == '__main__':
    key_word = 'caltech.edu'
    deq = deque(['https://www.caltech.edu/'])

    visited = []
    out_counter = Counter()
    in_counter = Counter()
    max_pages = 300

    G = nx.Graph()

    # build graph with BFS
    while deq:
        source = deq.popleft()
        in_counter[source] += 1
        if source not in visited:
            visited.append(source)
            # add node
            G.add_node(source)
            out_links = fetch_links(source)
            if out_links:
                deq = filt_add(out_links, key_word, deq,
                               graph=G, source=source)
                out_counter[source] = len(out_links)

            if len(visited) % 100 == 0:
                print(f'{len(visited)} pages have been visited.')
        else:
            out_links = fetch_links(source)
            if out_links:
                add_edge(G, source, out_links, key_word)

        if len(visited) > max_pages:
            break
    # compute statistics of the graph
    nx.draw(G, with_labels=False)
    plt.savefig('figs/p4-c300.pdf', bbox_inches='tight')