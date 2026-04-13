import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
salary = [30000, 35000, 40000, 50000, 60000, 65000, 70000, 80000, 90000, 100000]

plt.figure(figsize=(8, 5))
plt.scatter(experience, salary)

plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()