import subprocess

from datetime import datetime
import aiohttp
import asyncio
from celery import shared_task
from .models import *
from .SES import SESservice


@shared_task
def scheduled_website_check_24() -> object:
    urls = [url.domain for url in Websites.objects.filter(checker_rate=24).filter(verification_status="VERIFIED")]

    for url in urls:
        site = Websites.objects.get(domain=url)

        resp = subprocess.check_output(['curl', '-o', '/dev/null', '-w',
                                            '"Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} \n"',
                                            url])

        if resp:
            speed_data = bytes.decode(resp, 'utf-8')
        else:
            speed_data = "Could not fetch any website performance data"

        async def main():
            async with aiohttp.ClientSession() as session:
                async with session.get("http://" + url, ) as response:
                    if response.status != 200 and response.status != 301 and response.status != 302:
                        SES = SESservice(recipient="lilko.petkovv@gmail.com", status=response.status, time=datetime.utcnow())
                        SES.send_email()

                    log = await Logs.objects.acreate(status_code=response.status, response_headers=response.headers,
                                                     website_speed=speed_data, website=site)

        asyncio.run(main())


@shared_task
def scheduled_website_check_5_minutes() -> object:
    urls = [url.domain for url in Websites.objects.filter(checker_rate=5).filter(verification_status="VERIFIED")]

    for url in urls:
        site = Websites.objects.get(domain=url)

        resp = subprocess.check_output(['curl', '-o', '/dev/null', '-w',
                                            '"Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} \n"',
                                            url])

        if resp:
            speed_data = bytes.decode(resp, 'utf-8')
        else:
            speed_data = "Could not fetch any website performance data"

        async def main():
            async with aiohttp.ClientSession() as session:
                async with session.get("http://" + url, ) as response:
                    if response.status != 200 and response.status != 301 and response.status != 302:
                        SES = SESservice(recipient="lilko.petkovv@gmail.com", status=response.status, time=datetime.utcnow())
                        SES.send_email()

                    log = await Logs.objects.acreate(status_code=response.status, response_headers=response.headers,
                                                     website_speed=speed_data, website=site)

        asyncio.run(main())


@shared_task
def scheduled_website_check_15_minutes() -> object:
    urls = [url.domain for url in Websites.objects.filter(checker_rate=15).filter(verification_status="VERIFIED")]

    for url in urls:
        site = Websites.objects.get(domain=url)

        resp = subprocess.check_output(['curl', '-o', '/dev/null', '-w',
                                            '"Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} \n"',
                                            url])

        if resp:
            speed_data = bytes.decode(resp, 'utf-8')
        else:
            speed_data = "Could not fetch any website performance data"

        async def main():
            async with aiohttp.ClientSession() as session:
                async with session.get("http://" + url, ) as response:
                    if response.status != 200 and response.status != 301 and response.status != 302:
                        SES = SESservice(recipient="lilko.petkovv@gmail.com", status=response.status, time=datetime.utcnow())
                        SES.send_email()

                    log = await Logs.objects.acreate(status_code=response.status, response_headers=response.headers,
                                                     website_speed=speed_data, website=site)

        asyncio.run(main())


@shared_task
def scheduled_website_check_30_minutes() -> object:
    urls = [url.domain for url in Websites.objects.filter(checker_rate=30).filter(verification_status="VERIFIED")]

    for url in urls:
        site = Websites.objects.get(domain=url)

        resp = subprocess.check_output(['curl', '-o', '/dev/null', '-w',
                                            '"Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} \n"',
                                            url])

        if resp:
            speed_data = bytes.decode(resp, 'utf-8')
        else:
            speed_data = "Could not fetch any website performance data"

        async def main():
            async with aiohttp.ClientSession() as session:
                async with session.get("http://" + url, ) as response:
                    if response.status != 200 and response.status != 301 and response.status != 302:
                        SES = SESservice(recipient="lilko.petkovv@gmail.com", status=response.status, time=datetime.utcnow())
                        SES.send_email()

                    log = await Logs.objects.acreate(status_code=response.status, response_headers=response.headers,
                                                     website_speed=speed_data, website=site)

        asyncio.run(main())


@shared_task
def scheduled_website_check_60_minutes() -> object:
    urls = [url.domain for url in Websites.objects.filter(checker_rate=60).filter(verification_status="VERIFIED")]

    for url in urls:
        site = Websites.objects.get(domain=url)

        resp = subprocess.check_output(['curl', '-o', '/dev/null', '-w',
                                            '"Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} \n"',
                                            url])

        if resp:
            speed_data = bytes.decode(resp, 'utf-8')
        else:
            speed_data = "Could not fetch any website performance data"

        async def main():
            async with aiohttp.ClientSession() as session:
                async with session.get("http://" + url, ) as response:
                    if response.status != 200 and response.status != 301 and response.status != 302:
                        SES = SESservice(recipient="lilko.petkovv@gmail.com", status=response.status, time=datetime.utcnow())
                        SES.send_email()

                    log = await Logs.objects.acreate(status_code=response.status, response_headers=response.headers['content-type'],
                                                     website_speed=speed_data, website=site)

        asyncio.run(main())
