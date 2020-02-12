# Introduction

PDF tools by PyPDF2.  

# Details

Visit my blog for details:  
https://blog.valderfield.com/archives/19/  

## PDF Merger Usage:  

### Edit some values before run `pdfmerger.py` in `__init__` method:  
在运行程序之前，先设定一些`__init__`方法中重要的变量:  
`self.DIR_PATH = ` your directory where PDF files exist (DON'T end with "/")（放PDF文件的目录地址。最后不要加斜杠！）  

Fill the list of regular expressions:  
填正则表达式列表（这些表达式会被依次执行，每次执行的结果作为下一次的输入）：  
`RE_LIST = [`
`    `
`]`  
You can fill `\d+` in `[` and `]` if you are lucky.  
如果你的文件名中从头开始的第一个数字（连续数字如123视为一个数字）便是你想要的序号，那么你只需要在中括号里填入一项`\d+`即可。  

The start index that can be matched of the PDF：  
需要合并的PDF文件的文件名中起始的序号：  
`self.START_INDEX = 1`


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