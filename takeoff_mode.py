from pymavlink import mavutil 

address = 'udpin:localhost:14551'
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")

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

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("arac arm edildi")
takeoff(10)