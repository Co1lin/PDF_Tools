# Introduction

PDF tools by PyPDF2.  
So far only `merger.py` is availiable.  
现在只有合并多个PDF的程序`merger.py`。  

# Details

Visit my blog for details:  
[利用PyPDF批量处理PDF文件——合并篇](https://blog.valderfield.com/archives/19/)  

## New PDF Merger Usage(`merger.py`)

用之前改程序中的一些变量：

```python
# 本程序依赖于我自己编写的IndexMap模块运行。
# 详情见 https://github.com/Co1lin/Practical-Python-Scripts/tree/master/IndexMap
# 请确保IndexMap.py与这个程序在同一层目录下。
files = IndexMap()	# 创建IndexMap实例

# 设定PDF文件所在目录
files.set_dir('/path/to/dir_of_PDF_files')

# 正则匹配表达式列表（下面的配置从左起匹配第一个数字（连续数字如123视为一个数字123）作为序号）
RE_LIST = [
    '\d+'
]
files.set_patterns(RE_LIST)	# 将正则表达式应用于IndexMap实例
files.construct_map()	# IndexMap实例构建映射

merger = PdfMerger(files, 'output.pdf')	# 'output.pdf'字符串指定了输出PDF的文件名
```



## Old PDF Merger Usage(`pdfmerger.py`):  

### Edit some values before run `pdfmerger.py` in `__init__` method:  

在运行程序之前，先设定一些`__init__`方法中重要的变量:  
`self.DIR_PATH = ` your directory where PDF files exist (DON'T end with "/")（放PDF文件的目录地址。最后不要加斜杠！）  

Fill the list of regular expressions:  
填正则表达式列表（这些表达式会被依次执行，每次执行的结果作为下一次的输入）：  
```
RE_LIST = [
    
]
```
You can fill `\d+` between `[` and `]` if you are lucky.  
如果你的文件名中从头开始的第一个数字（连续数字如123视为一个数字）便是你想要的序号，那么你只需要在中括号里填入一项`\d+`即可。  

The start index that can be matched of the PDF：  
需要合并的PDF文件的文件名中可以提取出来的起始的序号（比如你是`xxx-002.pdf`是第一个文件那就填2）：  
`self.START_INDEX = 1	# 1 by default`  

A value greater than the number of PDFs:  
一个大于需要合并的PDF文件总数的数值：  
`self.INF_VALUE = 100000  # usually don't need to change unless you have toooo many PDFs`

You can change the codes in `__get_index` method for other(more complex) regular expression matching.  
如果你想实现更复杂的正则匹配功能，你可以修改`__get_index`方法中的代码。  

### Set the output file name and working type:
设置输出文件名称和工作模式：  
`merger.work('output.pdf', work_type = 3)`  

The output file is `output.pdf` in the directory you set before(where your original PDF files exist).  
此时输出文件为`output.pdf`，放在原来存放PDF的文件夹里。  

You can keep the `work_type` value.  
你可以不改变`work_type`的现有值。  
