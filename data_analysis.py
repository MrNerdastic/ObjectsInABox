f = open("csv_test_1.csv", "r")

full_lines = []
lines = []
frequency = []
fft = []

while line := f.readline():
    full_lines.append(line.rstrip())

for y in range(len(full_lines)):
    lines.append(full_lines[y].split(";"))

lines.pop(0)
for x in range(len(lines)):
    frequency.append(lines[x][1])
    fft.append(lines[x][3])

print(frequency)
print(fft)

import matplotlib.pyplot as plt



# Create a plot
plt.plot(frequency, fft)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Display the plot
plt.show()
