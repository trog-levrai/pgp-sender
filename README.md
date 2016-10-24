# pgp-sender

PGPSender sends PGP encryptes emails to a csv list of keyID/adress

Please find the required packages to run the script in requirements.txt

The main script is in the src directory: script.py

For a complete list of options:

```shell
./script.py --help
```
To send emails you need to have a Sendgrid API key and export it under *SENDGRID_API_KEY* environment variable.
