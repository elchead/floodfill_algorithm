import numpy as np
from floodfill import * 

def rgb_test():
      # Dimensions of paint screen 
      M = 8
      N = 8
      rgb = np.array([1,2,3])
      two = np.array([5,5,5])
      zero = np.array([0,0,0])
      screen_rgb = [[rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb], 
                  [rgb, rgb, rgb, rgb, rgb, rgb, zero, zero], 
                  [rgb, zero, zero, rgb, rgb, zero, rgb, rgb], 
                  [rgb, two, two, two, two, zero, rgb, zero], 
                  [rgb, rgb, rgb, two, two, zero, rgb, zero], 
                  [rgb, rgb, rgb, two, two, two, two, zero], 
                  [rgb, rgb, rgb, rgb, rgb, two, rgb, rgb], 
                  [rgb, rgb, rgb, rgb, rgb, two, two, rgb]]


      floodfill_rgb(screen_rgb,M,N,4,4,8,8,8)
      print ("Updated RGB colors after call to floodfill:")
      for i in range(M):
            for j in range(N):
                  print(screen_rgb[i][j], end = ' ')
            print()



def bw_test():
    screen = [[1, 1, 1, 1, 1, 1, 1, 1], 
          [1, 1, 1, 1, 1, 1, 0, 0], 
          [1, 0, 0, 1, 1, 0, 1, 1], 
          [1, 2, 2, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 2, 2, 0], 
          [1, 1, 1, 1, 1, 2, 1, 1], 
          [1, 1, 1, 1, 1, 2, 2, 1]]

    # Dimensions of paint screen 
    M = 8
    N = 8
    floodfill_bw(screen,M,N,4,4,3)
    answer = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1], [1, 3, 3, 3, 3, 0, 1, 0], [1, 1, 1, 3, 3, 0, 1, 0], [1, 1, 1, 3, 3, 3, 3, 0], [1, 1, 1, 1, 1, 3, 1, 1], [1, 1, 1, 1, 1, 3, 3, 1]]
    print ("Updated B/W colors after call to floodfill:")
    for i in range(M):
      for j in range(N):
            print(screen[i][j], end = ' ')
      print()
    assert screen == answer

bw_test()
rgb_test()