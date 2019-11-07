PROGRAM ENGINE_F90

USE mpi
USE ISO_C_binding
USE mdi,              ONLY : MDI_Init, MDI_Send, MDI_CHAR, MDI_NAME_LENGTH, &
     MDI_Accept_Communicator, MDI_Recv_Command, MDI_Recv, MDI_Conversion_Factor

IMPLICIT NONE

   INTEGER :: iarg, ierr
   INTEGER :: world_comm, world_rank
   INTEGER :: comm
   CHARACTER(len=1024) :: arg, mdi_options
   CHARACTER(len=:), ALLOCATABLE :: message

   ALLOCATE( character(MDI_NAME_LENGTH) :: message )

   ! Initialize the MPI environment
   call MPI_INIT(ierr)

   ! Read through all the command line options
   iarg = 0
   DO
      CALL get_command_argument(iarg, arg)
      IF (LEN_TRIM(arg) == 0) EXIT

      IF (TRIM(arg) .eq. "-mdi") THEN
         CALL get_command_argument(iarg + 1, mdi_options)

         ! Initialize the MDI Library
         world_comm = MPI_COMM_WORLD
         call MDI_Init( mdi_options, world_comm, ierr)

         EXIT
      END IF

      iarg = iarg + 1
   END DO

   ! Get the MPI rank within world_comm
   call MPI_Comm_rank( world_comm, world_rank, ierr );

   ! Connct to the driver
   call MDI_Accept_Communicator(comm, ierr)

   ! Respond to the driver's commands
   response_loop: DO

      call MDI_Recv_Command(message, comm, ierr)

      SELECT CASE( TRIM(message) )
      CASE( "EXIT" )
         EXIT
      END SELECT
      !!!!!! DEFAULT ????

   END DO response_loop

   ! Synchronize all MPI ranks
   call MPI_Barrier( world_comm, ierr )
   call MPI_Finalize( ierr )

END PROGRAM ENGINE_F90
