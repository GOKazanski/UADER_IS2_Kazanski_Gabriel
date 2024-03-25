import matplotlib.pyplot as plt

def collatz(num):
	sequence_list = [num]

	while num != 1:
		if num % 2 == 0:
			num = num // 2
		else:
			num = 3 * num + 1
		sequence_list.append(num)

	return sequence_list

x_values = []
y_values = []
for num in range(1, 10001):
    sequence_list = collatz(num)
    x_values.append(num)
    y_values.append(len(sequence_list))

plt.scatter(x_values, y_values, s=4)
plt.show()