""" A crack team of love scientists from OkEros (a hot new dating site) 
have devised a way to represent dating profiles as rectangles on a two-dimensional plane.

They need help writing an algorithm to find the intersection of two users' 
love rectangles. They suspect finding that intersection is the key to a matching 
algorithm so powerful it will cause an immediate acquisition by Google or Facebook 
or Obama or something.

Two rectangles overlapping a little. It must be love.

Write a function to find the rectangular intersection of two given love rectangles.

As with the example above, love rectangles are always "straight" and never "diagonal." 
More rigorously: each side is parallel with either the x-axis or the y-axis.

They are defined as dictionaries like this:

  my_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}

Your output rectangle should use this format as well.  """

# Start coding from here
def rectangle_intersect(rectangle1,rectangle2):
  rectangle1_x_indicies=[v for v in range(rectangle1['left_x'],rectangle1['left_x']+rectangle1['width']+1)]
  rectangle1_y_indicies=[v for v in range(rectangle1['bottom_y'],rectangle1['bottom_y']+rectangle1['height']+1)]
  rectangle2_x_indicies=[v for v in range(rectangle2['left_x'],rectangle2['left_x']+rectangle2['width']+1)]
  rectangle2_y_indicies=[v for v in range(rectangle2['bottom_y'],rectangle2['bottom_y']+rectangle2['height']+1)]
  req_rectangle_x_indicies=list(set(rectangle1_x_indicies).intersection(rectangle2_x_indicies))
  req_rectangle_y_indicies=list(set(rectangle1_y_indicies).intersection(rectangle2_y_indicies))
  req_rectangle={'left_x':req_rectangle_x_indicies[0],
            'bottom_y':req_rectangle_y_indicies[0],
            'width':len(req_rectangle_x_indicies)-1,
            'height':len(req_rectangle_y_indicies)-1}
  return req_rectangle
rectanglelove1 = {

    'left_x'   : 1,
    'bottom_y' : 1,

    'width'    : 6,
    'height'   : 3,

}
rectanglelove2 = {

    'left_x'   : 6,
    'bottom_y' : 2,

    'width'    : 1,
    'height'   : 3,

}
print(rectangle_intersect(rectanglelove1,rectanglelove2))
