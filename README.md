# PID Controller with RL Circuit Simulation (C + Python)

Welcome! This project demonstrates how to use a **PID controller written in C** to control an RL (Resistor–Inductor) circuit, with all simulation and visualization handled in **Python**.  

> **Note:** The included demo uses a **PI controller** (derivative gain= 0), which is a simplified version of PID and commonly used in industry.

---

## Folder Structure

- `demos/`  
  Demonstration of PID working in combination with RL Circuit and DCMotor.

- `docs/`  
  Documentation and tutorials, including a detailed PID theory and tuning guide.

- `embedded/`  
  C code for the PID controller (`pid.c`, `pid.h`).

- `pid/`  
  Python code for the PID controller (`pid.py`).

- `simulation/plants/`  
  Python code for the plant models from the demo.

- `simulation/`  
  Python framework for simulating and plotting the control system.

- `tests/`  
  Unit and integration tests running in a Github CI.



---

## How It Works

- **PID Controller:**  
  Written in C for embedded compatibility or in python for ready to use simulation.  
  The demos are using different configurations of the controller (PI, PID).

- **Simulation:**  
  All simulation logic, plant modeling, and visualization are handled in Python.

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
2. Run one of the demo scripts to see the simulation and plots.


## Learn More

Want to understand **how PID works** and how to tune it?

[Read the full PID tutorial](docs/PID_TUTORIAL.md)

---

## License

MIT License

## Support
If you like this project, consider supporting me on Ko-fi:
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/summit00)