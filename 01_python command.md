## Python 명령어

### 1. `pip`

- pip는 python의 패키지 관리시스템

- `list` : 현재 python이 가지고 있는 모듈의 list를 보여주는 명령어

  ```bash
  $ pip list
  ```

- `freeze` : 기본 모듈을 제외한 현재 설치된 모듈과 버전을 출력하는 명령어

  ```bash
  $ pip freeze
  $ pip freeze > requirements.txt # 현재 나의 가상환경에 설치된 모듈을 다른 환경의 PC에서도 설치할 수 있도록 requirements.txt에 저장한다.
  ```

- `install` : 필요한 모듈을 다운로드 하는 명령어

  ```bash
  $ pip install [모듈명]
  $ pip install -r requirements.txt # 다른 PC의 가상환경에 설치된 모듈목록인 requirements.txt을 현재 나의 디렉토리에 설치하는 것
  # -r 은 대략 recursive라는 의미
  ```

  

### 2. `venv`

- venv는 해당 디렉토리 내에서만 사용할 가상환경을 만드는 python 모듈이다.

  ```bash
  $ python -m venv [생성할 가상환경 디렉토리 명]
  # venv라는 모듈을 실행하여 디렉토리에 새로운 가상환경을 구성한다.
  # -m 은 module을 실행한다는 의미의 option
  ```

- 가상환경으로 구동

  ```bash
  $ source venv/Scripts/activate # venv라는 디렉토리에 저장된 가상환경을 작동시키겠다.
  ```

- 가상환경에서 빠져나오는 명령어

  ```bash
  $ deactivate
  ```

- 가상환경을 삭제

  ```bash
  $ rm -rf [가상환경 디렉토리 명]
  $ rm -rf venv
  ```

  

