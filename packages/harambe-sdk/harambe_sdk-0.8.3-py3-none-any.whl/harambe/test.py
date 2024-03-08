import asyncio
import re
from typing import Any

from playwright.async_api import Page

from harambe import SDK


@SDK.scraper(domain="https://www.microchip.com/", stage="detail")
async def scrape(sdk: SDK, url: str, context: Any, *args: Any, **kwargs: Any) -> None:
    page: Page = sdk.page
    await page.goto(url)
    await page.wait_for_selector(
        '//td[contains(text(),"Bid Number")]/following-sibling::td[1][@class="tableText-01"]'
    )
    post_title = await page.locator(
        '//td[contains(text(),"Description:")]/following-sibling::td[1][@class="tableText-01"]'
    ).first.inner_text()
    try:
        await page.wait_for_selector(
            '//td[contains(text(),"Bid Number")]/following-sibling::td[1][@class="tableText-01"]',
            timeout=2000,
        )
        notice_id = await page.locator(
            '//td[contains(text(),"Bid Number")]/following-sibling::td[1][@class="tableText-01"]'
        ).first.inner_text()
    except:
        notice_id = None
    try:
        await page.wait_for_selector(
            '//td[contains(text(),"Bulletin Desc")]/following-sibling::td[1][@class="tableText-01"]',
            timeout=1000,
        )
        desc = await page.locator(
            '//td[contains(text(),"Bulletin Desc")]/following-sibling::td[1][@class="tableText-01"]'
        ).first.inner_text()
        desc = desc.strip()
    except:
        desc = None
    try:
        buyer_agency = await page.locator(
            '//td[contains(text(),"Organization")]/following-sibling::td[1][@class="tableText-01"]'
        ).first.inner_text()
        buyer_agency = buyer_agency.strip()
    except:
        buyer_agency = None
    try:
        buyer_name = await page.wait_for_selector(
            '//td[contains(text(),"Purchaser")]/following-sibling::td[1][@class="tableText-01"]',
            timeout=2000,
        )
        buyer_name = await page.locator(
            '//td[contains(text(),"Purchaser")]/following-sibling::td[1][@class="tableText-01"]'
        ).first.inner_text()
        buyer_name = buyer_name.strip()
    except:
        buyer_name = None
    buyer_data = await page.locator(
        '//td[contains(text(),"Ship-to Address:")]/following-sibling::td[1][@class="tableText-01"]'
    ).first.inner_text()
    email_pattern = r"[\w\.-]+@[\w\.-]+"
    phone_pattern = r"\(\d{3}\)\d{3}-\d{4}"
    emails = re.findall(email_pattern, buyer_data)
    phones = re.findall(phone_pattern, buyer_data)

    if emails:
        buyer_email = emails[0]
    else:
        buyer_email = None
    if phones:
        buyer_phone = phones[0]
    else:
        buyer_phone = None
    try:
        location = await page.locator(
            '//td[contains(text(),"Location")]/following-sibling::td[1][@class="tableText-01"]'
        ).inner_text()
        location = location.strip()
    except:
        location = None
    try:
        await page.wait_for_selector(
            '//td[contains(text(),"Type Code")]/following-sibling::td[1][@class="tableText-01"]',
            timeout=1000,
        )
        typ = await page.locator(
            '//td[contains(text(),"Type Code")]/following-sibling::td[1][@class="tableText-01"]'
        ).inner_text()
        typ = typ.split("-")[-1].strip()
    except:
        typ = None
    # try:
    #     await page.wait_for_selector("//div[contains(text(),'Closed Date')]/following-sibling::div",timeout=1000)
    #     due_date=await page.locator("//div[contains(text(),'Closed Date')]/following-sibling::div").inner_text()
    #     due_date=due_date.strip()
    # except:due_date=None
    try:
        await page.wait_for_selector(
            '//td[contains(text(),"Bid Opening Date")]/following-sibling::td[1][@class="tableText-01"]',
            timeout=1000,
        )
        open_date = await page.locator(
            '//td[contains(text(),"Bid Opening Date")]/following-sibling::td[1][@class="tableText-01"]'
        ).inner_text()
        open_date = open_date.strip()
    except:
        open_date = None
    # try:
    #     await page.wait_for_selector("//div[contains(text(),'NIGP Code')]/following-sibling::div",timeout=1000)
    #     categories=await page.locator("//div[contains(text(),'NIGP Code')]/following-sibling::div").inner_text()
    #     category='\n'
    #     categories=categories.split('\n')
    #     for cat in categories:
    #         category+= cat.split(' ',1)[-1].strip()+'\n'
    #     category=category.strip()
    # except:category=None
    files = []
    for link in await page.query_selector_all(
        '//td[contains(text(),"File Attachments")]/following-sibling::td//a'
    ):
        download_meta = await sdk.capture_download(link)

        files.append({"title": download_meta["filename"], "url": download_meta["url"]})

    await sdk.save_data(
        {
            "id": notice_id,
            "title": post_title,
            "description": desc,
            "location": location,
            "type": typ,
            "category": None,
            "posted_date": open_date,
            "due_date": None,
            "buyer_name": buyer_agency,
            "buyer_contact_name": buyer_name,
            "buyer_contact_number": buyer_phone,
            "buyer_contact_email": buyer_email,
            "attachments": files,
        }
    )


@SDK.scraper(domain="https://www.microchip.com/", stage="detail")
async def scrape2(sdk: SDK, url: str, context: Any, *args: Any, **kwargs: Any) -> None:
    await sdk.page.goto(url)
    download_info = await sdk.capture_pdf()
    await sdk.save_data({"download_url": download_info})


if __name__ == "__main__":
    asyncio.run(
        SDK.run(
            scrape,
            # scrape2,
            "https://www.bidbuy.illinois.gov/bso/external/bidDetail.sdo?docId=23-444DHS-MIS44-B-34703&external=true&parentUrl=close",
            # "https://ncw.gov.eg/Page/394/%D8%A7%D9%84%D9%85%D8%AD%D9%88%D8%B1-%D8%A7%D9%84%D8%AA%D8%B4%D8%B1%D9%8A%D8%B9%D9%89",
            # "https://www.mofa.gov.qa/en/all-mofa-news/details/1445/08/22/prime-minister-and-minister-of-foreign-affairs-chairs-gcc-morocco-meeting",
        )
    )
    asyncio.run(SDK.run_from_file(scrape, headless=True))
