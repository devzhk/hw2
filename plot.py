import matplotlib.pyplot as plt
import pickle


with open('data/web_out_degree.pkl', 'rb') as f:
    out_degree = pickle.load(f)

with open('data/web_in_degree.pkl', 'rb') as f:
    in_degree = pickle.load(f)

