"""
Ensure that your image and mask are in a compatible format, such as .nii, .mha, .nrrd, or .dcm
"""
import json

from radiomics import featureextractor

# Paths to the input image and mask
image_path = "image.nii"  # image file
mask_path = "mask.nii"  # mask file

# Initialize the feature extractor
extractor = featureextractor.RadiomicsFeatureExtractor()

# Print available settings (optional)
print("Current settings:")
print(extractor.settings)

# Extract features
print("\nExtracting features...")
features = extractor.execute(image_path, mask_path)

# Display features
print("\nExtracted features:")
for feature_name, value in features.items():
    print(f"{feature_name}: {value}")

# Save the features to a JSON file
output_file = "radiomics_features.json"
with open(output_file, "w") as f:
    json.dump(features, f, indent=4)

print(f"\nFeatures saved to {output_file}")
