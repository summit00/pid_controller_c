class MagnitudeOptimumTuner:
    """
    A tuner class that uses the Magnitude Optimum criterion to calculate PID gains.
    """

    def __init__(self, plant, Ts_current):
        """
        Initializes the MagnitudeOptimumTuner.

        Args:
            plant: The plant object (e.g., DC motor).
            Ts_current: The desired closed-loop time constant (related to the current controller sample time).
        """
        self.plant = plant
        self.Ts_current = Ts_current

    def tune(self):
        """
        Calculates the PID gains using the Magnitude Optimum criterion.

        Returns:
            A tuple containing the calculated Kp, Ki, and Kd gains.  Kd is always 0.0.
        """
        if self.plant.R <= 0:
            raise ValueError("Resistance R must be bigger than 0.")
        if self.plant.L <= 0:
            raise ValueError("Inductance L must be bigger than 0.")
        
        Te = 2* self.Ts_current
        tau = self.plant.L / self.plant.R  # Electrical time constant

        Kp = self.plant.L / 2 / Te
        Ki = 1 / (Te*tau )
        Kd = 0.0  # Magnitude Optimum typically doesn't use a derivative term

        return Kp, Ki, Kd