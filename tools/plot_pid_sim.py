import matplotlib.pyplot as plt
import csv

# Storage for simulation data
time = []
setpoint = []
current = []
voltage = []

# Read the CSV file
with open('output.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        t, sp, i, v = map(float, row)
        time.append(t)
        setpoint.append(sp)
        current.append(i)
        voltage.append(v)

# Create plots
plt.figure(figsize=(10, 6))

# Plot current vs. setpoint
plt.subplot(2, 1, 1)
plt.plot(time, setpoint, label="Setpoint", linestyle='--')
plt.plot(time, current, label="Current (plant output)")
plt.ylabel("Current [A]")
plt.title("PID Response - RL Circuit")
plt.legend()
plt.grid(True)

# Plot control signal
plt.subplot(2, 1, 2)
plt.plot(time, voltage, label="Control Signal (Voltage)", color="orange")
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
