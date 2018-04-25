import pygraphviz as pgv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def make_search_tree(tree, graph, parent):
    """
    Make tree content inorder
    """
    if tree.left:
        graph = make_search_tree(tree.left, graph, tree)
    if (parent != None):
        graph.add_node(str(tree.key),color='blue')
        graph.add_edge(str(parent.key), str(tree.key))
    if tree.right:
        graph = make_search_tree(tree.right, graph, tree)
    return graph

def draw_search_tree(tree, directed=True, file_name='graph'):
    graph = pgv.AGraph(directed=True)
    graph.add_node(str(tree.key),color='red')
    graph = make_search_tree(tree, graph, None)
    graph.write('images/test.dot')
    
    graph.layout(prog='dot') # use dot
    graph.draw('images/' + file_name + '.png')
    img=mpimg.imread('images/' + file_name + '.png')
    plt.imshow(img)
    
def make_tree(tree, graph, parent):
    """
    Make tree content inorder
    """
    if tree.left:
        graph = make_tree(tree.left, graph, tree)
    if (parent != None):
        graph.add_node(str(tree.id))
        graph.add_edge(str(parent.id), str(tree.id))
    if tree.right:
        graph = make_tree(tree.right, graph, tree)
    return graph

def draw_tree(tree, directed=True, file_name='graph'):
    graph = pgv.AGraph(directed=True)
    graph.add_node(str(tree.id))
    graph = make_tree(tree, graph, None)
    graph.write('images/test.dot')
    
    graph.layout(prog='dot') # use dot
    graph.draw('images/' + file_name + '.png')
    img=mpimg.imread('images/' + file_name + '.png')
    plt.imshow(img)
    
def draw_graph(graph, directed=True, file_name='graph'):
    draw_graph = pgv.AGraph(directed=directed)
    for v in range(1, graph.length()):
        draw_graph.add_node(str(v))
        for u in graph.getEdges(v):
            draw_graph.add_edge(str(v), str(u))

    draw_graph.write('images/test.dot')
    
    draw_graph.layout(prog='dot') # use dot
    draw_graph.draw('images/' + file_name + '.png')
    img=mpimg.imread('images/' + file_name + '.png')
    plt.figure(figsize=(6, 6))
    plt.imshow(img)