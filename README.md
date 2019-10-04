# Clean-academic-paper
Some ideas concerning establishing an academic corpus


## Head

```
<journal>Cell Research</journal>
<year>2015</year>
<month>June</month>
<page>655-673</page>
<title>Combination of inflammation-related cytokines promotes long-term muscle stem cell expansion</title>
<author>Xin Fu, Jun Xiao, Ping Hu</author>
```

## Regex 配合emeditor可以进行多个文档的替换

```
 \[[1-9]] #匹配[1]
 \[[1-9][0-9]] #匹配[12]
 \[[1-9], [1-9]] #匹配[2, 3]
 \[[1-9]-[1-9]] #匹配[2-3]
 \[[1-9], [1-9][0-9]] #匹配[3, 14]
 \[[1-9][0-9], [1-9][0-9]] #匹配[13, 14]
 \[[1-9][0-9]-[1-9][0-9]] #匹配[13-14]
 \[[1-9][0-9], [1-9][0-9], [1-9][0-9]] #匹配[13, 14, 15]
```

## 语言数据的不同类型-table cr Xiong, 2015

类型 | 第一人称数据 | 第二人称数据 | 第三人称数据
------------ | ------------- | --------------|-----------
数据处理方法 | 内省 | 诱导 | 观察
