from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def welcome(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
<head>
    <title>Local Links</title>
</head>
<body>
    <h1>Welcome to My Local Server</h1>
    <p>Here are some links to local resources:</p>
    <ul>
        <li><a href="http://localhost:8000/admin/">Admin</a></li>
        <li><a href="http://localhost:8000/hello/">Hello</a></li>
    </ul>
</body>
</html>

""")