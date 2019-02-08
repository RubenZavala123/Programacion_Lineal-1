from pulp import *
x = LpVariable("x",0,3)
y = LpVariable("y",0,1)
prob = LpProblem("Problema1",LpMinimize)
prob += x + y <= 2
prob += -4*x + y
status = prob.solve()
value(x),value(y)
print(value(prob.objective))
print(value(x),value(y))
