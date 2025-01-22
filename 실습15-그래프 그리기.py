import matplotlib.pyplot as plt

#실습1.

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
# sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

# plt.plot(months, sales_2019, label="2019", color="#17becf")
# plt.plot(months, sales_2020, label="2020", color="#ff7f0e")

# plt.legend(loc="upper left", ncol=1) #범례
# plt.title("Monthly Sales Comparison (2019-2020)")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()

#실습2.

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
data = [20, 35, 15, 27, 45]

plt.bar(categories, data, width=0.7, color="#1f77b4", alpha=0.8, edgecolor="black", linewidth=1.2)
plt.grid(True, axis="both", linestyle="-", color="blue", alpha=0.2)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.tight_layout()
plt.xticks(rotation=45) # x축 이름을 45도 바꾸는 방법
plt.show()



# #실습 3.
sizes = [34.0, 18.0, 16.0, 32.0]
labels = ["Apple", "Grapes", "Melon", "Banana"]
colors = ["#d62728", "#9467bd", "#2ca02c", "#bcbd22"]
explode = [0, 0.1, 0, 0.1]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=10, colors=colors, explode=explode, wedgeprops={"width": 0.7})
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=10, colors=colors, explode=explode, wedgeprops={"width": 0.7, "edgecolor":"black"}) #엣지속에 색넣는 법법
plt.show()
