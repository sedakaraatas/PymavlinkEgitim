from pymavlink import mavutil, mavwp

address = 'udpin:localhost:14551'
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")
mavwp.MAVWPLoader()
def get_alt():
    message = vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking= True)
    alt=message.relative_alt
    alt = alt/1000
    return alt
def takeoff(alt):
    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, alt)
    while True: 
        current_alt= get_alt()
        if current_alt< alt:
            print(f"Anlik irtifa {current_alt}")
        elif current_alt >=  alt:
            print("Istenilen irtifaya ulasildi ")
            break
def mission_add(seq,lat="",lon="",alt=""):
    frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT 
    wp.add(mavutil.mavlink.MAVLink_mission_item_message(vehicle.target_system,
                            vehicle.target_component,
                            seq,
                            frame,
                            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,  0, 0, 0, 0, 0, 0, lat,lon, alt))    
    vehicle.waypoint_clear_all_send()
    vehicle.waypoint_count_send(wp.count())    
    for i in range(wp.count()):
                msg = vehicle.recv_match(type=['MISSION_REQUEST'],blocking=True)
                vehicle.mav.send(wp.wp(msg.seq))
                print ('Sending waypoint {0}'.format(msg.seq))

vehicle.set_mode("GUIDED)
vehicle.arducopter_arm()
takeoff(10)
vehicle.set_mode("AUTO")
mission_add(0,-35.36277760, 149.16600380)