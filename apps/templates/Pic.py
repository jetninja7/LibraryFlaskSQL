from sketchpy import canvas
from sklearn.preprocessing import scale
obj = canvas.sketch_from_svg("Ro.svg", scale=50)
obj.draw()