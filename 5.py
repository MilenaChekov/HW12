import pandas as pd
from scipy.stats import shapiro

breast = pd.read_csv('breast_cancer_1000_genes.tsv', sep='\t', index_col=0)
genes_amount = breast.shape[0]
norm = 0

for gene in breast.index:
    if shapiro(breast.loc[gene])[1] > 0.05:
        norm += 1

print(norm/genes_amount * 100)