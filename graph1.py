import networkx as nx
from multiprocessing import Process
import matplotlib.pyplot as plt
import time
graph=[]
labels=[]
def parse(filename):
	f=open("MacHost.txt","r");
	mac={};
	for line in f.readlines():
		p=line.split(" ")
		mac[p[0]]=p[1]
	f.close()
		
	f=open(filename,"r")
	for lines in f.readlines():
		p=lines.split()
		tup=p[0],p[1]+"\n"+str(mac[p[1]])
		graph.append(tup)
		labels.append(p[2])




def draw_graph(graph_layout='shell',
               node_size=8000,node_alpha=0.3,
               node_text_size=10,node_color='blue',
               edge_color='green', edge_alpha=0.8, edge_tickness=2,
               edge_text_pos=0.3,
               text_font='sans-serif'):
    global graph
    global labels	
    #print graph
    #print labels
    # create networkx graph
    
    G=nx.Graph()
    G2=nx.Graph()
    edge_color2='red'

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    graph_pos=nx.shell_layout(G)
    pos=nx.shell_layout(G2)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
		                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
			                               alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
			                                font_family=text_font)
    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    #print "edge ",edge_text_pos;
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=0.8)

    # show graph
    plt.axis('off')
    plt.show(block=False)
    time.sleep(15)
    plt.close()



# you may name your edge labels
#while(1):
graph=[]
labels=[]
time.sleep(15)
#parse("inp.txt")
#draw_graph()

# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
#draw_graph(graph,labels,graph2)
