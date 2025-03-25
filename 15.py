# Vacuum Cleaner Problem
environment = [[1, 0], [0, 1]]
for i in range(2):
    for j in range(2):
        if environment[i][j] == 1:
            environment[i][j] = 0
print("Cleaned environment:", environment)
