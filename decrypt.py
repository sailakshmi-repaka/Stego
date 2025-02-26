import cv2

def create_mapping():
    return {i: chr(i) for i in range(255)}

def decrypt_image(image_path, password):
    try:
        with open("passcode.txt", "r") as f:
            correct_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Passcode file not found.")
        return

    if password != correct_password:
        print("YOU ARE NOT AUTHORIZED")
        return

    try:
        with open("metadata.txt", "r") as f:
            message_length = int(f.readline().strip())
    except FileNotFoundError:
        print("Error: Metadata file not found.")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return

    c = create_mapping()
    message = ""
    n, m, z = 0, 0, 0

    for _ in range(message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)

if __name__ == "__main__":
    image_path = "encryptedImage.png"
    user_pass = input("Enter passcode for Decryption: ")
    decrypt_image(image_path, user_pass)