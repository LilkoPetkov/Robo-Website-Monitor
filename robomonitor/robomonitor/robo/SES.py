import boto3
from botocore.exceptions import ClientError
from decouple import config


class SESservice:
    def __init__(self, recipient, status, time):
        self.region = config("REGION")
        self.recipient = recipient
        self.status = status
        self.time = time
        self.ses = boto3.client('ses',
                                region_name=self.region
                                )

    # Needed only for sandbox env, otherwise this can be deleted.
    def is_verified(self):
        response = self.ses.list_identities(
            IdentityType='EmailAddress',
            MaxItems=10
        )

        if self.recipient in response["Identities"]:
            return True
        return False

    # Needed only for sandbox env, otherwise this can be deleted.
    def verify_email(self):
        response = self.ses.verify_email_identity(
            EmailAddress=self.recipient
        )

        return response

    def send_email(self):
        SENDER = config("MAIL_USERNAME")

        SUBJECT = "Your websites was down"

        BODY_TEXT = (f"Your website was down: \r\n"
                     "This email is sent automatically so please do not respond to it. "
                     "Best regards,"
                     "RoboChecker - Wall-E."
                     )
        # Send via email the payment link

        BODY_HTML = f"""<html>
        <head></head>
        <body>
          <h1>Your website was down</h1>
          <p>This email is sent automatically so please do not respond to it.</p>
          
          <p> Today, at {self.time} your website responded with status code:
            {self.status} , please do review the website as soon as possible.
           </p>
           <p> Error detected on: {self.time}</p>
              <p>"Best regards,"</p>
              <p>Wall-E</p>
        </body>
        </html>
        """

        CHARSET = "UTF-8"
        client = boto3.client('ses', region_name=self.region)

        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.recipient,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
