import gnupg
import os
import getpass

class GPGEngine:

    def __init__(self, keyId):
        home = os.path.expanduser('~')
        homedir = os.path.join(home, ".gnupg")
        self.gpg = gnupg.GPG(homedir=homedir)
        self.passphrase = "" if keyId == "" else getpass.getpass()
        self.senderId = keyId

    def encryptMail(self, message, keyId):
        return self.gpg.encrypt(message, keyId, default_key=self.senderId, passphrase=self.passphrase)
