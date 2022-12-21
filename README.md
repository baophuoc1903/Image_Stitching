# About this project
- *Python implementation for SIFT (Scale-Invariant Feature Transform)*
- *Image Panorama with open-cv*

**Steps for stitching image:** 
  - Step 1: Select the middle photo as the center to align for the left images and right images
  - Step 2: For each image in left and right part:
    - Compute key points/descriptor
    - Computing homography
    - Warping and blending images
  - Step 3: Warping and blending 2 part into panorama image

**How to run:**
```
python main.py
```
  

