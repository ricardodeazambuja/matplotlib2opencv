import cv2
import numpy
import matplotlib.pyplot as plt

# The idea for this hack came from this code: https://gist.github.com/joferkington/9138655

def annotate_mpl2cv(img_cv,text,text_posX,text_posY,text_font):
    '''
    Annotates an OpenCV image using Matplotlib!
    
    Parameters:
    
    img_cv: OpenCV image
    
    text: text to be added
    
    text_posX: X position
    text_posY: Y position
    text_font: font dictionary
    
    Examples:
    text_font = {'family': 'serif',
                 'color':  'white',
                 'weight': 'bold',
                 'size': 30,
                }

    text = r'an equation: $E=mc^2$'
    
    '''

    img_plt = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB ) # converts to numpy style

    fig = plt.figure(figsize=(img_cv.shape[1]/100., img_cv.shape[0]/100.), dpi=100)

    ax = plt.gca()
    ax.imshow(img_plt)
    ax.text(text_posX, text_posY, text, fontdict=text_font)
    plt.axis('off')
    fig.canvas.draw()
    buf = fig.canvas.tostring_rgb()
    ncols, nrows = fig.canvas.get_width_height()
    img_cv[:] = cv2.cvtColor(
                    numpy.fromstring(buf, dtype=numpy.uint8).reshape(nrows, ncols, 3),
                    cv2.COLOR_BGR2RGB)
    plt.close()
    
    return img_cv
