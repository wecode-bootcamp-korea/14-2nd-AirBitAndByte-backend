##

---

# Air Bit n Byte | 에어비트앤바이트

<img src='public/airBnb.png' alt='logo'>

<br><br>

---

## airbnb | 에어비앤비

- [에어비앤비](https://www.airbnb.co.kr/) 사이트
- 소개: 글로벌 1위 숙박 공유 사이트

## 팀원

- Front-end: 고은정, 장재원
- Back-end: 김기용(PM), 이성보, 이영주

## 개발 기간

- 기간: 2020.11.30 ~ 2020.12.11 (12일)

## 적용 기술

- Front-end: React.js(Hooks), Redux, React-router, Styled-components, Firebase
- Back-end: Django, Python, MySQL, jwt, bcrypt
- 협업툴: Trello, Slack, Github(Rebase)



## 영상

[에어비트앤바이트 영상](http://www.youtube.com)

## 구현 기능 및 개인 역할

`고은정`

- 숙소 상세페이지
  - React-slick 활용한 image slider 구현
  - React-dates 기반 숙소 예약 탭 기능 구현
  - 숙소 bookmark 기능
  - Kakao map API 활용, 숙소 위치 로딩 및 마커 설정 기능
- 회원가입 및 로그인
  - Firebase 기반 Google social login 기능 구현
  - Redux로 user 로그인 상태 글로벌 관리

`장재원`

-

`김기용`, `이성보`, `이영주` 

- Oauth2 인증방식을 통한 Google Social login 구현 
- queryString으로 동시에 여로 조건을 받아  field_lookup 을 통한 숙소검색 구현
- check_availability 함수를 구현, 날짜별 숙소 예약 여부를 확인하고 숙소예약 생성 및 예약가능 일 조회
- JWT -  Json Web token 을 사용해 로그인시 access token을 발행 하고 서버에서 access token을 복호화해 권한을 확인
- BCRYPT - 회원가입시 단방향 암호화 해싱함수를 사용해 암호화된  비밀번호를 데이터베이스에 저장
- Pagination - offset, limit 을 이용


## EndPoint

[get] PropertyListView       :      /property' <br>

[get]  PropertyListView       :    /propert/\<int:property_id\> <br>

[get] ReservationListView      :    /reservation <br>

[post] ReservationListView      :   /reservation <br>

[patch] PaymentView              :  /reservation/\<int:reservation_id\> <br>

[post] SocialLoginView            : /socialLogin

[post] RegisterView                : /register

[post] LoginView                   : /login

[post] bookmarkView                : /bookmark

[delete] bookmarkView              : /bookmark



## Modeling

<img src='public/abb_model.png' alt='logo'>

## 소감 및 후기

- 고은정: ([후기](https://업로드후수정.com)-개인 벨로그)

- 장재원:
- 김기용: 작성중
- 이성보: 작성중
- 이영주: 작성중





## 레퍼런스

- 이 프로젝트는 [에어비앤비](https://www.airbnb.co.kr/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
