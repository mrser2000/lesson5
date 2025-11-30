from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
    
    driver = webdriver.Chrome()

    try:
        
        driver.get("http://uitestingplayground.com/dynamicid")

       
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
        )

       
        button.click()
        print("Кнопка нажата успешно.")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    print("Запуск теста 1 из 3...")
    run_test()
    
    print("Запуск теста 2 из 3...")
    run_test()
    
    print("Запуск теста 3 из 3...")
    run_test()