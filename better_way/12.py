short_list = [1, 2]
first, second, *rest = short_list

print(first, second, rest)

tools.sort(key=lambda x: x.name)
tools.sort(key=lambda x: x.weight)
places.sort(key=lambda x: x.lower())

power_tools.sort(key=lambda x: (x.weight, x.name))
power_tools.sort(key=lambda x: (-x.weight, x.name))

power_tools.sort(key=lambda x: x.weight, reverse=True)
