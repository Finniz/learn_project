import investpy

indeces = investpy.indices.get_indices_overview(country='united states', n_results=4, as_json=True)
print(indeces)
print(f"Индекс {indeces[3]['name']} изменился на {indeces[3]['change']} %")