## `python` 내장함수

### 1. range

- 특정 범위의 숫자들을 생성할 때 사용하는 함수

```python
numbers = range(a,b) # a부터 b-1까지의 숫자들을 numbers에 저장한다.
num = range(c) # 0부터 c-1까지의 숫자들을 num에 저장한다.
# 바로 출력하면, range형태로 출력되므로
# list형태로 형변환해서 출력해야 한다.
# ex) print(list(range))
# 데이터를 다루는 것도 range형태에서는 불가능하므로 list와 같은 형태로 바꿔 사용해야 한다.
```



### 2. dir

- 특정 모듈에 저장된 함수들을 모두 출력하는 함수

```python
print(dir(random)) # random 모듈이 사용할 수 있는 모든 함수를 출력한다.
```



### 3. input

- 입력 값을 받는 함수

```python
str = input('input String: ') # str이라는 변수에 입력을 받는다.
```



### 4. type

- 변수의 형태를 반환해주는 함수

```python
a = 'ABC'
b = 123
c = 4.56
print(a, b, c)
print(type(a), type(b), type(c)) # <class 'str'> <class 'int'> <class 'float'>

d = True
e = False
print(d, e)
print(type(d), type(e)) # <class 'bool'> <class 'bool'>
```





