Title:Introduction to Django
Category:Django
Date:2016-2-1 18:31
# Django 简介
------

## 1.  初识Django



>django一种由Python写成的web开发框架，它源自于在线新闻web站点，在2005年的时候以开源的形式。它在Web开发领域的有很多优势，比如自带方便好用的ORM，即时生成的admin interface，还有详细错误提示等。目前我们公司的极客理财师平台就是用Django框架搭建的。在本文中我将对Django最主要的URLconf和View,template system，models stytem,这三个系统进行简单的介绍， 并将Django和同样为Python web开放框架之一的Flask进行一个简单的比较。



## 2. URLconf和 View



>Django是一个MVC框架，即将一个Web应用划分成三个部分：Model（负责与数据库相关的业务），View（负责将数据格式化后呈现给用户），Control(负责接受用户的操作，根据操作来和数据库互动，并调用View展示数据)。而MCV中的Control部分鹤View部分就分别由django中的urls.py和views.py来完成。



比如我们此时需要做一个最简单的hello world的演示：



>首先我们要写一个view来实现对请求进行回应，在Django中视图是一个函数，该函数接受一个HttpRequest参数，并返回一个HttpResponse。我们可以在任何地方定义这个函数，但通常会放在Django app 的 views.py 文件中。



    from django.http import HttpResponse

    def hello(request):

        return  HttpRespond('Hello,World!')



>然后我们需要将URL映射到这个函数中，这是由URLconf完成的。它的作用是将URL模式和与这个URL对应的视图函数建立关系。具体操作就是打开urls.py文件，引入刚刚的视图函数,然后在urlpattern中加入hello的映射关系。



    from django.conf.urls.defaults import patterns, include, url

    from depot.views import hello



    urlpatterns = patterns('',

        url(r'^hello/$', hello),

    )



>在一开始接触的Django的URLconf时，很多人会像我一样觉得这种用正则表达式的方法很麻烦，但过一段时间当感受过较为复杂的业务逻辑后，肯定会和我一样感受到正则表达式的自由性。


>从本质上来说，URLconf就是一张views.py中函数和对应URL的映射表。当Django 接收到HTTP请求的时候，从urlpatterns中找到匹配的表达式，并将请求发生给对应的视图函数，最后视图函数返回一个HTTP响应，交给Django处理。That is all.

## 3. Model模块

>现代web动态网页的基本就是和数据库的互动,在数据库部分django使用Model来对数据库进行管理. 简单来说的,models.py中的每个类对应了数据库中的一张表,而每个类的一个属性对应了表中的一行,而Django提供了一个自动生成的数据库访问API也就是自带一个类似sqlalchemy的ORM.

For example如果我们现在需要在数据库中有一张表来记录用户的信息,目前我们网站是采用一个这样的model(部分截取):


    class Account(models.Model):
       user = models.OneToOneField(User,unique=True,verbose_name="对应验证账号",related_name="account")
       create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
       update_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)

     #网站用户信息
       nickname = models.CharField(verbose_name="用户名",max_length=50,unique=True)
      avatar = models.ImageField('头像',upload_to=attachment_upload,blank=True,null=True)
      avatar_thumb = models.ImageField('头像缩略',upload_to=attachment_upload,blank=True,null=True)

     #真实信息
      real_name = models.CharField(max_length=20,verbose_name="真实姓名",blank=True)
      id_number = models.CharField(max_length=18,verbose_name="身份证号",blank=True)
      real_name_confirmation_date = models.DateTimeField('实名认证时期', blank=True, null=True)

其中CharFiel对应的是数据库中的CHAR字段,DateTimeField对应的是DATE字段依次类推,这样就可以在Django中将每个字段数据的类型限制下来.这样还有一个更大的好处,如果说有一天我们更换别的类型的数据库,我们不需要更改model.py 的类, 我们只需要在settings.py 中更改的数据库接口就可以了.比如我们公司目前就是这样,在生产环境中我们使用的是sqllite,而在生产环境中我们使用的是mySQL.但是两者切换过程中我们不需要做什么事情,只需要写一个简单的判断逻辑来更改DATABASE设置就可以了.


## 4. Template System



>由于在Django中MVC中Control部分由Django框架通过按照 URLconf 设置，对给定 URL 调用合适的 python 函数来自行处理了，所以Django里面更关注的是Model,Template和View，所以Django也被称作MTV框架。

* M 代表模型（Model），即数据存取层。该层处理与数据相关的所有事务：如何存取、如何确认有效性、包含哪些行为以及数据之间的关系等。



* T 代表模板(Template)，即表现层。该层处理与表现相关的决定：如何在页面或其他类型文档中进行显示。



* V 代表视图（View），即业务逻辑层。该层包含存取模型及调取恰当模板的相关逻辑。你可以把它看作模型与模板之间的桥梁。

>Django的设计理念是模板系统应该只负责控制显示和显示相关的逻辑我们视模板为一种控制显示和显示相关逻辑的工具，仅此而已。模板系统的功能就止于此。
基于这个原因，Django模板无法直接调用Python代码。在Django模板里，所有的程序设计活动都止于对标签的使用。
虽然你可以自定义模板标签来做任意的事情，但Django自己的模板标签不允许执行Python代码。

## 5. Django 和flask的比较

>flask 也是Python写成的web开发框架，它诞生于2010年，要比django年轻，但是在Github上它和django有类似的star数。它也是我一开始学习web开发时候使用的框架。我个人感觉django和flask有三个方面是差距比较大，分别是开发速度，文件构成，学习路径。
# Django 简介
------

## 1.  初识Django



>django一种由Python写成的web开发框架，它源自于在线新闻web站点，在2005年的时候以开源的形式。它在Web开发领域的有很多优势，比如自带方便好用的ORM，即时生成的admin interface，还有详细错误提示等。目前我们公司的极客理财师平台就是用Django框架搭建的。在本文中我将对Django最主要的URLconf和View,template system，models stytem,这三个系统进行简单的介绍， 并将Django和同样为Python web开放框架之一的Flask进行一个简单的比较。



## 2. URLconf和 View



>Django是一个MVC框架，即将一个Web应用划分成三个部分：Model（负责与数据库相关的业务），View（负责将数据格式化后呈现给用户），Control(负责接受用户的操作，根据操作来和数据库互动，并调用View展示数据)。而MCV中的Control部分鹤View部分就分别由django中的urls.py和views.py来完成。



比如我们此时需要做一个最简单的hello world的演示：



>首先我们要写一个view来实现对请求进行回应，在Django中视图是一个函数，该函数接受一个HttpRequest参数，并返回一个HttpResponse。我们可以在任何地方定义这个函数，但通常会放在Django app 的 views.py 文件中。



    from django.http import HttpResponse

    def hello(request):

        return  HttpRespond('Hello,World!')



>然后我们需要将URL映射到这个函数中，这是由URLconf完成的。它的作用是将URL模式和与这个URL对应的视图函数建立关系。具体操作就是打开urls.py文件，引入刚刚的视图函数,然后在urlpattern中加入hello的映射关系。



    from django.conf.urls.defaults import patterns, include, url

    from depot.views import hello



    urlpatterns = patterns('',

        url(r'^hello/$', hello),

    )



>在一开始接触的Django的URLconf时，很多人会像我一样觉得这种用正则表达式的方法很麻烦，但过一段时间当感受过较为复杂的业务逻辑后，肯定会和我一样感受到正则表达式的自由性。


>从本质上来说，URLconf就是一张views.py中函数和对应URL的映射表。当Django 接收到HTTP请求的时候，从urlpatterns中找到匹配的表达式，并将请求发生给对应的视图函数，最后视图函数返回一个HTTP响应，交给Django处理。That is all.

## 3. Model模块

>现代web动态网页的基本就是和数据库的互动,在数据库部分django使用Model来对数据库进行管理. 简单来说的,models.py中的每个类对应了数据库中的一张表,而每个类的一个属性对应了表中的一行,而Django提供了一个自动生成的数据库访问API也就是自带一个类似sqlalchemy的ORM.

For example如果我们现在需要在数据库中有一张表来记录用户的信息,目前我们网站是采用一个这样的model(部分截取):


    class Account(models.Model):
       user = models.OneToOneField(User,unique=True,verbose_name="对应验证账号",related_name="account")
       create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
       update_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)

     #网站用户信息
       nickname = models.CharField(verbose_name="用户名",max_length=50,unique=True)
      avatar = models.ImageField('头像',upload_to=attachment_upload,blank=True,null=True)
      avatar_thumb = models.ImageField('头像缩略',upload_to=attachment_upload,blank=True,null=True)

     #真实信息
      real_name = models.CharField(max_length=20,verbose_name="真实姓名",blank=True)
      id_number = models.CharField(max_length=18,verbose_name="身份证号",blank=True)
      real_name_confirmation_date = models.DateTimeField('实名认证时期', blank=True, null=True)

其中CharFiel对应的是数据库中的CHAR字段,DateTimeField对应的是DATE字段依次类推,这样就可以在Django中将每个字段数据的类型限制下来.这样还有一个更大的好处,如果说有一天我们更换别的类型的数据库,我们不需要更改model.py 的类, 我们只需要在settings.py 中更改的数据库接口就可以了.比如我们公司目前就是这样,在生产环境中我们使用的是sqllite,而在生产环境中我们使用的是mySQL.但是两者切换过程中我们不需要做什么事情,只需要写一个简单的判断逻辑来更改DATABASE设置就可以了.


## 4. Template System



>由于在Django中MVC中Control部分由Django框架通过按照 URLconf 设置，对给定 URL 调用合适的 python 函数来自行处理了，所以Django里面更关注的是Model,Template和View，所以Django也被称作MTV框架。

* M 代表模型（Model），即数据存取层。该层处理与数据相关的所有事务：如何存取、如何确认有效性、包含哪些行为以及数据之间的关系等。



* T 代表模板(Template)，即表现层。该层处理与表现相关的决定：如何在页面或其他类型文档中进行显示。



* V 代表视图（View），即业务逻辑层。该层包含存取模型及调取恰当模板的相关逻辑。你可以把它看作模型与模板之间的桥梁。

>Django的设计理念是模板系统应该只负责控制显示和显示相关的逻辑我们视模板为一种控制显示和显示相关逻辑的工具，仅此而已。模板系统的功能就止于此。
基于这个原因，Django模板无法直接调用Python代码。在Django模板里，所有的程序设计活动都止于对标签的使用。
虽然你可以自定义模板标签来做任意的事情，但Django自己的模板标签不允许执行Python代码。

## 5. Django 和flask的比较

>flask 也是Python写成的web开发框架，它诞生于2010年，要比django年轻，但是在Github上它和django有类似的star数。它也是我一开始学习web开发时候使用的框架。我个人感觉django和flask有三个方面是差距比较大，分别是开发速度，文件构成，学习路径。

* 开发速度:从开发速度上来说，django有强大的django——admin命令行工具，在它的帮助下可以快速地生成project，app并对数据库进行同步甚至是让它在本地跑起来，而且这个命令行工具可以进行自定义扩展，通过django自带的command库你可以对其进行任意的扩展，这让执行一些脚本也变得更加方便。另外由于django自带admin interface可以直接在页面上对数据库进行操作，所以django在前期和中期开发过程中要比flask快很多。

* 文件构成:django是将整个peoject分成若干个app 在每个app中有自己独立的urlconf，models和views文件，而所有的templates则是像上文所述放在顶级文件夹中，通过多级分层进行分类。而flask则是将url和view逻辑写在一起通过python装饰器，将url和对应的view函数映射起来。通过文件的构成我们可以感受到，两者之间的设计哲学的差异。django是做到在高度分化之后的高度整合，这样可以在保持可扩展性的前提下尽量一站式解决问题。而flask则是强调miroframework，支持和鼓励高度的自定义。比如要用flask完成一个上文的helloworld演示，只需要在一个文件中写短短的7行代码就可以解决需求。

	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
	    return "Hello World!"

	if __name__ == "__main__":
	    app.run()


在这也从侧面体现出了falsk比较适合小型网站的开发，django更适合大中型网站的开发。

* 学习路径:由于Flask鼓励高度定制,所以学习Flask的过程更像是在学习不同组件的过程,比如一开始学习数据库,在教程中会先用cursor写原生的SQL语言写起, 然后才会介绍给你如sqlalchemy这样的ORM,又比如在学习表单时,则要学习名称很容易让人产生误会WTForms模块.而在学习Django的过程中,这些都不是问题,因为Django自带ORM也有关于表单库.所以学习Django的过程, 更多的是学习Django所提供的每个库的使用.如果要做一个简单的评价的话,我觉得在学习Flask的过程可以更多地去了解到开发过程的中每个细节的问题,而学习Django的过程则能更快地完成一个项目,获得更多的成就感,让自己更有信心的学习下去.
* 开发速度:从开发速度上来说，django有强大的django——admin命令行工具，在它的帮助下可以快速地生成project，app并对数据库进行同步甚至是让它在本地跑起来，而且这个命令行工具可以进行自定义扩展，通过django自带的command库你可以对其进行任意的扩展，这让执行一些脚本也变得更加方便。另外由于django自带admin interface可以直接在页面上对数据库进行操作，所以django在前期和中期开发过程中要比flask快很多。

* 文件构成:django是将整个peoject分成若干个app 在每个app中有自己独立的urlconf，models和views文件，而所有的templates则是像上文所述放在顶级文件夹中，通过多级分层进行分类。而flask则是将url和view逻辑写在一起通过python装饰器，将url和对应的view函数映射起来。通过文件的构成我们可以感受到，两者之间的设计哲学的差异。django是做到在高度分化之后的高度整合，这样可以在保持可扩展性的前提下尽量一站式解决问题。而flask则是强调miroframework，支持和鼓励高度的自定义。比如要用flask完成一个上文的helloworld演示，只需要在一个文件中写短短的7行代码就可以解决需求。

	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
	    return "Hello World!"

	if __name__ == "__main__":
	    app.run()


在这也从侧面体现出了falsk比较适合小型网站的开发，django更适合大中型网站的开发。

* 学习路径:由于Flask鼓励高度定制,所以学习Flask的过程更像是在学习不同组件的过程,比如一开始学习数据库,在教程中会先用cursor写原生的SQL语言写起, 然后才会介绍给你如sqlalchemy这样的ORM,又比如在学习表单时,则要学习名称很容易让人产生误会WTForms模块.而在学习Django的过程中,这些都不是问题,因为Django自带ORM也有关于表单库.所以学习Django的过程, 更多的是学习Django所提供的每个库的使用.如果要做一个简单的评价的话,我觉得在学习Flask的过程可以更多地去了解到开发过程的中每个细节的问题,而学习Django的过程则能更快地完成一个项目,获得更多的成就感,让自己更有信心的学习下去.
