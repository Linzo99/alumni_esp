#!/usr/bin/env python
# coding: utf-8

# In[3]:


import asyncio
import time
from pyppeteer import launch

async def main():
    # Launch browser
    browser = await launch()
    # Open a new page and navigate to URL
    page = await browser.newPage()
    await page.goto('https://s.surveylegend.com/-NWKLkaIlnVKa7Pfgz6X')

    # Wait for the page to render the elements with class "gallery-grid-item"
    await page.waitForSelector('#choice-1685059209622')

    # Select the third element with class "gallery-grid-item"
    third_element = await page.querySelector('#choice-1685059209622')

    # Click on the third element
    await third_element.click()

    # Select the submit button and click it
    submit_button = await page.querySelector('.my-enter-button')
    await submit_button.click()
    time.sleep(1)
    print(f"Vote successful +1")

    # Clear local storage data
    #  await page.deleteCookie()
    #  await page.evaluate('sessionStorage.clear();')
    #  await page.evaluate('localStorage.clear();')
    #  await page.evaluate('window.localStorage.clear();')

    # Remove cookies and sessions
    await browser.close()
    
while True:
    asyncio.get_event_loop().run_until_complete(main())
#await main()
