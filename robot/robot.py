# External modules
import random
import asyncio
from playwright.async_api import async_playwright

# Internal modules
from settings import settings
from robot.progress import process_progress


with open('messages.txt', 'r') as file:
    msg_file = file.read()


async def main():
    '''All automation.'''

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(settings.SITE)

        input_login = '//*[@id="login_email"]'
        input_password = '//*[@id="formLogin"]/div[2]/div/div/input'
        button_login = '//*[@id="formLogin"]/div[3]/button'

        await page.fill(input_login, settings.EMAIL)
        await page.fill(input_password, settings.PASSWORD)
        await page.click(button_login)

        process_progress(1)
        print('logging...\n')

        # Waiting for loader a little bit of the page
        await page.wait_for_timeout(3000)

        process_progress(1)
        print('Successfully logged in!\n')

        process_progress(1)
        print('Interacting with the page...\n')

        # IMPORTANT!
        # The XPath may change, but you can easily change it by looking on the website which is the new XPath
        smile_lasted = '//*[@id="fdz-panel-form-mood"]/div[1]/div/label[5]/img'
        smile_first = '//*[@id="fdz-panel-form-mood"]/div[1]/div/label[4]/img'
        textarea = '//*[@id="fdz-panel-form-mood"]/div[2]/div/div[1]/textarea'
        button_send = '//*[@id="fdz-panel-form-mood"]/div[2]/div/button'
        champion_profile = '//*[@id="fdz-main"]/div/div/div[3]/div[2]/div[8]/div/div[2]/div[1]'

        emoji_list = [smile_first, smile_lasted]
        element_e = random.choice(emoji_list)

        msg = msg_file.split('\n')
        element_t = random.choice(msg)

        champion = await page.text_content(champion_profile)

        await page.click(element_e)

        # time included because it was giving an error not found
        await page.wait_for_timeout(300)

        await page.fill(textarea, element_t)

        # time included because it was giving an error not found
        await page.wait_for_timeout(500)
        await page.click(button_send)

        process_progress(1)
        print('Feedz done successfully!\n')

        # time included because it was giving an error not found
        await page.wait_for_timeout(300)
        print(f'Profile first: {champion}\n')

        await browser.close()

try:
    asyncio.run(main())

except Exception as e:
    print('Something went wrong! :/ ')
    print('Probably XPath changed or some other error, see below.: ', e)
