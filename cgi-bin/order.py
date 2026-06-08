import cgi
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()

name = form.getvalue("name")
pizza = form.getvalue("pizza")
size = form.getvalue("size")
quantity = form.getvalue("quantity")

print("<html>")
print("<head>")
print('<link rel="stylesheet" href="/style.css">')
print("</head>")
print("<body>")
print("<h1>Pizza Order Confirmation</h1>")

print(f"<p>Name: {name}</p>")
print(f"<p>Pizza: {pizza}</p>")
print(f"<p>Size: {size}</p>")
print(f"<p>Quantity: {quantity}</p>")

print("<p>Thank you for your order!</p>")

print('<p><a href="https://github.com/yunhanxiao/pizza-order-website">GitHub Repository</a></p>')

print("</body>")
print("</html>")

