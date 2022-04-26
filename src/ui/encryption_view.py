from tkinter import ttk, Message, Text, INSERT, constants
import services.encryption

class EncryptionView:
    def __init__(self, root, handle_keys, handle_decrypt):
        self._root = root
        self._handle_keys = handle_keys
        self._handle_decrypt = handle_decrypt
        self._frame = None
        self._message = None
        self._key = None

        self._heading1_font = ("Arial", "18", "bold")
        self._heading2_font = ("Arial", "14", "bold")
        self._body_font = ("Arial", "12")

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _encrypt_message(self):
        message = self._message.get("1.0", "end - 1 chars")
        key = self._key.get("1.0", "end - 1 chars")
        key_parts = key.split(",")
        key_modulus = int(key_parts[0][1:])
        key_exponent = int(key_parts[1][1:-1])

        if message and key:
            ciphertext = services.encryption.simple_encrypt(message, key_modulus, key_exponent)

        cipher_label = ttk.Label(
            master=self._frame,
            text="Encrypted Message:",
            font=self._heading2_font
        )
        cipher = Text(self._frame, height=15)
        cipher.insert(INSERT, ciphertext)

        cipher_label.grid(row=7, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)
        cipher.grid(row=8, column=0, columnspan=2,
                    padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        keys_button = ttk.Button(
            master=self._frame,
            text="KEYS",
            command=self._handle_keys
        )

        decryption_button = ttk.Button(
            master=self._frame,
            text="DECRYPTION",
            command=self._handle_decrypt
        )

        frame_label = ttk.Label(
            master=self._frame,
            text="Encryption",
            font=self._heading1_font
        )

        message_label = ttk.Label(
            master=self._frame,
            text="Type your message:",
            font=self._heading2_font
        )

        self._message = Text(self._frame, height=6)

        key_label = ttk.Label(
            master=self._frame,
            text="Give the encryption key:",
            font=self._heading2_font
        )

        self._key = Text(self._frame, height=6)

        encrypt_button = ttk.Button(
            master=self._frame,
            text="ENCRYPT",
            command=self._encrypt_message
        )

        keys_button.grid(row=0, column=0, padx=5,
                               pady=5, sticky=constants.W)
        decryption_button.grid(row=0, column=1, padx=5,
                               pady=5, sticky=constants.W)
        frame_label.grid(row=1, column=0, columnspan=2,
                         padx=10, pady=10, sticky=constants.EW)
        message_label.grid(row=2, column=0, columnspan=2,
                           padx=5, pady=5, sticky=constants.W)
        self._message.grid(row=3, column=0, columnspan=2,
                           padx=5, pady=5, sticky=constants.EW)
        key_label.grid(row=4, column=0, columnspan=2,
                       padx=5, pady=5, sticky=constants.W)
        self._key.grid(row=5, column=0, columnspan=2,
                       padx=5, pady=5, sticky=constants.EW)
        encrypt_button.grid(row=6, column=0, columnspan=2,
                            padx=10, pady=10, sticky=constants.EW)
        self._frame.grid_columnconfigure(1, weight=1)
