from tkinter import ttk, Message, Text, INSERT, constants
import services.keys

class KeyCreationView:
    def __init__(self, root, handle_encrypt, handle_decrypt):
        self._root = root
        self._handle_encrypt = handle_encrypt
        self._handle_decrypt = handle_decrypt
        self._frame = None

        self._heading1_font = ("Arial", "18", "bold")
        self._heading2_font = ("Arial", "14", "bold")
        self._body_font = ("Arial", "12")

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_keys(self):
        key_tuple = services.keys.create_keys()
        public_label = ttk.Label(
            master=self._frame,
            text="Public Key:",
            font=self._heading2_font
        )
        public_text = f"{key_tuple[0]}"
        public_key = Text(self._frame, height=10)
        public_key.insert(INSERT, public_text)

        private_label = ttk.Label(
            master=self._frame,
            text="Private Key:",
            font=self._heading2_font
        )
        private_text = f"{key_tuple[1]}"
        private_key = Text(self._frame, height=15)
        private_key.insert(INSERT, private_text)

        public_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=constants.W)
        public_key.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)
        private_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=constants.W)
        private_key.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        encryption_button = ttk.Button(
            master=self._frame,
            text="ENCRYPTION",
            command=self._handle_encrypt
        )

        decryption_button = ttk.Button(
            master=self._frame,
            text="DECRYPTION",
            command=self._handle_decrypt
        )

        frame_label = ttk.Label(
            master=self._frame,
            text="Key Creation",
            font=self._heading1_font
        )

        text = """Click the button below to create a secure key pair.\nCopy the created keys to a safe location. You can share the public key freely but you must keep the private key to yourself."""

        instructions = Message(
            self._frame,
            text=text,
            width=1400,
            font=self._body_font
        )

        create_button = ttk.Button(
            master=self._frame,
            text="CREATE KEYS",
            command=self._create_keys
        )

        encryption_button.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        decryption_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        frame_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=constants.EW)
        instructions.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=constants.W)
        create_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=constants.EW)
        self._frame.grid_columnconfigure(1, weight=1)
