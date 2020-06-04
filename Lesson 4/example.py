from distributions import Gaussian

g1 = Gaussian(22, 2)
g1.read_data_file('numbers.txt')
print(g1.mean)

g1.plot_histogram()
g1.plot_histogram_pdf()
