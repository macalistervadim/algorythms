import pulp

model = pulp.LpProblem("Profit.maximising problem", pulp.LpMaximize)
A = pulp.LpVariable("A", lowBound=0, cat="Integer")
B = pulp.LpVariable("B", lowBound=0, cat="Integer")

model += 5000 * A + 2500 * B, "Profit"

model += 3 * A + 2 * B <= 20 
model += 4 * A + 3 * B <= 30
model += 4 * A + 3 * B <= 44

model.solve()
pulp.LpStatus[model.status]

print(A.varValue)
print(B.varValue)
print(pulp.value(model.objective))