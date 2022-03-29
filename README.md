# Automate-Twitter-Selenium
Browser Automation Using Selenium

Selenium is a powerful tool for controlling a web browser through the program. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C#, etc, we will be working with Python.

Mastering Selenium will help you automate your day to day tasks like controlling your tweets, Whatsapp texting, and even just googling without actually opening a browser in just 15-30 lines of python code. The limits of automation are endless with selenium.

Installation

1.1 Selenium Bindings in Python

Selenium Python bindings provide a convenient API to access Selenium Web Driver like Firefox,Chrome,etc.

      Pip install Selenium 

1.2 Web Drivers

Selenium requires a web driver to interface with the chosen browser. Web drivers is a package to interact with a web browser. It interacts with the web browser or a remote web server through a wire protocol which is common to all. You can check out and install the web drivers of your browser choice.

Chrome:    https://sites.google.com/a/chromium.org/chromedriver/downloads

Firefox: https://github.com/mozilla/geckodriver/releases

Safari:    https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Dissecting the code:

The above script is for logging into twitter and searching for geeks for geeks handle.

So let’s see how it works:

1. Opening the browser
2. Creating a browser instance and using the .get function to connect the website.
3. Finding the element this can be anything finding the input box or a button and using the selenium function like click(), send_keys(), etc to interact with the element.
4. Closing the browser

As of now you must have realized this automation script works in an iterative manner of finding an element and interacting with it. There are various ways of finding an element in the web page, you just right click and inspect element and copy element either by name, css selector or xpath.
