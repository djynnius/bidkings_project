#writing an mvc wraper for mod python! :-)
from mod_python import apache

class Elipsis():
    def __init__(self, req, apache):
        self.req = req
        self.apache = apache
    
    def render(self, html):
        self.req.content_type = 'text/html'
        return html

if __name__ == "__main__":
    elipsis = Elipsis(req)
    elipsis.render('<h1>Hello world!</h1>')
