movie_list = ['interstellar', 'inception', 'prestage', 'insomnia', 'batman']
rating_list = [10, 3, 7, 8, 9]
zip_list1 = zip(movie_list, rating_list)
print(dict(zip_list1))

zip_list2 = zip(movie_list, rating_list)
print(list(zip_list2))

zip_list3 = zip(movie_list, rating_list)
print(tuple(zip_list3))

