#include <stdio.h>
#include "../source/pid.h"

/*
    RL circuit as the plant:
    V = L*(di/dt) + R*i

    Discretized:
    i[t+1] = i[t] + (dt/L) * (u[t] - R*i[t])
    where u[t] is the voltage applied by PID controller
*/

int main() {
    // PID setup
    PIDController pid;
    pid_init(&pid, 5.0f, 1.0f, 0.1f, 0.01f);  // kp, ki, kd, dt
    pid_set_output_limits(&pid, 0.0f, 12.0f); // Assume 12V max supply

    // Plant parameters
    float R = 1.0f;    // Ohms
    float L = 0.5f;    // Henry
    float dt = 0.01f;  // Time step
    float i = 0.0f;    // Initial current

    // Simulation parameters
    float setpoint = 1.0f;  // Target current in amps
    int steps = 2000;

    // Simulation loop
    for (int t = 0; t < steps; ++t) {
        float time = t * dt;

        // PID controller calculates voltage input
        float voltage = pid_compute(&pid, setpoint, i);

        // Simulate RL circuit: i[t+1] = i[t] + (dt/L)*(u - R*i)
        float di = (voltage - R * i) * (dt / L);
        i += di;

        // Print data for plotting: time, setpoint, current, voltage
        printf("%.4f,%.4f,%.4f,%.4f\n", time, setpoint, i, voltage);
    }

    return 0;
}
