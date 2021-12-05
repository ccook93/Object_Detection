The labeled dataset has coordinate information for images resolutions of 5184 x 3888 px.

The speed up the processing of the future training and evaluation sets the images were downsized to (original res/100), making the resized photos 518 x 388 px.

The original transformer csv spreadsheet will be used in an effort to save time and all coordinates will be calculated as follows:

x1 and y1 denote the new x and y coordinates for the resized image. 
x0 and y0 denote the original x and y coordinates for the original image resolution.

x1  = [ x0 * (518/5184)]

y1  = [ y0 * (388/3888)]

