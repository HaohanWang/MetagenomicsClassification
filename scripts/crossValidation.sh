#!/bin/bash

#SBATCH --partition=pool3-bigmem

# set the number of nodes
#SBATCH --nodes=1

#SBATCH --mem=80000

# set max wallclock time
#SBATCH --time=8:00:00

# set name of job
#SBATCH --job-name=mellon

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=haohanw@andrew.cmu.edu

# run the script

/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high original nb
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high ico nb
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high kmer nb
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high original svc
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high ico svc
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high kmer svc
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high original lr
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high ico lr
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/classification/crossValidation.py mellon_high kmer lr