from Cimpl import *
import random

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

            if rand_column <= get_width(image) - 1 and rand_column >= 0 and rand_row <= get_height(image)-1 and rand_row >= 0:
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        rand_color = get_color(image, rand_column, rand_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x,y,rand_color)
                    
    # Return the scattered image.
    return new_image

image=load_image(choose_file())