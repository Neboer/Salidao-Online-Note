# Salidao-Online-Note
To build a small pastebin service <br>
Paste bin方案：
1.	网页有一个框，用来存代码。输入代码之后，再输入一个identity值。
2.	网页存储identity和代码，并且返回包含查询值id的URL“/search/<id>”。
3.	访问“/search/<id>”时，网页会返回paste的结果。如果在页面下的输入框中输入“identity”并校验正确，网页会返回一个文本框包括的内容，可以提交修改，也可以删除。
