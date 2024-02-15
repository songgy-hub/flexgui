import os

from PyQt6.QtWidgets import QLabel

def postgui_hal(parent):
	postgui_halfiles = parent.inifile.findall("HAL", "POSTGUI_HALFILE") or None
	if postgui_halfiles is not None:
		for f in postgui_halfiles:
			if f.lower().endswith('.tcl'):
				res = os.spawnvp(os.P_WAIT, "haltcl", ["haltcl", "-i", parent.ini_path, f])
			else:
				res = os.spawnvp(os.P_WAIT, "halcmd", ["halcmd", "-i", parent.ini_path, "-f", f])
			if res: raise SystemExit(res)


def status_labels(parent):
	status_items = ['acceleration', 'active_queue', 'actual_position',
	'adaptive_feed_enabled', 'ain', 'angular_units', 'aout', 'axes', 'axis',
	'axis_mask', 'block_delete', 'call_level', 'command', 'current_line',
	'current_vel', 'cycle_time', 'debug', 'delay_left', 'din', 'distance_to_go',
	'dout', 'dtg', 'echo_serial_number', 'enabled', 'estop', 'exec_state',
	'feed_hold_enabled', 'feed_override_enabled', 'feedrate', 'file', 'flood',
	'g5x_index', 'g5x_offset', 'g92_offset', 'gcodes', 'homed', 'id',
	'ini_filename', 'inpos', 'input_timeout', 'interp_state',
	'interpreter_errcode', 'joint', 'joint_actual_position', 'joint_position',
	'joints', 'kinematics_type', 'limit', 'linear_units', 'lube', 'lube_level',
	'max_acceleration', 'max_velocity', 'mcodes', 'mist', 'motion_line',
	'motion_mode', 'motion_type', 'optional_stop', 'paused', 'pocket_prepped',
	'position', 'probe_tripped', 'probe_val', 'probed_position', 'probing',
	'program_units', 'queue', 'queue_full', 'rapidrate', 'read_line',
	'rotation_xy', 'settings', 'spindle', 'spindles', 'state', 'task_mode',
	'task_paused', 'task_state', 'tool_in_spindle', 'tool_from_pocket',
	'tool_offset', 'tool_table', 'velocity']

	for item in status_items:
		if parent.findChild(QLabel, f'{item}_lb'):
			setattr(parent, f'{item}_lb_exists', True)
		else:
			setattr(parent, f'{item}_lb_exists', False)

	axis_items = ['max_position_limit', 'min_position_limit', 'velocity']

	for i in range(9):
		for item in axis_items:
			if parent.findChild(QLabel, f'axis_{i}_{item}_lb'):
				setattr(parent, f'axis_{i}_{item}_lb_exists', True)
			else:
				setattr(parent, f'axis_{i}_{item}_lb_exists', False)

	joint_items = ['backlash', 'enabled', 'fault', 'ferror_current',
	'ferror_highmark', 'homed', 'homing', 'inpos', 'input', 'jointType',
	'max_ferror', 'max_hard_limit', 'max_position_limit', 'max_soft_limit',
	'min_ferror', 'min_hard_limit', 'min_position_limit', 'min_soft_limit',
	'output', 'override_limits', 'units', 'velocity']

	for i in range(9):
		for item in joint_items:
			if parent.findChild(QLabel, f'joint_{i}_{item}_lb'):
				setattr(parent, f'joint_{i}_{item}_lb_exists', True)
			else:
				setattr(parent, f'joint_{i}_{item}_lb_exists', False)

	spindle_items = ['brake', 'direction', 'enabled', 'homed', 'increasing',
	'orient_fault', 'orient_state', 'override', 'override_enabled', 'speed']

	for i in range(9):
		for item in spindle_items:
			if parent.findChild(QLabel, f'spindle_{i}_{item}_lb'):
				setattr(parent, f'spindle_{i}_{item}_lb_exists', True)
			else:
				setattr(parent, f'spindle_{i}_{item}_lb_exists', False)


