from igraph import Graph

g = Graph(directed=True)

tgraph=Graph(xtitle="x",ytitle="f(x)")
fx=gcurve(color=color.blue)

x=0
dx=0.01

while x<5:
    fx.plot(x,f(x))
    x=x+dx