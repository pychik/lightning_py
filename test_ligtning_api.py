from driver import WebDriver

if __name__ == "__main__":
    driver = WebDriver()
    print(driver.session_id)
    print(driver.get("http://google.com").get_page_source()[:50])
    driver.get("http://yandex.ru").back().forward()
    print(driver.screen_shot()[:50])
    driver.close()
