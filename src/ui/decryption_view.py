from tkinter import ttk, Text, INSERT, WORD, constants
import services.encryption


class DecryptionView:
    def __init__(self, root, handle_keys, handle_encrypt):
        self._root = root
        self._handle_keys = handle_keys
        self._handle_encrypt = handle_encrypt
        self._frame = None
        self._ciphertext = None
        self._key = None

        self._heading1_font = ("Arial", "18", "bold")
        self._heading2_font = ("Arial", "14", "bold")
        self._body_font = ("Arial", "12")

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _decrypt_message(self):
        ciphertext = self._ciphertext.get("1.0", "end - 1 chars")
        key = self._key.get("1.0", "end - 1 chars")
        key_parts = key.split(",")
        key_modulus = int(key_parts[0][1:])
        key_exponent = int(key_parts[1][1:-1])

        if ciphertext and key:
            plaintext = services.encryption.decrypt_message(
                ciphertext, key_modulus, key_exponent)

        message_label = ttk.Label(
            master=self._frame,
            text="Decrypted message:",
            font=self._heading2_font
        )
        message = Text(self._frame, height=8, wrap=WORD)
        message.insert(INSERT, plaintext)

        message_label.grid(row=7, column=0, columnspan=2,
                           padx=5, pady=5, sticky=constants.W)
        message.grid(row=8, column=0, columnspan=2,
                     padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        keys_button = ttk.Button(
            master=self._frame,
            text="KEYS",
            command=self._handle_keys
        )

        encryption_button = ttk.Button(
            master=self._frame,
            text="ENCRYPTION",
            command=self._handle_encrypt
        )

        frame_label = ttk.Label(
            master=self._frame,
            text="Decryption",
            font=self._heading1_font
        )

        cipher_label = ttk.Label(
            master=self._frame,
            text="Paste the ciphertext here:",
            font=self._heading2_font
        )

        self._ciphertext = Text(self._frame, height=8)

        key_label = ttk.Label(
            master=self._frame,
            text="Give the decryption key:",
            font=self._heading2_font
        )

        self._key = Text(self._frame, height=8)

        decrypt_button = ttk.Button(
            master=self._frame,
            text="DECRYPT",
            command=self._decrypt_message
        )

        keys_button.grid(row=0, column=0, padx=5,
                         pady=5, sticky=constants.W)
        encryption_button.grid(row=0, column=1, padx=5,
                               pady=5, sticky=constants.W)
        frame_label.grid(row=1, column=0, columnspan=2,
                         padx=10, pady=10, sticky=constants.EW)
        cipher_label.grid(row=2, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)
        self._ciphertext.grid(row=3, column=0, columnspan=2,
                              padx=5, pady=5, sticky=constants.EW)
        key_label.grid(row=4, column=0, columnspan=2,
                       padx=5, pady=5, sticky=constants.W)
        self._key.grid(row=5, column=0, columnspan=2,
                       padx=5, pady=5, sticky=constants.EW)
        decrypt_button.grid(row=6, column=0, columnspan=2,
                            padx=10, pady=10, sticky=constants.EW)
        self._frame.grid_columnconfigure(1, weight=1)
