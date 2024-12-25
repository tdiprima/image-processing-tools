import cv2


def draw_coordinates_on_image(image_path, coordinates, output_path, color=(0, 255, 0), radius=5, thickness=2,
                              font_scale=0.5):
    """
    Draws coordinates on an image for visualization and annotation.

    Parameters:
        image_path (str): Path to the input image.
        coordinates (list): List of tuples, each containing (x, y) coordinates to draw.
        output_path (str): Path to save the output annotated image.
        color (tuple): Color of the circles and text (B, G, R).
        radius (int): Radius of the circle for each point.
        thickness (int): Thickness of the circle and text.
        font_scale (float): Font scale for the text.

    Returns:
        None
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    # Draw each coordinate on the image
    for idx, (x, y) in enumerate(coordinates):
        # Draw a circle at the coordinate
        cv2.circle(image, (x, y), radius, color, thickness)
        # Add text annotation near the point
        cv2.putText(image, f"{idx + 1}: ({x},{y})", (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color,
                    thickness)

    # Save the annotated image
    cv2.imwrite(output_path, image)


# Example usage
if __name__ == "__main__":
    # Input image path
    input_image = "../images/testing.jpg"
    # Coordinates to draw (list of (x, y) tuples)
    coordinates_to_draw = [(50, 50), (150, 100), (200, 300)]
    # Output path for the annotated image
    output_image = "output_image.jpg"

    # Draw coordinates on the image
    draw_coordinates_on_image(input_image, coordinates_to_draw, output_image)

    print(f"Annotated image saved at {output_image}")
