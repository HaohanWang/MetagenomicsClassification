#!/bin/bash

#SBATCH --partition=pool3-bigmem

# set the number of nodes
#SBATCH --nodes=1

#SBATCH --mem=40000

# set max wallclock time
#SBATCH --time=4:00:00

# set name of job
#SBATCH --job-name=mellon

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=haohanw@andrew.cmu.edu

# run the application
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_high_contamination_1_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_high_contamination_2_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_high_contamination_3_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_high_contamination_4_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_1_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_2_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_3_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_4_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_5_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_6_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_7_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_8_filterMouse.fastq
/home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/originalFeature.py mellon_low_contamination_9_filterMouse.fastq

# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_high_contamination_1_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_high_contamination_2_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_high_contamination_3_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_high_contamination_4_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_1_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_2_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_3_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_4_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_5_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_6_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_7_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_8_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/kmerCount.py mellon_low_contamination_9_filterMouse.fastq

# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_high_contamination_1_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_high_contamination_2_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_high_contamination_3_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_high_contamination_4_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_1_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_2_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_3_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_4_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_5_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_6_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_7_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_8_filterMouse.fastq
# /home/haohanw/python2.7/bin/python /home/haohanw/metaGenomicsClustering/kmerCount/icoFeature.py mellon_low_contamination_9_filterMouse.fastq