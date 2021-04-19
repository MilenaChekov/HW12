import pandas as pd
from scipy import stats

df = pd.read_csv('colon_cancer_tumor_vs_normal_paired_FPKM.tsv', sep='\t', index_col=0)
df['ind'] = stats.ttest_ind(df.iloc[:, 0:5], df.iloc[:, 5:], axis=1)[1]
df['rel'] = stats.ttest_rel(df.iloc[:, 0:5], df.iloc[:, 5:10], axis=1)[1]
df = df.sort_values('ind')
print(df.loc[df['ind'] < 0.05])
ind = df.iloc[:10]
ind = ind[['ind']]
print(ind)
df = df.sort_values('rel')
print(df.loc[df['rel'] < 0.05])
rel = df.iloc[:10]
rel = rel[['rel']]
print(rel)
print(ind.join(rel))
