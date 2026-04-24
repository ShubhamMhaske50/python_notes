# A taste of things to come
# In this exercise, you'll explore both the Non-Pythonic and Pythonic ways of looping over a list.

# names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Suppose you wanted to collect the names in the above list that have six letters or more. In other programming languages, the typical approach is to create an index variable (i), use i to iterate over the list, and use an if statement to collect the names with six letters or more:

# i = 0
# new_list= []
# while i < len(names):
#     if len(names[i]) >= 6:
#         new_list.append(names[i])
#     i += 1
# Let's explore some more Pythonic ways of doing this.

# Print the list, new_list, that was created using a Non-Pythonic approach.

# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# A more Pythonic approach would loop over the contents of names, rather than using an index variable. Print better_list.
# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# The best Pythonic way of doing this is by using list comprehension. Print best_list.
# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)

#_____________________________________________________________________

# Built-in practice: range()
# In this exercise, you will practice using Python's built-in function range(). Remember that you can use range() in a few different ways:

# 1) Create a sequence of numbers from 0 to a stop value (which is exclusive). This is useful when you want to create a simple sequence of numbers starting at zero:

# range(stop)

# # Example
# list(range(11))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2) Create a sequence of numbers from a start value to a stop value (which is exclusive) with a step size. This is useful when you want to create a sequence of numbers that increments by some value other than one. For example, a list of even numbers:

# range(start, stop, step)

# # Example
# list(range(2,11,2))

# [2, 4, 6, 8, 10]

# Create a range object that starts at zero and ends at five. Only use a stop argument.
# Convert the nums variable into a list called nums_list.
# Create a new list called nums_list2 that starts at one, ends at eleven, and increments by two by unpacking a range object using the star character (*).

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)

#_____________________________________________________________________

# Built-in practice: enumerate()
# In this exercise, you'll practice using Python's built-in function enumerate(). This function is useful for obtaining an indexed list. For example, suppose you had a list of people that arrived at a party you are hosting. The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):

# names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# If you wanted to attach an index representing a person's arrival order, you could use the following for loop:

# indexed_names = []
# for i in range(len(names)):
#     index_name = (i, names[i])
#     indexed_names.append(index_name)

# [(0,'Jerry'),(1,'Kramer'),(2,'Elaine'),(3,'George'),(4,'Newman')]
# But, that's not the most efficient solution. Let's explore how to use enumerate() to make this more efficient.

# Instead of using for i in range(len(names)), update the for loop to use i as the index variable and name as the iterator variable and use enumerate().
# Rewrite the previous for loop using enumerate() and list comprehension to create a new list, indexed_names_comp.
# Create another list (indexed_names_unpack) by using the star character (*) to unpack the enumerate object created from using enumerate() on names. This time, start the index for enumerate() at one instead of zero.

# Rewrite the for loop to use enumerate
indexed_names = []
for i ,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i ,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

#_____________________________________________________________________

# Built-in practice: map()
# In this exercise, you'll practice using Python's built-in map() function to apply a function to every element of an object. Let's look at a list of party guests:

# names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase. you could accomplish this with the below for loop:

# names_uppercase = []

# for name in names:
#   names_uppercase.append(name.upper())

# ['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']
# Let's explore using the map() function to do this more efficiently in one line of code.

# Use map() and the method str.upper() to convert each name in the list names to uppercase. Save this to the variable names_map.
# Print the data type of names_map.
# Unpack the contents of names_map into a list called names_uppercase using the star character (*).
# Print names_uppercase and observe its contents.

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

#_____________________________________________________________________

# Practice with NumPy arrays
# Let's practice slicing numpy arrays and using NumPy's broadcasting concept. Remember, broadcasting refers to a numpy array's ability to vectorize operations, so they are performed on all elements of an object at once.

# A two-dimensional numpy array has been loaded into your session (called nums) and printed into the console for your convenience. numpy has been imported into your session as np.

# Print the second row of nums.
# Print the items of nums that are greater than six.
# Create nums_dbl that doubles each number in nums.
# Replace the third column in nums with a new column that adds 1 to each item in the original column.

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)

#_____________________________________________________________________

# Bringing it all together: Festivus!
# In this exercise, you will be throwing a party—a Festivus if you will!

# You have a list of guests (the names list). Each guest, for whatever reason, has decided to show up to the party in 10-minute increments. For example, Jerry shows up to Festivus 10 minutes into the party's start time, Kramer shows up 20 minutes into the party, and so on and so forth.

# We want to write a few simple lines of code, using the built-ins we have covered, to welcome each of your guests and let them know how many minutes late they are to your party. Note that numpy has been imported into your session as np and the names list has been loaded as well.

# Let's welcome your guests!

# Use range() to create a list of arrival times (10 through 50 incremented by 10). Create the list arrival_times by unpacking the range object.

# Create a list of arrival times
arrival_times = [*range(10, 51, 10)]

print(arrival_times)

# You realize your clock is three minutes fast. Convert the arrival_times list into a numpy array (called arrival_times_np) and use NumPy broadcasting to subtract three minutes from each arrival time.

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)

# Use list comprehension with enumerate() to pair each guest in the names list to their updated arrival time in the new_times array. You'll need to use the index variable created from using enumerate() on new_times to index the names list.

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[name],time) for name,time in enumerate(new_times)]

print(guest_arrivals)

# A function named welcome_guest() has been pre-loaded into your session. Use map() to apply this function to each element of the guest_arrivals list and save it as the variable welcome_map.

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

#_____________________________________________________________________

# Using %timeit: your turn!
# You'd like to create a list of integers from 0 to 50 using the range() function. However, you are unsure whether using list comprehension or unpacking the range object into a list is faster. Let's use %timeit to find the best implementation.

# For your convenience, a reference table of time orders of magnitude is provided below (faster at the top).

# symbol	name	      unit (s)
# ns	    nanosecond	  10-9
# µs (us)	microsecond	  10-6
# ms	    millisecond	  10-3
# s	        second	      100

# Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Use range() to create a list of integers from 0 to 50 and unpack its contents into a list called nums_unpack.

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*list(nums_list_comp)]
print(nums_unpack)

#_____________________________________________________________________

# Using %timeit: specifying number of runs and loops
# A list of 480 superheroes has been loaded into your session (called heroes). You'd like to analyze the runtime for converting this heroes list into a set. Instead of relying on the default settings for %timeit, you'd like to only use 5 runs and 25 loops per each run.

# What is the correct syntax when using %timeit and only using 5 runs with 25 loops per each run?

%timeit -r5 -n25 set(heroes)

#_____________________________________________________________________

# Using %timeit: formal name or literal syntax
# Python allows you to create data structures using either a formal name or a literal syntax. In this exercise, you'll explore how using a literal syntax for creating a data structure can speed up runtimes.

# data structure	formal name	literal syntax
# list	           list()	     []
# dictionary	       dict()	     {}
# tuple	           tuple()	     ()

# Create an empty list called formal_list using the formal name (list()).
# Create an empty list called literal_list using the literal syntax ([]).

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list and literal_list to show that both naming conventions create a list.

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

#_____________________________________________________________________

# Using %lprun: spot bottlenecks
# Profiling a function allows you to dig deeper into the function's source code and potentially spot bottlenecks. When you see certain lines of code taking up the majority of the function's runtime, it is an indication that you may want to deploy a different, more efficient technique.

# Lets dig deeper into the convert_units() function.

# def convert_units(heroes, heights, weights):

#     new_hts = [ht * 0.39370  for ht in heights]
#     new_wts = [wt * 2.20462  for wt in weights]

#     hero_data = {}

#     for i,hero in enumerate(heroes):
#         hero_data[hero] = (new_hts[i], new_wts[i])

#     return hero_data
# Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units() function acting on your superheroes data. Remember to use the special syntax for working with %lprun (you'll have to provide a -f flag specifying the function you'd like to profile).

%lprun -f convert_units convert_units(heroes, hts, wts)

Timer unit: 1e-09 s

Total time: 0.000525887 s
File: <ipython-input-1-2ae8c0194a47>
Function: convert_units at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units(heroes, heights, weights):
     2                                           
     3         1      70762.0  70762.0     13.5      new_hts = [ht * 0.39370  for ht in heights]
     4         1      62701.0  62701.0     11.9      new_wts = [wt * 2.20462  for wt in weights]
     5                                           
     6         1        580.0    580.0      0.1      hero_data = {}
     7                                           
     8       481     180193.0    374.6     34.3      for i,hero in enumerate(heroes):
     9       480     210181.0    437.9     40.0          hero_data[hero] = (new_hts[i], new_wts[i])
    10                                                   
    11         1       1470.0   1470.0      0.3      return hero_data

#_____________________________________________________________________

# Using %lprun: fix the bottleneck
# In the previous exercise, you profiled the convert_units() function and saw that the new_hts list comprehension could be a potential bottleneck. Did you notice that the new_wts list comprehension also accounted for a similar percentage of the runtime? This is an indication that you may want to create the new_hts and new_wts objects using a different technique.

# Since the height and weight of each hero is stored in a numpy array, you can use array broadcasting rather than list comprehension to convert the heights and weights. This has been implemented in the below function:

# def convert_units_broadcast(heroes, heights, weights):

#     # Array broadcasting instead of list comprehension
#     new_hts = heights * 0.39370
#     new_wts = weights * 2.20462

#     hero_data = {}

#     for i,hero in enumerate(heroes):
#         hero_data[hero] = (new_hts[i], new_wts[i])

#     return hero_data
# Load the line_profiler package into your IPython session. Then, use %lprun to profile the convert_units_broadcast() function acting on your superheroes data. The convert_units_broadcast() function, heroes list, hts array, and wts array have been loaded into your session. After you've finished coding, answer the following question:


%load_ext line_profiler
%lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

Timer unit: 1e-09 s

Total time: 0.00080031 s
File: <ipython-input-1-84e44a6b12f5>
Function: convert_units_broadcast at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units_broadcast(heroes, heights, weights):
     2                                           
     3                                               # Array broadcasting instead of list comprehension
     4         1      62071.0  62071.0      7.8      new_hts = heights * 0.39370
     5         1       6230.0   6230.0      0.8      new_wts = weights * 2.20462
     6                                           
     7         1        770.0    770.0      0.1      hero_data = {}
     8                                           
     9       481     268836.0    558.9     33.6      for i,hero in enumerate(heroes):
    10       480     460903.0    960.2     57.6          hero_data[hero] = (new_hts[i], new_wts[i])
    11                                                   
    12         1       1500.0   1500.0      0.2      return hero_data

#_____________________________________________________________________

# Using %mprun: Hero BMI
# You'd like to calculate the body mass index (BMI) for a selected sample of heroes. BMI can be calculated using the below formula:

# BMI = mass(kg) / height(m)^2

# A random sample of 25,000 superheroes has been loaded into your session as an array called sample_indices. This sample is a list of indices that corresponds to each superhero's index selected from the heroes list.

# A function named calc_bmi_lists has also been created and saved to a file titled bmi_lists.py. For convenience, it is displayed below:

# def calc_bmi_lists(sample_indices, hts, wts):

#     # Gather sample heights and weights as lists
#     s_hts = [hts[i] for i in sample_indices]
#     s_wts = [wts[i] for i in sample_indices]

#     # Convert heights from cm to m and square with list comprehension
#     s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

#     # Calculate BMIs as a list with list comprehension
#     bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

#     return bmis
# Notice that this function performs all necessary calculations using list comprehension (hence the name calc_bmi_lists()). Dig deeper into this function and analyze the memory footprint for performing your calculations using lists:

# Load the memory_profiler package into your IPython session.
# Import calc_bmi_lists from bmi_lists.
# Once you've completed the above steps, use %mprun to profile the calc_bmi_lists() function acting on your superheroes data. The hts array and wts array have already been loaded into your session.
# After you've finished coding, answer the following question:

%load_ext memory_profiler

%mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1    105.8 MiB    105.8 MiB           1   def calc_bmi_lists(sample_indices, hts, wts):
     2                                         
     3                                             # Gather sample heights and weights as lists
     4    106.5 MiB      0.8 MiB       25001       s_hts = [hts[i] for i in sample_indices]
     5    107.3 MiB      0.8 MiB       25001       s_wts = [wts[i] for i in sample_indices]
     6                                         
     7                                             # Convert heights from cm to m and square with list comprehension
     8    108.2 MiB      0.9 MiB       25001       s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]
     9                                         
    10                                             # Calculate BMIs as a list with list comprehension
    11    109.0 MiB      0.8 MiB       25001       bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]
    12                                         
    13    109.0 MiB      0.0 MiB           1       return bmis

#_____________________________________________________________________

# Using %mprun: Hero BMI 2.0
# Let's see if using a different approach to calculate the BMIs can save some memory. If you remember, each hero's height and weight is stored in a numpy array. That means you can use NumPy's handy array indexing capabilities and broadcasting to perform your calculations. A function named calc_bmi_arrays has been created and saved to a file titled bmi_arrays.py. For convenience, it is displayed below:

# def calc_bmi_arrays(sample_indices, hts, wts):

#     # Gather sample heights and weights as arrays
#     s_hts = hts[sample_indices]
#     s_wts = wts[sample_indices]

#     # Convert heights from cm to m and square with broadcasting
#     s_hts_m_sqr = (s_hts / 100) ** 2

#     # Calculate BMIs as an array using broadcasting
#     bmis = s_wts / s_hts_m_sqr

#     return bmis
# Notice that this function performs all necessary calculations using arrays.

# Let's see if this updated array approach decreases your memory footprint:

# Load the memory_profiler package into your IPython session.
# Import calc_bmi_arrays from bmi_arrays.
# Once you've completed the above steps, use %mprun to profile the calc_bmi_arrays() function acting on your superheroes data. The sample_indices array, hts array, and wts array have been loaded into your session.
# After you've finished coding, answer the following question:

# How much memory do the array indexing and broadcasting lines of code consume in the calc_bmi_array() function? (i.e., what is the total sum of the Increment column for these four lines of code?)
                                                                                                                
In [1]:
%load_ext memory_profiler
In [2]:
from bmi_arrays import calc_bmi_arrays
In [3]:
%mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices, hts, wts)
ERROR! Session/line number was not unique in database. History logging moved to new session 83
Filename: /tmp/tmpjqilefcq/bmi_arrays.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1    105.5 MiB    105.5 MiB           1   def calc_bmi_arrays(sample_indices, hts, wts):
     2                                         
     3                                             # Gather sample heights and weights as arrays
     4    105.5 MiB      0.0 MiB           1       s_hts = hts[sample_indices]
     5    105.5 MiB      0.0 MiB           1       s_wts = wts[sample_indices]
     6                                         
     7                                             # Convert heights from cm to m and square with broadcasting
     8    105.5 MiB      0.0 MiB           1       s_hts_m_sqr = (s_hts / 100) ** 2
     9                                         
    10                                             # Calculate BMIs as an array using broadcasting
    11    105.5 MiB      0.0 MiB           1       bmis = s_wts / s_hts_m_sqr
    12                                         
    13    105.5 MiB      0.0 MiB           1       return bmis

#_____________________________________________________________________

# Bringing it all together: Star Wars profiling
# A list of 480 superheroes has been loaded into your session (called heroes) as well as a list of each hero's corresponding publisher (called publishers).

# You'd like to filter the heroes list based on a hero's specific publisher, but are unsure which of the below functions is more efficient.

# def get_publisher_heroes(heroes, publishers, desired_publisher):

#     desired_heroes = []

#     for i,pub in enumerate(publishers):
#         if pub == desired_publisher:
#             desired_heroes.append(heroes[i])

#     return desired_heroes
# def get_publisher_heroes_np(heroes, publishers, desired_publisher):

#     heroes_np = np.array(heroes)
#     pubs_np = np.array(publishers)

#     desired_heroes = heroes_np[pubs_np == desired_publisher]

#     return desired_heroes

# Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect heroes from the Star Wars universe. The desired_publisher for Star Wars is 'George Lucas'.

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, desired_publisher = 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, desired_publisher = 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

# Within your IPython console, load the line_profiler and use %lprun to profile the two functions for line-by-line runtime. When using %lprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

In [1]:
%load_ext line_profiler
In [2]:
%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, desired_publisher = 'George Lucas')
Timer unit: 1e-09 s

Total time: 0.000336133 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2                                           
     3         1        860.0    860.0      0.3      desired_heroes = []
     4                                           
     5       481     173512.0    360.7     51.6      for i,pub in enumerate(publishers):
     6       480     156912.0    326.9     46.7          if pub == desired_publisher:
     7         4       3219.0    804.8      1.0              desired_heroes.append(heroes[i])
     8                                           
     9         1       1630.0   1630.0      0.5      return desired_heroes

# Within your IPython console, load the memory_profiler and use %mprun to profile the two functions for line-by-line memory consumption.
# The get_publisher_heroes() function and get_publisher_heroes_np() function have been saved within a file titled hero_funcs.py (i.e., you can import both functions from hero_funcs). When using %mprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

from hero_funcs import get_publisher_heroes, get_publisher_heroes_np
In [10]:
%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, desired_publisher = 'George Lucas')
Filename: /tmp/tmpq63ugmeu/hero_funcs.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4    104.2 MiB    104.2 MiB           1   def get_publisher_heroes(heroes, publishers, desired_publisher):
     5                                         
     6    104.2 MiB      0.0 MiB           1       desired_heroes = []
     7                                         
     8    104.2 MiB      0.0 MiB         481       for i,pub in enumerate(publishers):
     9    104.2 MiB      0.0 MiB         480           if pub == desired_publisher:
    10    104.2 MiB      0.0 MiB           4               desired_heroes.append(heroes[i])
    11                                         
    12    104.2 MiB      0.0 MiB           1       return desired_heroes

#_____________________________________________________________________

# Combining Pokémon names and types
# Three lists have been loaded into your session from a dataset that contains 720 Pokémon:

# The names list contains the names of each Pokémon.
# The primary_types list contains the corresponding primary type of each Pokémon.
# The secondary_types list contains the corresponding secondary type of each Pokémon (nan if the Pokémon has only one type).
# We want to combine each Pokémon's name and types together so that you easily see a description of each Pokémon. Practice using zip() to accomplish this task.

# # Combine the names list and the primary_types list into a new list object (called names_type1).
# Combine names, primary_types, and secondary_types (in that order) using zip() and unpack the zip object into a new lis
# Use zip() to combine the first five items from the names list and the first three items from the primary_types list.

# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')

#_____________________________________________________________________

# Counting Pokémon from a sample
# A sample of 500 Pokémon has been generated, and three lists from this sample have been loaded into your session:

# The names list contains the names of each Pokémon in the sample.
# The primary_types list containing the corresponding primary type of each Pokémon in the sample.
# The generations list contains the corresponding generation of each Pokémon in the sample.
# You want to quickly gather a few counts from these lists to better understand the sample that was generated. Use Counter from the collections module to explore what types of Pokémon are in your sample, what generations they come from, and how many Pokémon have a name that starts with a specific letter.

# Counter has already been imported into your session for convenience.

# Collect the count of each primary type from the sample.
# Collect the count of each generation from the sample.
# Use list comprehension to collect the first letter of each Pokémon in the names list. Save this as starting_letters.
# Collect the count of starting letters from the starting_letters list. Save this as starting_letters_count.

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

#_____________________________________________________________________

# Combinations of Pokémon
# Ash, a Pokémon trainer, encounters a group of five Pokémon. These Pokémon have been loaded into a list within your session (called pokemon) and printed into the console for your convenience.

# Ash would like to try to catch some of these Pokémon, but his Pokédex can only store two Pokémon at a time. Let's use combinations from the itertools module to see what the possible pairs of Pokémon are that Ash could catch.

# Import combinations from itertools.
# Create a combinations object called combos_obj that contains all possible pairs of Pokémon from the pokemon list. A pair has 2 Pokémon.
# Unpack combos_obj into a list called combos_2.
# Ash upgraded his Pokédex so that it can now store four Pokémon. Use combinations to collect all possible combinations of 4 different Pokémon. Save these combinations directly into a list called combos_4 using the star character (*).

# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)

#_____________________________________________________________________

# Comparing Pokédexes
# Two Pokémon trainers, Ash and Misty, would like to compare their individual collections of Pokémon. Let's see what Pokémon they have in common and what Pokémon Ash has that Misty does not.

# Both Ash and Misty's Pokédex (their collection of Pokémon) have been loaded into your session as lists called ash_pokedex and misty_pokedex. They have been printed into the console for your convenience.

# Convert both lists (ash_pokedex and misty_pokedex) to sets called ash_set and misty_set respectively.
# Find the Pokémon that both Ash and Misty have in common using a set method.
# Find the Pokémon that are within Ash's Pokédex but are not within Misty's Pokédex with a set method.
# Use a set method to find the Pokémon that are unique to either Ash or Misty (i.e., the Pokémon that exist in exactly one of the Pokédexes but not both).

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

#_____________________________________________________________________

# Searching for Pokémon
# Two Pokémon trainers, Ash and Brock, have a collection of ten Pokémon each. Each trainer's Pokédex (their collection of Pokémon) has been loaded into your session as lists called ash_pokedex and brock_pokedex respectively.

# You'd like to see if certain Pokémon are members of either Ash or Brock's Pokédex.

# Let's compare using a set versus using a list when performing this membership testing.

# Convert Brock's Pokédex list (brock_pokedex) to a set called brock_pokedex_set.
# Check if 'Psyduck' is in Ash's Pokédex list (ash_pokedex) and if 'Psyduck' is in Brock's Pokédex set (brock_pokedex_set).
# Check if 'Machop' is in Ash's Pokédex list (ash_pokedex) and if 'Machop' is in Brock's Pokédex set (brock_pokedex_set).

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

#_____________________________________________________________________

# Gathering unique Pokémon
# A sample of 500 Pokémon has been created with replacement (meaning a Pokémon could be selected more than once and duplicates exist within the sample).

# Three lists have been loaded into your session:

# The names list contains the names of each Pokémon in the sample.
# The primary_types list containing the corresponding primary type of each Pokémon in the sample.
# The generations list contains the corresponding generation of each Pokémon in the sample.
# The below function was written to gather unique values from each list:

# def find_unique_items(data):
#     uniques = []

#     for item in data:
#         if item not in uniques:
#             uniques.append(item)

#     return uniques
# Let's compare the above function to using the set data type for collecting unique items.

# Use the provided function to collect the unique Pokémon in the names list. Save this as uniq_names_func.
# Use a set data type to collect the unique Pokémon in the names list. Save this as uniq_names_set.
# Use the most efficient approach for gathering unique items to collect the unique Pokémon types (from the primary_types list) and Pokémon generations (from the generations list).


# Use the provided function to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types) 
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n') 

#_____________________________________________________________________

# Gathering Pokémon without a loop
# A list containing 720 Pokémon has been loaded into your session as poke_names. Another list containing each Pokémon's corresponding generation has been loaded as poke_gens.

# A for loop has been created to filter the Pokémon that belong to generation one or two, and collect the number of letters in each Pokémon's name:

# gen1_gen2_name_lengths_loop = []

# for name,gen in zip(poke_names, poke_gens):
#     if gen < 3:
#         name_length = len(name)
#         poke_tuple = (name, name_length)
#         gen1_gen2_name_lengths_loop.append(poke_tuple)

# Eliminate the above for loop using list comprehension and the map() function:

# Use list comprehension to collect each Pokémon that belongs to generation 1 or generation 2. Save this as gen1_gen2_pokemon.
# Use the map() function to collect the number of letters in each Pokémon's name within the gen1_gen2_pokemon list. Save this map object as name_lengths_map.
# Combine gen1_gen2_pokemon and name_lengths_map into a list called gen1_gen2_name_lengths.

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

#_____________________________________________________________________

# Pokémon totals and averages without a loop
# A list of 720 Pokémon has been loaded into your session called names. Each Pokémon's corresponding statistics has been loaded as a NumPy array called stats. Each row of stats corresponds to a Pokémon in names and each column represents an individual Pokémon stat (HP, Attack, Defense, Special Attack, Special Defense, and Speed respectively.)

# You want to gather each Pokémon's total stat value (i.e., the sum of each row in stats) and each Pokémon's average stat value (i.e., the mean of each row in stats) so that you find the strongest Pokémon.

# The below for loop was written to collect these values:

# poke_list = []

# for pokemon,row in zip(names, stats):
#     total_stats = np.sum(row)
#     avg_stats = np.mean(row)
#     poke_list.append((pokemon, total_stats, avg_stats))

# Replace the above for loop using NumPy:
# Create a total stats array (total_stats_np) using the .sum() method and specifying the correct axis.
# Create an average stats array (avg_stats_np) using the .mean() method and specifying the correct axis.
# Create a final output list (poke_list_np) by combining the names list, the total_stats_np array, and the avg_stats_np array.

# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis = 1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

#_____________________________________________________________________

# One-time calculation loop
# A list of integers that represents each Pokémon's generation has been loaded into your session called generations. You'd like to gather the counts of each generation and determine what percentage each generation accounts for out of the total count of integers.

# The below loop was written to accomplish this task:

# for gen,count in gen_counts.items():
#     total_count = len(generations)
#     gen_percent = round(count / total_count * 100, 2)
#     print(
#       'generation {}: count = {:3} percentage = {}'
#       .format(gen, count, gen_percent)
#     )
# Let's make this loop more efficient by moving a one-time calculation outside the loop.

# Import Counter from the collections module.
# Use Counter() to collect the count of each generation from the generations list. Save this as gen_counts.
# Write a better for loop that places a one-time calculation outside (above) the loop. Use the exact same syntax as the original for loop (simply copy and paste the one-time calculation above the loop).

# Import Counter
from collections import Counter

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
    
#_____________________________________________________________________

# Holistic conversion loop
# A list of all possible Pokémon types has been loaded into your session as pokemon_types. It's been printed in the console for convenience.

# You'd like to gather all the possible pairs of Pokémon types. You want to store each of these pairs in an individual list with an enumerated index as the first element of each list. This allows you to see the total number of possible pairs and provides an indexed label for each pair.

# The below loop was written to accomplish this task:

# enumerated_pairs = []

# for i,pair in enumerate(possible_pairs, 1):
#     enumerated_pair_tuple = (i,) + pair
#     enumerated_pair_list = list(enumerated_pair_tuple)
#     enumerated_pairs.append(enumerated_pair_list)
# Let's make this loop more efficient using a holistic conversion.

# combinations from the itertools module has been loaded into your session. Use it to create a list called possible_pairs that contains all possible pairs of Pokémon types (each pair has 2 Pokémon types).
# Create an empty list called enumerated_tuples above the for loop.
# Use a built-in function to convert each tuple in enumerated_tuples to a list.

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

#_____________________________________________________________________

# Bringing it all together: Pokémon z-scores
# A list of 720 Pokémon has been loaded into your session as names. Each Pokémon's corresponding Health Points is stored in a NumPy array called hps. You want to analyze the Health Points using the z-score to see how many standard deviations each Pokémon's HP is from the mean of all HPs.

# The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based on their z-scores:

# poke_zscores = []

# for name,hp in zip(names, hps):
#     hp_avg = hps.mean()
#     hp_std = hps.std()
#     z_score = (hp - hp_avg)/hp_std
#     poke_zscores.append((name, hp, z_score))
# highest_hp_pokemon = []

# for name,hp,zscore in poke_zscores:
#     if zscore > 2:
#         highest_hp_pokemon.append((name, hp, zscore))

# Use NumPy to eliminate the for loop used to create the z-scores.
# Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2.

# Calculate the total HP avg and total HP standard deviation
hp_avg = np.mean(hps)
hp_std = np.std(hps)

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(names, hps, z_scores) for names,hps,z_scores in poke_zscores2 if z_scores > 2]
print(*highest_hp_pokemon2, sep='\n')

#_____________________________________________________________________

Iterating with .iterrows()
In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs. But, what does this mean? Let's explore with a few coding exercises.

A pandas DataFrame has been loaded into your session called pit_df. This DataFrame contains the stats for the Major League Baseball team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012. It has been printed into your console for convenience.
    
# Use .iterrows() to loop over pit_df and print each row. Save the first item from .iterrows() as i and the second as row.
# Add two lines to the loop: one before print(row) to print each index variable and one after to print each row's type.
# Instead of using i and row in the for statement to store the output of .iterrows(), use one variable named row_tuple.
# Add a line in the for loop to print the type of each row_tuple.

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

# Iterate over pit_df and print each index variable, row, and row type
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))

# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

#_____________________________________________________________________

# Run differentials with .iterrows()
# You've been hired by the San Francisco Giants as an analyst—congrats! The team's owner wants you to calculate a metric called the run differential for each season from the year 2008 to 2012. This metric is calculated by subtracting the total number of runs a team allowed in a season from the team's total number of runs scored in a season. 'RS' means runs scored and 'RA' means runs allowed.

# The below function calculates this metric:

# def calc_run_diff(runs_scored, runs_allowed):

#     run_diff = runs_scored - runs_allowed

#     return run_diff
# A DataFrame has been loaded into your session as giants_df and printed into the console. Let's practice using .iterrows() to add a run differential column to this DataFrame.

# Create an empty list called run_diffs that will be used to store the run differentials you will calculate.

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)

    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

#_____________________________________________________________________

# Iterating with .itertuples()
# Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple. You can look up an attribute within a namedtuple with a special syntax. Let's practice working with namedtuples.

# A pandas DataFrame has been loaded into your session called rangers_df. This DataFrame contains the stats ('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs') for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').

# Use .itertuples() to loop over rangers_df and print each row.
# Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.
# Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs.

# Loop over the DataFrame and print each row
for namedtuple in rangers_df.itertuples():
  print(namedtuple)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

#_____________________________________________________________________

Run differentials with .itertuples()
The New York Yankees have made a trade with the San Francisco Giants for your analyst contract— you're a hot commodity! Your new boss has seen your work with the Giants and now wants you to do something similar with the Yankees data. He'd like you to calculate run differentials for the Yankees from the year 1962 to the year 2012 and find which season they had the best run differential.

You've remembered the function you used when working with the Giants and quickly write it down:

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff
Let's use .itertuples() to loop over the yankees_df DataFrame (which has been loaded into your session) and calculate run differentials.

Use .itertuples() to loop over yankees_df and grab each row's runs scored and runs allowed values.
Now, calculate each row's run differential using calc_run_diff(). Be sure to append each row's run differential to run_diffs.
Append a new column called 'RD' to the yankees_df DataFrame that contains the run differentials you calculated.

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

#_____________________________________________________________________

# Analyzing baseball stats with .apply()
# The Tampa Bay Rays want you to analyze their data.

# They'd like the following metrics:

# The sum of each column in the data
# The total amount of runs scored in a year ('RS' + 'RA' for each year)
# The 'Playoffs' column in text format rather than using 1's and 0's
# The below function can be used to convert the 'Playoffs' column to text:

# def text_playoffs(num_playoffs): 
#     if num_playoffs == 1:
#         return 'Yes'
#     else:
#         return 'No' 
# Use .apply() to get these metrics. A DataFrame (rays_df) has been loaded and printed to the console. This DataFrame is indexed on the 'Year' column.


# Apply sum() to each column of rays_df to collect the sum of each column. Be sure to specify the correct axis.
# Apply sum() to each row of rays_df, only looking at the 'RS' and 'RA' columns, and specify the correct axis.
# Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

#_____________________________________________________________________

# Settle a debate with .apply()
# Word has gotten to the Arizona Diamondbacks about your awesome analytics skills. They'd like for you to help settle a debate amongst the managers. One manager claims that the team has made the playoffs every year they have had a win percentage of 0.50 or greater. Another manager says this is not true.

# Let's use the below function and the .apply() method to see which manager is correct.

# def calc_win_perc(wins, games_played):
#     win_perc = wins / games_played
#     return np.round(win_perc,2)
# A DataFrame named dbacks_df has been loaded into your session.

# Print the first five rows of the dbacks_df DataFrame to see what the data looks like.
# Create a pandas Series called win_percs by applying the calc_win_perc() function to each row of the DataFrame with a lambda function.
# Create a new column in dbacks_df called WP that contains the win percentages you calculated in the above step.

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

#_____________________________________________________________________

# Replacing .iloc with underlying arrays
# Now that you have a better grasp on a DataFrame's internals let's update one of your previous analyses to leverage a DataFrame's underlying arrays. You'll revisit the win percentage calculations you performed row by row with the .iloc method:

# def calc_win_perc(wins, games_played):
#     win_perc = wins / games_played
#     return np.round(win_perc,2)

# win_percs_list = []

# for i in range(len(baseball_df)):
#     row = baseball_df.iloc[i]

#     wins = row['W']
#     games_played = row['G']

#     win_perc = calc_win_perc(wins, games_played)

#     win_percs_list.append(win_perc)

# baseball_df['WP'] = win_percs_list
# Let's update this analysis to use arrays instead of the .iloc method. A DataFrame (baseball_df) has been loaded into your session.

# Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them directly into the calc_win_perc() function. Store the result as a variable called win_percs_np.
# Create a new column in baseball_df called 'WP' that contains the win percentages you just calculated.

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

#_____________________________________________________________________

# Bringing it all together: Predict win percentage
# A pandas DataFrame (baseball_df) has been loaded into your session. For convenience, a dictionary describing each column within baseball_df has been printed into your console. You can reference these descriptions throughout the exercise.

# You'd like to attempt to predict a team's win percentage for a given season by using the team's total runs scored in a season ('RS') and total runs allowed in a season ('RA') with the following function:

# def predict_win_perc(RS, RA):
#     prediction = RS ** 2 / (RS ** 2 + RA ** 2)
#     return np.round(prediction, 2)
# Let's compare the approaches you've learned to calculate a predicted win percentage for each season (or row) in your DataFrame.
    
# Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function. Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc() to each row of the baseball_df DataFrame using a lambda function. Save the predicted win percentage as win_perc_preds_apply.

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df into predict_win_perc(). Save these predictions as win_perc_preds_np.

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())