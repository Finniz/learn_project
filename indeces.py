import investpy

indeces = investpy.indices.get_indices_overview(country='united states', n_results=4)

# тут много вариантов попробовал, в т.ч. с помощью функции для вывода информации по отдельному индексу -
# investpy.indices.get_index_information(index, country, as_json=False)
# пока неясно что сделать нужно