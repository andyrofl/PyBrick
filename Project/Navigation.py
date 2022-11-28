#!/usr/bin/env pybricks-micropython

#CONSTANTS
INDEX_DISTANCE = 0
INDEX_ROTATION = 1
INDEX_TRACKING_EDGE = 2
INDEX_FISH = 3

EDGE_LEFT = -1
EDGE_CENTER = 0
EDGE_RIGHT = 1

ROTATE_90_LEFT = -90
ROTATE_90_RIGHT = 90
ROTATE_NONE = 0
'''
Each step in the instructions is manually entered here
'''

def get_path_by_ID(step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	check_fish=0		#1=check fish, 0=do nothing
	match step:
		case 1:
			forward_distance=6
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 2:
			forward_distance=2.2
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 3:
			forward_distance=2.3
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 4:
			forward_distance=2.0
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 5:
			forward_distance=0.4
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 6:
			forward_distance=2
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 7:
			forward_distance=1.2
			turn_angle=90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 8:
			forward_distance=2
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 9:
			forward_distance=2.3
			turn_angle=-90
			check_fish=0
			tracking_edge=EDGE_RIGHT
		case 10:
			forward_distance=2.0
			turn_angle=0
			check_fish=0
			tracking_edge=EDGE_CENTER
		case 11:
			forward_distance=0
			turn_angle=0
			check_fish=0
			tracking_edge=EDGE_CENTER

	return [forward_distance, turn_angle, tracking_edge, check_fish]

'''
	function returns a set of instructions to navigate from the current point to the dock and back
	IDs are not the same as the previous function and are specific to the location of each fish
'''
def get_return_path_by_fishID(fishID, step):
	forward_distance=0	#number of blocks to move forward
	turn_angle=0		#Degrees to turn from the direction robot is facing (0 is forward)
	tracking_edge=0		#The edge of the robot that will track the line. 1 is right, -1 is left, and 0 goes off grid.
	drop_fish=0
	match fishID:
		case 1:
			match step:
				case 1:
					forward_distance=0
					turn_angle=0
					tracking_edge=EDGE_CENTER
					drop_fish=0
				case 2:
					forward_distance=0
					turn_angle=0
					tracking_edge=EDGE_CENTER
					drop_fish=0
				case 3:
					forward_distance=0
					turn_angle=0
					tracking_edge=EDGE_CENTER
					drop_fish=0
				case 4:
					forward_distance=0
					turn_angle=0
					tracking_edge=EDGE_CENTER
					drop_fish=0
				case 5:
					forward_distance=0
					turn_angle=0
					tracking_edge=EDGE_CENTER
					drop_fish=0
				case 6:
					forward_distance=0
					turn_angle=0
					tracking_edge=EDGE_CENTER
					drop_fish=0
				case 7:
					forward_distance=0
					turn_angle=0
					tracking_edge=EDGE_CENTER
					drop_fish=0

	return [forward_distance, turn_angle, tracking_edge]