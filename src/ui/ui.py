from ui.key_creation_view import KeyCreationView
from ui.encryption_view import EncryptionView
from ui.decryption_view import DecryptionView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_key_creation_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_key_creation_view(self):
        self._hide_current_view()

        self._current_view = KeyCreationView(
            self._root,
            self._show_encryption_view,
            self._show_decryption_view
        )

        self._current_view.pack()

    def _show_encryption_view(self):
        self._hide_current_view()

        self._current_view = EncryptionView(
            self._root,
            self._show_key_creation_view,
            self._show_decryption_view
        )

        self._current_view.pack()

    def _show_decryption_view(self):
        self._hide_current_view()

        self._current_view = DecryptionView(
            self._root,
            self._show_key_creation_view,
            self._show_encryption_view
        )

        self._current_view.pack()
