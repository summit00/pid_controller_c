class PIDController:
    """
    A simple PID controller implementation.
    
    The PID controller computes an output based on the error between a setpoint and a measured value.
    It uses three components:
        - Proportional (P): reacts to the current error
        - Integral (I): reacts to the accumulated error over time
        - Derivative (D): reacts to the rate of change of error
    
    Equation:
        output = Kp * error + Ki * ∫error dt + Kd * d(error)/dt
    """

    def __init__(self, kp: float, ki: float, kd: float, dt: float):
        """
        Initialize the PID controller with given gains and time step.
        
        Args:
            kp: Proportional gain
            ki: Integral gain
            kd: Derivative gain
            dt: Sampling time (seconds)
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt

        # Internal states
        self.integral = 0.0         # Accumulated integral term
        self.prev_error = 0.0       # Previous error for derivative calculation

        # Output limits (default: very large range)
        self.out_min = -1e9
        self.out_max = 1e9

    def set_output_limits(self, out_min: float, out_max: float):
        """
        Set the minimum and maximum output limits to prevent excessive control signal.
        
        Args:
            out_min: Minimum output value
            out_max: Maximum output value
        """
        self.out_min = out_min
        self.out_max = out_max

    def reset(self):
        """
        Reset the controller state (integral term and previous error).
        """
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint: float, measurement: float) -> float:
        """
        Compute the PID control output based on the current setpoint and measurement.
        
        Args:
            setpoint: Desired target value
            measurement: Current measured value
        
        Returns:
            Control output (clamped within set limits)
        """
        # Calculate error between desired setpoint and current measurement
        error = setpoint - measurement

        # Proportional term: reacts to the current error
        p_term = self.kp * error

        # Integral term: accumulates error over time
        self.integral += error * self.dt

        # Anti-windup: clamp integral term to avoid excessive growth
        self.integral = max(min(self.integral, self.out_max), self.out_min)

        i_term = self.ki * self.integral

        # Derivative term: reacts to the rate of change of error
        derivative = (error - self.prev_error) / self.dt
        d_term = self.kd * derivative

        # Update previous error for next iteration
        self.prev_error = error

        # Combine all terms to get the control output
        output = p_term + i_term + d_term

        # Clamp the final output within specified limits
        output = max(min(output, self.out_max), self.out_min)

        return output
