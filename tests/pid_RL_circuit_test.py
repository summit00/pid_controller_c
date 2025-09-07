import pytest
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from pid.pidController import PIDController
from simulation.plants.RL_circuit import RLCircuit
from simulation.magnitudeOptimum import MagnitudeOptimumTuner
from simulation.simulator import Simulator
from simulation.simulation_plotter import SimulationPlotter

@pytest.mark.parametrize("R, L, setpoint, t_final", [
    (1.0, 0.05, 0.1, 0.05),
])
def test_rl_circuit_magnitude_optimum(R, L, setpoint, t_final):
    controller_dt = 0.001
    plant = RLCircuit(R, L)
    current_tuner = MagnitudeOptimumTuner(plant, controller_dt)
    Kp_current, Ki_current, Kd_current = current_tuner.tune()

    controller = PIDController(
        kp=Kp_current,
        ki=Ki_current,
        kd=Kd_current,
        dt=controller_dt
    )

    controller.set_output_limits(-5.0, 5.0)

    setpoint_func = lambda t: setpoint
    sim = Simulator(plant, controller, setpoint_func, dt=controller_dt, t_final=t_final)
    results = sim.run()

    plotter = SimulationPlotter(results)
    plotter.plot_current_and_voltage()

    assert abs(results["output"][-1] - setpoint) < 0.01  # tolerance can be adjusted