from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from PIL import Image
from django.conf import settings
from core.utils import id_generator

class Sel():
    def __init__(self, var=None):
        self.var = var
    	
    def dashboard_nivel_2(self):             
        #driver = webdriver.Chrome("C:/Users/Javier Orellana/Downloads/chromedriver.exe")
        path=settings.MEDIA_ROOT + '/informes/'
        """chrome_options = Options()
        chrome_options.headless = True
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument("--remote-debugging-port=9222")

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-dev-shm-usage')"""

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")
        
        chromeOptions.add_argument("--remote-debugging-port=9222")
        chromeOptions.add_argument("--disable-dev-shm-using")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        chromeOptions.add_argument("--headless")
        driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chromeOptions)

        #driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chromeOptions)
        
        #driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
        #driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", service_args=["--verbose", "--log-path=/var/www/logs/qc1.log"], chrome_options=chrome_options)
        
        #driver = webdriver.Chrome("C:/Users/Javier Orellana/Downloads/chromedriver.exe", chrome_options=chrome_options)
        #driver.get("http://127.0.0.1:8000/")
        driver.get("http://riesgoscl.tk/dashboard/")
        time.sleep(60)
        #driver.find_element_by_id("id_username").send_keys("admin@admin.com")
        #driver.find_element_by_id("id_username").send_keys("admin")
        
        #driver.find_element_by_id("id_password").send_keys("alicia(04)")
        #driver.find_element_by_id("id-div-links").click()
        #driver.find_element_by_id("btn_entrar").click()
        #time.sleep(3)
        #driver.find_element_by_id("span_detalle_riesgos_criticos").click()
        #time.sleep(2)        
        #the element with longest height on page
        ele=driver.find_element_by_tag_name('body')
        total_height = ele.size["height"]+800

        id_generado = id_generator()

        driver.set_window_size(1920, total_height)      #the trick
        time.sleep(2)
        driver.save_screenshot(path+" "+str(id_generado)+"_dashboard_nivel_2_png.png")
        driver.quit()
        #C:\Users\Javier Orellana\Documents\JO\desarrollos\Riesgos\AppRiesgos
        image1 = Image.open(path+" "+str(id_generado)+"_dashboard_nivel_2_png.png")
        im1 = image1.convert('RGB')
        im1.save(path+"/ "+str(id_generado)+"_dashboard_nivel_2_pdf.pdf")

        return [""+str(id_generado)+"_dashboard_nivel_2_png", ""+str(id_generado)+"_dashboard_nivel_2_pdf"]                    

    def dashboard_nivel_3(self):           
        #driver = webdriver.Chrome("C:/Users/Javier Orellana/Downloads/chromedriver.exe")
        path=settings.MEDIA_ROOT + '/informes/'
        """chrome_options = Options()
        chrome_options.headless = True
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument("--remote-debugging-port=9222")

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-dev-shm-usage')"""

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")
        
        chromeOptions.add_argument("--remote-debugging-port=9222")
        chromeOptions.add_argument("--disable-dev-shm-using")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        chromeOptions.add_argument("--headless")
        driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chromeOptions)

        #driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chromeOptions)
        
        #driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
        #driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", service_args=["--verbose", "--log-path=/var/www/logs/qc1.log"], chrome_options=chrome_options)
        
        #driver = webdriver.Chrome("C:/Users/Javier Orellana/Downloads/chromedriver.exe", chrome_options=chrome_options)
        #driver.get("http://127.0.0.1:8000/")
        driver.get("http://riesgoscl.tk/dashboard/")
        time.sleep(8)
        #driver.find_element_by_id("id_username").send_keys("admin@admin.com")
        #driver.find_element_by_id("id_username").send_keys("admin")
        
        #driver.find_element_by_id("id_password").send_keys("alicia(04)")
        #driver.find_element_by_id("id-div-links").click()
        #driver.find_element_by_id("btn_entrar").click()        
        driver.find_element_by_id("span_detalle_riesgos_criticos").click()
        time.sleep(8)
        #the element with longest height on page
        ele=driver.find_element_by_tag_name('body')
        total_height = ele.size["height"]+800

        id_generado = id_generator()

        driver.set_window_size(1920, total_height)      #the trick
        time.sleep(2)
        driver.save_screenshot(path+" "+str(id_generado)+"_dashboard_nivel_3_png.png")
        driver.quit()
        #C:\Users\Javier Orellana\Documents\JO\desarrollos\Riesgos\AppRiesgos
        image1 = Image.open(path+" "+str(id_generado)+"_dashboard_nivel_3_png.png")
        im1 = image1.convert('RGB')
        im1.save(path+"/ "+str(id_generado)+"_dashboard_nivel_3_pdf.pdf")

        return [""+str(id_generado)+"_dashboard_nivel_3_png", ""+str(id_generado)+"_dashboard_nivel_3_pdf"]                   
