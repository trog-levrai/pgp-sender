import src.mail
import src.encrypt

if __name__ == "__main__":
    gpgEngine = src.encrypt.GPGEngine()
    message = str(gpgEngine.encryptMail("Mail sent using GPG", "9DDDB2C0"))
    src.mail.sendMail("foo@test.com", "ilan.dubois@epita.fr", "PGP Test", message)
