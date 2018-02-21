#!/bin/bash

# set the number of nodes and processes per node
#SBATCH --nodes=2

# set the number of tasks (processes) per node.
#SBATCH --ntasks-per-node=16

# set max wallclock time
#SBATCH --time=100:00:00

# set name of job
#SBATCH --job-name=smith

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=haohanw@andrew.cmu.edu

# run the application
python clustering/clustering.py