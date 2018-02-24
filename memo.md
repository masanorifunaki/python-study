# pythonメモ
## 6.1.1.3
### raw文字列
生の文字列を意味し、文字列の中のエスケープ文字を無視する。
バックスラッシュをバックスラッシュとして扱う。
```python
print(r'That is Carol\'s cat.')
```

## 6.1.2
### 文字列の取得
```python
hello = 'Hello'
# 文字列の位置の0~4までを取得できる。
hello[0:5]
```

## 6.2.4
### join()
文字列に対して呼び出し、リストを渡す。
文字列を連結させたいときに使う。
```python

','.join(['cats', 'rats', 'bats'])
# 'cats,rats,bats'
```