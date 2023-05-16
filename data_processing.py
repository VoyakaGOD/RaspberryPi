import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np

with open("settings.txt", "r") as file:
    settings = [float(x) for x in file.read().split("\n")]
    dt = 1/settings[0]
    q = settings[1]

with open("data.txt") as file:
    values = np.array([float(x) for x in file.read().split("\n")])

times = np.arange(values.size) * dt

charge_time = values.argmax() * dt

fig, axis = plt.subplots(figsize=[12, 6])
axis.plot(times, values, "-", color="#008B8B", marker="^", markevery=250, markersize=10)
axis.legend(["V(t)"])
axis.xaxis.set_major_locator(ticker.MultipleLocator(20))
axis.xaxis.set_minor_locator(ticker.MultipleLocator(4))
axis.yaxis.set_major_locator(ticker.MultipleLocator(1))
axis.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))
axis.grid(True, linestyle='-', which="major", color="black")
axis.grid(True, linestyle='--', which="minor", color="grey")
axis.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")
axis.set_xlabel("Время, c")
axis.set_ylabel("Напряжение, B")
axis.text(70, 2.5, "Время заряда = " + str(charge_time.round(2)) + "c", color="#008B8B")
axis.text(70, 2, "Время разряда = " + str((times[-1] - charge_time).round(2)) + "c", color="#008B8B")

plt.savefig("plot.svg", format="svg")
plt.show()