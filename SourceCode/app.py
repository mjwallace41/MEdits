import os
from videoGen import generate_slideshow



# Example usage
if __name__ == "__main__":
    image_dir = "images"
    music_dir = "songs"
    output_path = "output/final_video.mp4"

    # Load image file paths
    image_paths = [
        os.path.join(image_dir, fname)
        for fname in os.listdir(image_dir)
        if fname.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    if len(image_paths) < 2:
        print("Please add at least two images to the 'images' folder.")
    else:
        generate_slideshow(image_paths, music_dir, output_path)
