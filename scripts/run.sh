#!/bin/bash

#SBATCH --partition=compute

# set the number of nodes
#SBATCH --nodes=1

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