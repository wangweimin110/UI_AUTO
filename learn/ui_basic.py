
# web页面组成
'''
常用：HTML+CSS+JavaScript
HTML:
    定义页面呈现的内容
    HTML标记标签通常被称为HTML标签（HTML tag）
    HTML标签是由尖括号包围的关键词，比如<html>
    HTML标签通常是成对出现的，比如<b>和</b>
    标签对中的第一个是开始标签第二个是结束标签
    开始标签和结束标签也叫开放标签和闭合标签
CSS:
    Cascading Style Sheets
    页面布局（字体颜色，字体大小）
JavaScript:
    使网页依据不同的情形做不同的事情
'''

# web页面元素
'''
id--唯一的，有可能是变化的
style（样式设置）--visibility:visible(代表可见)   display：block（块） display：none（不可见）
'''

# DOM对象
'''
DOM(Document Object Mode)文档对象模型  是一套web标准
定义了访问HTML文档的一套属性、方法和事件（对HTML页面增删改查）
本质：
    网页与脚本语言沟通的桥梁
    脚本语言通过DOM对象来访问HTML页面，从而改变文档的结构、样式和内容
    当浏览器载入HTML文档，它就会成为document对象
HTML DOM独立于平台和编程语言
它可以被任何语言使用（Java python JavaScript VBScript）
JavaScript-简单语法
    <script></script>
    变量表达：
        var 变量名 = 值
        列表 var li = [1,3,2] alert(li[1])
        字典 var dic = {'name':'wwm'} 
    函数：
        function 函数名(参数){
            return 值；
        }
        调用：函数名(参数)
查找元素：
    document.getElementById('')
    document.getElementsByClassName("")
        0: input#j_password.pass-text-input.pass-text-input-password
         length: 1   (0代表查到的第一个元素，1代表一共查找到几个元素)
    document.getElementsByTagName("")
    document.getElementsByName("")
    document.querySelector(css)
元素的属性：
    改变属性：
        document.getElementBy***('').setAttribute(属性名,属性值)
        document.getElementBy***('').属性名=属性值
    获取属性：
        document.getElementBy***('').getAttribute(属性名)
    改变元素的内容：
        包含HTML元素标签 -- 有后代
        document.getElementBy***('').innerHTML = new HTML
        不包含HTML标签  纯文字
        document.getElementBy***('').innerText = new text
样式：
    改变样式
        document.getElementBy***('').style.样式名 = 样式值
        例：
        元素的可见性
        document.getElementBy***('').style.visibility = 'hidden'
        元素的颜色
        document.getElementBy***('').style.color = 'red'
事件：
    浏览器和用户事件-触发-执行js代码带来不同的页面响应
    例如：点击事件、输入事件、鼠标事件
    页面加载完成事件
        window.onload = function{
        alert('jajajajajjajaja')
        }
    点击事件
    document.getElementById('').onclick = function(){
        alert('点我点我点我')
    }
'''

# selenium原理
'''

'''

# selenium常用方法
'''
 #coding = UTF-8
from selenium import webdriver   #导入 selenium 的 webdriver 包
driver = webdriver.Chrome()  #打开浏览器
help(driver.get)
driver.get("http://103.160.103.133:9080/hxdsbank/inner/userservices/loginPage-view.html") #打开网页
driver.maximize_window()#浏览器最大化显示
driver.set_window_size(480, 800)设置浏览器宽480、高800显示
driver.back()#后退
driver.forward()#前进
driver.refresh()#刷新
driver.submit()提交表单
print(driver.title)#获取标题
print(driver.current_url)#获取网址
print(driver.current_window_handle)#获取句柄(id)
driver.quit()#退出并关闭窗口的每一个相关的驱动程序
driver.title,current_url#判断访问是否有效
find_element_by_id().clear()#清空输入值
find_element_by_id().send_keys()#输入值
find_element_by_id().click()#点击
size = b.find_element_by_id("j_username").size
print (size)   #返回元素的尺寸
text=driver.find_element_by_id("cp").text
print text    #获取元素的文本
attribute=driver.find_element_by_id("kw").get_attribute('type')
print attribute  #返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
result=driver.find_element_by_id("kw").is_displayed()
print result    ##返回元素的结果是否可见，返回结果为 True 或 False
'''

#元素定位
'''
find_element_by_id()
find_element_by_name()
find_element_by_class_name()
find_element_by_tag_name()
find_element_by_link_text()#针对链接
find_element_by_partial_link_text()#模糊查询
find_element_by_xpath()
    绝对定位：以/开头 非常依赖于页面的顺序和位置
    相对定位：以//开头 不依赖页面的顺序和位置 只看整个页面中有没有符合表达式的元素
        //标签名[@属性名='属性值']、//标签名[@属性名='属性值' and @属性名='属性值'] #
        #层级定位
        //父级标签名[@父级属性名='父级属性值']/标签名 、//父级标签名[@父级属性名='父级属性值']/标签名[@属性名='属性值']
        #函数使用
        text()：元素的text内容
            例：//*[@id='xxx']//标签名[text()='xxx']
        contains
            //标签名[contains(@属性名/text(),'属性值/文本内容')]
            例：//input[contains(@type,'password')]、//input[contains(@type,'password') and xxx]、
                //input[contains(text(),'系统参数定义维护')]
    轴定位：
        ancestor：祖先节点 包括父
        parent：父节点
        preceding:当前元素节点标签之前的所有节点
        preceding-sibling：当前元素节点标签之前的所有兄弟节点
        following：当前元素节点标签之后的所有节点
        follow-sibling：当前元素节点标签之后的所有兄弟节点
        使用语法：
            /轴名称::节点名称
            例：//div//table//td//preceding::td
                //span[text()='xxx']/ancestor::a(祖先标签名)/following-sibling（祖先的兄弟）::div//a 
        应用场景：
        页面显示为一个表格样式的数据列，需要通过组合来定位元素
    动态元素定位：
        尾部：//标签名[ends_with(@属性名,'属性值')]
find_element_by_css_selector()
find_element_by_css_selector("input[id=\"...\"]")
find_element_by_css_selector('input[style =" width: 100%;"]')
find_element_by_xpath("//*[count(input)=2]/..")#统计xxx元素个数=2的节点/父节点
find_element_by_xpath(" //input[@id=’input’] ") #通过自身的 id 属性定位
find_element_by_xpath(" //span[@id=’input-container’]/input ") #通过上一级目录的id属性定位
find_element_by_xpath(" //div[@id=’hd’]/form/span/input ") #通过上三级目录的 id 属性定位
find_element_by_xpath(" //div[@name=’q’]/form/span/input ")#通过上三级目录的 name 属性定位
find_element_by_xpath("//*[local-name()='xxx']")#查找tag为xxx的元素
find_element_by_xpath("//*[starts-with(local-name,'i')]")#找到所有tag以x开头的元素
find_element_by_xpath("//yyy//*[contains(local-name(),'x')][last()-1]")#找到某节点下所有tag包含x的元素/最后一个/最后-1
find_element_by_xpath("//*[string-length(local-name())=x]")#查找tag长度为X的元素
find_element_by_xpath("//xxx|//yyy")多路径查找
'''

#定位一组对象
'''
from selenium import webdriver
import time
b = webdriver.Chrome()
'b.get('file:///C:/Users/issuser/Desktop/ccc.html')
inputs = b.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()'  #
checkboxs = b.find_elements_by_css_selector('input[type = "checkbox"]')
for checkbox in checkboxs:
    checkbox.click()
print(len(checkboxs))
time.sleep(2)
b.find_elements_by_css_selector('input[type = "checkbox"]').pop().click()
'''

#鼠标事件
'''
from selenium.webdriver.commom.action_chains import ActionChains
ActionChains(driver)#生成模拟用户行为
    driver: wedriver 实例执行用户操作。
    ActionChains 用于生成用户的行为；所有的行为都存储在 actionchains 对象。通过 perform()执行存储的行为。
perform()
    执行所有 ActionChains 中存储的行为。perfrome()同样也是 ActionChains 类提供的的方法，通常与ActionChains（）配合使用

context_click #右击事件
    例：
        #定位到要右击的元素
        right =driver.find_element_by_xpath("xx")
        #对定位到的元素执行鼠标右键操作
        ActionChains(driver).context_click(right).perform()
double_click #双击事件
    例：
        #定位到要双击的元素
        double =driver.find_element_by_xpath("xxx")
        #对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(double).perform()
drag_and_drop #鼠标拖放操作
    drag_and_drop(source, target)
    source: 鼠标按下的源元素。
    target: 鼠标释放的目标元素。
    例：
        #定位元素的原位置
        element = driver.find_element_by_name("xxx")
        #定位元素要移动到的目标位置
        target = driver.find_element_by_name("xxx")
        #执行元素的移动操作
        ActionChains(driver).drag_and_drop(element, target).perform()
move_to_element() #鼠标停在一个元素上
    例：
        #定位到鼠标移动到上面的元素
        above = driver.find_element_by_xpath("xxx")
        #对定位到的元素执行鼠标移动到上面的操作
        ActionChains(driver).move_to_element(above).perform()
click_and_hold #按下鼠标左键在一个元素上
    例：
        #定位到鼠标按下左键的元素
        left=driver.find_element_by_xpath("xxx")
        #对定位到的元素执行鼠标左键按下的操作
        ActionChains(driver).click_and_hold(left).perform()
'''

#键盘事件
'''
#引入 Keys 类包
from selenium.webdriver.common.keys import Keys
#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
#删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
#通过回车键盘来代替点击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE) 空格键(Space)
send_keys(Keys.TAB) 制表键(Tab)
send_keys(Keys.ESCAPE) 回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
'''

#下拉框处理
'''
#先定位到下拉框
m=driver.find_element_by_id("ShippingMethod")
#再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()
    需要说明的是在实际的 web 测试时，会发现各种类型的下拉框，并非我们我们上面所介绍的传统的下
拉框。对这种类型的下拉框一般的处理是两次点击，第一点击弹出下拉框，第二次点击操作元
素。当然，也有些下拉框是鼠标移上去直接弹出的，那么我们可以使用 move_to_element()进行操作。

select类-下拉框处理
    from selenium.webdriver.support.ui import Select
选择下拉列表值
    通过下标选择：select_by_index(index)从0开始
    通过value属性：select_by_value(value值)
    通过文本内容：select_by_visible_text(文本内容)
    例：
    #找到select类
    WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.ID,'ShippingMethod')))
    ele = driver.find_element_by_id('ShippingMethod')
    #实例化select类
    s = Select(ele)
    #选择下拉列表值
    #方式一：下标 从0开始
    s.select_by_index(2)
    #方式二：value值
    s.select_by_value('3.20')
    #方式三：文本内容
    s.select_by_visible_text('UPS 2nd Day Air ==> $9.03')
    #Select(driver.find_element_by_id('ShippingMethod')).select_by_index(2)
    
'''

#脚本中的等待方法
'''
#强制等待
    time.sleep()
#隐性等待
    implicitly_wait() 设置最长等待时间,该时间内查找到元素后继续，全局可用
#显性等待
    WebDriverWait #程序每隔X秒看一眼，等待条件满足执行下一步，否则继续等待，超时后抛出TimeoutException
    WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
    timeout - 最长超时时间，默认以秒为单位
    poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
    ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
    例：
    from selenium.webdriver.support.ui import WebDriverWait
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(“someId”))
    is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).
            until_not(lambda x: x.find_element_by_id(“someId”).is_displayed())
            
    WebDriverWait()一般由 unit()或 until_not()方法配合使用，下面是 unit()和 until_not()方法的说明。
    until(method, message=’’)
    调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
    until_not(method, message=’’)
    调用该方法提供的驱动程序作为一个参数，直到返回值为 False。
    
    expected_conditions模块：提供了一系列期望发生的条件
    presence_of_element_located:元素存在
    visibility_of_element_located:元素可见  visibility_of_element_located(By.元素的定位类型,元素的定位表达式)
    element_to_be_clickable:元素可点击
    例：
        xpath = '//*[@id="operNo"]/input'
        WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,xpath)))
    #导入库
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
'''

#切换
'''
#alert对象   
    alert不是HTML页面元素
    WebDriverWait(driver,10).until(ec.alert_is_present())#确定是否有弹出框 返回 true或false
    alert = driver.switch_to.alert() #切到alter，返回一个alter对象
    alert.accept()  #确认
    alert.dismiss() #取消
    alert.send_keys()  #有输入框才能使用
    print(alert.text())#得到文本信息并打印

#多窗口切换
    handles = driver.window_handles#获取窗口的总数以及句柄，新打开的窗口 一般位于最后一个
    driver.switch_to.window(handles[*])#切换页面
    driver.current_window_handle#当前窗口的句柄
    方式二：
        handles = driver.window_handles#获取窗口的总数
        driver.find_element_by_xx('').click()
        #等待新窗口出现
        WebDriverWait(driver,10).until(ec.new_window_is_opened(handles))
        #重新获取一次窗口数
        handles = driver.window_handles
        #切换窗口
        driver.switch_to.window(handles[-1])
        
#ifram切换
    方式一：
        driver.switch_to.frame('')#切换到iframe
        或driver.switch_to.frame(driver.find_element_by_xxx('xxx'))#切换到iframe
        time.sleep(1)
    方式二：
        WebDriverWait(driver,10).until(ec.frame_to_be_available_and_switch_to_it(''))
        time.sleep(0.5)
    driver.switch_to.default_content()#切换回默认页面
    driver.switch_to.parent_frame()#切回父级
'''

#js处理
'''
滚动条处理：
    #移动到元素element对象的'底端'与当前窗口的'底部'对齐
    element = driver.find_element_by_xx('xx')
    driver.execute_script('arguments[0].scrollIntoView(false);',element)
    #移动到元素element对象的'顶端'与当前窗口的'顶部'对齐
    driver.execute_script('arguments[0].scrollIntoView;',element)
    #移动到页面底部
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    #移动到页面顶部
    driver.execute_script('window.scrollTo(document.body.scrollHeight,0)')
日期处理：
    1、选择日期为只读模式处理：
        将readonly改为false
        ele = document.getElementById('')
        ele.readonly = false
        ele.value = yyyy-mm-rr
        js = 'var ele = document.getElementById('');ele.readOnly = false;ele.value = yyyy-mm-rr;'
        driver.execute_script(js)
    2、移除属性
        ele = document.getElementById('')
        ele.removeAttribute('readonly')
'''

#上传文件
'''
1、input标签：
    #定位上传按钮，添加本地文件
    driver.find_element_by_name("file").send_keys('文件路径')
2、非input标签
    2.1、AutoIt  去调用其生成au3或exe文件
    2.2、python pywin32库+win32(winspy++)识别对话框句柄，进而操作
        具体演示在python自动化全栈测试093部分
        
'''

#框架
'''
前提：
    需求分析
    web自动化测试背景。应用场景
    自动化用例设计：原则、筛选、评审、计划
1、PO（PageObject）模式应用(分层设计)（页面对象与测试用例分离）
    原理：
        将页面的元素定位和元素行为封装成一个page类
        类的属性：元素的定位
        类的行为：元素的操作
    测试用例：    
        调用所需页面对象中的行为，组成测试用例
    好处：
        1、当某个页面的元素发生变化，只需要修改该页面对象中的代码即可，测试用例不需要修改
        2、提高代码重用率。结构清晰，维护容易
        3、测试用例发生变化时，不需要或者只需要修改少数页面对象代码即可
2、引入ddt
3、深入分层：测试数据分离
4、遵循原则：测试用例的独立性
5、深入分层：元素定位分离
6、框架优化：提取basepage，具备处理异常、日志、截图功能
7、框架优化：使用pytest框架
'''

# pytest
'''
pytest:基于unittest之上的单元测试框架
1、自动发现测试模块和测试方法
2、断言使用assert+表达式即可
3、可以设置会话级、模块级、函数级的fixture  数据准备+清理工作
4、有300+丰富的插件库

安装命令： pip install pytest
安装HTML报告的插件：pip install pytest-html
pytest插件地址：http://pugincompat.herokuapp.com

pytest 收集测试用例规则：
1、默认从当前目录中收集测试用例，即在哪个目录下运行pytest,则从哪个目录当中搜索
2、搜索规则：
    1、符合命名规则test_*.py 或 *_test.py的文件
    2、以test_开头的函数名
    3、以Test开头的测试类（没有__init__函数）当中，以test_开头的函数
    
pytest-mark
对测试用例进行打标签，在运行测试用例的时候，可根据标签名来过滤要运行的用例
使用方法：
    在测试用例/测试类前面加：@pytest.mark.标记名
    例：@pytest.mark.smoke
         pytest -m smoke(执行选中的用例)
可以在一个用例上打多个标签

pytest-定义fixture
    fixture:测试用例执行的环境准备和清理，相当于unittest中的setup/teardown/setupclass/teardownClass
    fixture主要目的是为了提供一种可靠和可重复性的手段去运行那些最基本的测试内容
    比如在测试网站的功能时，每个测试用例都要登录和退出，利用fixture就可以只做一次
    把一个函数定义为fixture：在函数声明之前加@pytest.fixture  表示此函数为测试环境数据的准备和清理
    在函数内使用yield关键字 区分fixture的环境准备和环境清理
    yield关键字以后的代码，就是环境清理的代码，即测试用例执行完成之后会执行的代码
    fixture返回值
    fixture定义之后的使用

pytest-参数化
    在测试用例前面加上：@pytest.mark.parametrize('参数名', 列表数据)
    参数名：用来接收每一项数据，并作为测试用例的参数
    列表数据：一组测试数据

pytest-重运行机制
    安装插件：rerunfailures   pip install rerunfailures
    使用方式：
        命令行参数形式  pytest --reruns 重试次数 例：pytest --reruns 2    运行失败的用例可以重新运行两次
        pytest --reruns 重试次数 --reruns-delay 次数之间的时间间隔（秒）
        pytest --reruns 2 --reruns-delay 5

pytest -html
安装 pytest -html插件
1、生成junitXML格式的测试报告  命令：--junitxml=path
2、生成result log 格式的测试报告   命令：--resultlog=report\log.txt
3、生成HTML格式的测试报告  命令：--html=report\test_one_func.html

pytest-allure报告
1、安装allure
    下载allure.zip  解压到本地目录、配置allure的环境变量ALLURE_HOME
2、pytest插件安装 命令：pip install allure-pytest
3、pytest生成allure测试报告的命令参数  命令：--alluredir=/xxx/my_allure_results
4、查看allure的测试报告命令
    allure serve allure报告路径
    例：allure serve D:\python_web_pytest_allure\HtmlTestReport\allure
allure文档: https://docs.qameta.io/allure/
'''

# 持续集成
'''
概念：持续集成（CI）
    持续集成是一种实践，可以让团队在持续的基础上收到反馈并进行改进，不必等到开发周期后期才寻找和修复缺陷（一开始用于开发，打包，
    查询是否缺少文件或者依赖包等）
sonarQube工具（可以做静态代码检查，复杂度，重复度，语法规范、安全隐患等等）
部署测试环境：
持续集成流程：
    代码检查-编译打包-单元测试-自动部署-冒烟测试-回归测试
持续集成的好处：
    1、解放了重复性劳动
    2、更快的修复问题
    3、更块的交付成果
    4、减少手工的错误
    5、减少了等待时间
    6、更高的产品质量
'''

# jenkins
'''
概念
    1、job
        在Jenkins平台中，都是以job（任务/工程）为单位去完成一件事情的
    2、plugin（插件）
        Jenkins提供平台，集成各种插件来完成一个job
        比如：Windows命令，Linux命令支持，SVN和Git代码获取、邮件发送等
    3、workspace（工作空间）
        Jenkins是通过文件形式来存储和管理数据的
        workspace给Jenkins制定一个专门的目录来存储其所有的配置和数据
        Jenkins和workspace是根目录，每个job都有属于自己的workspace
Master/Slave   （管理者）安装了Jenkins的电脑/其他电脑
    master：Jenkins服务器
    slave：执行机，执行master分配的任务，返回任务的进度和结果
jenkins安装的电脑是主机  其他电脑是执行机
    分担Jenkins服务器的压力，分配任务到其他执行机来执行
Jenkins allure 报告集成
    1、安装allure插件：http://updates.jenkins-ci.org/download/plugins/allure-jenkins-plugin
    2、在全局工具配置中，配置allure命令行
        1、安装JDK1.8+
        2、如果是在slave上执行allure命令，那么安装方式要选择'从Mavenn中心'自动安装
    3、全局工具配置中，添加jdk配置
    4、配置slave节点的工具（JDK+allure）
Role-based-Authorization Strategy     用户权限管理插件
GitHub  开源代码托管平台    https://github.com/
用户名：wangweimin110   密码：WangWeimin941016
GitHub 是一个面向开源及私有软件项目的托管平台，因为只支持Git作为唯一的版本库格式进行托管，故名GitHub
作用：看开源的代码
    上传自己的代码
上传代码到github过程
       pycharm-VCS-Enable Version...-Git
       VCS-Git-Remotes-url
       VCS-Git-add-Commit File
       VCS-Git-
jenkins与github建立连接的凭证
    用户名和密码http连接
    插件：
构建触发器：
    Poll SCM
        每隔一段指定时间去代码管理工具（Github）检查是否有新代码上传，如果有则自动构建
        *****  分别代表分钟、小时、天、月、星期
        例：H/30**** 每隔30分钟执行一次
            *3**1-5   周一到周五凌晨三点执行
            *11**  每月1号1点执行
            *代表全部，-代表区间，/表示间隔  H 1-17/3***  每天1点到17点，每三小时构建一次
Jenkins代码构建：
    1、设置python解释器位置（r'C:\Users\WWM\AppData\Local\Programs\Python\Python37\python.exe'）放在全局变量
        系统管理-系统配置-全局属性-Environment variables（键：python 值：解释器位置）
    2、设置文件路径及命令
        项目-配置-构建-增加构建步骤-Execute Windows batch command（执行Windows批处理命令）
发送邮件：
    整个邮件配置分为三部分
        1、发件人测试邮件配置
            163邮箱为例：设置-开启POP3/SMTP服务获取授权码
            系统管理-配置-Jenkins Location-系统管理员邮件地址（邮箱号）
            系统管理-配置-邮件通知-SMTP server（163中SMTP服务器地址）
            系统管理-配置-邮件通知-Default user E-mail suffix（邮箱默认后缀 @163.com）
            系统管理-配置-邮件通知-高级-Use SMTP Authentication（使用SMTP认证）
                用户名（邮箱）  密码（授权码）
                通过发送测试邮件测试配置
        2、发件人正式邮件配置
            安装插件 Emile Extension
            系统管理-配置-Extended E-mail Notification-SMTP server（163中SMTP服务器地址）
            系统管理-配置-Extended E-mail Notification-Default user E-mail suffix（邮箱默认后缀 @163.com）
            系统管理-配置-Extended E-mail Notification-高级-Use SMTP Authentication（使用SMTP认证）
                用户名（邮箱）  密码（授权码）
            系统管理-配置-Extended E-mail Notification-Default Content Type
            系统管理-配置-Extended E-mail Notification-Default Content
        3、收件人配置
            项目-配置-构建后操作-Editable Email Notification-set..(高级)-
             Triggers-Recipient List(收件人列表，1391691574@qq.com)
部署过程：
    1、开发者提交代码到代码管理平台
    2、Jenkins获取远程代码（代码管理平台上）
    3、Jenkins将源代码实现自动化打包
    4、执行shell脚本
'''
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()

