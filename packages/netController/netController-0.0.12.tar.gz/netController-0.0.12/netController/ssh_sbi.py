from netmiko import ConnectHandler
from .nas_inventory import get_host

class NetworkDevice:
    #allowed_commands = ["show access-lists", "show interfaces", "show ip route", "show ip bgp summary","show configuration","show running-config", "show version"]

    def __init__(self, hostname):
        self.hostname = hostname
        self.net_connect = self.get_netmiko_connection()

    def get_netmiko_connection(self):
        host = get_host(hostname=self.hostname)
        device_params = {
                    "host": host["ip"],
                    "username": host["user"],
                    "password": host["password"],
                    "secret": host["password"],
                    "device_type": "vyos" if host["vendor"] == "VyOS" else "juniper" if host["vendor"] == "Juniper" else "cisco_ios"
                }
        try:
            net_connect = ConnectHandler(**device_params)
            return net_connect
        except Exception as e:
            print(f'Error: {e}')
            return None

    def send_command(self, command:str):
        #if command not in self.allowed_commands:
            #return "Command not allowed"
        try:
            output = self.net_connect.send_command(command)
            return output
        except Exception as e:
            print(f'Error: {e}')
        return None

    def get_backup(self):
        if self.net_connect:
            if self.net_connect.device_type == "vyos":
                output = self.send_command("show configuration")
            else:
                self.net_connect.enable()
                output = self.send_command("show running-config")
            if output:
                return output
            return "Error retrieving backup"
        else:
            return "Error connecting to the device"

    def get_version(self):
        if self.net_connect:
            if self.net_connect.device_type == "vyos":
                output = self.send_command("show version")
            else:
                self.net_connect.enable()
                output = self.send_command("show version")
            if output:
                return output
            return "Error retrieving backup"
        else:
            return "Error connecting to the device"

    def configure_device(self, config: str):
        if self.net_connect:
            output = self.net_connect.send_config_set(config)
            if output:
                return output
            return "Error retrieving backup"
        else:
            return "Error connecting to the device"