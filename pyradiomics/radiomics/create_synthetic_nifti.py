"""
Running this will leave you with image.nii (random values) and mask.nii (0/1 values).
"""
import nibabel as nib
import numpy as np

# Create some random 3D data
data = np.random.rand(64, 64, 64)

# Create an identity affine (so no spatial transform)
affine = np.eye(4)

# Save the image data
img = nib.Nifti1Image(data, affine)
nib.save(img, 'image.nii')

# Create and save a mask (thresholded at 0.5)
mask_data = (data > 0.5).astype(np.uint8)
mask = nib.Nifti1Image(mask_data, affine)
nib.save(mask, 'mask.nii')

print("Generated image.nii and mask.nii")
