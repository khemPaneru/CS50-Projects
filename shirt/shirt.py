import sys
import os
from PIL import Image, ImageOps

def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check extensions
    valid_exts = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_exts or output_ext not in valid_exts:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    if not os.path.isfile(input_file):
        sys.exit("Input does not exist")

    try:
        # Open input image and shirt
        photo = Image.open(input_file)
        shirt = Image.open("shirt.png")

        # Resize and crop input image to match shirt's size
        photo = ImageOps.fit(photo, shirt.size)

        # Overlay shirt using shirt as mask for transparency
        photo.paste(shirt, shirt)

        # Save result
        photo.save(output_file)

        #  Show the final image in the default image viewer
        photo.show()

    except Exception as e:
        sys.exit(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
