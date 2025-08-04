# PID Controller with RL Circuit Simulation (in C)

This project implements a simple but effective **PID controller in C**, applied to an RL (Resistor–Inductor) circuit simulation. It’s ideal for learning how control systems behave and how PID works in practice.

---

## How to Run the Simulation (VS Code)

This project is preconfigured for **Visual Studio Code** with a `Run Task` option.

### Steps

1. Open the folder in **VS Code**.
2. Press `Ctrl+Shift+P` and choose **Run Task**.
3. Select `build pid sim`.
4. Select `run pid sim and export CSV`.
5. Run Python script in tools/ folder and watch the simulated graph.


---

## What’s Inside

- `source/pid.c` / `pid.h`: Core PID implementation
- `examples/`: Example simulation setup (e.g., RL circuit)
- `.vscode/tasks.json`: Predefined task to compile and run
- `docs/PID_TUTORIAL.md`: Full tutorial on PID theory, tuning, and application

---

## Learn More

Want to understand **how PID works** and how to tune it?

[Read the full PID tutorial](docs/PID_TUTORIAL.md)

---

## 📄 License

MIT License