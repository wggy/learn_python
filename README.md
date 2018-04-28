# Python日记

## 一、变量变量的命令和使用（2018-04-26）
- 变量名只能包含字母、 数字和下划线。 变量名可以字母或下划线打头， 但不能以数字打头， 例如， 可将变量命名为message_1， 但不能将其命名为1_message。
- 变量名不能包含空格， 但可使用下划线来分隔其中的单词。 例如， 变量名greeting_message可行， 但变量名greeting message会引发错误。
- 不要将Python关键字和函数名用作变量名， 即不要使用Python保留用于特殊用途的单词， 如print （请参见附录A.4） 。
- 变量名应既简短又具有描述性。 例如， name比n好， student_name比s_n好， name_length比length_of_persons_name好。
- 慎用小写字母l和大写字母O， 因为它们可能被人错看成数字1和0。
---
## 二、字符串
- 字符串 就是一系列字符。 在Python中， 用引号括起的都是字符串， 其中的引号可以是单引号， 也可以是双引号。
---
## 三、数字
- 3.1 在Python中， 可对整数执行加（\+） 减（\-） 乘（\*） 除（\/ ） 运算。
- 3.2 Python将带小数点的数字都称为浮点数 。 大多数编程语言都使用了这个术语， 它指出了这样一个事实： 小数点可出现在数字的任何位置。 每种编程语言都须细心设计， 以妥善地处理浮点数， 确保不管小数点出现在什么位置， 数字的行为都是正常的。
---
- 3.3 使用函数str() 避免类型错误
如：
```
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
```
代码报错：
```
Traceback (most recent call last):
File "birthday.py", line 2, in <module>
message = "Happy " + age + "rd Birthday!"
❶ TypeError: Can't convert 'int' object to str implicitly
```
这是一个类型错误 ， 意味着Python无法识别你使用的信息。 在这个示例中， Python发现你使用了一个值为整数（int ） 的变量， 但它不知道该如何解读这个值（见❶） 。 Python知道， 这个变量表示的可能是数值23， 也可能是字符2和3。 像上面这样在字符串中使用整数时， 需要显式地指出你希望Python将这个整数用作字符串。 为此， 可调用函数str() ，它让Python将非字符串值表示为字符串：
```
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```
---
- 3.4 Python2的整数
在Python 2中， 将两个整数相除得到的结果稍有不同
```
>>> python2.7
>>> 3 / 2
1
```
Python返回的结果为1， 而不是1.5。 在Python 2中， 整数除法的结果只包含整数部分， 小数部分被删除。 请注意， 计算整数结果时， 采取的方式不是四舍五入， 而是将小数部分直接删除。

---
## 四、Python之禅
```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
---
## 五、列表
**5.1 列表特征**
- 在Python中， 用方括号（[]） 来表示列表， 并用逗号来分隔其中的元素。
- 列表是有序集合， 因此要访问列表的任何元素， 只需将该元素的位置或索引告诉Python即可。 要访问列表元素， 可指出列表的名称， 再指出元素的索引， 并将其放在方括号内。
- 索引从0而不是1开始。
- Python为访问最后一个列表元素提供了一种特殊语法。 通过将索引指定为-1 ， 可让Python返回最后一个列表元素。
- 在列表中添加新元素时， 最简单的方式是将元素附加到列表末尾，使用append()方法。
- 在列表中插入元素，使用insert()方法。
- 如果知道要删除的元素在列表中的位置， 可使用del 语句。
- 使用方法pop() 删除元素。删除末尾元素，并返回该元素。
- 以使用pop() 来删除列表中任何位置的元素， 只需在括号中指定要删除的元素的索引即可。
- 如果你不确定该使用del 语句还是pop() 方法， 下面是一个简单的判断标准： 如果你要从列表中删除一个元素， 且不再以任何方式使用它， 就使用del 语句； 如果你要在删除元素后还能继续使用它， 就使用方法pop() 。
- 根据值删除元素，使用remove()方法，传入取值。方法remove() 只删除第一个指定的值。 如果要删除的值可能在列表中出现多次， 就需要使用循环来判断是否删除了所有这样的值。
---
**5.2组织列表**
- Python方法sort() 让你能够较为轻松地对列表进行排序。
- 还可以按与字母顺序相反的顺序排列列表元素， 为此， 只需向sort() 方法传递参数reverse=True 。
- 要保留列表元素原来的排列顺序， 同时以特定的顺序呈现它们， 可使用函数sorted() 。 
- 要反转列表元素的排列顺序， 可使用方法reverse() 。
- 使用函数len() 可快速获悉列表的长度。
---
**5.3遍历整个列表**
- 每个缩进的代码行都是循环的一部分， 且针对列表中的每个值都执行一次。
``
magicians = ['alice', 'david', 'carolina']
for ma in magicians:
&ensp;&ensp;&ensp;&ensp;print(ma.title() + ", that was a great trick!");
&ensp;&ensp;&ensp;&ensp;print("I can't wait to see your next trick, " + ma.title() + ".\n")
print("Thank you, everyone. That was a great magic show!");

``
- 使用函数list(range(1, 5))创建数字数组，包头不包尾。
---
**5.4列表解析**
- 使用一行代码精简数组创建、遍历、赋值等。
``
print([value ** 2 for value in range(1,11)]);
``
---
**5.5列表的部分元素-切片**
- 切片即截取数组，原则是切头不切尾。

``
players = ['charles', 'martina', 'michael', 'florence', 'eli'];
print(players[0:3]);

``

- 复制列表，利用切片复制，可创建一个包含整个列表的切片， 方法是同时省略起始索引和终止索引（[:] ） 。 这让Python创建一个始于第一个元素， 终止于最后一个元素的切片， 即复制整个列表。
---
**5.6原组**
- Python将不能修改的值称为不可变的 ， 而不可变的列表被称为元组 。
- 元组看起来犹如列表， 但使用圆括号而不是方括号来标识。 定义元组后， 就可以使用索引来访问其元素， 就像访问列表元素一样。
---
## 六、Py格式设置
- 缩进——PEP 8建议每级缩进都使用四个空格， 这既可提高可读性， 又留下了足够的多级缩进空间。
- 行长——很多Python程序员都建议每行不超过80字符。
- 空行——要将程序的不同部分分开， 可使用空行。
- 本章的每个示例都展示了良好的格式设置习惯。 在条件测试的格式设置方面， PEP 8提供的唯一建议是， 在诸如== 、 >= 和<= 等比较运算符两边各添加一个空格， 例如， if age < 4: 要比if age<4: 好。
---
##if语句
- **要判断两个值是否不等， 可结合使用惊叹号和等号（!= ） ， 其中的惊叹号表示不 ， 在很多编程语言中都如此。   **
- **你可能想同时检查多个条件， 例如， 有时候你需要在两个条件都为True 时才执行相应的操作， 而有时候你只要求一个条件为True 时就执行相应的操作。 在这些情况下， 关键字and 和or 可助你一臂之力。**
- **要判断特定的值是否已包含在列表中， 可使用关键字in 。 **
- **确定特定的值未包含在列表中很重要； 在这种情况下， 可使用关键字not in 。 **经常需要检查超过两个的情形， 为此可使用Python提供的if-elif-else 结构。**
- **确定列表不是空的。**


