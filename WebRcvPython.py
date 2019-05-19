import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Parsing a request")
        orig = self.get_argument("orig")
        dest = self.get_argument("dest")
        cgtype = self.get_argument("cgtype")
        cgdesc = self.get_argument("cgdesc")
        date1 = self.get_argument("date1")
        date2 = self.get_argument("date2")
        opt = self.get_argument("opt")
        print(orig, dest, cgtype, cgdesc, date1, date2, opt)
        file = open("shipBroker/Requests.txt","w")
        file.write(orig+";  "+ dest+";  "+cgtype+";  "+cgdesc+";  "+date1+"-->"+date2+";  "+opt)
        file.close() 
        os.rename('shipBroker\FromTarragona.txt','shipBroker\Facilities.txt')
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
