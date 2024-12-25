import SimpleITK as sitk

try:
    image = sitk.ReadImage("image.nii")
    mask = sitk.ReadImage("mask.nii")
    print("Files are readable!")
except Exception as e:
    print("Error reading files:", e)
