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
- Reacts to current error
-  $P = K_p \cdot e(t) $
- Higher $K_p $: faster response, but may cause oscillations

### Integral (I)
- Accumulates past errors
- $I = K_i \cdot \int e(t) dt $
- Fixes steady-state error, but can lead to overshoot

### Derivative (D)
- Predicts future error trends
- $D = K_d \cdot \frac{de}{dt} $
- Helps reduce overshoot and oscillations

---

## 3. How It’s Implemented in This Project

See `source/pid.c` and `pid.h`:

- Modular, reusable structure
- `pid_init()`: sets gains and resets memory
- `pid_compute()`: computes output based on P, I, D
- Anti-windup: clamps the integral to output limits
- Output is clamped between `out_min` and `out_max`

---

## 4. Application to RL Circuit

We use the PID to control an **RL circuit**, modeled as:

$$
V(t) = L \frac{di(t)}{dt} + R i(t)
$$

- Setpoint: desired current
- Output: voltage applied
- System response is printed/simulated

---

## 5. How to Tune a PID

### Manual Tuning

1. Start with $K_i = 0 $, $ K_d = 0 $
2. Increase $ K_p $ until the system starts oscillating, then reduce slightly
3. Add $ K_d $ to reduce overshoot
4. Add $ K_i $ to eliminate steady-state error

### Rule-of-Thumb Table

| Gain | Effect | Too Low | Too High |
|------|--------|---------|----------|
| $ K_p $ | Speed | Sluggish | Oscillations |
| $ K_i $ | Accuracy | Steady error | Overshoot |
| $ K_d $ | Stability | Oscillations | Noise sensitivity |

---

## 6. Where PID Is Used

- Motor control
- Temperature regulation
- Robotics
- Audio gain control
- Drones and flight control
- Industrial automation

---

## Back to Main Project
[Back to project overview](../README.md)
