from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class PCFWeb:

    def __init__(self, url, user, password):
        self.user = user
        self.password = password
        self.url = url

        chrome_opt = Options()
        chrome_opt.add_argument("--headless")
        chrome_opt.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(chrome_options=chrome_opt)
        self.driver.set_page_load_timeout(1800) # 1800s = 30 minutes | Install proccess is very slow
        self.driver.get(self.url)

    def login(self):
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys(self.user)

        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(self.password)

        signin_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/input[4]")
        signin_button.click()

    def import_file(self, file_path):
        self.login()

        import_product_button = self.driver.find_element_by_id("component_add_file")
        import_product_button.send_keys(file_path)