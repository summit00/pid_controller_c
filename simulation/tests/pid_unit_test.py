import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from simulation.utils.pid_wrapper import PyPID

class TestPyPID:
    def test_pid_basic(self):
        pid = PyPID(kp=2.0, ki=0.5, kd=0.1, dt=0.1)
        pid.set_output_limits(-100, 100)
        pid.reset()
        setpoint = 10.0
        measurement = 5.0
        output = pid.update(setpoint, measurement)

        # Manual calculation:
        # error = 5.0
        # P = 2.0 * 5.0 = 10.0
        # I = 0.5 * (5.0 * 0.1) = 0.25
        # D = 0.1 * ((5.0 - 0.0) / 0.1) = 5.0
        expected = 10.0 + 0.25 + 5.0
        assert abs(output - expected) < 1e-6, f"Expected {expected}, got {output}"

    def test_pid_saturation_max(self):
        pid = PyPID(kp=100, ki=20, kd=10, dt=0.1)
        pid.set_output_limits(-10, 10)
        pid.reset()
        setpoint = 10.0
        measurement = 5.0
        output = pid.update(setpoint, measurement)
        assert output == 10.0, "Output should be saturated to satMax"

    def test_pid_saturation_min(self):
        pid = PyPID(kp=100, ki=20, kd=10, dt=0.1)
        pid.set_output_limits(-10, 10)
        pid.reset()
        setpoint = -10.0
        measurement = 5.0
        output = pid.update(setpoint, measurement)
        assert output == -10.0, "Output should be saturated to satMin"

    def test_pid_integral_accumulation(self):
        pid = PyPID(kp=0, ki=1.0, kd=0, dt=0.5)
        pid.set_output_limits(-100, 100)
        pid.reset()
        setpoint = 10.0
        measurement = 8.0

        out1 = pid.update(setpoint, measurement)
        out2 = pid.update(setpoint, measurement)
        # error = 2.0, dt = 0.5, I after two steps = 2.0
        assert abs(out2 - 2.0) < 1e-6, f"Expected 2.0, got {out2}"
