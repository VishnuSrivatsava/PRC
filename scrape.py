import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def get_company_urls(driver):
    url = "https://www.indeed.com/companies/search?q=software+engineer"
    driver.get(url)

    all_links = driver.find_elements(By.TAG_NAME, 'a')
    company_urls = [link.get_attribute('href') for link in all_links if "/cmp/" in link.get_attribute('href') and "reviews" in link.get_attribute('href')]

    return company_urls

def get_reviews(driver, company_url):
    driver.get(company_url)

    reviews = driver.find_elements(By.CSS_SELECTOR, 'span.eu4oa1w0')

    return [review.text for review in reviews[:150]]

# Setup Chrome WebDriver
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

company_urls = get_company_urls(driver)

company_urls = list(set(company_urls))

print(company_urls)
with open('company_reviews.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Company", "Reviews"])

    for url in company_urls:
        company_name = url.split('/')[-2]
        reviews = get_reviews(driver, url)

        # Join all reviews into a single string with each review separated by a new line
        reviews_str = "\n".join(reviews)
        writer.writerow([company_name, reviews_str])

driver.quit()
