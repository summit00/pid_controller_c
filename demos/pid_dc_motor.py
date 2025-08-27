import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))


from pid.pid import PIDController
from simulation.plants.dc_motor import DCMotor
from simulation.magnitudeOptimum import MagnitudeOptimumTuner
from simulation.simulator import Simulator
from simulation.simulation_plotter import SimulationPlotter


def run_dcMotor_sim(setpoint=500, t_final=1):
    controller_dt = 0.001
    motor = DCMotor()
    motor.set_motor_parameters(J=7.0865e-4, b=5.4177e-6, K=0.0061, R=0.0045, L=1.572e-4)

    Kp_current, Ki_current, Kd_current = [0.02,0.1,0.0002]

    controller = PIDController(kp=Kp_current, ki=Ki_current, kd=Kd_current, dt=controller_dt)

    controller.set_output_limits(-5.0, 5.0)

    setpoint_func = lambda t: setpoint
    sim = Simulator(motor, controller, setpoint_func, dt=controller_dt, t_final=t_final)
    results = sim.run()

    plotter = SimulationPlotter(results)
    plotter.plot_current_and_voltage()

    # Optional: print final error
    print("Final error:", abs(results["output"][-1] - setpoint))


if __name__ == "__main__":
    run_dcMotor_sim()