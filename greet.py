from bottle import route, run
import os

@route('/')
def hello():

   print("Content-type: text/html; charest=utf-8")

   print("")

   print("<html><head><meta charest='utf-8'><body>")
   print("聞くことに早く語ることに遅くあるべき")
   print("</body></html>")

run(host='localhost', port=8082, debug=True)
