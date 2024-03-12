# -*- coding: utf-8 -*-

from xython import jfinder, scolor, youtil, basic_data, pynal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pyclick

class html:
   def __init__(self):
      self.color = scolor.scolor()
      self.auto = pyclick.pyclick()
      self.found_object =""
      self.selected_object =""

      self.driver_path = './chromedriver.exe'  # 본인의 chromedriver 경로를 넣어줍니다.
      chrome_options = webdriver.ChromeOptions()
      s = Service(self.driver_path)
      # 브라우저 꺼짐 방지 옵션
      chrome_options.add_experimental_option("detach", True)

      self.driver = webdriver.Chrome(service=s, options=chrome_options)
      self.web = self.driver

   def connect(self, url, wait_sec=3):
      self.driver.get(url)
      self.driver.implicitly_wait(wait_sec)


   def close_all_child_tabs(self):
      for index in range(2, len(self.web.window_handles)):
         try:
            self.web.switch_to.window(self.web.window_handles[index])
            self.web.close()  # 현재 탭 닫기
         except:
            pass

   def move_to_first_tab(self):
      self.web.switch_to.window(self.web.window_handles[0])

   def move_to_nth_tab(self, input_no):
      self.web.switch_to.window(self.web.window_handles[int(input_no) -1])

   def backword(self):
      self.web.back()  # 뒤로가기

   def forward(self):
      self.web.forward()  # 앞으로가기

   def close_current_tab(self):
      self.web.close()  # 현재 탭 닫기

   def close(self):
      self.web.quit()  # 브라우저 닫기

   def screen_capture(self, file_name):
      self.web.get_screenshot_as_file(file_name)  # 화면캡처

   def open_web_site(self, web_site, wait_sec = 3):
      self.web.get(web_site)
      self.web.implicitly_wait(wait_sec)

   def option(self):

      # 브라우저 꺼짐 방지 옵션
      self.web.add_experimental_option("detach", True)

      # headless 옵션 설정
      self.web.add_argument('headless')
      self.web.add_argument("no-sandbox")

      # 브라우저 윈도우 사이즈
      self.web.add_argument('window-size=1920x1080')

   def count_all_haldles(self):
      # 현재 브라우저의 모든 핸들 보기
      print(self.web.window_handles)
      return self.web.window_handles

   def read_current_haldle(self):
      # 현재 활성화된 핸들 보기
      print(self.web.current_window_handle)
      return self.web.current_window_handle

   def alert_dismiss(self):
      # 경고창으로 이동
      self.web.switch_to.alert.dismiss()

   def alert_text(self):
      alert = self.web.switch_to.alert.text
      print(alert)

   def alert(self):
      # 경고창으로 이동
      alert = self.web.switch_to.alert
      from selenium.webdriver.common.alert import Alert

      # text
      alert.text
      # 확인
      alert.accept()
      # 취소
      alert.dissmiss()

   def move_frame(self):
      # iframe 지정
      element = self.web.find_element_by_tag_name('iframe')

      # 프레임 이동
      self.web.switch_to.frame(element)

      # 프레임에서 빠져나오기
      self.web.switch_to.default_content()

   def move_down_for_scroll_bar(self):
      # 브라우저 스크롤 최하단으로 이동
      self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

   def search_by_link(self, input_text):
      result = self.driver.find_element(By.LINK_TEXT, input_text)  # 링크가 달려 있는 텍스트로 접근
      return result

   def search_by_tag_name(self):
      result = self.driver.find_element(By.TAG_NAME, 'input name').find_element(By.TAG_NAME, 'Cobi_Sub')
      return result

   def search_element(self):
      self.driver.find_element_by_xpath('//*[@id="main-area"]/div[7]/a[2]')  # xpath 로 접근
      self.driver.find_element_by_class_name('ico_search_submit')  # class 속성으로 접근
      self.driver.find_element_by_id('k_btn')  # id 속성으로 접근
      self.driver.find_element_by_link_text('회원가입')  # 링크가 달려 있는 텍스트로 접근
      self.driver.find_element_by_css_selector('#account > div > a')  # css 셀렉터로 접근
      self.driver.find_element_by_name('join')  # name 속성으로 접근
      self.driver.find_element_by_partial_link_text('가입')  # 링크가 달려 있는 엘레먼트에 텍스트 일부만 적어서 해당 엘레먼트에 접근
      self.driver.find_element_by_tag_name('input')  # 태그 이름으로 접근

      #이중으로 find_element를    사용 할 수 있다.

      # input 태그 하위태그인 a 태그에 접근
      self.driver.find_element_by_tag_name('input').find_element_by_tag_name('a')

      # xpath 로 접근한 엘레먼트의 안에 join 이라는 속성을 가진 tag 엘레먼트에 접근
      self.driver.find_element_by_xpath('/html/body/div[3]/form//span[2]').find_element_by_name('join')


      #< EC용 코드 모음 >
      EC.title_is(...)
      EC.title_contains(...)
      EC.presence_of_element_located(...)  # 내가 많이 썼던 코드1
      EC.visibility_of_element_located(...)
      EC.visibility_of(...)
      EC.presence_of_all_elements_located(...)
      EC.text_to_be_present_in_element(...)
      EC.text_to_be_present_in_element_value(...)
      EC.frame_to_be_available_and_switch_to_it(...)
      EC.invisibility_of_element_located(...)
      EC.element_to_be_clickable(...)  # 내가 많이 썼던 코드2
      EC.staleness_of(...)
      EC.element_to_be_selected(...)
      EC.element_located_to_be_selected(...)
      EC.element_selection_state_to_be(...)
      EC.element_located_selection_state_to_be(...)
      EC.alert_is_present(...)

   def keyboard_enter(self, input_obj):
      input_obj.send_keys(Keys.ENTER)

   def keyboard_click(self, input_obj):
      input_obj.send_keys(Keys.LEFT)

   def type_action_for_selected_object(self, input_obj, action):
      input_obj.send_keys(Keys.ENTER)

   def keyboard_tab(self):
      self.auto.type_keyboard("tab")

   def windows_handles(self):
      #w = self.driver.getWindowHandles()
      print(self.web.window_handles)

   def write_by_keyboard(self):
      from selenium.webdriver.common.keys import Keys
      요소 = self.driver.find_element(...)  # 위에서 설명한 방식으로 요소를 찾아 변수로 만든다
      요소.send_keys("보낼텍스트값 or Keys.요소")
      """
      #< Keys.요소모음 >
      Keys.ENTER or Keys.RETURN  # 엔터 입력
      Keys.ARROW_DOWN  # 화살표 아래 입력
      Keys.BACK_SPACE  # 백스페이스 입력
      Keys.CONTROL  # 컨트롤키 입력
      """

   def write_text(self, input_object, input_text):
      input_object.send_keys(input_text)

   def write_text_at_current(self, input_text):
      self.auto.type_text_one_by_one(input_text)

   def type_action_key(self, input_text):
      self.auto.type_action_key(input_text)


   def get_object_by_id(self, input_id):
      self.found_object = self.driver.find_element(By.ID, input_id)
      return self.found_object

   def get_object_by_xpath(self, input_id):
      self.found_object = self.driver.find_element(By.ID, input_id)
      return self.found_object

   def get_object_by_class(self, input_id):
      #self.found_object = self.driver.find_element_by_class_name(input_id)
      self.found_object = self.driver.find_element(By.CLASS_NAME,input_id )
      return self.found_object

   def get_object_by_css_selector(self, input_id):
      self.found_object = self.driver.find_element(By.CSS_SELECTOR, input_id)
      return self.found_object


   def read_text(self):
      result = []
      for a_object in self.found_object:
         result.append(a_object.text)

   def type_action(self, input_text):
      if input_text == "enter":
         changed_action = Keys.RETURN
      self.found_object.send_keys(changed_action)

   def search_nth_button(self, input_no):
      #번째의 버튼에 대한 객체를 갖고오는 것
      pass

   def read_all_text_in_web_site(self):
      print(self.driver.find_element(By.XPATH, "/html/body").text)

   def read_all_source(self):
      print(self.driver.page_source)

   def search_nth_input_box(self, input_no):
      #번째의 입력박스에 대한 객체를 갖고오는 것
      self.found_object = self.driver.find_elements(By.CSS_SELECTOR, "input")
      print(len(self.found_object))
      self.selected_object = self.found_object[input_no]
      return self.selected_object


