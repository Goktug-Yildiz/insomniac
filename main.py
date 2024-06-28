# initalising strings

from multiprocessing.sharedctypes import Value

      

      

str1 = "10"

str2 = "FavTutor blogs"

str3 = "for10"

   # creating a list of all the variables to check multiple cases

variables = [str1, str2, str3]

      

   # declaring a flag for check

flag = True

      

for var in variables:

   # Applying error - handling method

          try:

              # try converting to integer

              int(var)

          except ValueError:

              flag = False

      

          # flag check

          if flag:

              print("This is an integer")

          else:

              print("This is not an integer")