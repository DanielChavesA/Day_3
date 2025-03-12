from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


local_value = rank


total_sum = comm.reduce(local_value, op=MPI.SUM, root=0)

#result from rank 0
if rank == 0:
    print(f"Total sum of all ranks: {total_sum}")
