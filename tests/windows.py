import os
import subprocess

build_dir = "../build"

##########################
# TCP Method             #
##########################

command = "cd " + build_dir + '''
mkdir AAAAAA_dir
touch output
./$(find driver_cxx*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find engine_cxx*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

print("Before command")
cmd_return = os.system( command )
print("After command")

command = '''./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

print("Before command2")
cmd_return = os.system( command )
print("After command2")

print("No redirect")
command = '''mkdir AAA1_dir
./driver_cxx.exe -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
mkdir AAA2_dir
./engine_cxx.exe -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
mkdir AAA3_dir
wait
mkdir AAA4_dir'''
cmd_return = os.system( command )
print("After no redirect")
print("Error code: " + str(cmd_return))

print("Mkdir")
command = ( "mkdir BBB1_dir;" + 
            "mkdir BBB11_dir;" + 
            "./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &;" +
            "mkdir BBB2_dir;" +
            "./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &;" + 
            "mkdir BBB3_dir;" +
            "wait;" +
            "mkdir BBB4_dir" )
ierr = os.system(command)
print("Error code: " + str(ierr))


print("Doing subprocess")
command = ( "ls;" + 
            "pwd" )
#result = subprocess.check_output(command, shell=True)
#result = subprocess.check_output(["cmd.exe","pwd"])
#result = subprocess.check_output(["ls","."])
driver_name = subprocess.check_output(["find","../build/driver_cxx*"], shell=True)
engine_name = subprocess.check_output(["find","../build/engine_cxx*"], shell=True)
print("driver_name: " + str(driver_name))
print("engine_name: " + str(engine_name))
print("End of subprocess: " + str(result))
