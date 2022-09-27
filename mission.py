from pymavlink import mavutil, mavwp

address = 'udpin:localhost:14551'
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")
mavwp.MAVWPLoader()
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
mission_add(0,-35.36277760, 149.16600380)