import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/g_g/workspaces/ros2_py_ws/install/my_py_pkg'
