from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

def main():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")
    # Uncomment to run in headless mode:
    # options.add_argument("--headless")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()  # Maximize browser window

    try:
        # 1. Navigate to the website
        driver.get("https://www.intervue.io/")
        print("Navigated to https://www.intervue.io/")

        navbar_locator = (By.CSS_SELECTOR, 'a.iv-homepage-navbar-7.header-links[data-text="Why Intervue?"]')
        navbar_element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(navbar_locator))
        driver.execute_script("arguments[0].scrollIntoView(true);", navbar_element)
        print("Navbar element found and scrolled into view.")

        actions = ActionChains(driver)
        nav_elements = [
            ('a.iv-homepage-navbar-7.header-links[data-text="Products"]', 3),
            ('a#solutions', 3),
            ('a#pricing', 3),
            ('a#resources', 3),
            ('a#contact-us', 2)
        ]
        for selector, wait_time in nav_elements:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
                )
                actions.move_to_element(element).perform()
                print(f"Hovered over element: {selector}")
                time.sleep(wait_time)
            except Exception as ex:
                print(f"Error hovering over {selector}: {ex}")

        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/nav/div[2]/div[1]/div[2]/div/a[2]"))
        )
        login_button.click()
        print("Clicked homepage login button.")

        WebDriverWait(driver, 15).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        print("Switched to new login tab/window.")

        second_login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.AccessAccount-ColoredButton'))
        )
        second_login_button.click()
        print("Clicked second login button.")

        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "login_email"))
        )
        email_input.clear()
        email_input.send_keys("neha@intervue.io")
        print("Email entered.")
        
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "login_password"))
        )
        password_input.clear()
        password_input.send_keys("Ps@neha@123")
        print("Password entered.")

        login_submit_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                "button.ant-btn.btn.LoginDarkButton-sc-1ertvag-0.isOnQC.ant-btn-primary.ant-btn-lg.ant-btn-block"
            ))
        )
        login_submit_button.click()
        print("Login form submitted.")

        time.sleep(5)

        search_placeholder = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.search_placeholder"))
        )
        search_placeholder.click()
        print("Search placeholder clicked.")

        search_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.SearchBox__StyledInput-ctnsh0-4.lhwsuL[placeholder="Type what you want to search for"]'))
        )
        search_input.clear()
        search_input.send_keys("hello")
        print("Search text entered: 'hello'")
        time.sleep(5)

        search_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.SearchThrough__PlaceholderText-sc-8f4vh4-0'))
        )
        search_result.click()
        print("Search result clicked.")

        time.sleep(5)

        profile_dropdown = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ant-dropdown-link.ProfileHeader__StyedDropdownHoverLink-sc-1gwp6c1-3'))
        )
        profile_dropdown.click()
        print("Profile dropdown clicked.")
        time.sleep(2)

        actions = ActionChains(driver)
        menu_items = [
            'a[href="/profile/billing"]',
            'a[href="/profile/settings/team"]',
            'a[href="/profile/settings/integrations"]',
            'a[href="/profile/settings/user"]'
        ]
        for item in menu_items:
            try:
                menu_element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, item))
                )
                actions.move_to_element(menu_element).perform()
                print(f"Hovered over profile menu item: {item}")
                time.sleep(2)
            except Exception as ex:
                print(f"Error with menu item {item}: {ex}")

        logout_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/a[5]'))
        )
        logout_button.click()
        print("Clicked logout button.")

        time.sleep(5)
        print("Automation completed. Final page title:", driver.title)

    except Exception as e:
        print("An error occurred during automation:")
        traceback.print_exc()
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
