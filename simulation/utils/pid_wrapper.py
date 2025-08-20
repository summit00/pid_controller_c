import ctypes
import os
import sys

# Detect platform and set library name
if sys.platform == "win32":
    lib_name = "pid.dll"
else:
    lib_name = "pid.so"

dll_path = os.path.join(os.path.dirname(__file__), lib_name)
print("PID library path:", dll_path)

if not os.path.isfile(dll_path):
    raise FileNotFoundError(f"Could not find {lib_name} at: {dll_path}")

pid_lib = ctypes.CDLL(dll_path)

# Define the PIDController struct
class PIDController(ctypes.Structure):
    _fields_ = [
        ("kp", ctypes.c_float),
        ("ki", ctypes.c_float),
        ("kd", ctypes.c_float),
        ("dt", ctypes.c_float),
        ("integral", ctypes.c_float),
        ("prev_error", ctypes.c_float),
        ("out_min", ctypes.c_float),
        ("out_max", ctypes.c_float),
    ]

# Function prototypes
pid_lib.pid_init.argtypes = [ctypes.POINTER(PIDController), ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
pid_lib.pid_set_output_limits.argtypes = [ctypes.POINTER(PIDController), ctypes.c_float, ctypes.c_float]
pid_lib.pid_reset.argtypes = [ctypes.POINTER(PIDController)]
pid_lib.pid_compute.argtypes = [ctypes.POINTER(PIDController), ctypes.c_float, ctypes.c_float]
pid_lib.pid_compute.restype = ctypes.c_float

# Python wrapper class
class PyPID:
    def __init__(self, kp, ki, kd, dt):
        self.pid = PIDController()
        pid_lib.pid_init(ctypes.byref(self.pid), kp, ki, kd, dt)

    def set_output_limits(self, min_val, max_val):
        pid_lib.pid_set_output_limits(ctypes.byref(self.pid), min_val, max_val)

    def reset(self):
        pid_lib.pid_reset(ctypes.byref(self.pid))

    def update(self, setpoint, measurement):
        return pid_lib.pid_compute(ctypes.byref(self.pid), setpoint, measurement)