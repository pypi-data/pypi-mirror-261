'''
Author : Arihant Pal
library name : star_pattern
description : This library provide diffrent type of patterns. user just need to provid number of rows and character as argument.

'''
class Star():
    def pyramid(n,c):
        k = 2 * n - 2
        for i in range(0,n):
            for j in range(0,k):
               print(end=" ")
            k = k - 1
            for j in range(0, i+1):
                print(c, end=" ")
            print("\r")

    def pyramid_r(n,c):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print(c, end=" ")
           print("\r")

    def star_r(n,c):
      for i in range(0, n):
           for j in range(0, i + 1):
                print(c, end="")
           print("\r")
      for i in range(n, 0 , -1):
          for j in range(0, i + 1):
               print(c, end="")
          print("\r")

    def star_l(n,c):
        k = 2 * n - 2
        for i in range(0, n-1):
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i + 1):
                print(c, end="")
            print("\r")
        k = -1
        for i in range(n-1,-1,-1):
            for j in range(k,-1,-1):
                print(end=" ")
            k = k + 2
            for j in range(0, i + 1):
                print(c, end="")
            print("\r")

    def hourglass(n,c):
        k = n - 2
        for i in range(n, -1 , -1):
            for j in range(k , 0 , -1):
                print(end=" ")
            k = k + 1    
            for j in range(0, i+1):
                print(c , end="")
            print("\r")
        k = 2 * n  - 2
        for i in range(0 , n+1):
            for j in range(0 , k):
                print(end="")
            k = k - 1
            for j in range(0, i + 1):
                print(c, end="")
            print("\r")

    
    def h_pyramid(n,c):
     for i in range(0,n):
         for j in range(0, i+1):
              print(c , end="")
         print("\r")
    
    def h_pyramid_l(n,c):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0, k):
               print(end=" ")
          k = k - 2
          for j in range(0, i + 1):
              print(c, end="")
          print("\r")

    def dh_pyramid(n,c):
      for i in range(n, -1, -1):
           for j in range(0, i + 1):
               print(c, end="")
           print("\r")

    def diamond(n,c):
        k = 2 * n - 2
        for i in range(0, n):
            for j in range(0 , k):
                print(end=" ")
            k = k - 1
            for j in range(0 , i + 1 ):
                print(c, end="")
            print("\r")
        k = n - 2
        for i in range(n , -1, -1):
            for j in range(k , 0 , -1): 
                print(end=" ")
            k = k + 1
            for j in range(0 , i + 1):
                print(c, end="")
            print("\r")





