from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_test():
   
    driver = webdriver.Chrome()  
    try:
       
        driver.get("http://uitestingplayground.com/classattr")

   
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
        )

      
        button.click()
        print("Кнопка нажата успешно.")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    for i in range(3):
        print(f"\n--- Запуск {i + 1} ---")
        run_test()