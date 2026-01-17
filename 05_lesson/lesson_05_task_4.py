from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    
    driver = webdriver.Firefox()  
    try:
       
        driver.get("http://the-internet.herokuapp.com/login")

       
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        )

      
        username_field.send_keys("tomsmith")
        print("Логин введен: tomsmith")

        
        password_field.send_keys("SuperSecretPassword!")
        print("Пароль введен: SuperSecretPassword!")

       
        login_button.click()
        print("Кнопка Login нажата")

      
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.flash-success"))
        )

       
        message_text = success_message.text.strip()
        print(f"Текст сообщения: {message_text}")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
   
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    run_test()