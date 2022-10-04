from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys

kakao_id=
kakao_password=

# 다운받은 크롬드라이버를 불러와서 사이트를 실행한다.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://reservation.everland.com/web/el.do?method=productMain&top_menu_id=01')

# 로그인
driver.find_element(By.ID, 'h_btn_log').click()
driver.find_element(By.CLASS_NAME, 'kakaotalk').click()
driver.find_element(By.ID, 'kakaotalkBtn').click()
driver.find_element(By.ID, 'id_email_2').send_keys(kakao_id)
driver.find_element(By.ID, 'id_password_3').send_keys(kakao_password)
driver.find_element(By.CLASS_NAME, 'submit').click()

# 호러메이즈 접속
time.sleep(3)
driver.find_element(By.XPATH, '//article[@id="list_0102"]/ul/li[11]').click()

# 날짜 입력
time.sleep(2)
driver.find_element(By.XPATH, '//a[text()="7"]').click()
driver.find_element(By.ID, 'CALENDAR_BTN_NEXT').click()

# 팝업 처리
try:
  driver.switch_to.alert.accept()
except:
  pass

# 호러메이즈 상세화면
time.sleep(1)

while(True):
  # 인원 추가
  driver.find_element(By.XPATH, '//dd[@id="base_prod_tit"]/em').click()
  driver.find_element(By.ID, 'up_base_prod0').click()
  driver.find_element(By.ID, 'up_base_prod0').click()

  # 시간 확인
  driver.find_element(By.ID, 'time_tit').click()
  time_slots = driver.find_elements(By.XPATH, '//ul[@id="opt13_time"]/li/span/small[string-length(text())>4]')
  if(len(time_slots) > 0):
    for slot in time_slots: 
      slot.click()
        
      # 예약 버튼 클릭
      driver.find_element(By.ID, 'time_tit').click()
      time.sleep(1)
      driver.find_element(By.ID, 'btn_cartInsert1').click()
      time.sleep(2)

      # 잔여 수량 부족 팝업
      try:
        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.find_element(By.ID, 'time_tit').click()
        continue
      except:
        # 동의
        driver.find_element(By.XPATH, '//p[@class="total"]/label/i').click()
        driver.find_element(By.XPATH, '//a[text()="확인"]').click()

        # 잔여 수량 부족 팝업
        try:
          time.sleep(1)
          driver.switch_to.alert.accept()
          time.sleep(1)
          driver.find_element(By.ID, 'time_tit').click()
          continue
        except:
          break
    driver.refresh()
  else:
    driver.refresh()
    continue
# selenium이 꺼지지 않도록 유지
while(True):
  pass
 