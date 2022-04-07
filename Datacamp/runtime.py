# %timeit

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [range(51)]
print(nums_unpack)

# in console

# %timeit [num for num in range(51)]
# 5 us +- 668 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)

# %timeit [range(51)]
# 286 ns +- 27.7 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each

# Using %timeit: formal name or literal syntax

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

# %lprun
# pip install line-profiler
# %load_ext line_profiler
# %lprun -f function_name function_name(a, b, c)

# %mprun
# pip install memory-profiler
# %load_ext memory_profiler
# %mprun -f function_name function_name(a, b, c)

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

%load_ext line_profiler

%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')

%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')


from hero_funcs import get_publisher_heroes, get_publisher_heroes_np

%load_ext memory_profiler

%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')

%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')

