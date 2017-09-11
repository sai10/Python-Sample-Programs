from skimage.viewer import ImageViewer
from skimage import data


image = data.astronaut()
viewer = ImageViewer(image)
viewer.show()


#               or

#   import skimage.io as io
#   image = io.imread("dataset\img (2).jpg")
#   viewer = ImageViewer(image)
#   viewer.show()


