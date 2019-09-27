PROGRAM DRIVER_F90

USE mpi
USE ISO_C_binding
USE mdi,              ONLY : MDI_Init, MDI_Send, MDI_CHAR, MDI_NAME_LENGTH, &
     MDI_Accept_Communicator, MDI_Send_Command, MDI_Recv, MDI_Conversion_Factor

IMPLICIT NONE

   !INTEGER :: niter = 10000
   !INTEGER :: mpi_ptr
   !INTEGER :: world_comm, world_rank
   !INTEGER :: i, ierr
   !INTEGER :: comm_world, comm
   !CHARACTER(len=:), ALLOCATABLE :: message
   !CHARACTER(len=1024) :: arg
   !CHARACTER(len=1024) :: mdi_options
   !DOUBLE PRECISION :: initial_time, final_time
   !DOUBLE PRECISION :: conversion_factor

   INTEGER :: iarg, ierr
   INTEGER :: world_comm, world_rank
   INTEGER :: comm
   CHARACTER(len=1024) :: arg, mdi_options
   CHARACTER(len=:), ALLOCATABLE :: message

!   INTEGER :: world_rank
!   TYPE(MPI_Comm) :: world_comm

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
         !WRITE(6,*)'NULL:   ',MPI_COMM_NULL
         WRITE(6,*)'WORLD:  ',MPI_COMM_WORLD
         WRITE(6,*)'BEFORE: ',world_comm
         call MDI_Init( mdi_options, world_comm, ierr)
         WRITE(6,*)'AFTER:  ',world_comm

         EXIT
      END IF

      iarg = iarg + 1
   END DO

   ! Get the MPI rank within world_comm
!   call MPI_Comm_rank( world_comm, world_rank, ierr );

   ! Connect to the engine
!   call MDI_Accept_Communicator(comm)

   ! Determine the name of the engine
!   call MDI_Send_Command("<NAME", comm, ierr)
!   call MDI_Recv(message, MDI_NAME_LENGTH, MDI_CHAR, comm, ierr)

!   WRITE(6,*)'Engine name: ', message

!   call MDI_Send_Command("EXIT", comm, ierr)

   ! Synchronize all MPI ranks
   call MPI_Barrier( world_comm, ierr )
   call MPI_Finalize( ierr )

END PROGRAM DRIVER_F90
