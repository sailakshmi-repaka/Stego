
import cv2
import os
import sys

def create_mapping():
    return {chr(i): i for i in range(255)}

def encrypt_image(image_path, message, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return

    d = create_mapping()
    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")  # Open encrypted image (Windows)
    print("Encryption complete. Image saved as", output_path)

    with open("metadata.txt", "w") as f:
        f.write(f"{len(message)}\n")

if __name__ == "__main__":
    image_path = "pic.png"
    output_path = "encryptedImage.png"
    
    msg = input("Enter secret message: ")
    passcode = input("Enter a passcode: ")
    encrypt_image(image_path, msg, output_path)
    
    with open("passcode.txt", "w") as f:
        f.write(passcode)