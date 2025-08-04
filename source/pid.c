#include "pid.h"

void pid_init(PIDController* pid, float kp, float ki, float kd, float dt) {
    pid->kp = kp;
    pid->ki = ki;
    pid->kd = kd;
    pid->dt = dt;

    pid->integral = 0.0f;
    pid->prev_error = 0.0f;
    pid->out_min = -1e9f;
    pid->out_max = 1e9f;
}

void pid_set_output_limits(PIDController* pid, float min, float max) {
    pid->out_min = min;
    pid->out_max = max;
}

void pid_reset(PIDController* pid) {
    pid->integral = 0.0f;
    pid->prev_error = 0.0f;
}

float pid_compute(PIDController* pid, float setpoint, float measurement) {
    // Calculate error.
    float error = setpoint - measurement;

    // Proportional.
    float p_term = pid->kp * error;

    // Integral.
    pid->integral += error * pid->dt;

    // Anti-windup: clamp integral term.
    if (pid->integral > pid->out_max) pid->integral = pid->out_max;
    if (pid->integral < pid->out_min) pid->integral = pid->out_min;

    float i_term = pid->ki * pid->integral;

    // Derivative.
    float derivative = (error - pid->prev_error) / pid->dt;
    float d_term = pid->kd * derivative;

    pid->prev_error = error;

    // Combine terms.
    float output = p_term + i_term + d_term;

    // Clamp final output.
    if (output > pid->out_max) output = pid->out_max;
    if (output < pid->out_min) output = pid->out_min;

    return output;
}
