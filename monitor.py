from time import sleep
import sys

# ----------------------------
# PURE LOGIC FUNCTIONS
# ----------------------------

def is_temperature_ok(temperature):
    return 95 <= temperature <= 102

def is_pulse_ok(pulse_rate):
    return 60 <= pulse_rate <= 100

def is_spo2_ok(spo2):
    return spo2 >= 90

def check_vitals(temperature, pulse_rate, spo2):
    if not is_temperature_ok(temperature):
        return "Temperature critical!"
    if not is_pulse_ok(pulse_rate):
        return "Pulse Rate is out of range!"
    if not is_spo2_ok(spo2):
        return "Oxygen Saturation out of range!"
    return None

# ----------------------------
# I/O FUNCTIONS
# ----------------------------

def alert_animation():
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def notify_and_alert(message):
    print(message)
    alert_animation()

# ----------------------------
# WRAPPER FUNCTION
# ----------------------------

def vitals_ok(temperature, pulse_rate, spo2):
    message = check_vitals(temperature, pulse_rate, spo2)
    if message:
        notify_and_alert(message)
        return False
    return True
