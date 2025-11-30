from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    
    driver = webdriver.Firefox()  

    try:
    
        driver.get("http://the-internet.herokuapp.com/inputs")

     
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        input_field.send_keys("Sky")
        print('Введено: "Sky"')

      
        input_field.clear()
        print("Поле очищено")

        
        input_field.send_keys("Pro")
        print('Введено: "Pro"')

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
      
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    run_test()