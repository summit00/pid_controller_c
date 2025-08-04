#ifndef PID_H
#define PID_H

typedef struct {
    float kp;
    float ki;
    float kd;

    float dt;  // Sampling time [s]

    float integral;
    float prev_error;

    float out_min;
    float out_max;
} PIDController;

// Initialize with gains and time step.
void pid_init(PIDController* pid, float kp, float ki, float kd, float dt);

// Set output limits..
void pid_set_output_limits(PIDController* pid, float min, float max);

// Reset integral and derivative state.
void pid_reset(PIDController* pid);

// Compute the PID output.
float pid_compute(PIDController* pid, float setpoint, float measurement);

#endif
