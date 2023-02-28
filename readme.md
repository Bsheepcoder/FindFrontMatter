# 识别markdown中的front-matter

- 在hexo配置中，要求md文件中有类似如下的信息：

  ```markdown
  ---
  title: XXXXX
  date: 1990-12-12
  tags: XXX
  categories: XXX
  description: XXXXXXXXXX
  ---
  ```
  
为了能够识别，方便做markdown文件的管理，该包用来识别其中的信息返回为一个字典。

## 使用说明

```py
import findfm

with open('XX.md', 'r', encoding='utf-8') as file:
    data = file.read()
    dict = findfm.find(data)  # <----- 调用find即可
    print(dict) 
```

