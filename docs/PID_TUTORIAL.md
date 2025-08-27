# PID Control: Theory, Implementation & Tuning

This tutorial walks through the theory and implementation of a **PID (Proportional–Integral–Derivative) controller**, as implemented in C for this project.

---

## 1. What is a PID Controller?

A PID controller is a **feedback control loop** used in engineering systems to maintain a variable (like temperature, current, or position) close to a desired target value.

### Equation

$$
u(t) = K_p \cdot e(t) + K_i \cdot \int_0^t e(\tau) d\tau + K_d \cdot \frac{de(t)}{dt}
$$

Where:
- $e(t)$ = setpoint - measurement 
- $u(t)$: control output
- $K_p$: proportional gain
- $K_i$: integral gain
- $K_d$: derivative gain


---

## 2. Understanding Each Component

### Proportional (P)
- **How it works:**  
  The proportional term produces an output value that is proportional to the current error value.  
  If the error is large, the controller output is large; if the error is small, the output is small.

$$
P = K_p \cdot e(t) 
$$

- **Effect:**  
  - Increases the speed of the system response.
  - Too high $K_p$ can cause oscillations or instability.
  - Too low $K_p$ makes the system sluggish and slow to reach the setpoint.

- **When to use:**  
  - Always present in PID and PI controllers.  
  - Use higher $K_p$ for faster response, but watch for overshoot and oscillations.

- **Limitations:**  
  - Cannot eliminate steady-state error on its own (the system may settle close to, but not exactly at, the setpoint).


### Integral (I)
- **How it works:**  
  The integral term sums the error over time.  
  If there is a persistent error, the integral term increases, driving the output to reduce the error.
$$
I = K_i \cdot \int e(t) dt 
$$

- **Effect:**  
  - Eliminates steady-state error (offset).
  - Can cause overshoot and oscillations if set too high.
  - Responds slowly to changes, but is powerful for accuracy.

- **When to use:**  
  - Use when you need the system to reach and stay exactly at the setpoint (e.g., temperature control, speed regulation).

- **Limitations:**  
  - Can cause "integral windup" if the error persists for a long time and the output saturates.
  - Anti-windup strategies (like clamping the integral) are often used.


### Derivative (D)
- **How it works:**  
  The derivative term predicts future error based on its rate of change.  
  It dampens the system response by reacting to how quickly the error is changing.

$$
D = K_d \cdot \frac{de}{dt} 
$$

- **Effect:**  
  - Reduces overshoot and improves stability.
  - Makes the system less oscillatory.
  - Can make the controller sensitive to noise (since noise is high-frequency and derivative amplifies it).

- **When to use:**  
  - Use when you need to reduce overshoot or dampen oscillations (e.g., position control, robotics).

- **Limitations:**  
  - Not always needed; many practical controllers use only PI.
  - Sensitive to measurement noise; may require filtering.

---


## 3. When to Use PID, PI, or PD Controllers

- **PID:**  
  Use when you need fast response, zero steady-state error, and minimal overshoot.  
  Common in motion control, robotics, and process control.

- **PI:**  
  Use when derivative action is not needed (e.g., slow processes, temperature control, flow control).  
  Most industrial controllers are PI.

- **PD:**  
  Use when you need fast response and damping, but steady-state error is not critical (e.g., some position controls).

---

## 4. Practical Limits and Considerations

- **Output Saturation:**  
  Real actuators have limits (e.g., max voltage, max speed).  
  The controller output must be clamped to these limits.

- **Integral Windup:**  
  If the output saturates, the integral term can accumulate excessively, causing slow recovery.  
  Use anti-windup techniques (clamping, conditional integration).

- **Noise Sensitivity:**  
  Derivative action amplifies noise.  
  Use low-pass filtering on the measurement or derivative term.

- **Sampling Time ($dt$):**  
  The controller must be tuned for the sampling rate.  
  Too slow: poor performance.  
  Too fast: unnecessary computation and possible instability.

---

## 5. How It’s Implemented in This Project

See `source/pid.c` and `pid.h` or `pid/pid.py`:

- Modular, reusable structure
- `init()`: sets gains and resets memory
- `compute()`: computes output based on P, I, D
- Anti-windup: clamps the integral to output limits
- Output is clamped between `out_min` and `out_max`

---

## 6. Application to RL Circuit

We use the PID (PI in demo) to control an **RL circuit**, modeled as:

$$
V(t) = L \frac{di(t)}{dt} + R i(t)
$$

- **Setpoint:** desired current
- **Output:** voltage applied
- **System response:** simulated and visualized in Python

---

## 7. How to Tune a PID

### Manual Tuning

1. Start with $K_i = 0$, $K_d = 0$
2. Increase $K_p$ until the system starts oscillating, then reduce slightly
3. Add $K_d$ to reduce overshoot
4. Add $K_i$ to eliminate steady-state error

### Rule-of-Thumb Table

| Gain | Effect | Too Low | Too High |
|------|--------|---------|----------|
| $K_p$ | Speed | Sluggish | Oscillations |
| $K_i$ | Accuracy | Steady error | Overshoot |
| $K_d$ | Stability | Oscillations | Noise sensitivity |

---

## 8. Where PID Is Used

- Motor control
- Temperature regulation
- Robotics
- Audio gain control
- Drones and flight control
- Industrial automation

---

## 9. Further Reading

- [PID Wikipedia](https://en.wikipedia.org/wiki/PID_controller)
- [Back to project overview](../README.md)
