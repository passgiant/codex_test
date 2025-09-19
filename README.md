# 파이썬 계산기 웹앱

Flask와 Decimal 모듈을 사용하여 정밀한 사칙연산을 지원하는 간단한 계산기 웹 애플리케이션입니다.

## 주요 기능

- 두 개의 숫자에 대해 덧셈, 뺄셈, 곱셈, 나눗셈을 수행
- 잘못된 입력 또는 0으로 나누기 시 친절한 오류 메시지 제공
- 반응형 디자인을 적용해 데스크톱과 모바일에서 모두 사용 가능

## 실행 방법

1. 가상 환경을 생성하고 활성화합니다.

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows의 경우 .venv\\Scripts\\activate
   ```

2. 필요한 의존성을 설치합니다.

   ```bash
   pip install -r requirements.txt
   ```

3. 개발 서버를 실행합니다.

   ```bash
   flask --app app run --debug
   ```

4. 브라우저에서 [http://localhost:5000](http://localhost:5000)을 열어 계산기를 사용합니다.

## 테스트

애플리케이션이 정상적으로 로드되는지 확인하려면 Python 바이트코드 컴파일 검사를 실행할 수 있습니다.

```bash
python -m compileall .
```
