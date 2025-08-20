# PID Controller with RL Circuit Simulation (in C)

This project demonstrates a **PID controller implemented in C** and a simulation environment in **Python**. The PID controller is used to control an RL (Resistor–Inductor) circuit, making this repository ideal for learning control systems and practical PID usage.

---

## Folder Structure

- `src/`  
  Core C code for the PID controller (`pid.c`, `pid.h`).

- `simulation/utils/`  
  Python utility modules for simulation, including plant models, simulators, tuners, and plotting tools.

- `simulation/demo/`  
  Example scripts and ready-to-run demos for simulating and visualizing the RL circuit with the PID controller.

- `simulation/tests/`  
  Unit and integration tests running in a Github CI.

- `docs/`  
  Documentation and tutorials, including a detailed PID theory and tuning guide.

---

## How It Works

- **PID Controller:**  
  Written in C for performance and clarity. The C code is compiled into a shared library (`.dll` for Windows, `.so` for Linux).

- **Simulation:**  
  All simulation logic, plant modeling, and visualization are handled in Python. The Python code calls the C PID controller via a wrapper (`pid_wrapper.py`).

---

## Getting Started (VS Code)

1. Open the project folder in **Visual Studio Code**.
2. You do **not** need to compile the C code, the required `.dll` (Windows) is already included.
3. Run the demo script from `simulation/demo/` to see the simulation and plots.
   - For example, open a terminal
     ```
     python simulation/demo/sim_plot.py
     ```
---

## Learn More

Want to understand **how PID works** and how to tune it?

[Read the full PID tutorial](docs/PID_TUTORIAL.md)

---

## 📄 License

MIT License