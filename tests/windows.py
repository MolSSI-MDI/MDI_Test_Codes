import os
import subprocess
import glob

print("Doing subprocess")

# get the name of the driver
#dproc = subprocess.Popen(["find ../build -maxdepth 1 -name driver_cxx*"], stdout=subprocess.PIPE, shell=True)
#dproc = subprocess.Popen(["find", "../build/driver_cxx*"], stdout=subprocess.PIPE)
#dproc = subprocess.Popen(["find", "../build", "-maxdepth", "1", "-name", "driver_cxx*"], stdout=subprocess.PIPE)
#output, err = dproc.communicate()
#driver_name = output.decode('utf-8')
#driver_name = driver_name[:-1]

driver_name = glob.glob("../build/driver_cxx*")[0]

# get the name of the engine
#engine_name = subprocess.check_output(["find","../build/engine_cxx*"], shell=True)
#engine_name = engine_name.decode('utf-8')
#engine_name = engine_name[:-1]

#find ../build -maxdepth 1 -name "driver_cxx*"
#eproc = subprocess.Popen(["find ../build -maxdepth 1 -name engine_cxx*"], stdout=subprocess.PIPE, shell=True)
#eproc = subprocess.Popen(["find", "../build", "-maxdepth", "1", "-name", "engine_cxx*"], stdout=subprocess.PIPE)
#output, err = eproc.communicate()
#engine_name = output.decode('utf-8')
#engine_name = engine_name[:-1]

engine_name = glob.glob("../build/engine_cxx*")[0]

print("driver_name: " + str(driver_name))
print("engine_name: " + str(engine_name))

#driver_proc = subprocess.Popen([driver_name + " -mdi \"-role DRIVER -name driver -method TCP -port 8021\""],
#                               stdout=subprocess.PIPE, shell=True)
driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                               stdout=subprocess.PIPE)
#engine_proc = subprocess.Popen([engine_name + " -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\""], shell=True)
engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
output, err = driver_proc.communicate()
engine_proc.communicate()

driver_output = output.decode('utf-8')
print("driver output: " + driver_output)
print("After wait")
