problem=problem()
numpieces=8
cols=range(numpieces)
rows=range(numpieces)
problem.addVariables(cols,row)
for col1 in cols:
for col2 in cols:
if col1<col2:
problem.addConstraint(lambda row1,row2!=row2,(col1,col2))
solutions=problem.getSolutions()
