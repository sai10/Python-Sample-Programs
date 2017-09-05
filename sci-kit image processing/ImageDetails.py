import skimage.io as io
image = io.imread("dataset\img (2).jpg")

# ndarray attributes
print("Shape-",image.shape)         # Tuple of array dimensions.
print("Size-",image.size)           # Number of elements in the array.
print("DataType",image.dtype)       # Data-type of the array’s elements.
print("ItemSize-",image.itemsize)   # Length of one array element in bytes.
print("Flags-",image.flags)         # Information about the memory layout of the array.
print("nbytes-",image.nbytes)       # Total bytes consumed by the elements of the array.
print("ndims-",image.ndim)          # Number of array dimensions.
print("T-",image.T)                 # Same as self.transpose(), except that self is returned if self.ndim < 2.
print("Data-",image.data)           # Python buffer object pointing to the start of the array’s data.
print("flat-",image.flat)           # A 1-D iterator over the array.    
print("imag-",image.imag)           # The imaginary part of the array.
print("real-",image.real)           # The real part of the array.
print("strides-",image.strides)     # Tuple of bytes to step in each dimension when traversing an array.
print("base-",image.base)           # Base object if memory is from some other object.

print("min-",image.min())
print("max-",image.max())
print("mean-",image.mean())
print("sum-",image.sum())