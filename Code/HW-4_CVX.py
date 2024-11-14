import cvxpy as cp

# Define variables
x = cp.Variable(nonneg=True)
y = cp.Variable(nonneg=True)
z = cp.Variable()
u = cp.Variable(nonneg=True)
v = cp.Variable(nonneg=True)
t = cp.Variable(nonneg=True)
w = cp.Variable(nonneg=True)

# Define constraints
constraints = []

# Constraint (a): 1/x + 1/y <= 1
# Reformulate using u = 1/x and v = 1/y
# constraints_a += [
#     u + v <= 1,
#     cp.inv_pos(x) <= u,
#     cp.inv_pos(y) <= v
# ]

# # Constraint (b): xy >= 1
# # Reformulate using t = 1/(xy)
constraints_b = [
    x + y >= 2
]

# Relaxation: (x + y)^2 <= z * (x - y + 5) is non-convex
# Instead, use a simpler convex constraint for testing
# constraints_c = [
#     x + y <= x - y + 5  
# ]

# Relaxation: x + y <= 1 is a simple convex constraint
# given is nonconvex
# constraints_d = [
#     x + y <= 1  
# ]

# Define a dummy objective function
objective = cp.Minimize(x + y)

# Formulate the problem
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Print the results
print(f"x: {x.value}, y: {y.value}")