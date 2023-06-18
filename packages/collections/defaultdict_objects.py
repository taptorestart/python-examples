# Reference: https://docs.python.org/3/library/collections.html#defaultdict-objects
import collections


def get_smartphone_prices(data):
    result = collections.defaultdict(list)
    for model, price in data:
        result[model].append(price)
    return result


if __name__ == "__main__":
    # (smartphone, price)
    smartphone_prices_data = [("iPhone SE3", 500000), ("iPhone SE3", 550000), ("S22", 1200000), ("S22", 1250000)]
    smartphone_prices = get_smartphone_prices(smartphone_prices_data)
    print(smartphone_prices.items())

"""
# Result
dict_items([('iPhone SE3', [500000, 550000]), ('S22', [1200000, 1250000])])
"""
