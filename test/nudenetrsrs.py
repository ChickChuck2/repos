# Import module
from nudenet import NudeDetector

# initialize detector (downloads the checkpoint file automatically the first time)
detector = NudeDetector() # detector = NudeDetector('base') for the "base" version of detector.

# Detect single image
det = detector.detect('des2.jpg')
# Returns [{'box': LIST_OF_COORDINATES, 'score': PROBABILITY, 'label': LABEL}, ...]
print(det)

if det == [{'label': 'EXPOSED_BELLY'}]:
    print("BARRIGA EXPOSTA")