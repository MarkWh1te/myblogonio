Title: REST介绍
Modified: 2016-02-01 19:30
Category: Web
Tags: pelican, publishing
Slug: introduction-to-REST
Authors: Mark
Summary: Introduction to REST

REST 介绍
====================
### REST的起源
REST是目前最为流行的一种互联网软件架构风格,它最早出现在2000年Roy Fielding 提出的一篇博士论文 (Architectural Styles andthe Design of Network-based Software Architectures)中 ,Roy Fielding是HTTP协议的主要作者之一, 也是大名鼎鼎的Apache基金会的第一届主席。在这篇论文中，他首先阐述了架构风格的定义，即一种抽象，高级的模式，来表达架构方法背后的核心理念，每一个架构风格由一系列的约束定义形成。然后他在符合这个架构原理的前提下，理解和评估了以网络为基础的应用软件的架构设计，得到了一种功能强，性能好，适宜通信的架构————REST。

### 理解REST
刚刚了解到REST的人，会将REST和RESTful理解为同一种东西。其实它们的关系就像Beauty和Beautifull一样，符合REST规则的WebService就是RESTfull的。而REST本身则是由很多约束构成一种抽象化的风格，很多人会将REST和HTTP绑在一起，因为HTTP目前是REST最好实现。但是我们的必须知道REST不仅仅会有这一种实现方式。而在Dr.Roy Fielding 论文之中，他也没有详细叙述REST的实现，也是为了让我们把重点放在REST的设计架构本质中。我会用HTTP举例，以便让大家更快更方便的理解REST。但是请大家注意REST不是标准或者规则,是由多个相互协调的限制而形成的架构风格.所以它不是一种具体的技术,在其他的信息交换系统中依然可以实现这样的概念。


REST 的全称是 Representational state transfer 中文直译过来的就是表现层状态转移.


这个名称省去了representational的主语resource, 全称 应该是 Rescource Representational State Transfer*即 资源在表现层的状态转移,分开解释的话:

1. _**Resource**_指的是资源, 资源可以是数据如图片文本或者是声音,可以是一种服务,甚至是一组资源的集合,而每种资源对应了一个特定的url, 通过url就可以定位资源.
 _**Representational**_指的是资源的表现形式,比如一张图片可以用PNG格式表现,也可以用JPG格式表示;
 * _**State Transfer**_指的是资源状态的转变,即为服务器端和客户端的互动,而客户端操作只能通过HTTP的协议来进行.而HTTP协议中四个verb:POST,GET,PUT,DELETE刚好对应了CRUD.

 _*for example*_:

 GET /products 查看所有产品信息

 GET /products /12 - 查看12号产品信息

 POST /products - 新建某个产品信息

 PUT /products /12 - 更新12号产品信息

 DELETE /products /12 - 删除12号

 而状态的转变是发生在表现层的,所以REST全称是"表现层状态转化"。而REST的本质就是**通过http提供的verb对URL定位的资源进行状态转化.**.接下来我讲详细解释,REST是通过哪些限制来做到这件事情的.
 ### REST的限制

 1. 客户-服务器(Client-Server)

 	即客户端和服务器分离,这样做的优点是提高了用户界面便携性,也使得客户端和服务器可以分别进行优化.

2. 无状态(Stateless)
	
	即从客户端的每个请求中包含服务器需要的所有信息,这样不但提升了可靠性,也让服务器可以单独考虑每个请求.

3. 缓存(Cache)
	
	就是服务器返回的信息都要标记是否可以进行缓存,如果可以缓存,则客户端可以使用之前的信息发送请求.这样做可以极大地降低交互的延迟.

4. 分层系统(Layered System)

就是让系统组件无法进行跨过层交流,把服务封装起来.这样在限制系统复杂性的同时提升可扩展性.

5. 统一接口(Uniform Interface)
	
	这个限制是为了鼓励单独改善组件,并让交互可见性提升.

6. 支持按需代码(Code-On-Demand)
	
	就是让客户端可以下载和执行代码(JavaScript),这提高系统可扩展性,但是也减少了系统的可见度,所以这是一个可选限制.

如果用一张图来表现REST限制条件的话,就像下面这样:
![](http://7xq2dq.com1.z0.glb.clouddn.com/rest_derivation.gif)	

### 总结

这篇文章里面，我从REST的起源说起，从REST的名称和约束两个角度对REST进行了介绍。由于我接触REST的时间不是很久，所以肯定还有认识不到位的地方，希望以后有机会能对REST有更进一步的体验和认知。

### Reference

1. [Architectural Styles and the Design of Network-based Software Architectures](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
2. [wikipedia Representational_state_transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)
3. [知乎 REST架构该如何生动的理解](https://www.zhihu.com/question/27785028)
