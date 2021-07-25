import socket
import os

print("[A] Network Scanner\n[B] Port Scanner\n[C] Both\n[D] Exit")
option = input('Enter your option: ').upper()

if option == 'A':

    print('\nOpening NetScanner...!')
    print('Input example: 10.1.1\n')
    def commands(a):
        r = int(input("Enter the scope of scan: "))
        for i in range(1,r+1):
            c = f'ping -n 1 {a}.{i} | grep "TTL" | cut -d " " -f 3 | sed \'s/.$//\''
            os.system(c) 
    commands(input('Enter network: '))


elif option == 'B':
    
    print('Opening PortScanner...!\n')
    print('Input example: 192.168.1.10\n')
    def port_sacnner(ip):
        c = input("Recommended || Do you want to use defult ports scan[Y/N]: ").upper()

        if c == 'Y':
            l =[20,21,22,23,25,53,67,68,69,70,79,80,88,110,123,143,144,443,465,587,520,666,993,995,3389,139,445,161,389,105,106,2224,3360]
            for i in l:
                port = i
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                if s.connect_ex((ip,port)):
                    pass

                else:
                    print(f"{port} is open")
        
        elif c == 'N':
            start= int(input("Enter Starting Point: "))
            end= int(input("Enter Ending Point: "))
            l = []
            for num in range(start,end+1):
                l.append(num)
            for i in l:
                port = i
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                if s.connect_ex((ip,port)):
                    pass

                else:
                    print(f"{port} is open")
        
        else:
            print('Invalid Option')
    port_sacnner(input('Enter your IP: '))

elif option == 'C':

    print('\nOpening NetScanner...!')
    print('Input example: 10.1.1\n')
    def commands(a):
        r = int(input("Enter the scope of scan: "))
        for i in range(1,r+1):
            c = f'ping -n 1 {a}.{i} | grep "TTL" | cut -d " " -f 3 | sed \'s/.$//\''
            os.system(c)
    commands(input('Enter network: '))

    print('Opening PortScanner...!\n')
    print('Input example: 192.168.1.10\n')
    def port_sacnner(ip):
        c = input("Recommended || Do you want to use defult ports scan[Y/N]: ").upper()

        if c == 'Y':
            l =[20,21,22,23,25,53,67,68,69,70,79,80,88,110,123,143,144,443,465,587,520,666,993,995,3389,139,445,161,389,105,106,2224,3360]
            for i in l:
                port = i
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                if s.connect_ex((ip,port)):
                    pass

                else:
                    print(f"{port} is open")
        
        elif c == 'N':
            start= int(input("Enter Starting Point: "))
            end= int(input("Enter Ending Point: "))
            l = []
            for num in range(start,end+1):
                l.append(num)
            for i in l:
                port = i
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                if s.connect_ex((ip,port)):
                    pass

                else:
                    print(f"{port} is open")
        
        else:
            print('Invalid Option')
    port_sacnner(input('Enter your IP: '))

else:
    exit()
