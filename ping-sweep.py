import subprocess
import multiprocessing

def listIPRange():
        #Create list of all ip addresses in the range
    ip_addr = []
    for ip in range(ip_range_high + 1):
        ip_addr.append('192.168.1.' + str(ip))
    return ip_addr

def pingSweep(ip_addr):
    # Run the ping command with '-c 2' to send only 1 packet
    ping_reply = subprocess.run(
            ["ping", "-n", "2", ip_addr],
            stdout=subprocess.PIPE,     # Capture standard output
            stderr=subprocess.PIPE      # Capture standard error
    )
    #Convert the byte array to a string
    str_stdout=ping_reply.stdout.decode("utf-8")

    if "TTL" in str_stdout :
        print("\n* {} is reachable :)\n".format(ip_addr))
       
    else:
        print('\n* {} not reachable'.format(ip_addr))

#-------------------------------------------------------------------
ip_range_high=254
ip_range_low=1

if __name__ == "__main__":
    ips = listIPRange()  # Your IP range

    with multiprocessing.Pool() as pool:
        pool.map(pingSweep, ips)