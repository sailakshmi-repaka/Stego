# Project Description
This project implements image-based steganography to hide secret messages within image pixels using OpenCV. The encrypted message is embedded into an image, and only users with the correct passcode can decrypt and retrieve the hidden text.

# Technologies Used
**Python** – Main programming language

**OpenCV (cv2)** – For image processing

**OS & File Handling** – To manage encryption, decryption, and passcode storage

# How to Run the Project
 ## Encrypt a Message into an Image
  Place your image (e.g., mypic.jpeg) in the project folder.
 ### Run the encryption script:
     python encrypt.py
     
 Enter the secret message and a passcode when prompted.
 
 The encrypted image (encryptedImage.jpg) will be saved in the same folder.
 ## Decrypt the Hidden Message
 ### Run the decryption script:
   python decrypt.py
   
Enter the correct passcode to retrieve the hidden message.

   
 ## Security Features
 **Passcode Protection** – Only users with the correct passcode can decrypt the message.
 
 **Pixel Manipulation** – The message is stored in the image’s RGB values.
 
 **Automatic Message Retrieval** – No need to manually enter message length.

 ## License
This project is for educational purposes. Feel free to modify and enhance it!
