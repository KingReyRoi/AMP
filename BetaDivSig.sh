#!/bin/bash
#SBATCH --job-name=BetaD
#SBATCH --partition=kbs
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=j725k763@ku.edu
#SBATCH --ntasks=3
#SBATCH --mem=2GB
#SBATCH --time=0-00:40:00
#SBATCH --output=BetaDiversity.log

module load qiime2/2019.7 \

qiime diversity beta-group-significance \
  --i-distance-matrix /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted_unifrac_distance_matrix.qza \
  --m-metadata-file /panfs/pfs.local/work/kbs/j725k763/metadata/metadatasheet.1.tsv \
 --m-metadata-column sample_location \
  --o-visualization /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted-unifrac-sample-location-significance.qzv \
  --p-pairwise

qiime diversity beta-group-significance \
  --i-distance-matrix /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted_unifrac_distance_matrix.qza \
  --m-metadata-file /panfs/pfs.local/work/kbs/j725k763/metadata/metadatasheet.1.tsv \
 --m-metadata-column family \
  --o-visualization /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted-unifrac-family-significance.qzv \
  --p-pairwise

qiime diversity beta-group-significance \
  --i-distance-matrix /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted_unifrac_distance_matrix.qza \
  --m-metadata-file /panfs/pfs.local/work/kbs/j725k763/metadata/metadatasheet.1.tsv \
 --m-metadata-column genus \
  --o-visualization /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted-unifrac-genus-significance.qzv \
  --p-pairwise

qiime diversity beta-group-significance \
  --i-distance-matrix /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted_unifrac_distance_matrix.qza \
  --m-metadata-file /panfs/pfs.local/work/kbs/j725k763/metadata/metadatasheet.1.tsv \
 --m-metadata-column elevation \
  --o-visualization /panfs/pfs.local/work/kbs/j725k763/core-metrics-results/unweighted-unifrac-elevation-significance.qzv \
  --p-pairwise