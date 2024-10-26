from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def monitor_discord_channel():
    # Setup the WebDriver
    driver = webdriver.Chrome()  # Ensure you have the correct WebDriver for your browser

    url = 'https://discord.com/channels//'
    driver.get(url)

    # Wait for the page to load and login if necessary
    time.sleep(20)  # Adjust the sleep time as needed for manual login

    try:
        # Locate the div with the specific class
        div_content = driver.find_element(By.CLASS_NAME, 'scrollerInner__37fee')

        # Store the initial content of the div
        previous_elements = div_content.find_elements(By.XPATH, "./*")

        while True:
            # Scroll to the bottom to load new messages
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div_content)

            # Update the div content
            current_elements = div_content.find_elements(By.XPATH, "./*")
            if len(current_elements) != len(previous_elements):
                # Find the new elements
                new_elements = current_elements[len(previous_elements):]
                print("Nuevo contenido del div:")
                for elem in new_elements:
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of(elem))
                    print("HTML ELEM", elem.get_attribute("innerHTML"))
                    if 'button__581d0 lookFilled__950dd colorPrimary_ebe632 sizeSmall_da7d10 grow__4c8a4' in elem.get_attribute('innerHTML'):
                        print("HAY BOTOOOOOON")
                        button = elem.find_element(By.XPATH,
                                                   ".//button[contains(@class, 'button__581d0') and contains(@class, 'lookFilled__950dd') and contains(@class, 'colorPrimary_ebe632') and contains(@class, 'sizeSmall_da7d10') and contains(@class, 'grow__4c8a4')]")
                        div_inside = button.find_element(By.CLASS_NAME, "contents__322f4")
                        div_inside2 = div_inside.find_element(By.CLASS_NAME,"content_da5e31")
                        emoji = div_inside2.find_element(By.CLASS_NAME,"emoji")
                        print(emoji.get_attribute("src"))
                        button.click()
                        if emoji.get_attribute("src") != 'https://cdn.discordapp.com/emojis/847502744176820256.webp?size=56&quality=lossless' or emoji.get_attribute("src") != 'https://cdn.discordapp.com/emojis/847502746025459792.webp?size=56&quality=lossless':
                            button.click()
                    #print("Text ELEM", elem.text)
                # Update the previous elements
                previous_elements = current_elements

            # Wait before checking again to avoid too frequent checks
            time.sleep(0.8)

    except Exception as e:
        print(f"No se pudo encontrar el div: {e}")

    finally:
        # Keep the browser open for debugging
        input("Presiona Enter para cerrar el navegador y terminar el script...")
        driver.quit()

# Start monitoring the Discord channel
monitor_discord_channel()
