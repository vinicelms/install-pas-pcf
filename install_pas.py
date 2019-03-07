from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import argparse

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
        print("{}".format("-"*50))
        print("Searching field: \"username\"")
        username_field = self.driver.find_element_by_name("username")
        print("The field was found: \"username\"")
        username_field.send_keys(self.user)
        print("Filling the field \"username\" with value: \"{}\"".format(self.user))
        print("{}".format("-"*50))

        print("Searching field: \"password\"")
        password_field = self.driver.find_element_by_name("password")
        print("The field was found: \"password\"")
        password_field.send_keys(self.password)
        print("Filling the field \"password\" with value: \"{}\"".format(self.password))
        print("{}".format("-"*50))

        print("Searching button to Enter")
        signin_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/input[4]")
        print("Button found")
        signin_button.click()
        print("Click on button")
        print("{}".format("-"*50))

    def import_file(self, file_path):
        self.login()

        print("Searching field: \"component_add_file\"")
        import_product_button = self.driver.find_element_by_id("component_add_file")
        print("The field was found: \"component_add_file\"")
        print("Importing file: {}".format(file_path))
        print("\n\nWait! This process usually takes about 20 minutes!")
        import_product_button.send_keys(file_path)
        print("{}".format("-"*50))

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="PCF URL", action="store",
        dest="url", required=True)
    parser.add_argument("--user", help="User to login on PCF", action="store",
        dest="user", required=True)
    parser.add_argument("--pass", help="Password to login on PCF", action="store",
        dest="pass", required=True)
    parser.add_argument("--file", help="File Path", action="store",
        dest="file_path", required=True)

    args = parser.parse_args()

    start = datetime.datetime.now()
    print("Starting script: {}".format(datetime.datetime.strftime(start, "%Y-%m-%d %H:%M:%S")))
    pcf = PCFWeb(url=args.url, user=args.user, password=args.password)
    
    try:
        pcf.import_file(args.file_path)
        print("File imported successfully!")
    except Exception as e:
        print(e)
        print("\n\nThere was an error while running")
    finally:
        pcf.close()
        print("Script completed!")
        print("{}".format("-"*50))
        end = datetime.datetime.now()
        print("End script: {}".format(datetime.datetime.strftime(end, "%Y-%m-%d %H:%M:%S")))