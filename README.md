# Melon-Macro
Selenium을 이용한 멜론 스트리밍 서비스 친밀도 상승용 공유 및 조회 매크로

## 환경
* Windows 10
* Python 3.8.x

## 필요한 것들
* Python 3.8.x
* Selenium

## 사용법
* Twitter 로 공유를 원할시 tweet_template.py 이용
* 멜론 내 친구(자신의 다른 계정) 으로 공유를 원할시 friend_template.py 이용

## 주의사항
* Twitter로 사용시 스팸으로 계정이 비활성화를 대비하여 일정시간 Delay를 주는 것이 좋음
* 타기기로 스트리밍중 매크로 사용 시, 동영상 조회 과정에 오류가 발생할 수 있음

## Extra
* Headless 사용시 더 편함 (아래 코드를 삽입)

```
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('C:/Python/chromedriver.exe', chrome_options = options)
```
## 궁금한 것들
* Issues 탭에 남겨주길 바람

## 스크린샷
![initial](https://user-images.githubusercontent.com/11593330/80552350-57bfa800-8a01-11ea-980a-1ea00b44d349.jpg)

