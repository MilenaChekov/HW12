
import pandas as pd
from scipy import stats

df = pd.read_csv('colon_cancer_tumor_vs_normal_paired_FPKM.tsv', sep='\t', index_col=0)
df['ind'] = stats.ttest_ind(df.iloc[:, 0:5], df.iloc[:, 5:], axis=1)[1]
df['rel'] = stats.ttest_rel(df.iloc[:, 0:5], df.iloc[:, 5:10], axis=1)[1]
ind = set(df.sort_values(by='ind', ascending=True).index[:10])
rel = set(df.sort_values(by='rel', ascending=True).index[:10])
print(ind.intersection(rel))