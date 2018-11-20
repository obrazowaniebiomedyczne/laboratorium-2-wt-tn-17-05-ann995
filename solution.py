import numpy as np


# Zadanie na ocenę dostateczną
def renew_pictures():
    img = []
	kernel = np.ones((3, 3), np.uint8)
	kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)

    	for i in range(1, 5):
		if (i == 1):
		    img.append(cv.imread('figures/crushed.png', 0))
		else:
		    img.append(cv.imread('figures/crushed'+str(i)+'.png', 0))
		
		opening = cv.morphologyEx(img[i-1], cv.MORPH_OPEN, kernel, iterations=1)
		closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel, iterations=1)
		opening = cv.morphologyEx(closing, cv.MORPH_OPEN, kernel, iterations=2)
		closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel, iterations=2)
		opening = cv.morphologyEx(opening, cv.MORPH_OPEN, kernel, iterations=3)
		closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel, iterations=2)
		
		if (i == 1):
		    cv.imwrite('figures/result_crushed.jpg', closing)
		else:
		    cv.imwrite('figures/result_crushed'+str(i)+'.png', closing)

    pass


# Zadanie na ocenę dobrą
def own_simple_erosion(image):
    kernel = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]], np.uint8)
    erosion = cv2.erode(image,kernel,iterations = 5)

return erosion




# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])

    # ---------------
    # Do uzupełnienia
    # ---------------

    return new_image
