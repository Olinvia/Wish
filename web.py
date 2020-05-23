from tornado import web,ioloop,httpserver

import yagmail
import random

#首页模块
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("shouye.html")                   #渲染
   
#许愿模块
class WishHandler(web.RequestHandler):
    #返回许愿页面
    def get(self,*args,**kwargs):       #对应http get请求
        self.render('xuyuan.html')
    #接收前端post请求
    def post(self,*args,**kwargs):       #对应http post请求
        #获取前端传递的数据
        name = self.get_argument('name')
        email1 = self.get_argument('email1')
        email2 = self.get_argument('email2')
        email3 = self.get_argument('email3')
        gift = self.get_argument('text')
        email = random.choice([email1,email2,email3])
        mail = yagmail.SMTP("865401097@qq.com", "vnzuxilbanfbbbij", "smtp.qq.com", 465)
        content = """
        朋友，你好！我是{}的心愿精灵。我的主人最近特别想拥有{}，你能帮他实现吗？他一定会超开心的~
        与此同时，你也获得了一张万能心愿卡，一起来许愿吧！
        """.format(name,gift)
        mail.send(email, "叮咚！一项传递幸福的任务，请查收！", content)
        self.redirect('/success')
        #跳转页面
class SuccessHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('chenggong.html')
        
#路由系统 分机 

settings=dict(
        template_path='templates',
        static_path='static'
        )

application = web.Application([
        (r"/",MainPageHandler),         # 首页的路由
        (r"/wish",WishHandler),         #许愿的路由
        (r"/success",SuccessHandler)
        ],**settings)
    
if __name__ == '__main__':
    #socket服务
    http_server = httpserver.HTTPServer(application)
    http_server.listen(10130)
    ioloop.IOLoop.current().start()
