#%%
import matplotlib.pyplot as plt
import pickle
import numpy as np

#%%
with open('data/web_out_degree.pkl', 'rb') as f:
    out_degree = pickle.load(f)

with open('data/web_in_degree.pkl', 'rb') as f:
    in_degree = pickle.load(f)


#%%
out_array = [value for key, value in out_degree.items()]
in_array = [value for key, value in in_degree.items()]
# %%
plt.hist(out_array, 100)
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('Number of hyperlinks per page', fontsize=15)
# plt.title('Histogram for number of hyperlinks per page', fontsize=15)
plt.savefig('figs/p1-fig1.pdf', bbox_inches='tight', dpi=200)
plt.show()
# %%
plt.hist(in_array, 40)
plt.ylabel('Frequency', fontsize=15)
plt.xlabel('Number of hyperlinks pointing to each page', fontsize=15)
# plt.title('Histogram for number of hyperlinks pointing to each page', fontsize=15)
plt.savefig('figs/p1-fig2.pdf', bbox_inches='tight', dpi=200)
plt.show()
# %%
def get_ccdf(array):
    num, counts = np.unique(array, return_counts=True)
    cum_sum = np.cumsum(counts)
    ccdf = 1 - cum_sum / cum_sum[-1]
    num = np.insert(num, 0, num[0])
    ccdf = np.insert(ccdf, 0, 1.0)
    return num, ccdf
# %%
out_num, out_ccdf = get_ccdf(out_array)
#
# %%
plt.plot(out_num, out_ccdf, drawstyle='steps-post')
plt.ylabel('Probability', fontsize=15)
plt.xlabel('Number of hyperlinks per page', fontsize=15)
# plt.title('Complementary CDF for Number of hyperlinks per page', fontsize=15)
plt.savefig('figs/p1-ccdf1.pdf', bbox_inches='tight', dpi=200)
plt.show()
# %%
in_num, in_ccdf = get_ccdf(in_array)
plt.plot(in_num, in_ccdf, drawstyle='steps-post')
plt.ylabel('Probability', fontsize=15)
plt.xlabel('Number of hyperlinks pointing to each page', fontsize=15)
# plt.title('Complementary CDF for Number of hyperlinks pointing to each page', fontsize=15)
plt.savefig('figs/p1-ccdf2.pdf', bbox_inches='tight', dpi=200)
plt.show()
# %%
