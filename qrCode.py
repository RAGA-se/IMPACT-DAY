import qrcode
import os
from PIL import Image

def generate_qr_code(url_or_path, output_filename="qrcode.png", size=10):
    """
    Generate a QR code that links to a URL or local HTML file.
    
    Parameters:
    url_or_path (str): URL or file path to link to
    output_filename (str): Filename to save the QR code image
    size (int): Size of the QR code (higher number = larger image)
    
    Returns:
    str: Path to the generated QR code image
    """
    # Check if the input is a local file path
    if os.path.exists(url_or_path) and url_or_path.endswith('.html'):
        # For local files, create a file:// URL
        # On Windows, we need to add an extra / and convert backslashes
        if os.name == 'nt':  # Windows
            absolute_path = os.path.abspath(url_or_path).replace('\\', '/')
            url = f"file:///{absolute_path}"
        else:  # Unix-like systems
            absolute_path = os.path.abspath(url_or_path)
            url = f"file://{absolute_path}"
    else:
        # Assume it's already a URL
        url = url_or_path
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(output_filename)
    
    return output_filename

# Example usage
if __name__ == "__main__":
    # Change these values to match your HTML file location
    html_file_path = "index.html"  # Path to your HTML file
    output_qr_image = "my_webpage_qr.png"  # Name for the output QR code image
    
    qr_path = generate_qr_code(html_file_path, output_qr_image)
    print(f"QR code generated and saved as {qr_path}")
    
    # Optional: Open the generated QR code image
    try:
        Image.open(qr_path).show()
    except Exception as e:
        print(f"Could not display the image: {e}")