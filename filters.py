""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""

from Cimpl import *
import random


def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image




def weighted_grayscale(image):
    """
    (Cimpl.image) -> Cimpl.image
    
    file=choose_file()
    image= load_image(file)
    takes different pixel color values
    change them based on the values given
    gives a better grayscale
    
    """    
    new_image = copy(image)
    for x,y,(r,g,b) in image:
        brightness = (r * 0.299 + g * 0.587 + b * 0.114)
        new_color=create_color(brightness,brightness,brightness)
        set_color(new_image,x,y,new_color)
       
    return new_image




def extreme_contrast(image):
    """
    (Cimpl.image) -> Cimpl.image
    
    file=choose_file()
    image= load_image(file)
   
    check the red green and blue value of each pixel
    if the values of colour is above 128, goes to very bright(255)
    if below 128 goes to  dark (0)
    this gives contrast of colours
    
    """      
    new_image = copy(image)
    
    for x,y,(r,g,b) in image:
        if r >= 128:
            r_contrast=255
        else:
            r_contrast = 0
            
        if (g >= 128):
            g_contrast=255
        else:
            g_contrast = 0
            
        if (b >= 128):
            b_contrast = 255
        else:
            b_contrast = 0
        new_color=create_color(r_contrast,g_contrast,b_contrast)
        set_color(new_image,x,y,new_color)
            
    return new_image
        




def sepia_tint(image):
    """
    (Cimpl.image) -> Cimpl.image
    
    file=choose_file()
    image= load_image(file)
    
    takes the image and runs it through grayscale
    
    3 ranges are set up and all colours are altered to certain values depending on range
    
    """      
    gray_image= weighted_grayscale(image)
    for x,y,(r,g,b) in gray_image:
        
        if r < 63:
            r = r * 1.1
            b = b * 0.9
        elif r >= 63 and r < 191:
            r = r * 1.15
            b = b * 0.85
        else:
            b = b * 0.93
            r = r * 1.08
        new_color = create_color(r,g,b)
        set_color(gray_image,x,y,new_color)
        
    return gray_image




def _adjust_component(amount):
    """
    (int) -> int
  changes the value of number depending on range set up that the original number is tested  in
  function is never called by user however, it is called by posterize function to find correct value to posterize to
    
    """      
    if amount < 64:
        amount = 31
    elif amount < 128:
        amount = 95
    elif amount < 192:
        amount = 159
    else:
        amount = 223
        
    return amount
    
      


def posterize(image):
    """
    (Cimpl.image) -> Cimpl.image
    
    file=choose_file()
    image= load_image(file)
    
    using the function above adjust the values of the colours and reprint new image 
    
    """      
    new_image = copy(image)
    for x,y,(r,g,b) in image:
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        
        new_color = create_color(r,g,b)
        set_color(new_image,x,y,new_color)
    return new_image




def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red + right_red + center_red ) // 5

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green + right_green + center_green ) // 5

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue + right_blue + center_blue ) // 5

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target




def detect_edges(image,threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that contains a copy of the original image that has been modified using edge detection
    
    >>>image=load_image(choose_file())
    >>>filtered = detect_edges(image,10.0)
    >>>show(filtered)
    """
    new_image = copy(image)
    black = create_color(0,0,0)
    white = create_color(255,255,255)
    
    for y in range(0,get_height(image) - 1):
        for x in range(0,get_width(image)):
            r,g,b = get_color(image,x,y)
            r_check,g_check,b_check = get_color(image,x,y+1)
            
            brightness=(r + g + b) // 3
            brightness2=(r_check + g_check + b_check) // 3
            
            if abs(brightness-brightness2) > threshold:
                set_color(new_image,x,y,black)
            else:
                set_color(new_image,x,y,white)
                
    return new_image

    
    
    
def detect_edges_better(image,threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image
    Return a new image that contains a copy of the original image that has been modified using edge detection
    
    >>>image=load_image(choose_file())
    >>>filtered = detect_edges(image,10.0)
    >>>show(filtered)
    """
    new_image=copy(image)
    black=create_color(0,0,0)
    white=create_color(255,255,255)
    
    for y in range(0,get_height(image) - 1):
        for x in range(0,get_width(image) - 1):
            r,g,b = get_color(image,x,y)
            
            r_check, g_check, b_check = get_color(image,x,y + 1)
            r_check2, g_check2, b_check2 = get_color(image,x + 1,y)
            
            brightness = (r + g + b) // 3
            brightness2 = (r_check + g_check + b_check) // 3
            brightness3 = (r_check2 + g_check2 + b_check2) // 3
            
            if abs(brightness - brightness2) > threshold or abs(brightness - brightness3) > threshold:
                set_color(new_image,x,y,black)
            else:
                set_color(new_image,x,y,white)
                
    return new_image





def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x,y,(r,g,b) in image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        
        row_and_column_are_in_bounds = False
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = random.randint(0,10)
            rand2 = random.randint(0,10)
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            rand_column = x + rand1
            rand_row = y + rand2
            
            # Determine if the random coordinates are in bounds.

            if rand_column <= get_width(image) - 1 and rand_column >= 0 and rand_row <= get_height(image) - 1 and rand_row >= 0:
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        rand_color = get_color(image, rand_column, rand_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, rand_color)
                    
    # Return the scattered image.
    return new_image

