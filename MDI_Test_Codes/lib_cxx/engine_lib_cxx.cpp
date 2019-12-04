#include <mpi.h>
#include <iostream>
#include <stdexcept>
#include <string.h>
#include "mdi.h"
#include "engine_lib_cxx.h"

int engine_lib_cxx_create(MPI_Comm mpi_comm) {
  printf("Initializing ENGINE\n");
  MPI_Comm world_comm = mpi_comm;

  // Initialize MDI
  int ret = MDI_Init("-role ENGINE -method LIBRARY -name MM -driver_name driver", &world_comm);

  // Set the execute_command callback
  MDI_Set_Command_Func(execute_command);

  printf("Initialized ENGINE\n");
  return 0;
}

int execute_command(const char* command, MDI_Comm comm) {
  printf("EXECUTE COMMAND\n");
}
