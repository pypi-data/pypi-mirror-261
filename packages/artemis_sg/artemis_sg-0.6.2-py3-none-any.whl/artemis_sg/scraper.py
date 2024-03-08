import logging
import os.path
import re
import time  # for additional sleeps in page load.  This is a smell.
import urllib.parse

from rich.console import Console
from rich.text import Text

# Selenium
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)

# Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as SeleniumKeys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from artemis_sg import spreadsheet, vendor
from artemis_sg.config import CFG
from artemis_sg.items import Items

# Firefox
# from selenium.webdriver.firefox.service import Service as FirefoxService

MODULE = os.path.splitext(os.path.basename(__file__))[0]
console = Console()

IMG_FAILOVER_THRESHHOLD = 2


class BaseScraper:
    """
    Scraper objects know how to scrape base url
    """

    def __init__(self, selenium_driver, base_url=None):
        self.selenium_driver = selenium_driver
        if not base_url:
            self.base_url = ""
        else:
            self.base_url = base_url
        self.login_xpath_query = ""

    def load_item_page(self, item_number):
        return False

    def scrape_description(self):
        description = ""
        return description

    def scrape_dimension(self):
        dimension = ""
        return dimension

    def scrape_item_image_urls(self):
        urls = []
        return urls

    def login(self):
        namespace = f"{type(self).__name__}.{self.login.__name__}"

        self.delay(2)
        input_text = Text(
            """
        ********    USER INPUT REQUIRED    ********
        Locate the selenium controlled browser
        and manually enter your login credentials.
        ********  WAITING FOR USER INPUT   ********
        """
        )
        input_text.stylize("bold cyan")
        console.print(input_text)
        try:
            WebDriverWait(self.selenium_driver,
                          CFG["asg"]["scraper"]["login_timeout"]).until(
                ec.presence_of_element_located((By.XPATH, self.login_xpath_query))
            )
            success_text = Text(
                """
            ********      LOGIN SUCCESSFUL     ********
            ********   CONTINUING EXECUTION    ********
            """
            )
            success_text.stylize("green")
            console.print(success_text)
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"{namespace}: failed to login")
            logging.error(f"{namespace}: Cannot proceed.  Exiting.")
            raise e

    def delay(self, secs):
        time.sleep(secs)


class GJScraper(BaseScraper):
    """
    GJScraper objects know how to scrape GJ item pages
    """

    def __init__(self, selenium_driver, base_url="https://greatjonesbooks.com"):
        super().__init__(selenium_driver, base_url)
        self.timeout = 3
        self.login_xpath_query = "//a[@href='/account']"

    def load_item_page(self, item_number, tries=0):
        namespace = f"{type(self).__name__}.{self.load_item_page.__name__}"

        # GJ does not maintain session if the links on page are not used
        # if not logged in, then build url; else use search facility
        try:
            self.delay(1)
            WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//a[@href='/account' and text()='Account Summary']")
                )
            )
        except (NoSuchElementException, TimeoutException):
            start = "/product/"
            url = self.base_url + start + item_number
            self.selenium_driver.get(url)
            return True
        try:
            search = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.XPATH, "//a[@href='/search']"))
            )
            search.click()
            self.delay(2)

            # wait until Publisher list is populated
            # by finding sentinel publisher
            sentinel = CFG["asg"]["scraper"]["gjscraper"]["sentinel_publisher"]
            timeout_bak = self.timeout
            self.timeout = 60
            WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located(
                    (By.XPATH, f"//option[@value='{sentinel}']")
                )
            )
            self.timeout = timeout_bak
            # then get itemCode field for search
            item_field = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='itemCode']"))
            )
            search_button = self.selenium_driver.find_element(
                By.CSS_SELECTOR, ".buttonSet > button:nth-child(1)"
            )
            clear_button = self.selenium_driver.find_element(
                By.CSS_SELECTOR, ".buttonSet > button:nth-child(2)"
            )
            clear_button.click()
            item_field.send_keys(item_number)
            self.delay(2)
            search_button.click()
            self.delay(2)
            # check for No Results
            e = self.selenium_driver.find_element(
                By.XPATH, "//div[@class='formBox']/div"
            )
            if "No Results" in e.text:
                # Do not continue to try
                logging.info(f"{namespace}: No Results found for {item_number}")
                return False
            items = self.selenium_driver.find_elements(By.ID, "product.item_id")
            items[0].click()
            return True
        except (NoSuchElementException, TimeoutException, IndexError):
            tries += 1
            if tries < self.timeout:
                self.load_item_page(item_number, tries)
            else:
                logging.info(f"{namespace}: failed item search for {item_number}")
                return False

    def scrape_description(self):
        try:
            self.delay(1)
            elem = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "desc"))
            )
            span = elem.find_element(By.CLASS_NAME, "short-comments")
            description = span.text
        except (NoSuchElementException, TimeoutException):
            description = ""

        return description

    def scrape_item_image_urls(self):
        namespace = f"{type(self).__name__}.{self.scrape_item_image_urls.__name__}"

        urls = []
        try:
            self.delay(1)
            # GJ appears to only have single cover images
            elem = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "cover"))
            )
            img = elem.find_element(By.TAG_NAME, "img")
            src = img.get_attribute("src")
            if src and "noimage.png" not in src:
                urls.append(src)
        except (NoSuchElementException, TimeoutException) as e:
            logging.warning(f"{namespace}: error {e}")
        return urls

    def load_login_page(self):
        # Load search page while logged out in an attempt to get the
        # Publishers list to populate when the page is loaded after login.
        self.selenium_driver.get(self.base_url + "/search")
        self.delay(self.timeout)
        login = "/login"
        url = self.base_url + login
        self.selenium_driver.get(url)

    def add_to_cart(self, qty):
        # TODO: Can we DRY this up?  Some duplication between scrapers
        namespace = f"{type(self).__name__}.{self.add_to_cart.__name__}"

        self.delay(1)
        stock_elem = self.selenium_driver.find_element(By.CLASS_NAME, "on-hand")
        m = re.search(r"([0-9]+) in stock", stock_elem.text)
        if m:
            stock = m.group(1)
            if int(stock) < int(qty):
                qty = stock
        self.delay(1)
        try:
            # gather html elements needed
            add_div = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "add"))
            )
            qty_field = add_div.find_element(By.XPATH, "//input[@name='qty']")

            qty_field.clear()
            qty_field.send_keys(qty + SeleniumKeys.ENTER)
        except (NoSuchElementException, TimeoutException) as e:
            logging.warning(f"{namespace}: error {e}")
            return 0
        return int(qty)

    def load_cart_page(self):
        # TODO: Can we DRY this up?  Some duplication between scrapers
        namespace = f"{type(self).__name__}.{self.load_cart_page.__name__}"
        try:
            cart = self.selenium_driver.find_element(By.CLASS_NAME, "cart")
            cart.click()
            self.delay(1)
            cart.click()
            self.delay(1)
        except Exception as e:
            logging.warning(f"{namespace}: error {e}")
            return False
        return True

    def scrape_error_msg(self):
        try:
            elem = self.selenium_driver.find_element(By.CLASS_NAME, "errorMsg")
            msg = elem.text
        except NoSuchElementException:
            msg = ""
        return msg


class SDScraper(BaseScraper):
    """
    SDScraper objects know how to scrape SD item pages
    """

    def __init__(self, selenium_driver, base_url="https://strathearndistribution.com"):
        super().__init__(selenium_driver, base_url)
        self.timeout = 3
        self.login_xpath_query = "//span[text()='My lists']"

    def load_login_page(self):
        namespace = f"{type(self).__name__}.{self.load_login_page.__name__}"
        try:
            self.selenium_driver.get(self.base_url)
            self.delay(2)
            button = self.selenium_driver.find_element(By.ID, "styled_btn")
            button.click()
        except (
            StaleElementReferenceException,
            NoSuchElementException,
            TimeoutException,
        ) as e:
            logging.error(f"{namespace}: failed to load login page")
            logging.error(f"{namespace}: Cannot proceed.  Exiting.")
            raise e

    def load_item_page(self, item_number, tries=0):
        namespace = f"{type(self).__name__}.{self.load_item_page.__name__}"
        try:
            self.selenium_driver.get(self.base_url)
            self.delay(2)
            search = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.ID, "search"))
            )
            search.send_keys(item_number + SeleniumKeys.ENTER)
            self.delay(2)
            elem = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "listItem"))
            )
            self.delay(2)
            elem.click()
            return True
        except (
            StaleElementReferenceException,
            NoSuchElementException,
            TimeoutException,
        ) as e:
            tries += 1
            if tries < self.timeout:
                self.load_item_page(item_number, tries)
            else:
                logging.warning(
                    f"{namespace}: Failed to load item page '{item_number}': {e}"
                )
                return False

    def scrape_description(self):
        try:
            # rc-* IDs are dynamic, must use classes
            elem = self.selenium_driver.find_element(By.CLASS_NAME, "ant-tabs-nav-list")
            tab_btn = elem.find_element(By.CLASS_NAME, "ant-tabs-tab-btn")
            tab_btn.click()
            pane = self.selenium_driver.find_element(By.CLASS_NAME, "ant-tabs-tabpane")
            description = pane.text
        except NoSuchElementException:
            description = ""

        return description

    def scrape_dimension(self):
        try:
            dets_xpath ="//div[@class='ant-tabs-tab-btn'][text()='Details']"
            btn = self.selenium_driver.find_element(By.XPATH, dets_xpath)
            btn.click()
            elem = self.selenium_driver.find_element(
                    By.XPATH, "//div[strong[contains(text(), 'Physical Dimensions:')]]")
            t = elem.text
            dimension = t.replace("Physical Dimensions:\n", "")
        except NoSuchElementException:
            dimension = ""

        return dimension

    def scrape_item_image_urls(self):
        namespace = f"{type(self).__name__}.{self.scrape_item_image_urls.__name__}"
        urls = []
        try:
            # main only
            elem = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "full-image"))
            )
            src = elem.get_attribute("src")
            if src:
                urls.append(src)
            # ensure we are seeing the top of the page
            html = self.selenium_driver.find_element(By.TAG_NAME, "html")
            html.send_keys(SeleniumKeys.PAGE_UP)
            # image gallery for additional images
            elems = self.selenium_driver.find_elements(By.CLASS_NAME, "gallery-vert")
            for elem in elems:
                src = elem.get_attribute("src")
                if src:
                    urls.append(src)
        except NoSuchElementException as e:
            logging.warning(f"{namespace}: error {e}")
        return urls

    def add_to_cart(self, qty):
        namespace = f"{type(self).__name__}.{self.add_to_cart.__name__}"

        self.delay(1)
        # try:???
        stock_elem = self.selenium_driver.find_element(
            By.XPATH, "//span[contains(text(), 'in stock')]"
        )
        m = re.search(r"([0-9]+) in stock", stock_elem.get_attribute("innerHTML"))
        if m:
            stock = m.group(1)
            if int(stock) < int(qty):
                qty = stock
        self.delay(1)
        try:
            # gather html elements needed
            elems = self.selenium_driver.find_elements(By.CLASS_NAME, "ant-btn-primary")
            button = None
            for e in elems:
                if "Add to cart" in e.text:
                    button = e
                    break
            qty_field = self.selenium_driver.find_element(
                By.XPATH,
                (
                    "//input[@class='ant-input' and @type='text' "
                    "and not(ancestor::div[contains(@class, '-block')])]"
                ),
            )
            # the qty field must be clicked to highlight amount.  Clearing doesn't work
            qty_field.click()
            qty_field.send_keys(qty)
            button.click()
        except Exception as e:
            logging.warning(f"{namespace}: error {e}")
            return 0
        return int(qty)

    def load_cart_page(self):
        namespace = f"{type(self).__name__}.{self.load_cart_page.__name__}"
        try:
            cart = "/checkout/cart"
            url = self.base_url + cart
            self.selenium_driver.get(url)
            self.delay(1)
            return True
        except Exception as e:
            logging.warning(f"{namespace}: error {e}")
            return False


class TBScraper(BaseScraper):
    """
    TBScraper objects know how to scrape TB item pages
    """

    def __init__(self, selenium_driver, base_url="https://texasbookman.com/"):
        super().__init__(selenium_driver, base_url)
        self.timeout = 3
        self.login_xpath_query = "//a[@href='/admin']"

    def load_item_page(self, item_number):
        start = "p/"
        url = self.base_url + start + item_number
        self.selenium_driver.get(url)
        return True

    def scrape_description(self):
        try:
            elem = self.selenium_driver.find_element(
                By.CLASS_NAME, "variant-description"
            )
            text = elem.text
            description = text.replace("NO AMAZON SALES\n\n", "")
        except NoSuchElementException:
            description = ""

        return description

    def scrape_dimension(self):
        try:
            elem = self.selenium_driver.find_element(
                By.CLASS_NAME, "full-description"
            )
            m = re.search(r"(Size:.+)\n", elem.text)
            dimension = m.group(1).replace("Size:", "").strip()
        except (NoSuchElementException, AttributeError):
            dimension = ""

        return dimension

    def scrape_item_image_urls(self):
        urls = []
        try:
            elem = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "a-left"))
            )
            elem = self.selenium_driver.find_element(By.CLASS_NAME, "picture-thumbs")
            left = elem.find_element(By.CLASS_NAME, "a-left")
            left.click()
            while True:
                self.delay(2)
                thumb = self._get_thumb_from_slimbox()
                if thumb:
                    urls.append(thumb)
                next_link = WebDriverWait(self.selenium_driver, self.timeout).until(
                    ec.presence_of_element_located((By.ID, "lbNextLink"))
                )
                self.delay(2)
                next_link.click()
        except (
            NoSuchElementException,
            ElementNotInteractableException,
            TimeoutException,
        ):
            try:
                elem = self.selenium_driver.find_element(By.CLASS_NAME, "picture")
                img = elem.find_element(By.TAG_NAME, "img")
                thumb = img.get_attribute("src")
                urls.append(thumb)
            except NoSuchElementException:
                pass

        return urls

    def _get_thumb_from_slimbox(self):
        timeout = 3
        thumb = None
        try:
            img_div = WebDriverWait(self.selenium_driver, timeout).until(
                ec.presence_of_element_located((By.ID, "lbImage"))
            )
            style = img_div.get_attribute("style")
            m = re.search('"(.*)"', style)
            if m:
                thumb = m.group(1)
        except (NoSuchElementException, TimeoutException):
            pass

        return thumb

    def load_login_page(self):
        login = "login"
        url = self.base_url + login
        self.selenium_driver.get(url)

    def impersonate(self, email):
        namespace = f"{type(self).__name__}.{self.impersonate.__name__}"

        # Go to /Admin/Customer/List
        customers = "/Admin/Customer/List"
        url = self.base_url + customers
        self.selenium_driver.get(url)
        self.delay(1)
        try:
            # search for email
            search_email = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.ID, "SearchEmail"))
            )
            search_email.clear()
            search_email.send_keys(email + SeleniumKeys.ENTER)
            # Get customer link associated with email
            email_xpath = (
                f"//div[@id='customers-grid']/table/tbody/tr/td/a[text()='{email}']"
            )
            customer_link = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.XPATH, email_xpath))
            )
            links = self.selenium_driver.find_elements(By.XPATH, email_xpath)
            # Bail if multiple customer records for given email.
            if len(links) > 1:
                logging.error(
                    f"{namespace}: Found multiple customer records for email "
                    f"'{email}' to impersonate"
                )
                logging.error(f"{namespace}: Cannot proceed.  Exiting.")
                raise Exception
            customer_link.click()
            # click "Place Order (impersonate)"
            impersonate = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//a[text()='Place order (Impersonate)']")
                )
            )
            impersonate.click()
            # click "Place Order" button
            button = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//input[@name='impersonate']")
                )
            )
            button.click()
            self.delay(1)
            WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "finish-impersonation"))
            )
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"{namespace}: failed to impersonate")
            logging.error(f"{namespace}: Cannot proceed.  Exiting.")
            raise e
        return True

    def add_to_cart(self, qty):
        namespace = f"{type(self).__name__}.{self.add_to_cart.__name__}"

        qty = int(qty)
        self.delay(1)
        stock_elem = self.selenium_driver.find_element(By.CLASS_NAME, "stock")
        m = re.search(r"Availability: ([0-9]+) in stock", stock_elem.text)
        if m:
            stock = m.group(1)
            stock = int(stock)
            if stock < qty:
                qty = stock
        try:
            # gather html elements needed
            qty_field = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.CLASS_NAME, "qty-input"))
            )
            button = self.selenium_driver.find_element(
                By.CLASS_NAME, "add-to-cart-button"
            )
            qty_field.clear()
            # ENTERing out of the qty_field DOES NOT add to cart.
            # The button must be clicked instead.
            qty_field.send_keys(qty)
            button.click()
            self.delay(1)
        except Exception as e:
            logging.warning(f"{namespace}: error {e}")
            return 0
        return qty

    def load_cart_page(self):
        cart = "cart"
        url = self.base_url + cart
        self.selenium_driver.get(url)
        return True

    def search_item_num(self, search):
        namespace = f"{type(self).__name__}.{self.search_item_num.__name__}"

        item_num = ""
        search = urllib.parse.quote_plus(search)
        url = self.base_url + "search?q=" + search
        self.selenium_driver.get(url)
        self.delay(2)
        timeout_bak = self.timeout
        self.timeout = 120
        WebDriverWait(self.selenium_driver, self.timeout).until(
            ec.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )
        self.timeout = timeout_bak
        links = self.selenium_driver.find_elements(
            By.XPATH, "//div[@class='search-results']//a[contains(@href, '/p/')]"
        )
        if links:
            item_urls = [x.get_attribute("href") for x in links]
            for item_url in item_urls:
                m = re.search(r"\/p\/([0-9]+)\/(?!uk-)", item_url)
                if m:
                    item_num = m.group(1)
                    break
        else:
            logging.warning(f"{namespace}: Failed to find item using q='{search}'")
        return item_num


class AmznScraper(BaseScraper):
    """
    AmznScraper objects know how to scrape amazon item pages
    """

    def __init__(self, selenium_driver, base_url="https://www.amazon.com/"):
        super().__init__(selenium_driver, base_url)
        self.timeout = 1
        self.captcha_link = self.base_url + "/errors/validateCaptcha"

    def solve_captcha(self, link=None):
        from amazoncaptcha import AmazonCaptcha

        if not link:
            link = self.captcha_link
        try:
            self.selenium_driver.get(link)
            captcha = AmazonCaptcha.fromdriver(self.selenium_driver)
            solution = captcha.solve()
            if solution.lower() == "not solved":
                raise(NoSuchElementException)
            return solution
        except (NoSuchElementException, TimeoutException):
            return ""

    def enter_captcha(self, solution):
        namespace = (
            f"{type(self).__name__}.{self.enter_captcha.__name__}"
        )
        if solution:
            elem = self.selenium_driver.find_element(By.ID, "captchacharacters")
            elem.send_keys(solution + SeleniumKeys.ENTER)
        else:
            input_text = Text(
                """
            ********    USER INPUT REQUIRED    ********
            Locate the selenium controlled browser
            and manually enter the requested CAPTCHA characters.
            ********  WAITING FOR USER INPUT   ********
            """
            )
            input_text.stylize("bold cyan")
            console.print(input_text)
            try:
                timeout_bak = self.timeout
                self.timeout = self.timeout * 100
                WebDriverWait(self.selenium_driver, self.timeout).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//a[@href='/ref=nav_logo']"))
                )
                self.timeout = timeout_bak
                success_text = Text(
                    """
                ********    CAPTCHA SUCCESSFUL     ********
                ********   CONTINUING EXECUTION    ********
                """
                )
                success_text.stylize("green")
                console.print(success_text)
            except (NoSuchElementException, TimeoutException):
                logging.error(f"{namespace}: failed CAPTCHA")

    def load_item_page(self, item_number):
        start = "dp/"
        url = self.base_url + start + item_number
        self.selenium_driver.get(url)
        return True

    def scrape_description(self):
        description = ""
        description = self._scrape_amazon_editorial_review()
        if not description:
            description = self._scrape_amazon_description()

        return description

    def scrape_dimension(self):
        dimension = ""
        try:
            xpath = "//span/span[contains(text(), 'Dimensions')]//following::span"
            elem = self.selenium_driver.find_element(By.XPATH, xpath)
            dimension = elem.get_attribute("innerHTML")
        except NoSuchElementException:
            dimension = ""
        return dimension

    def _scrape_amazon_editorial_review(self):
        descr = ""
        try:
            elem = self.selenium_driver.find_element(
                By.ID, "editorialReviews_feature_div"
            )
            text = elem.text
            descr_lines = re.split("^.*\\n.*\\n", text)  # trim off first two lines
            descr = descr_lines[-1]
        except NoSuchElementException:
            descr = ""

        return descr

    def _scrape_amazon_description(self):
        descr = ""
        try:
            elem = self.selenium_driver.find_element(
                By.ID, "bookDescription_feature_div"
            )
            # read_more = elem.find_element(By.CLASS_NAME, 'a-expander-prompt')
            # read_more.click()
            descr = elem.text
        except NoSuchElementException:
            descr = ""

        return descr

    def get_span_type_thumb_id_prefix(self):
        """Get span_type and thumb_id_prefix from amazon images widget."""
        namespace = (
            f"{type(self).__name__}.{self.get_span_type_thumb_id_prefix.__name__}"
        )
        span_type = None
        thumb_id_prefix = None
        try:
            span = WebDriverWait(self.selenium_driver, self.timeout).until(
                ec.presence_of_element_located((By.ID, "imgThumbs"))
            )
            span_type = "imgThumbs"
        except (NoSuchElementException, TimeoutException):
            logging.info(f"{namespace}: No imgThumbs id, trying imgTagWrapperID")
            try:
                span = WebDriverWait(self.selenium_driver, self.timeout).until(
                    ec.presence_of_element_located((By.ID, "imgTagWrapperId"))
                )
                span_type = "imgTagWrapperId"
            except (NoSuchElementException, TimeoutException):
                logging.info(f"{namespace}: No imgTagWrapperId id")
                logging.info(f"{namespace}: Returning empty urls list")
                return (span_type, thumb_id_prefix)

        if span_type == "imgThumbs":
            link = span.find_element(By.CLASS_NAME, "a-link-normal")
            thumb_id_prefix = "ig-thumb-"
        else:
            link = span
            thumb_id_prefix = "ivImage_"
        try:
            link.click()
        except ElementClickInterceptedException:
            logging.info(f"{namespace}: Failed to click images widget")
            logging.info(f"{namespace}: Returning empty urls list")
            return (span_type, thumb_id_prefix)
        return (span_type, thumb_id_prefix)

    def scrape_item_image_urls(self):
        namespace = f"{type(self).__name__}.{self.scrape_item_image_urls.__name__}"
        counter = 0
        urls = []

        span_type, thumb_id_prefix = self.get_span_type_thumb_id_prefix()
        if thumb_id_prefix:
            logging.debug(f"{namespace}: Clicked images widget")
            # get image urls
            while True:
                try:
                    thumb = ""
                    xpath = f"//*[@id='{thumb_id_prefix}{counter}']"
                    elem = WebDriverWait(self.selenium_driver, self.timeout).until(
                        ec.presence_of_element_located((By.XPATH, xpath))
                    )
                    if span_type == "imgThumbs":
                        thumb = elem.get_attribute("src")
                    if span_type == "imgTagWrapperId":
                        inner_elem = elem.find_element(By.CLASS_NAME, "ivThumbImage")
                        style = inner_elem.get_attribute("style")
                        m = re.search('"(.*)"', style)
                        if m:
                            thumb = m.group(1)
                    sub, suff = os.path.splitext(thumb)
                    indx = sub.find("._")
                    url = sub[:indx] + suff
                    if url:
                        urls.append(url)
                    logging.debug(f"{namespace}: Thumbnail src is {thumb}")
                    logging.debug(f"{namespace}: Full size URL is %r" % url)
                    counter += 1
                except (NoSuchElementException, TimeoutException):
                    break
        # amazon adds stupid human holding book images
        # remove this
        if len(urls) > 1:
            urls.pop()

        return urls


class AmznUkScraper(AmznScraper):
    """
    AmznUkScraper objects know how to scrape amazon.co.uk item pages
    """

    def __init__(self, selenium_driver, base_url="https://www.amazon.co.uk/"):
        super().__init__(selenium_driver, base_url)

    def decline_cookies(self):
        try:
            decline_button = self.selenium_driver.find_element(
                By.ID, "sp-cc-rejectall-link"
                )
            decline_button.click()
            self.delay(2)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def load_item_page(self, isbn):
        # Search by ISBN
        start = "s?isbn="
        url = self.base_url + start + isbn
        self.selenium_driver.get(url)
        self.decline_cookies()
        # Look for results
        elem = WebDriverWait(self.selenium_driver, self.timeout).until(
            ec.presence_of_element_located((By.CLASS_NAME, "s-result-list"))
        )
        # Get ASIN from first result
        inner_e = elem.find_element(By.CLASS_NAME, "a-link-normal")
        link = inner_e.get_attribute("href")
        m = re.search(r"\/dp\/([0-9A-Z]+)/", link)
        asin = m.group(1) if m else ""
        # Load ASIN page
        if asin:
            start = "dp/"
            url = self.base_url + start + asin
            self.selenium_driver.get(url)
            return True
        return False


##############################################################################
# utility functions
##############################################################################
def get_headless_driver():
    return get_driver("--headless=new")


def get_driver(option_args: str = ""):
    """Creates a new instance of the chrome driver.

    :param option_args:
       Option arguments to pass to the driver
    :returns: selenium.webdriver object
    """
    namespace = f"{MODULE}.{get_driver.__name__}"
    service = ChromeService()
    options = webdriver.ChromeOptions()
    if option_args:
        options.add_argument(option_args)
        logging.info(f"{namespace}: Setting webdriver option to '{option_args}'.")
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def scrape_item(scrapr, item_id, description="", dimension="", image_urls=None):
    if image_urls is None:
        image_urls = []
    namespace = f"{MODULE}.{scrape_item.__name__}"
    scrapr.load_item_page(item_id)
    logging.info(
        f"{namespace}: Getting item image urls via {scrapr.__class__.__name__}"
    )
    l_image_urls = scrapr.scrape_item_image_urls()
    if image_urls and len(l_image_urls) > 1:
        l_image_urls.pop(0)
    image_urls = image_urls + l_image_urls
    logging.info("     URLs: %r" % image_urls)
    if image_urls and not description:
        logging.info(
            f"{namespace}: Getting description via {scrapr.__class__.__name__}"
        )
        description = scrapr.scrape_description()
        logging.info("     Description: %r" % description[:140])
    if image_urls and not dimension:
        logging.info(
            f"{namespace}: Getting dimension via {scrapr.__class__.__name__}"
        )
        dimension = scrapr.scrape_dimension()
        logging.info("     Dimension: %r" % dimension[:140])
    return description, dimension, image_urls


def get_failover_scraper_item_id(driver, vendr, item):
    namespace = f"{MODULE}.{get_failover_scraper_item_id.__name__}"
    failover_scrapr = None
    item_id = item.isbn
    if vendr.vendor_code == "tb":
        try:
            url = item.data["LINK"]
            m = re.search(r"\/([0-9]+)\/", url)
            if m:
                item_id = m.group(1)
        except KeyError:
            logging.error(f"{namespace}: No link found in item")
    if vendr.failover_scraper in globals():
        failover_scrapr= globals()[vendr.failover_scraper](driver)
    return failover_scrapr, item_id


def main(vendor_code, sheet_id, worksheet, scraped_items_db):  # noqa: C901
    namespace = f"{MODULE}.{main.__name__}"
    # get vendor info from database
    logging.debug(f"{namespace}: Instantiate vendor.")
    vendr = vendor.Vendor(vendor_code)
    vendr.set_vendor_data()

    sheet_data = spreadsheet.get_sheet_data(sheet_id, worksheet)

    sheet_keys = [x for x in sheet_data.pop(0) if x]  # filter out None
    items_obj = Items(sheet_keys, sheet_data, vendr.isbn_key)
    items_obj.load_scraped_data(scraped_items_db)
    driver = None
    prime_scrapr = None
    failover_scrapr = None
    for item in items_obj:
        if not item.isbn:
            if "TBCODE" in item.data:
                item.isbn = item.data["TBCODE"]
            if not item.isbn:
                logging.info(f"{namespace}: No isbn for item, skipping lookup")
                continue
        description = ""
        dimension = ""
        image_urls = []
        # if scraped_item image_urls is not empty:
        #    skip scraped_item
        logging.info(f"{namespace}: Searching for {item.isbn} ...")
        if item.image_urls != []:
            logging.info(f"{namespace}: {item.isbn} found in database, skipping")
            continue

        if not driver and not prime_scrapr:
            logging.info(f"{namespace}: Opening browser...")
            if CFG["asg"]["scraper"]["headless"]:
                driver = get_headless_driver()
            else:
                driver = get_driver()
            prime_scrapr = AmznScraper(driver)
            solution = prime_scrapr.solve_captcha()
            prime_scrapr.enter_captcha(solution)


        logging.info(f"{namespace}: No scraped data currently: {item.isbn}")
        description, dimension, image_urls = scrape_item(
            prime_scrapr, item.isbn10, description, dimension, image_urls
        )
        if len(image_urls) < IMG_FAILOVER_THRESHHOLD:
            failover_scrapr, item_id = get_failover_scraper_item_id(
                driver, vendr, item
            )
            if failover_scrapr:
                if isinstance(failover_scrapr, AmznScraper):
                    solution = failover_scrapr.solve_captcha()
                    failover_scrapr.enter_captcha(solution)
                description, dimension, image_urls = scrape_item(
                    failover_scrapr, item_id, description, dimension, image_urls
                )

        item.data["DESCRIPTION"] = description
        item.data["DIMENSION"] = dimension
        item.image_urls = image_urls

        # Save db after every item scraping
        logging.info(f"{namespace}: Saving scraped item data")
        items_obj.save_scraped_data(scraped_items_db)

    if driver:
        logging.info(f"{namespace}: Closing browser...")
        driver.quit()
