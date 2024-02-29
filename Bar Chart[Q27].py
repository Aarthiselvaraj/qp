import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(x, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Set tick positions to a range of integers corresponding to the indices of the x list
plt.xticks(range(len(x)), x)

plt.tight_layout()
plt.show()
