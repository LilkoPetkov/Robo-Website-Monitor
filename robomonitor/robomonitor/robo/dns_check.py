import dns.resolver
import uuid
from .models import Websites


class DNS:
    def __init__(self, domain):
        self.domain = domain

    @staticmethod
    def generate_record():
        return str(uuid.uuid4())

    def get_website(self):
        return Websites.objects.get(domain=self.domain)
    
    def attach_record(self):
        website = self.get_website()
        record = self.generate_record()

        if website:
            website.verification_record = record
            website.save()

    def record_check(self):
        website = self.get_website()
        response: dns.resolver.Answer = dns.resolver.resolve(website.domain, 'TXT')

        if website:
            for data in response:
                txt_records = str(data)
                record = website.verification_record

                if record in txt_records:
                    website.verification_status = "VERIFIED"
                    website.save()
