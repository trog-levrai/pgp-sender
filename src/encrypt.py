import gnupg
import os

class GPGEngine:

    def __init__(self):
        home = os.path.expanduser('~')
        homedir = os.path.join(home, ".gnupg")
        self.gpg = gnupg.GPG(homedir=homedir)

    def encryptMail(self, message, keyId):
        return self.gpg.encrypt(message, keyId)
