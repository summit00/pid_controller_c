# 🧠 PID Controller in C

This project provides a clean, reusable implementation of a **PID controller in C**, designed for embedded systems and simulation. It also includes an educational explanation of how PID control works, how it's implemented, and how to tune it.

---

## What is a PID Controller?

A **PID controller** is a feedback mechanism that minimizes the error between a desired setpoint and a measured variable by adjusting a control input.

### Continuous-Time Formula:

\[
u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)d\tau + K_d \cdot \frac{de(t)}{dt}
\]

Where:
- `e(t)` = setpoint - measurement
- `Kp` = proportional gain
- `Ki` = integral gain
- `Kd` = derivative gain

---

## Discrete Implementation for Code

With fixed timestep `dt`:

- Error: \( e[k] = r[k] - y[k] \)
- Integral: \( I[k] = I[k-1] + e[k] \cdot dt \)
- Derivative: \( D[k] = \frac{e[k] - e[k-1]}{dt} \)

```c
error = setpoint - measurement;
integral += error * dt;
derivative = (error - prev_error) / dt;
output = kp * error + ki * integral + kd * derivative;
```

---

## 🔧 Code Mapping

| Term       | Code Variable            |
|------------|--------------------------|
| `e[k]`     | `error`                  |
| `I[k]`     | `pid->integral`          |
| `D[k]`     | `(error - prev_error)/dt`|
| `u[k]`     | `output`                 |

---

## Project Structure

- `src/` — PID library (`pid.c`, `pid.h`)
- `examples/` — RL simulation example (`rl_simulation.c`)
- `tools/` — Python plotting (`plot_pid_sim.py`)

---

## RL Plant Model

This project simulates an RL circuit as the controlled plant:

```
V = L * di/dt + R * i
```

Discretized:

```
i[t+1] = i[t] + (dt / L) * (V - R * i[t])
```

The PID controller adjusts voltage `V` to make the current `i` track the setpoint.

---

## Tuning Tips

- **Start with Kp only** — increase until response is reasonably fast but not oscillating
- Add **Ki** to remove steady-state error
- Add **Kd** to reduce overshoot and oscillations
- Use step responses to fine-tune

---

## Common Pitfalls

- **Integral windup**: prevent integral from growing too large when output is saturated
- **Noisy derivative**: avoid using raw sensor data; apply filtering or smoothing
- **Wrong sampling time (`dt`)**: always ensure `dt` matches your control loop rate

---

## Further Reading

- [Control Systems Engineering - Nise](https://www.wiley.com/en-us/Control+Systems+Engineering%2C+7th+Edition-p-9781118170519)
- [MIT OCW - Feedback Control](https://ocw.mit.edu/courses/res-6-010-electronic-feedback-systems-spring-2013/)
- Ziegler-Nichols tuning, Cohen-Coon method, Lambda tuning

---

## License

MIT — free to use, modify, and distribute.
