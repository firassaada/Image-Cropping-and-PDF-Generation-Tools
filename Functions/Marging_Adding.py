import numpy as np

def add_margin_to_photo_frame(image, margin_size=10):
    # Create a blank mask
    mask = np.zeros_like(image[:,:,0], dtype=np.uint8)
    
    # Set the outer pixels to white
    mask[:margin_size, :] = 255  # Top edge
    mask[-margin_size:, :] = 255  # Bottom edge
    mask[:, :margin_size] = 255  # Left edge
    mask[:, -margin_size:] = 255  # Right edge
    
    # Replace edge pixels with white in the original image
    result = np.copy(image)
    result[mask != 0] = [255, 255, 255]
    
    return result
