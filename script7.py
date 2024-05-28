from netmiko import ConnectHandler

# Declare variables
deviceType = "cisco_ios"
user = "developer"  # Replace with your username
password = "cisco"  # Replace with your password
secret = "secret"   # Replace with your secret

# Define the device parameters
SW1 = {
    'device_type': deviceType,
    'ip': '172.17.6.68',  # Replace with your device's IP address
    'username': user,
    'password': password,
    'secret': secret,
}

SW2 = {
    'device_type': deviceType,
    'ip': '172.17.6.69',  # Replace with your device's IP address
    'username': user,
    'password': password,
    'secret': secret,
}

SW3 = {
    'device_type': deviceType,
    'ip': '172.17.6.70',  # Replace with your device's IP address
    'username': user,
    'password': password,
    'secret': secret,
}

R1 = {
    'device_type': deviceType,
    'ip': '172.17.6.66',  # Replace with your device's IP address
    'username': user,
    'password': password,
    'secret': secret,
}

R2 = {
    'device_type': deviceType,
    'ip': '172.17.6.67',  # Replace with your device's IP address
    'username': user,
    'password': password,
    'secret': secret,
}

devices = [SW1, SW2, R1, R2]  # Store devices in a list
config_commands = [
    'show ip interfaces brief'
]

for device in devices:
    # Initialize the connection to the device
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    # Send configuration commands to the device
    output = net_connect.send_command('show ip interface brief')
    print(output)


    # Save the configuration
    net_connect.save_config()

    # Close the connection
    net_connect.disconnect()
