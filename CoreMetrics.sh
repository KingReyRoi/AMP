#!/bin/bash
#SBATCH --job-name=CoreMetrics  
#SBATCH --partition=kbs          
#SBATCH --mail-type=END,FAIL          
#SBATCH --mail-user=j725k763@ku.edu     
#SBATCH --ntasks=3                    
#SBATCH --mem=4GB                     
#SBATCH --time=0-00:40:00             
#SBATCH --output=qiime2.log

module load qiime2/2019.7 \

qiime diversity core-metrics-phylogenetic \
  --i-phylogeny /panfs/pfs.local/work/kbs/j725k763/qza_files/rooted-tree.qza \
  --i-table /panfs/pfs.local/work/kbs/j725k763/qza_files/table.qza \
  --p-sampling-depth 449 \
  --m-metadata-file /panfs/pfs.local/work/kbs/j725k763/qiime2_metadata.tsv \
  --output-dir core-metrics-resultsls
  