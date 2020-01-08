#!/usr/bin/python3

import subprocess

def main():
    gpuout = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True)
    if gpuout.stdout.startswith(b"temp="):
        part = gpuout.stdout[len("temp="):]
        if part.endswith(b"'C\n"):
            gpu = float(part[:len(part) - len("'C\n")])

    cpufile = '/sys/class/thermal/thermal_zone0/temp'
    with open(cpufile) as file:  
        data = file.read() 
        cpu = int(data) / 1000

    print('# HELP node_temp_gpu The node GPU temperature in C.')
    print('# TYPE node_temp_gpu gauge')
    print('node_temp_gpu ', gpu)

    print('# HELP node_temp_cpu The node CPU temperature in C.')
    print('# TYPE node_temp_cpu gauge')
    print('node_temp_cpu ', cpu)

if __name__=='__main__':
    main()
