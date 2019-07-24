""" 
SYSC 1005 A Fall 2018.

User Interface to use filters
"""

from filters import *
from Cimpl import *

load_status = False

def UI_display():
    print("L)oad image")
    print("B)lur  E)dge detect  P)osterize  S)catter  T)int sepia \nW)eighted grayscale X)treme contrast ")
    print("Q)uit")
    return


def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    file = choose_file()
    
    if file == "":
        sys.exit("File Open cancelled, exiting program")
    img = load_image(file)

    return img


while(True):
    UI_display()
    output=input(":")
    
    if output not in ["L", "B", "E", "P", "S", "T", "W", "X", "Q"]:
        print("No such command")
    
    else:
        
        if output == "L":
            img = get_image()
            load_status = True
            show(img)
            
        if output == "Q":
            sys.exit("exiting program")        
            
        if load_status == True:
            
    
            if output == "B":
                img = blur(img) 
                show(img)
        
    
            if output == "E":
                while True:
                    thres=int(input("Threshold (0-256)"))
                    if thres >= 0 and thres <= 256:
                        img = detect_edges_better(img,thres)
                        show(img)
                        break
                    else:
                        print("That values is not within the expected range")
    
    
            if output == "P":
                img=posterize(img)
                show(img)

    
            if output== "S":
                img = scatter(img)
                show(img)
                
    
            if output == "T":
                img = sepia_tint(img)
                show(img)
                
            
            if output == "W":
                img = weighted_grayscale(img)
                show(img)
                
                
            if output == "X":
                img = extreme_contrast(img)
                show(img)

              
        else:
            print("No image has been loaded")