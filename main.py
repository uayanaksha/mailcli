from getargs import read_args
from smtp import Job

if __name__ == '__main__':
    args = read_args()
    if args is not None:
        job = Job(args)
        job.connect()
