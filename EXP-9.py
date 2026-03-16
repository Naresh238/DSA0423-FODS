import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr']
sales = [200,300,250,400]

plt.plot(months,sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
