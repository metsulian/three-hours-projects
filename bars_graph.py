from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)

plt.ylabel('Numero de Premiacoes')
plt.title('Meus filmes favoritos')

plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()