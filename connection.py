from pymavlink import mavutil 

address = 'udpin:localhost:14551' #simulasyon
# address= '/dev/ttyACM0' #pixhawk usb
# address= '/dev/ttyTHS1' #pixhawk telem2 baudrate= 115200
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")

# while True:
#     message= vehicle.recv_match(blocking= True)
#     print(message)


battery= vehicle.recv_match(type='BATTERY_STATUS', blocking=True)  
print(f"Pil Yuzdesi: {battery.battery_remaining}")
    
message= vehicle.recv_match(type='VFR_HUD', blocking=True)
print(f"Pitch:  {message.airspeed}")

msg = vehicle.recv_match(type = 'HEARTBEAT', blocking = True)
mode = mavutil.mode_string_v10(msg)
print(f"Mode: {mode}")