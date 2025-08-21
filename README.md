# PID Controller with RL Circuit Simulation (C + Python)

Welcome! This project demonstrates how to use a **PID controller written in C** to control an RL (Resistor–Inductor) circuit, with all simulation and visualization handled in **Python**.  

> **Note:** The included demo uses a **PI controller** (derivative gain= 0), which is a simplified version of PID and commonly used in industry.

---

## Folder Structure

- `source/`  
  Core C code for the PID controller (`pid.c`, `pid.h`).

- `simulation/utils/`  
  Python utility modules for simulation, including plant models, simulators, tuners, and plotting tools.

- `simulation/demo/`  
  Example scripts and ready-to-run demos for simulating and visualizing the RL circuit with the PI controller.

- `simulation/tests/`  
  Unit and integration tests running in a Github CI.

- `docs/`  
  Documentation and tutorials, including a detailed PID theory and tuning guide.

---

## How It Works

- **PID Controller:**  
  Written in C for embedded compatibility. The C code is compiled into a shared library (`.dll` for Windows, `.so` for Linux).  
  The demo uses only the **P** and **I** terms (PI controller).

- **Simulation:**  
  All simulation logic, plant modeling, and visualization are handled in Python. The Python code calls the C PI controller via a wrapper (`pid_wrapper.py`).

---

## Example Output

Below is a typical result from running the demo.  
The PI controller regulates the current in the RL circuit to reach the setpoint:

![RL Circuit PI Control Demo](docs/image.png)

- **Top:** Current response (orange) tracks the setpoint (blue dashed).
- **Bottom:** Voltage applied by the controller.

---

## Getting Started (VS Code)

1. Open the project folder in **Visual Studio Code**.
2. You do **not** need to compile the C code—the required `.dll` (Windows) is already included.
3. Run the demo script from `simulation/demo/` to see the simulation and plots:
   ```sh
   python simulation/demo/sim_plot.py

(detailed dll generation explaination follows).


## Learn More

Want to understand **how PID works** and how to tune it?

[Read the full PID tutorial](docs/PID_TUTORIAL.md)

---

## 📄 License

MIT License