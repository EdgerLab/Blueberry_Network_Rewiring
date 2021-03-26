# scripts for development
# __file__ Makefile
# __author__ Scott Teresi

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DEV_DATA := $(ROOT_DIR)/../Blueberry_Data
DEV_SYNTELOGS := $(DEV_DATA)/AtBB/data_input/synmap_out_8_12_2020.txt
DEV_HOMOLOGS := $(DEV_DATA)/AtBB/data_input/At-Blueberry.blast
DEV_DIFFEXDIR := $(DEV_DATA)/Diff_Ex/EdgeR_Output/

.PHONY: dev help

# All Hap ATBB
at_bb_allbf:                ## execute orthology code with our data
	$(ROOT_DIR)/scripts/At_BB/generate_pairs.py $(DEV_SYNTELOGS) $(DEV_HOMOLOGS) $(DEV_DIFFEXDIR)/All_Hap/Bonferroni Bonferroni All

at_bb_allfdr:                ## execute orthology code with our data
	$(ROOT_DIR)/scripts/At_BB/generate_pairs.py $(DEV_SYNTELOGS) $(DEV_HOMOLOGS) $(DEV_DIFFEXDIR)/All_Hap/FDR FDR All

# Single Hap ATBB
at_bb_singlebf:                ## execute orthology code with our data
	$(ROOT_DIR)/scripts/At_BB/generate_pairs.py $(DEV_SYNTELOGS) $(DEV_HOMOLOGS) $(DEV_DIFFEXDIR)/Single_Hap/Bonferroni Bonferroni Single
at_bb_singlefdr:                ## execute orthology code with our data
	$(ROOT_DIR)/scripts/At_BB/generate_pairs.py $(DEV_SYNTELOGS) $(DEV_HOMOLOGS) $(DEV_DIFFEXDIR)/Single_Hap/FDR FDR Single


#Gene count in module and histogram creation
module_df:
	python $(ROOT_DIR)/scripts/graphs/executor.py $(DEV_DATA)/WGCNA_Data/modulecolors_AT_with_duplicates/

module_df_histograms:
	python $(ROOT_DIR)/scripts/graphs/executor.py $(DEV_DATA)/WGCNA_Data/modulecolors_AT_with_duplicates/ --create_histograms
#----------------------------------------#

# TODO add methods for FPKM


#fpkm:                ## execute fpkm code with our data

help:               ## Show this help.
	fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

