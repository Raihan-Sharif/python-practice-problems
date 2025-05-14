
def isLandscape(width, height):

    if width > height:
        return "Landscape"
    else:
        return "Portrait"
    
# Example of usage
width = 1920
height = 1080
print(isLandscape(width, height)) 