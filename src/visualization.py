from graphviz import Digraph
from collections import defaultdict


class DAG:
    def __init__(self, root):
        self.root = root

    def trace(self):
        nodes, edges = set(), set()

        def build(v):
            if v not in nodes:
                nodes.add(v)
                for child in v._prev:
                    edges.add((child, v))
                    build(child)

        build(self.root)
        return nodes, edges

    def draw_dot(self, ext='svg', rankdir='LR'):
        """
        ext: png | svg | ...
        rankdir: TB (top to bottom graph) | LR (left to right)
        """

        assert rankdir in ['LR', 'TB']
        nodes, edges = self.trace()
        dot = Digraph(format=ext, graph_attr={'rankdir': rankdir})

        # Define colors for specific labels
        label_colors = defaultdict(lambda: 'white')
        label_colors[str(self.root.label)] = 'beige'

        for n in nodes:
            node_label = "%s \n| {data: %.2f } | {grad: %.2f}" % (n.label, n.data, n.grad)
            node_color = label_colors.get(n.label, label_colors[n.label])
            node_shape = 'record'
            dot.node(name=str(id(n)), label=node_label, shape=node_shape, style='filled', fillcolor=node_color)

            if n._op:
                dot.node(name=str(id(n)) + n._op, label=n._op, style='filled', fillcolor='aliceblue')
                dot.edge(str(id(n)) + n._op, str(id(n)))

        for n1, n2 in edges:
            dot.edge(str(id(n1)), str(id(n2)) + n2._op)

        return dot


def line_plot(
        ax,
        xs, ys,
        linecolor='b', linestyle='-', linewidth=0.9,
        marker='h', markerfacecolor='red', markersize=5, markeredgecolor='k', markeredgewidth=.5,
        gridlinecolor='grey', gridlinestyle='--', gridlinewidth=0.5,
        facecolor='white',
        invertx=False, inverty=False
):
    ax.plot(xs, ys,
            color=linecolor,
            linestyle=linestyle,
            linewidth=linewidth,
            marker=marker,
            markerfacecolor=markerfacecolor,
            markersize=markersize,
            markeredgecolor=markeredgecolor,
            markeredgewidth=markeredgewidth
            )

    ax.grid(color=gridlinecolor, linestyle=gridlinestyle, linewidth=gridlinewidth)

    if invertx:
        ax.invert_xaxis()

    if inverty:
        ax.invert_yaxis()

    ax.set_facecolor(facecolor)
    ax.tick_params(axis="both", which="both", direction="in")
