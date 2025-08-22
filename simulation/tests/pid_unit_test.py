import pytest
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

from simulation.utils.pid_wrapper import PyPID

@pytest.mark.parametrize("kp, ki, kd, dt, setpoint, measurement, expected", [
    (2.0, 0.5, 0.1, 0.1, 10.0, 5.0, 10.0 + 0.25 + 5.0),  # Basic PID case
])
def test_pid_basic(kp, ki, kd, dt, setpoint, measurement, expected):
    pid = PyPID(kp=kp, ki=ki, kd=kd, dt=dt)
    pid.set_output_limits(-100, 100)
    pid.reset()

    output = pid.update(setpoint, measurement)
    assert abs(output - expected) < 1e-6, f"Expected {expected}, got {output}"


@pytest.mark.parametrize("kp, ki, kd, dt, setpoint, measurement, expected", [
    (100, 20, 10, 0.1, 10.0, 5.0, 10.0),  # Should saturate at max
])
def test_pid_saturation_max(kp, ki, kd, dt, setpoint, measurement, expected):
    pid = PyPID(kp=kp, ki=ki, kd=kd, dt=dt)
    pid.set_output_limits(-10, 10)
    pid.reset()

    output = pid.update(setpoint, measurement)
    assert output == expected, f"Expected saturation at {expected}, got {output}"


@pytest.mark.parametrize("kp, ki, kd, dt, setpoint, measurement, expected", [
    (100, 20, 10, 0.1, -10.0, 5.0, -10.0),  # Should saturate at min
])
def test_pid_saturation_min(kp, ki, kd, dt, setpoint, measurement, expected):
    pid = PyPID(kp=kp, ki=ki, kd=kd, dt=dt)
    pid.set_output_limits(-10, 10)
    pid.reset()

    output = pid.update(setpoint, measurement)
    assert output == expected, f"Expected saturation at {expected}, got {output}"


@pytest.mark.parametrize("kp, ki, kd, dt, setpoint, measurement, steps, expected", [
    (0, 1.0, 0, 0.5, 10.0, 8.0, 2, 2.0),  # After two steps, I term accumulates to 2.0
])
def test_pid_integral_accumulation(kp, ki, kd, dt, setpoint, measurement, steps, expected):
    pid = PyPID(kp=kp, ki=ki, kd=kd, dt=dt)
    pid.set_output_limits(-100, 100)
    pid.reset()

    for _ in range(steps):
        output = pid.update(setpoint, measurement)

    assert abs(output - expected) < 1e-6, f"Expected {expected}, got {output}"
