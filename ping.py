# import pyping

# response = pyping.ping('www.google.com')

# if response.ret_code == 0:
#     print("reachable")
# else:
#     print("unreachable")


# import os

# ip_list = ['www.goggle.com']
# for ip in ip_list:
#     response = os.popen(f"ping {ip}").read()
#     if "Received = 4" in response:
#         print(f"UP {ip} Ping Successful")
#     else:
#         print(f"DOWN {ip} Ping Unsuccessful")


# import platform    # For getting the operating system name
# import subprocess  # For executing a shell command

# def ping(host):
#     """
#     Returns True if host (str) responds to a ping request.
#     Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
#     """

#     # Option for the number of packets as a function of
#     param = '-n' if platform.system().lower()=='windows' else '-c'

#     # Building the command. Ex: "ping -c 1 google.com"
#     command = ['ping', param, '1', host]

#     return subprocess.call(command) == 0


# response = ping('www.youdddtube.com') 

# if response == 'ping: www.youdddtube.com: Name or service not known':
#     print('here')


import platform
import subprocess

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False