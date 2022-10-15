from pymavlink import mavutil 

address = 'udpin:localhost:14551'
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")
def change_ground_speed(ground_speed):
    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED,0,0,ground_speed,-1,0,0,0,0)


def change_yaw(heading,yaw_speed):
    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_CONDITION_YAW,0,heading,yaw_speed,1,1,0,0,0)

change_yaw(100,50)