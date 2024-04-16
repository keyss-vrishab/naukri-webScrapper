# from faulthandler import is_enabled
import time
# from tkinter import Button
# from xmlrpc.client import boolean
from selenium import webdriver
from selenium.webdriver.chrome.options import Options    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuzzywuzzy import fuzz
# from selenium.common.exceptions import NoSuchElementException
import csv
# import undetected_chromedriver as uc
# import seleniumwire.undetected_chromedriver as uc
import sys

# class GlassDoor:
     
#     def __init__(self):
#         company = ' '.join([str(elem) for elem in sys.argv[1:]])
#         self.Reviews = '';
#         self.Jobs = '';
#         self.company_names = [];
#         self.value = company
#         self.score = []
#         self.detailed_review = [];
#         self.rating = [];
#         # self.driver = webdriver.Chrome()    
#         time.sleep(20)  
#         mobile_emulation = {

#    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

#    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

#         chrome_options = Options()

#         chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

#         self.driver = webdriver.Chrome(chrome_options = chrome_options)

                
#     def login(self):
#         driver = self.driver
#         driver.get("https://www.glassdoor.co.in/index.htm");
#         time.sleep(5);
#         print("111111111111111111111")
#         try:
#             element = driver.find_element(By.XPATH,"//*[@id='SiteNav']/nav/div[1]/div[1]/button").click()
#             # time.sleep(2)
#             # element = driver.find_element(By.CSS_SELECTOR,"#SiteNav > nav > div.d-none.d-md-block.LockedHomeHeaderStyles__bottomBorder > div > div > div > button").click()
#             time.sleep(2)
#             # //*[@id="SiteNav"]/nav/div[1]/div[1]/button
        
#         except Exception as e:
#             print("no signin button")
#         try:
#             element = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.XPATH,"//*[@id='modalUserEmail']"))
#                 )

#         except Exception as e:
#             print(e)
#         element.send_keys("gawajay629@haizail.com");
        
#         time.sleep(2);
        
#         # click continou with email
        
#         element = driver.find_element(By.XPATH,'//*[@id="LoginModal"]/div/div/div[2]/div[2]/div/div/div/div/div/div/form/div[2]/button/span').click()
#         # //*[@id="LoginModal"]/div/div/div[2]/div[2]/div/div/div/div/div/div/form/div[2]/button/span
        
#         time.sleep(2);
#         #  click submit 
#         try:
#             element = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.XPATH,'//*[@id="modalUserPassword"]'))
#                 )

#         except Exception as e:
#             print(e)
#         element.send_keys("vrishab@123");
  
#         time.sleep(2);
        
#         # click on sign in   
#         element = driver.find_element(By.XPATH,'//*[@id="LoginModal"]/div/div/div[2]/div[2]/div/div/div/div/div/div/form/div[2]/button/span').click()
          
          
#         time.sleep(2);     
      
         
#     def chk_company(self):
        
#         driver = self.driver
#         # driver.get("https://www.glassdoor.co.in/member/home/index.htm")
#         time.sleep(2);
        
#         # element = driver.find_element(By.CSS_SELECTOR,'#SiteNav  nav:nth-child(2) > div >div >div:nth-child(2)  > div:nth-child(2)').click()
        
        
#         # try:
#         #     element = driver.find_element(By.CSS_SELECTOR,'#sc\.keyword').click()
#         # except Exception as e:
#         #     print("no search menu")
#         # time.sleep(2);
        
        
        
#         #  here i am clicking menu for comapines
#         try:
#             element = WebDriverWait(driver, 5).until(
                
#                 #   EC.element_to_be_clickable((By.CSS_SELECTOR,"#SearchForm .search__SearchStyles__iconBtn .SVGInline-svg"))
#                 EC.element_to_be_clickable((By.CSS_SELECTOR,"#SiteNav > nav.mt-std.mb-std.mb-lg-0.pb-xsm.siteHeader__HeaderStyles__bottomShadow > div > div > div.css-trqft4 > div:nth-child(2) > div.d-none.d-lg-flex.align-items-center.justify-content-center > div > a > span > div"))
                
#             ).click()

#         except Exception as e:
#              print("no search menu")
        
#         time.sleep(2)
#         try:
#             element = WebDriverWait(driver, 5).until(
                
#                 #   EC.element_to_be_clickable((By.CSS_SELECTOR,"#SearchForm .search__SearchStyles__iconBtn .SVGInline-svg"))
#                 EC.element_to_be_clickable((By.CSS_SELECTOR,"#sc\.keyword"))
                
#             ).click()

#         except Exception as e:
#              print("no search menu")
#         time.sleep(2);
#         try:
#             element = WebDriverWait(driver, 5).until(
                
#                 #   EC.element_to_be_clickable((By.XPATH,"/html/body/header/nav[1]/div/div/div/div[4]/div[3]/div[2]/form/div[2]/div[1]/div/div/input"))
#                 EC.element_to_be_clickable((By.CSS_SELECTOR,"#sc\.keyword"))
#             )
#             element.send_keys(self.value)

#         except Exception as e:
#             print(e)
#         time.sleep(2)
      
            
#     def fetch_company_suggestions(self):
        
#         driver = self.driver;
#         time.sleep(5);
#         try:
#             # dropdown = driver.find_elements(By.XPATH,'//*[@id="sc"]/div[2]/div[1]/div/div/div')
#             dropdown = driver.find_elements(By.CSS_SELECTOR,'#scBar > div > div.d-flex.col-6.p-0.search__SearchStyles__searchKeywordContainer > div > div > div.autocomplete-suggestions ')
            
#             for i in dropdown:
#                 self.company_names = i.get_attribute("innerText").split("\n")
#                 # print(i.get_attribute("innerText").split("\n"))
#         except Exception as e:
#             print(e)
#         # print(self.company_names)
#         time.sleep(2);
   
   
#     def submit(self):
        
        
        
#         driver = self.driver;
#         # score = self.my_score
#         print(self.score)
#         for value in self.company_names:
#             print(value)
            
#             print(fuzz.ratio(self.value.lower(), value.lower()))            
#             # self.score.append(fuzz.ratio(self.value.lower(), value.lower())); 
            
#         time.sleep(2);
#         # print(self.score)
        
#         try:
#             # self.driver.find_element(By.XPATH,"//*[@id='scKeyword']").clear()
#             self.driver.find_element(By.CSS_SELECTOR,"#sc\.keyword").send_keys(Keys.CONTROL + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
#         except Exception as e:
#             print("issue while cleaning search bar")
#             # print(e)

#         print("123")
#         try:
#             # element = WebDriverWait(driver, 5).until(
#             #       EC.element_to_be_clickable((By.XPATH,"//*[@id='scKeyword']"))

#             # )
#             element = WebDriverWait(driver, 5).until(
#                   EC.element_to_be_clickable((By.CSS_SELECTOR,"#sc\.keyword"))

#             )
#             element.send_keys(self.company_names[self.score.index(max(self.score))])
#             element.send_keys(Keys.RETURN);   
            
#         except Exception as e:
#             print("issue while sending company name")
#             # print(e)
            
            
#         try:
#             # dropdown = driver.find_element(By.CSS_SELECTOR,'#MainCol > div > div:nth-child(2) > div > div > div >div:nth-child(2) >h2 >a ').click()
#             dropdown = driver.find_element(By.CSS_SELECTOR,'//*[@id="scBar"]/div/button/span/span').click()
#             # dropdown = driver.find_element(By.CLASS_NAME,'col-9.pr-0').click();
#         except Exception as e:
#             pass
#             # print(e)
#             # col-9 pr-0 > h2 
        
#         time.sleep(2);


#     def scrape_details_Heading(self):
#         driver = self.driver

#         try:
#             dropdown = driver.find_elements(By.XPATH,'//*[@id="EIProductHeaders"]/div/a[2]/div')
#             for i in dropdown:
#                 self.Reviews=i.get_attribute("innerText")   
#                 print(i.get_attribute("innerText"))
#         except Exception as e:
#             print(e)
#         time.sleep(2)
#         try:
#             dropdown = driver.find_elements(By.XPATH,' //*[@id="EIProductHeaders"]/div/a[3]/div')
#             for i in dropdown:
#                 self.Reviews=i.get_attribute("innerText")   
#                 print(i.get_attribute("innerText"))
#         except Exception as e:
#             print(e)

#         time.sleep(2)
        
#         # element = driver.find_element(By.CSS_SELECTOR,'.stickyNavWrapper > div  div:nth-child(2) > div > div > div   a:nth-child(2)').click()
#         # time.sleep(2);
        
        


#     def get_detailed_review(self):
        
#         driver = self.driver
#         try:
#             cards = driver.find_elements(By.CSS_SELECTOR, '#ReviewsFeed > ol > li ')
            
#             for i in cards:
                
                
#                 # print(i)
#                 # #  getting rating here
#                 try:
#                         reviews = i.find_elements(By.CSS_SELECTOR,'#ReviewsFeed > ol > li > div > div  > div > div > div  > span:nth-child(1)')
#                         print(reviews[0].text);
#                 except Exception as e:
#                             print("no star here *")
#                     #  here i am trying get review heading 
#                 try:
#                         reviews1 = i.find_elements(By.CSS_SELECTOR, '.mt-xsm.px-std > h2 a')
#                         print(reviews1[0].text)
#                 except Exception as e:
#                             print("no heading here *")
                
#                 # #  here we are getting pros and cons 
                
#                 try:
#                         value =i.find_element(By.CSS_SELECTOR,' #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5) > div.px-std >div:nth-child(1) >p.mb-0.strong')
#                         # checking if we get pros or not 
#                         print(value.text)
#                         if value.text == "Pros" :
#                             #  if we got pros we need to check if it has inner data or not 
#                             try:
#                                 pros_value = i.find_element(By.CSS_SELECTOR,' #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5)> div.px-std > div >p:nth-child(2)')
#                                 print(pros_value.text)
#                             except Exception as e:
#                                 print("did not got pros value or data ")
#                 except Exception as e:
#                         print("no Pros Mentioned here")
                        
#                 #  i here will check cons 
                
#                 try:
#                         cons =i.find_element(By.CSS_SELECTOR,'  #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5) > div.px-std >div:nth-child(2) >p.mb-0.strong')
#                         # checking if we get pros or not 
#                         print(cons.text)
#                         if cons.text == "Cons" :
#                             #  if we got pros we need to check if it has inner data or not 
#                             try:
#                                 cons_value = i.find_element(By.CSS_SELECTOR,' #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5) > div.px-std >div:nth-child(2) >p:nth-child(2)')
#                                 print(cons_value.text)
#                             except Exception as e:
#                                 print("did not got cons value or data ")
#                 except Exception as e:
#                         print("no Cons Mentioned here")
                        
                        
                        
                        
#         except Exception as e:
#             print("did not got review listing")


#     def next_page_details(self):
#         #EIProductHeaders > div > a.eiCell.cell.reviews > span.subtle
#         # print("in next page")
#         driver = self.driver
#         time.sleep(2)
#         data = []
#         fields = ['rating','title' , 'likes' , 'dislikes'] 
#         star_value=''
#         pros_data=''
#         cons_data=''
#         heading_data = ''
#         isPresent = True
        
#         # clicking on review
#         try:
#                         reviews = i.find_elements(By.CSS_SELECTOR,'#EIProductHeaders > div > a.eiCell.cell.reviews > span.subtle').click()
                       
#         except Exception as e:
#             print("issue while clicking review button")
            
#         while(isPresent):
#             time.sleep(10)
#         #  this below script was for banner issue that i was facing in mobile 
#     #         try:
#     #             driver.execute_script("""
#     # var l = document.getElementById("SmarterBanner");
#     # l.parentNode.removeChild(l);
#     # """)
#     #         except Exception as e:
                
#     #             print("no banner displayed")
                
                
                
                
                
#     #         try:
#     #             driver.execute_script("""
#     # var l = document.getElementById(".d-flex.justify-content-between.mx-std.eiHeaderLinks");
#     # l.parentNode.removeChild(l);
#     # """)
#     #         except Exception as e:
                
#     #             print("no banner2 displayed")
#             # page_no=WebDriverWait(driver, 20).until(
#             #  EC.element_to_be_clickable((By.CSS_SELECTOR,'#MainContent > div > div:nth-child(1) > div.d-flex.flex-column.align-items-top > div > div.pageContainer > button.nextButton.css-1hq9k8.e13qs2071 > span > svg')))
         
#             # print(page_no.text)
#             # driver.execute_script("document.querySelectorAll('#MainContent > div > div:nth-child(1) > div.d-flex.flex-column.align-items-top > div > div.pageContainer > button.nextButton.css-1hq9k8.e13qs2071 > span > svg')[0].click()")
            
            
            
#             # svg_element = driver.find_element(By.CSS_SELECTOR, "#MainContent > div > div:nth-child(1) > div.d-flex.flex-column.align-items-top > div > div.pageContainer > button.nextButton.css-1hq9k8.e13qs2071")
#             # driver.execute_script("arguments[0].click();", svg_element)
            
            
            
            
            
            
#             # WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#MainContent > div > div:nth-child(1) > div.d-flex.flex-column.align-items-top > div > div.pageContainer > button.nextButton.css-1hq9k8.e13qs2071 > span > svg'")))
#             # driver.execute_script("var x= document.getElementsByClassName('buy-button buy-button--sticky buy-button--buy-now visible-xs visible-sm')[0];"+"x.click();")
#             # page_no.click()
#             print("just clicked !!!!!!!!!")
#             time.sleep(3)
#             try:
#                 cards = driver.find_elements(By.CSS_SELECTOR, '#ReviewsFeed > ol > li ')
            
#                 for i in cards:
                    
#                     # print(i)
#                     # #  getting rating here
#                     try:
#                         reviews = i.find_elements(By.CSS_SELECTOR,'#ReviewsFeed > ol > li > div > div  > div > div > div  > span:nth-child(1)')
#                         star_value = reviews[0].text
#                         # print(reviews[0].text);
#                     except Exception as e:
                        
#                         reviews[0].text = "no star here"
#                             # print("no star here *")
#                     #  here i am trying get review heading 
#                     try:
#                         reviews1 = i.find_elements(By.CSS_SELECTOR, '.mt-xsm.px-std > h2 a')
#                         heading_data = reviews1[0].text
#                         # print(reviews1[0].text)
#                     except Exception as e:
#                             # print("no heading here *")
#                             heading_data = "no heading here"
#                     # #  here we are getting pros and cons 
                    
#                     try:
#                             value =i.find_element(By.CSS_SELECTOR,' #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5) > div.px-std >div:nth-child(1) >p.mb-0.strong')
#                             # checking if we get pros or not 
#                             print(value.text)
#                             if value.text == "Pros" :
#                                 #  if we got pros we need to check if it has inner data or not 
#                                 try:
#                                     pros_value = i.find_element(By.CSS_SELECTOR,' #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5)> div.px-std > div >p:nth-child(2)')
#                                     pros_data = pros_value.text
#                                     # print(pros_value.text)
#                                 except Exception as e:
#                                     pros_data ="did not got pros value or data "
#                                     # print("did not got pros value or data ")
#                     except Exception as e:
#                             pros_data = "no pro element"
#                             # print("no Pros Mentioned here")
                            
#                     #  i here will check cons 
                    
#                     try:
#                             cons =i.find_element(By.CSS_SELECTOR,'  #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5) > div.px-std >div:nth-child(2) >p.mb-0.strong')
#                             # checking if we get pros or not 
#                             print(cons.text)
#                             if cons.text == "Cons" :
#                                 #  if we got pros we need to check if it has inner data or not 
#                                 try:
#                                     cons_value = i.find_element(By.CSS_SELECTOR,' #ReviewsFeed > ol > li > div.gdGrid > div:nth-child(5) > div.px-std >div:nth-child(2) >p:nth-child(2)')
#                                     cons_data = cons_value.text
#                                     # print(cons_value.text)
#                                 except Exception as e:
#                                     cons_value.text = "did not get cons value or data "
#                                     # print("did not get cons value or data ")
#                     except Exception as e:
#                             cons_data = "no cons element here"
                    
#                     data.append([star_value,heading_data,pros_data,cons_data])
#                             # print("no Cons Mentioned here"  
#             except Exception as e:
#                 print("did not got review listing")
#             # try:
#             #     element = WebDriverWait(driver, 10).until(
#             # EC.element_to_be_clickable((By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[1]/div[2]/nav/ul/li[11]/a'))
#             # ).is_displayed()
#             #     isPresent = True;
#             # except NoSuchElementException:
#             #     isPresent = False;
#             # print(isPresent)
            
#             try:
#                 element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#MainContent > div > div:nth-child(1) > div.d-flex.flex-column.align-items-top > div > div.pageContainer > button.nextButton.css-1hq9k8.e13qs2071'))).is_displayed()
#                 isPresent = True;
#                 try:
#                     s = driver.find_element(By.CSS_SELECTOR,'#MainContent > div > div:nth-child(1) > div.d-flex.flex-column.align-items-top > div > div.pageContainer > button.nextButton.css-1hq9k8.e13qs2071')
#                     # perform click with execute_script method
#                     driver.execute_script("arguments[0].click();",s)
#                 except Exception as e:
#                         print("was not able to click")
#             except Exception as e:         
#                 isPresent = False;
#                 print("no next button")
           
#             print(isPresent)
#             time.sleep(2)
#         with open('export_glassdoor.csv', 'w') as f:
            
#             write = csv.writer(f)
#             write.writerow(fields)
#             write.writerows(data)
#             # print(data) 
   
   
   
# # class Indeed:
     
#     def __init__(self):
        
#         self.value = "google"
#         self.company_names = [];
#         self.company_names_score = [];
        
        
#         #  for this i need to update my chrome 
#         # chrome_options = uc.ChromeOptions()

#         # self.driver = uc.Chrome(
#         #     options=chrome_options,
#         #     seleniumwire_options={}
#         # )
#         # mobile_emulation = {                 
#         #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
#         #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
#         #  }
#         # mobile_emulation = {                 
#         #         "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
#         #         "userAgent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
#         #     }
#         # chrome_options = Options();
#         # # chrome_options.add_argument('--headless')
#         # # chrome_options.add_argument('--disable-gpu')
#         # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#         # self.driver = webdriver.Chrome(options=chrome_options)     
#         self.driver = uc.Chrome()


#     def _login(self):
#         # siliy69430@corylan.com
#         # root@123
#         driver = self.driver
#         driver.get("https://www.indeed.com/companies")
#         time.sleep(2);
#         try:
#             element = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR,'#gnav-main-container > div > div > div.gnav-header-4atbqz.e37uo190 > div.gnav-header-chsy6r.e37uo190 > div.gnav-header-1ble2gn.eu4oa1w0 > a'))
#             ).click()
            
#         except Exception as e:
#             print("no sign in button")
#         time.sleep(5)
#         #  now finding email input form 
#         try:
#                     element = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.XPATH,'//*[@id="ifl-InputFormField-3"]'))
#                         )
#                     element.send_keys("siliy69430__@corylan.com")

#                     # element.send_keys(Keys.RETURN)
#                     # button = driver.find_element(By.CSS_SELECTOR,'#emailform > button > span')
#                     # button.click()
                    
#         except Exception as e:
#                     print("no email button")
           
#         time.sleep(5)           
                    
#         # try:
#         # element = WebDriverWait(driver, 10).until(
#         #             EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox"]'))
#         #                 ).click()
#         #             print("check box was clicked")
#         # except Exception as e:
#         #             print("bot detected lol for email !!!!!!!")
                    
        
#         time.sleep(5)
#         try:
#                     print("312")
#                     element = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR,'#emailform > button > span'))
#                         ).click()
                    
#         except Exception as e:
#                     print("i hit enter here for email")
        
                
#         try:
#                     element = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR,'#ifl-InputFormField-131'))
#                         )
#                     element.send_keys("root@123")

#         except Exception as e:
#                     print("no password button")
        
        
#         # try:
#         element = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR,'#checkbox'))
#                         ).click()
#                     # print("check box was clicked")
                    
#         # except Exception as e:
#         #             print("bot detected lol at password!!!!!!!")
                    
                    
                    
#         try:
#                     element = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR,'#registerform > button > span'))
#                         ).click()
               
                    

#         except Exception as e:
#                     print("cant find the login button")
                
  
#     def search(self):
#         driver = self.driver;
#         # driver.get("https://www.indeed.com/companies")
#         time.sleep(2);
#         try:
#             element = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.XPATH,'//*[@id="ifl-InputFormField-3"]'))
#                 )

#         except Exception as e:
#             print(e)
            
#         #  clicking on submit
#         element.send_keys(self.value);
#         try:
#             element = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[1]/form/div/div[2]/button'))
#                 ).click();

#         except Exception as e:
#             print(e)
#         time.sleep(2)


#     def select_company(self):
#         driver = self.driver;
#         try:
#             dropdown = driver.find_elements(By.CLASS_NAME,"css-1s5eo7v.eu4oa1w0")
#             for i in dropdown:
#                 self.company_names.append(i.get_attribute("innerText"))
#                 # print(i.get_attribute("innerText"))
#         except Exception as e:
#             print(e)

#         for value in (self.company_names):            
#             self.company_names_score.append(fuzz.ratio(self.value.lower(), value.lower()));
#         time.sleep(2);
#         try:
#             driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div[1]/form/div/div[1]/div/div/div/span/input').send_keys(Keys.CONTROL + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
#         except Exception as e:
#             print("issue while cleaning search bar")
#             print(e)
#         try:
#             element = WebDriverWait(driver, 5).until(
#                   EC.element_to_be_clickable((By.XPATH,'//*[@id="ifl-InputFormField-3"]'))

#             )
#             #  entering again while making exactly like drop down values
#             element.send_keys(self.company_names[self.company_names_score.index(max(self.company_names_score))])
            
#             element.send_keys(Keys.RETURN);
            
#         except Exception as e:
#             print(e)
#         #  checking if we are getting unique value or not 
#         try:
#             dropdown = driver.find_element(By.CLASS_NAME,'css-1s5eo7v.eu4oa1w0').click();
#         except Exception as e:
#             print(e)
#         time.sleep(5);   


#     def general_score(self):
#         driver = self.driver;
        
#         # getting basic information here 
#         try:
#             work_happiness_score = driver.find_elements(By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[1]/section/div[1]/div/div[2]/div[1]/div[1]/div[1]')
#             for i in work_happiness_score:
#                 print(i.get_attribute("innerText"))
#         except Exception as e:
#             print(e)

#         time.sleep(2);

#         try:
#             appreciation_score = driver.find_elements(By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[1]/section/div[1]/div/div[2]/div[2]/div[1]/div[1]')
#             for i in appreciation_score:
#                 print(i.get_attribute("innerText"))
#         except Exception as e:
#             print(e)
#         time.sleep(2);

#         try:
#             learning_score = driver.find_elements(By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[1]/section/div[1]/div/div[2]/div[3]/div[1]/div[1]')
#             for i in  learning_score:
#                 print(i.get_attribute("innerText"))
#         except Exception as e:
#             print(e)
#         time.sleep(2);


#     # def more_detailed_review(self):
#         driver = self.driver;
#         #cmp-skip-header-desktop > div > ul > li:nth-child(3) > a > span
#         try:
#             element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#cmp-skip-header-desktop > div > ul > li:nth-child(3) > a > span')))
#             element.click()
#         except Exception as e:
#             print(e)
#         # try:
#         #     element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cmp-container"]/div/div[1]/main/div[2]/div[6]/section/div/div[1]/div[2]/a')))
#         #     element.send_keys(Keys.RETURN);
#         # except Exception as e:
#         #     print(e)
            
#         time.sleep(2);
        
#         #  here we are star and info from the first page dont know where will i use it again
        
#         # get star rating
#         # css-rr5fiy eu4oa1w0
#         # try:
#         #     rating_score = driver.find_elements(By.CLASS_NAME,'css-1c33izo.e1wnkr790')
#         #     for i in rating_score:
#         #         print(i.get_attribute("innerText").split("\n"))
#         # except Exception as e:
#         #     print(e)

#         # try:
#         #     review_heading_info = driver.find_elements(By.CLASS_NAME,'css-82l4gy.eu4oa1w0')
#         #     for i in review_heading_info:
#         #         print(i.get_attribute("innerText"))
#         # except Exception as e:
#         #     print(e)
        
#         time.sleep(2);


#     def more_detailed_review(self):
#         print("::::::::::::")
#         driver = self.driver
       
#         dropdown = driver.find_elements(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys')          
#         for i in dropdown:
#             # print(i)
#             try:
#                 rating = i.find_element(By.CLASS_NAME,'css-1c33izo.e1wnkr790')
#                 print(rating.text)
#             except Exception as e:
#                 print("no rating")
#                 pass
#             try :
#                 main_Data = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div.css-e6s05i.eu4oa1w0 > div.css-rr5fiy.eu4oa1w0')
#                 print(main_Data.text)
#             except Exception as e:
#                 print("no main_data")
#                 pass
#             #  checking pros and cons here 
            
#             try:
#                 pros = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div >h2.css-yuegbt.e1tiznh50') 
                
#                 # print(pros.text)
#                 if pros.text == "Pros":
#                     pros_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div:nth-child(1) > div >span')
#                     print(pros_value.text)    
#             except Exception as e:
#                 print("no pros")
#                 pass
#             try:
#                 cons = i.find_element(By.CSS_SELECTOR,'#cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div:nth-child(2)>h2.css-i6a6qi.e1tiznh50') 
                
#                 # print(cons.text)
#                 if cons.text == "Cons":
#                     cons_value = i.find_element(By.CSS_SELECTOR,' #cmp-container > div > div.i-unmask.css-kyg8or.eu4oa1w0 > main > div.css-16ydvd8.e37uo190 > div.css-1cm81qf.eu4oa1w0 > div.cmp-ReviewsList > div.css-t3vkys > div > div > div:nth-child(2)  >div:nth-child(4) > div>div:nth-child(2) > div >span')
#                     print(cons_value.text)    
#             except Exception as e:
#                 print("no cons")
#                 pass
        
    
    
    
    
                
class Naukri_com:
    
    
    def __init__(self):
        
        # email -> sigep86197@ekbasia.com
        # password -> root@123
        company = ' '.join([str(elem) for elem in sys.argv[1:]])
        self.company_suggestion  = []
        self.company_names_score = []
        self.value = company 
        chrome_options = Options()
        # chrome_options.headless = True
        # chrome_options.add_argument("--start-maximized");
        
        # chrome_options.add_argument("--window-size=2560,1440")

        
        self.driver = webdriver.Chrome()    
        self.driver = webdriver.Chrome(chrome_options = chrome_options)
        self.driver.set_window_rect(width=1920, height=1080)

  
    def login(self):
        driver = self.driver
        driver.get("https://www.ambitionbox.com")
        
    #  here i am handling the current page to chk change in the new page so as to hanle login page 
        main_page = driver.current_window_handle
        
        time.sleep(5)
        
        
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#ambitionbox-header > div > div.right-container > div > div.list-item.profileIcon > a'))
                ).click()
            time.sleep(2)
        except Exception as e:
            print(e)
        #  login in using naukri_email and naukri_password
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'  #loginModal > div > div > div.modal__body > div.social-login__button.naukri > p'))
                ).click()
            time.sleep(2)
        except Exception as e:
            print(e)
            
    #  handling the changing the window here as we are going to the signin page here we are looking for the driver.change in window handle 
    
        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle

        driver.switch_to.window(login_page)
        #  entering email and password 
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#usernameField'))
                )
            element.send_keys("sigep86197@ekbasia.com")
            time.sleep(2)
        except Exception as e:
            print(e)
            
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#passwordField'))
                )
            element.send_keys("root@123")
            time.sleep(2)
        except Exception as e:
            print(e)
        element.send_keys(Keys.RETURN)

        driver.switch_to.window(main_page)
        
        time.sleep(2);
        
        
    def search(self):
        driver = self.driver
        driver.get("https://www.ambitionbox.com")
        time.sleep(2)
        element = driver.find_element(By.CLASS_NAME,'hero-section__searchbox').click()
        time.sleep(4)
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#homeTypeahead > div > div > div.component-search-company.search-company-wth-btn.home-search-bar > span > input'))
                )
            element.send_keys(self.value)
            time.sleep(2)
        except Exception as e:
            print(e)
        
        
        time.sleep(4);
        
    
    def suggestion(self):
        driver = self.driver;

        time.sleep(2)
        
        try:

            dropdown = driver.find_elements(By.CLASS_NAME,'tt-dataset.tt-dataset-company-search')
        
            for i in dropdown:
                
                i.find_element(By.CSS_SELECTOR,"#homeTypeahead > div > div > div.border-inputbox.component-search-company.search-company-wth-btn.home-search-bar > span > div > div.tt-dataset.tt-dataset-company-search > div:nth-child(2) > div.suggestion > div > span")
                self.company_suggestion.append(i.text.split('\n')[1:][::3])
                print(i.text.split('\n')[1:][::3]) 
        except Exception as e:
            print(e)
        time.sleep(5)
    
        
    def select_company(self):
        driver = self.driver
        company_suggestion = self.company_suggestion[0]
        for value in company_suggestion:            
            self.company_names_score.append(fuzz.ratio(self.value.lower(), value.lower()));
        print(self.company_names_score)
        value = company_suggestion[self.company_names_score.index(max(self.company_names_score))]
        # printing value here 
        print(value)    
        element = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[1]/span/input').send_keys(Keys.CONTROL + Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
        time.sleep(4)
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#homeTypeahead > div > div > div.component-search-company.search-company-wth-btn.home-search-bar > span > input'))
                )
            element.send_keys(value)
            element.send_keys(Keys.RETURN)
            time.sleep(4)
        except Exception as e:
            print(e) 
        time.sleep(5)
        
    
    # def detail_review(self):
      
    #     driver = self.driver
        
    #     time.sleep(2)
    #     #getting star value
    #     try:
    #         star = driver.find_element(By.CSS_SELECTOR,' #abh_info > div.content-wrap > div.content > div > p > span')
    #         print("review::"+star.text)
    #     except Exception as e:
    #         print(e) 
                   
    #     try:
    #         print("********___________")
    #         dropdown = driver.find_elements(By.CSS_SELECTOR,'#all-reviews-card > div.ab_comp_review_card')          
    #         for i in dropdown:
                
                
    #             #all-reviews-card > div.ab_comp_review_card > div:nth-child(3) >div:nth-child(2) > span > span.avg-rating.bold-Labels
    #             star = i.find_element(By.CSS_SELECTOR,'#all-reviews-card > div.ab_comp_review_card > div:nth-child(3) >div:nth-child(2) > span > span.avg-rating.bold-Labels')
                
    #             print(star.text)
                
    #             print("above is star")
    #             #  here i am getting review
    #             #  main_listing
    #             review = i.find_element(By.CSS_SELECTOR,"#all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body")
                
    #             # this is the listing of the likes 
    #             try:
    #                 pass
    #                 review = i.find_element(By.CSS_SELECTOR," #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(1) >h3.input-fields.sub-heading")
    #                 # print(review.text)
    #                 if review.text == "Likes":
    #                         like = i.find_element(By.CSS_SELECTOR,"  #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(1) >p.body-medium.overflow-wrap")
    #                         print("pros :"+like.text)
    #                 else:
    #                     print("__")
               
    #             except:
    #                 print("*__*")
    #                 pass
    #             #  this is the listing of the dislikes from the users
    #             try:
    #                 pass
    #                 review = i.find_element(By.CSS_SELECTOR," #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(2) >h3.input-fields.sub-heading")
    #                 # print(review.text)
    #                 if review.text == "Dislikes":
    #                         dislike = i.find_element(By.CSS_SELECTOR,"  #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(2) >p.body-medium.overflow-wrap")
    #                         print("cons :"+dislike.text)
    #                 else:
    #                     print("__")
               
    #             except:
    #                 print("*__*")
    #                 pass
    #             print("_____________________________________________________________________________")
               
    #     except NoSuchElementException:
    #         pass       
    #     time.sleep(5)
       
     
    # def is_element_exist(self):
    #     driver = self.driver
    #     try:
    #         driver.find_element(By.CSS_SELECTOR,'#ab-paginator-wrapper > a > i.next')
    #         return True
    #     except NoSuchElementException:
    #         return False   
    
    
    def full_detail_review(self):
        driver = self.driver
        time.sleep(2)
        isPresent = True
        data = []
        fields = ['rating', 'likes' , 'dislikes'] 
        star_value=''
        pros=''
        cons=''
        while(isPresent):
            print("start")
            time.sleep(5)
            try:
                
                dropdown = driver.find_elements(By.CSS_SELECTOR,'#all-reviews-card > div.ab_comp_review_card') 
                
                        
                for i in dropdown:
                    
                    
                    
                    #all-reviews-card > div.ab_comp_review_card > div:nth-child(3) >div:nth-child(2) > span > span.avg-rating.bold-Labels
                    try:
                        star = i.find_element(By.CSS_SELECTOR,'#all-reviews-card > div.ab_comp_review_card > div:nth-child(3) >div:nth-child(2) > span > span.avg-rating.bold-Labels')
                        
                        star_value=star.text
                        # print(star.text)
 
                    except Exception as e:    
                        star_value="No Star"    
                    # isPresent = False;
                    
                        # print("no star")
                    
                    #  here i am getting review
                    #  main_listing
                    try:
                        review = i.find_element(By.CSS_SELECTOR,"#all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body")
                        
                        
                        # this is the listing of the likes 
                        try:
                            pass
                            review = i.find_element(By.CSS_SELECTOR," #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(1) >h3.input-fields.sub-heading")
                            # print(review.text)
                            if review.text == "Likes":
                                    like = i.find_element(By.CSS_SELECTOR,"  #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(1) >p.body-medium.overflow-wrap")
                                    # print("pros :"+like.text)
                                    pros=like.text
                            else:
                                # print("__")
                                pros="no pros jsut extra info"
                    
                        except:
                            # print("no pros")
                            pros="no pros"
                            # pass
                        try:
                        
                            review = i.find_element(By.CSS_SELECTOR," #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(2) >h3.input-fields.sub-heading")
                            # print(review.text)
                            if review.text == "Dislikes":
                                try:
                                    
                                    dislike = i.find_element(By.CSS_SELECTOR,"  #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(2) >p.body-medium.overflow-wrap")
                                    # print("cons :"+dislike.text)
                                    cons=dislike.text
                                except Exception as e:        
                                    cons="no cons"
                            else:
                                    cons="no cons just extra info"
                                    # print("no cons just extra info")
                    
                        except Exception as e:         
                            cons="no cons"
                            # print("no cons")
                    except Exception as e:         
                    # isPresent = False;
                        pros="no main body so no pro"
                        # print("no main body")
                        
                        
                        
                        
                    #  this is the listing of the dislikes from the users
                    # try:
                        
                    #     review = i.find_element(By.CSS_SELECTOR," #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(2) >h3.input-fields.sub-heading")
                    #     # print(review.text)
                    #     if review.text == "Dislikes":
                    #         try:
                                
                    #             dislike = i.find_element(By.CSS_SELECTOR,"  #all-reviews-card > div.ab_comp_review_card > div:nth-child(4) > div > div.review-body > div:nth-child(2) >p.body-medium.overflow-wrap")
                    #             print("cons :"+dislike.text)
                    #             cons=dislike.text
                    #         except Exception as e:        
                    #             cons="no cons"
                    #     else:
                    #             pros="no cons"
                
                    # except Exception as e:         
                    #     cons="no main body for cons"
                    #     print("no main body")
                    print("_____________________________________________________________________________")
                    data.append([star_value,pros,cons])
                
            except Exception as e:         
                    # isPresent = False;
                    print("no listing avaiable")
                    # pass
            # time.sleep(5)
            # data.append([star_value,pros,cons])
            print(data)
            # print(data)
            try:
                
                element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#ab-paginator-wrapper > a > i.next'))).is_displayed()
                isPresent = True;
                try:
                    
                    s = driver.find_element(By.CSS_SELECTOR,'#ab-paginator-wrapper > a > i.next')
                        # perform click with execute_script method
                    driver.execute_script("arguments[0].click();",s)
                except Exception as e:
                    
                    print("no next button")
                    
            except Exception as e:         
                    isPresent = False;
                    print("no next page")
            print(isPresent)
            
            
            
            
            
        with open('naukri_export.csv', 'w') as f:
                write = csv.writer(f)
                
                write.writerow(fields)
                write.writerows(data)
                # print(data)


if __name__ == '__main__':  

    rt = Naukri_com()
    rt.login()
    rt.search()
    rt.suggestion()
    rt.select_company()
    rt.full_detail_review()
    
