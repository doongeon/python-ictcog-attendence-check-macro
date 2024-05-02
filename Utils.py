from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

MANAGER_ID = 'your id'
MANAGER_PW = 'your password'

def moveToMyPage(wd):
  url = "https://lms.ictcog.or.kr/page/uat/uia/loginUsr.do"

  wd.get(url)

  sId = wd.find_element(By.ID, 'sId')

  sId.send_keys(MANAGER_ID)

  sPw = wd.find_element(By.ID, 'sPassword')

  sPw.send_keys(MANAGER_PW)

  wd.find_element(By.CLASS_NAME, 'btn_login').click()

  wd.find_element(By.CLASS_NAME, 'myPage').click()
  time.sleep(0.5)

  #get first child window
  chwd = wd.window_handles

  wd.switch_to.window(chwd[1])

  wd.find_element(By.CSS_SELECTOR, '.bbsList tbody tr td a').click()
  time.sleep(0.5)

  wd.find_element(By.XPATH, '/html/body/div[1]/section/div/div[1]/div/div[2]/div[1]/ul/li[10]').click()
  time.sleep(0.5)
  
def makeAttendance(wd):
  wd.find_elements(By.CSS_SELECTOR, '#attendForm .button_area .button_right a')[0].click()
  alert = wd.switch_to.alert
  alert.accept()
  time.sleep(0.5)
  alert = wd.switch_to.alert
  alert.accept()
  time.sleep(0.5)
  chwd = wd.window_handles
  wd.switch_to.window(chwd[1])
  time.sleep(0.5)

def makeAbsent(wd, absentStudents):
  count = 0;

  tr = wd.find_elements(By.CSS_SELECTOR, '.bbsList tbody tr')
  sheets = wd.find_elements(By.CSS_SELECTOR, '.divider .pagination li a')

  for k in range(len(sheets)):
    if(count == len(absentStudents)): break;
    sheets = wd.find_elements(By.CSS_SELECTOR, '.divider .pagination li a')
    sheets[k].click()
    tr = wd.find_elements(By.CSS_SELECTOR, '.bbsList tbody tr')

    for i in range(len(tr) - 2):
      if(count == len(absentStudents)): break;
      td = tr[i].find_elements(By.CSS_SELECTOR, 'td')
      
      if(td[1].text in absentStudents):
        if(count == len(absentStudents)): break;
        count = count + 1;

        for j in range(3):
          td = tr[i].find_elements(By.CSS_SELECTOR, 'td')
          attendance = td[5].find_elements(By.TAG_NAME, 'a')
          attendance[j].click()
          time.sleep(0.5)
          abseBtn = wd.find_element(By.ID, 'abseBtn')
          abseBtn.click()
          time.sleep(0.5)
          alert = wd.switch_to.alert
          alert.accept()
          time.sleep(0.5)
          chwd = wd.window_handles
          wd.switch_to.window(chwd[1])
          time.sleep(0.5)
          tr = wd.find_elements(By.CSS_SELECTOR, '.bbsList tbody tr')

def absentChecker(wd, absentStudents):
  moveToMyPage(wd);
  makeAttendance(wd);
  makeAbsent(wd, absentStudents);

def readAbsentStudent():
  absentStudents = input('결석 강의생을 모두 입력하세요. (ex. 나동건,이재찬)\n1,2,3차 모두 결석처리 됩니다.\n')
  return absentStudents.split(',');

def App():
  absentStudents = readAbsentStudent();
  wd = webdriver.Chrome()
  wd.maximize_window()
  absentChecker(wd, absentStudents);
  wd.close();
  print('결석 체크가 완료되었습니다.')
