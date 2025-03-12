from mpi4py import MPI

# Initialize MPI communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Get the rank of the current process
size = comm.Get_size()  # Get the total number of processes

print(f"Hello from rank {rank} out of {size}")
