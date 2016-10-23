from optparse import OptionParser
import src.mail
import src.encrypt
import csv

if __name__ == "__main__":
    parser = OptionParser(description="This script is used to send GPG encrypted emails to a list of recipients.")
    parser.add_option("-f", "--file", dest="file", help="CSV file containing the list. The first column should have Key IDs and the second one the adress to send to", metavar="FILE", default="")
    parser.add_option("-s", "--subject", dest="subject", help="sets the email subject", metavar="STR", default="")
    args, trash = parser.parse_args()
    with open(args.file, 'r') as csvFile:
        gpgEngine = src.encrypt.GPGEngine()
        csvData = csv.reader(csvFile, delimiter=',')
        for i in csvData:
            message = str(gpgEngine.encryptMail("Mail sent using GPG", i[0]))
            src.mail.sendMail("foo@test.com", i[1], args.subject, message)
