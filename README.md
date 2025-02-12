# Steganography With Python(IBM)

Overview

This project demonstrates steganography—the technique of hiding secret messages inside an image to ensure secure communication. The system allows users to encode a secret message into an image and later retrieve it using a passcode for decryption. The encoded message remains hidden and undetectable to the naked eye.

Features

Message Encoding: Embed secret messages within an image.    
Password Protection: Ensure only authorized users can decode the hidden message.     
Simple and User-Friendly: Easy-to-use interface with simple inputs for encoding and decoding.      
Error Handling: Alerts the user if the image is not found or the passcode is incorrect.    

Technologies Used

Python: A versatile programming language used to implement the system.     
OpenCV: Used for image manipulation, including reading, editing, and saving images.       
Steganography: Hides messages within the image by altering pixel values, making the message invisible to the user.     
Character Encoding: Maps characters to numeric values and embeds them within the image's pixel values.    

Installation

Prerequisites:      
Python 3.6+ installed on your system.        
OpenCV Python library installed.  

Steps to Install 

Clone the repository:
git clone https://github.com/your-username/Steganography-with-Python.git    
Install the necessary libraries:  
pip install opencv-python         
Download or place the image (Treeimage.jpg) where it’s accessible by the program.       

![Screenshot 2025-02-12 185904](https://github.com/user-attachments/assets/f164fced-5c5c-41bd-b783-3851141b5b45)


Usage:  
Step 1: Encoding a Message  
Input: Provide the secret message and passcode.The secret message will be embedded into the image (Treeimage.jpg), and the result will be saved as Treebranch.jpg.     
Step 2: Decoding the Message  
Input: Provide the passcode to decrypt the secret message from Treebranch.jpg.  


Future Scope    
Encryption: Add encryption algorithms to encrypt the hidden message for additional security before embedding.    
Compression: Implement compression techniques to allow longer messages to be hidden without significantly altering the image.   
Cross-Format Support: Extend the project to support other image formats such as PNG, BMP, and GIF.   
Multi-Layer Embedding: Explore embedding multiple messages in one image using different channels or layers.    
 

License
This project is licensed under the MIT License - see the LICENSE file for details.
