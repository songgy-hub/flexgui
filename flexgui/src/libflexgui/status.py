

#  (returns integer) - This is the mode of the Motion controller.
# One of TRAJ_MODE_COORD, TRAJ_MODE_FREE, TRAJ_MODE_TELEOP

#print(stat_dict['motion_mode'][getattr(parent.status, 'motion_mode')])
'''
// types for EMC_TASK mode
EMC_TASK_MODE_MANUAL = 1,
EMC_TASK_MODE_AUTO = 2,
EMC_TASK_MODE_MDI = 3

// types for EMC_TASK state
EMC_TASK_STATE_ESTOP = 1,
EMC_TASK_STATE_ESTOP_RESET = 2,
EMC_TASK_STATE_OFF = 3,
EMC_TASK_STATE_ON = 4

// types for EMC_TASK execState
EMC_TASK_EXEC_ERROR = 1,
EMC_TASK_EXEC_DONE = 2,
EMC_TASK_EXEC_WAITING_FOR_MOTION = 3,
EMC_TASK_EXEC_WAITING_FOR_MOTION_QUEUE = 4,
EMC_TASK_EXEC_WAITING_FOR_IO = 5,
EMC_TASK_EXEC_WAITING_FOR_MOTION_AND_IO = 7,
EMC_TASK_EXEC_WAITING_FOR_DELAY = 8,
EMC_TASK_EXEC_WAITING_FOR_SYSTEM_CMD = 9,
EMC_TASK_EXEC_WAITING_FOR_SPINDLE_ORIENTED = 10

// types for EMC_TASK interpState
EMC_TASK_INTERP_IDLE = 1,
EMC_TASK_INTERP_READING = 2,
EMC_TASK_INTERP_PAUSED = 3,
EMC_TASK_INTERP_WAITING = 4

// types for motion control
EMC_TRAJ_MODE_FREE = 1,	// independent-axis motion,
EMC_TRAJ_MODE_COORD = 2,	// coordinated-axis motion,
EMC_TRAJ_MODE_TELEOP = 3	// velocity based world coordinates motion,

interpreter_errcode
INTERP_OK = 0,
INTERP_EXIT = 1,
INTERP_EXECUTE_FINISH = 2,
INTERP_ENDFILE = 3,
INTERP_FILE_NOT_OPEN = 4,
INTERP_ERROR = 5,

kinematics_type
KINEMATICS_IDENTITY 0
KINEMATICS_FORWARD_ONLY 1
KINEMATICS_INVERSE_ONLY 2
KINEMATICS_BOTH 3

// types for emcIoAbort() reasons
EMC_ABORT_TASK_EXEC_ERROR = 1,
EMC_ABORT_AUX_ESTOP = 2,
EMC_ABORT_MOTION_OR_IO_RCS_ERROR = 3,
EMC_ABORT_TASK_STATE_OFF = 4,
EMC_ABORT_TASK_STATE_ESTOP_RESET = 5,
EMC_ABORT_TASK_STATE_ESTOP = 6,
EMC_ABORT_TASK_STATE_NOT_ON = 7,
EMC_ABORT_TASK_ABORT = 8,
EMC_ABORT_INTERPRETER_ERROR = 9,	// interpreter failed during readahead
EMC_ABORT_INTERPRETER_ERROR_MDI = 10,	// interpreter failed during MDI execution
EMC_ABORT_USER = 100  // user-defined abort codes start here

motion_mode
TRAJ_MODE_FREE 1
TRAJ_MODE_COORD 2
TRAJ_MODE_TELEOP 3

motion_type
MOTION_TYPE_NONE 0
MOTION_TYPE_TRAVERSE 1
MOTION_TYPE_FEED 2
MOTION_TYPE_ARC 3
MOTION_TYPE_TOOLCHANGE 4
MOTION_TYPE_PROBING 5
MOTION_TYPE_INDEXROTARY 6

program_units
CANON_UNITS_INCHES=1
CANON_UNITS_MM=2
CANON_UNITS_CM=3

state
linuxcnc.RCS_DONE
linuxcnc.RCS_EXEC
linuxcnc.RCS_ERROR

task_mode
linuxcnc.MODE_MDI
linuxcnc.MODE_AUTO
linuxcnc.MODE_MANUAL

task_state
linuxcnc.STATE_ESTOP
linuxcnc.STATE_ESTOP_RESET
linuxcnc.STATE_ON


linuxcnc.

: '', 
'''
def update(parent):
	parent.status.poll()
	stat_dict = {'adaptive_feed_enabled': {0: False, 1: True},
	'motion_mode': {1: 'TRAJ_MODE_FREE', 2: 'TRAJ_MODE_COORD', 3: 'TRAJ_MODE_TELEOP'},
	'exec_state': {1: 'EXEC_ERROR', 2: 'EXEC_DONE', 3: 'EXEC_WAITING_FOR_MOTION',
		4: 'EXEC_WAITING_FOR_MOTION_QUEUE', 5: 'EXEC_WAITING_FOR_IO',
		7: 'EXEC_WAITING_FOR_MOTION_AND_IO', 8: 'EXEC_WAITING_FOR_DELAY',
		9: 'EXEC_WAITING_FOR_SYSTEM_CMD', 10: 'EXEC_WAITING_FOR_SPINDLE_ORIENTED',},
	'estop': {0: False, 1: True},
	'flood': {0: 'FLOOD_OFF', 1: 'FLOOD_ON'},
	'g5x_index': {1: 'G54', 2: 'G55', 3: 'G56', 4: 'G57', 5: 'G58', 6: 'G59',
		7: 'G59.1', 8: 'G59.2', 9: 'G59.3'},
	'interp_state': {1: 'EMC_TASK_INTERP_IDLE', 2: 'EMC_TASK_INTERP_READING',
		3: 'EMC_TASK_INTERP_PAUSED', 4: 'EMC_TASK_INTERP_WAITING'},
	'interpreter_errcode': {0: 'INTERP_OK', 1: 'INTERP_EXIT',
		2: 'INTERP_EXECUTE_FINISH', 3: 'INTERP_ENDFILE', 4: 'INTERP_FILE_NOT_OPEN',
		5: 'INTERP_ERROR'},
	'kinematics_type': {0: 'KINEMATICS_IDENTITY', 1: 'KINEMATICS_FORWARD_ONLY',
		2: 'KINEMATICS_INVERSE_ONLY', 3: 'KINEMATICS_BOTH'},
	'motion_mode': {1: 'TRAJ_MODE_FREE', 2: 'TRAJ_MODE_COORD', 3: 'TRAJ_MODE_TELEOP'},
	'motion_type': {0: 'MOTION_TYPE_NONE', 1: 'MOTION_TYPE_TRAVERSE',
		2: 'MOTION_TYPE_FEED', 3: 'MOTION_TYPE_ARC', 4: 'MOTION_TYPE_TOOLCHANGE',
		5: 'MOTION_TYPE_PROBING', 6: 'MOTION_TYPE_INDEXROTARY'},
	'program_units': {1: 'CANON_UNITS_INCHES', 2: 'CANON_UNITS_MM', 3: 'CANON_UNITS_CM'}
	}

	for key, value in parent.status_labels.items(): # update all status labels
		# get the label and set the text to the status value of the key
		if key in stat_dict:
			getattr(parent, f'{value}').setText(f'{stat_dict[key][getattr(parent.status, f"{key}")]}')
		else:
			getattr(parent, f'{value}').setText(f'{getattr(parent.status, f"{key}")}')

	for key, value in parent.axis_labels.items():
		if key == 'velocity':
			vel = abs(round(getattr(parent, 'status').axis[int(value[5])][key] * 60, 1))
			getattr(parent, f'{value}').setText(f'{vel}')
		else:
			getattr(parent, f'{value}').setText(f'{getattr(parent, "status").axis[int(value[5])][key]}')

	for key, value in parent.joint_labels.items():
		getattr(parent, f'{value}').setText(f'{getattr(parent, "status").joint[int(value[6])][key]}')



