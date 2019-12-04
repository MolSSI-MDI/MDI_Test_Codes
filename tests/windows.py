import os

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
