# Decision Tree
from sklearn.tree import DecisionTreeClassifier
X, y = [[0], [1], [2]], [0, 1, 1]
model = DecisionTreeClassifier().fit(X, y)
print("Decision Tree Trained")
