# Instructions for Use (Linux)

## Installation

1. Download the project .zip file to your computer and unzip it.
2. Navigate to the root folder `keysmith-main`.
3. Install the necessary dependencies with this command:
```bash
poetry install
```

## Running the App

Launch the app with this command in the root folder:
```bash
poetry run invoke start
```
This opens a simple graphical user interface with three views:
* Key creation view
* Encryption view
* Decryption view

You can change views by clicking the buttons on the top left corner of the view.

## Key Creation View

You can create a new pair of keys by clicking the `CREATE KEYS` button.
The public and private key will be shown in separate text boxes.
Copy both keys to a safe location. To copy the text, you need to select it with your mouse and then press Ctrl + C.
Make sure that you copy the whole key with the brackets.
You may share the public key freely but **you must keep the private key to yourself**.

![](./images/key_creation_view.png)

## Encryption View

You can encrypt any message you like by typing it to the first text box and pasting the encryption key to the other text box. Then, click the `ENCRYPT` button.
To paste, copy the key to clipboard, click the text box, and press Ctrl + V.
Either of the keys can be used for encryption as long as the other is used for decryption.
* Encrypting the message with the public key ensures that you are the only person who can decrypt the message.
* Encrypting the message with the private key works as a signature: if the recipient can decrypt the message with your public key, they know that the message must be from you and not from anybody else. Note: If you have shared the public key with several people, do not use the private key to encrypt any information that they are not all allowed to see.

The encrypted message will appear in a third text box. You may copy it the same way as the keys.
If you give an invalid key, error message will appear in the third box.

![](./images/encryption_view.png)

## Decryption View

You can decrypt a message by pasting the ciphertext (the encrypted message) to the first text box and the decryption key to the other box. Then, click the `DECRYPT` button.
The decrypted message should appear in a third text box. If you give an incorrect key, error message will appear in that box.

![](./images/decryption_view.png)

## Closing the App

The application closes by clicking the `x` button on the top right corner of the window.
The app does not store any data so make sure that you have copied and saved all the information you might want to use again.
