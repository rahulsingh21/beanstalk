import logging.handlers

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = '/tmp/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login System</title>
    <style>
    * {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI';
    font-size: 25px;
}

.form input {
    min-width: 400px;
    display: block;
    margin: 20px;
    padding: 15px 20px;
    background-color: #ece7e7;
    font-size: 20px;
    border: none;
    outline: none;
    box-shadow: 15px 15px 25px #a8a8a8;
    transition: box-shadow 0.5s;
}

.form input:focus {
    box-shadow: 5px 5px 15px #a8a8a8;
}

.form .btn {
    margin: auto;
    padding: 10px 35px;
    background-color: #f1a566;
    color: #fff;
    border: none;
    font-size: 22px;
    border-radius: 10px;
    box-shadow: 15px 15px 20px #a8a8a8;
    transition: box-shadow 0.5s;
    outline: none;
}

.form .btn:hover {
    box-shadow: 5px 5px 15px #aaa;
}

.form {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    height: 50vh;
    width: 50vw;
    position: absolute;
    bottom: 0px;
    font-size: 35px;
}

.left-section .form {
    float: left;
    margin: 35vh auto;
}

.right-section .form {
    float: right;
    margin: 30vh auto;
    right: 0;
}

.cover .switch-btn {
    position: absolute;
    bottom: 0;
    font-size: 25px;
    margin: 40vh auto;
    padding: 10px 55px;
    background-color: #f1a566;
    color: #fff;
    border: none;
    border-radius: 10px;
    box-shadow: 15px 15px 25px #a8a8a8;
    transition: box-shadow 0.5s;
    outline: none;
}

.cover .switch-btn:hover {
    box-shadow: 5px 5px 15px #aaa;
}

.left-section .cover {
    float: left;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.left-section .cover img {
    height: 100vh;
    width: 50vw;
}

.left-section .cover h1 {
    position: absolute;
    bottom: 0;
    margin: 60vh auto;
    color: #fff;
    font-size: 50px;
}

.left-section .cover h3 {
    position: absolute;
    bottom: 0;
    margin: 50vh auto;
    color: #fff;
    font-size: 35px;
}

.left-section .cover-hide {
    visibility: hidden;
}

.left-section .form-hide {
    visibility: hidden;
}

.right-section .cover {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.right-section .cover img {
    height: 100vh;
    width: 50vw;
}

.right-section .cover h1 {
    position: absolute;
    bottom: 0;
    margin: 60vh auto;
    font-size: 50px;
    color: #fff;
}

.right-section .cover h3 {
    position: absolute;
    bottom: 0;
    margin: 50vh auto;
    color: #fff;
    font-size: 35px;
}

.right-section .cover-hide {
    visibility: hidden;
}

.right-section .form-hide {
    visibility: hidden;
}

.fade-in-element {
    animation-name: fade-in-element;
    animation-duration: 1s;
    animation-fill-mode: forwards;
}

@keyframes fade-in-element {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
    </style>
</head>
<script>


function switchSignup() {
    right_form.classList.add("fade-in-element");
    left_cover.classList.add("fade-in-element");

    left_form.classList.add("form-hide");
    left_cover.classList.remove("cover-hide");
    right_form.classList.remove("form-hide");
    right_cover.classList.add("cover-hide");
}

function login() {
    var left_cover = document.getElementById("left-cover");
    var left_form = document.getElementById("left-form");

    var right_cover = document.getElementById("right-cover");
    var right_form = document.getElementById("right-form");

    var login_username = document.getElementById("login-username");
    var login_password = document.getElementById("login-password");

    var incorrect_login_left = document.getElementById("incorrect-login-left-cover");
    var incorrect_login_right = document.getElementById("incorrect-login-right-form");

    let loginMap = new Map();

    loginMap.set('Rahul', 'Singh');
    loginMap.set('Arpana', 'a@123');
    var username = login_username.value
    var password = login_password.value
    var value = loginMap.get(username)
    
    if(value == undefined || value != password) {
        incorrect_login_right.classList.add("fade-in-element")
        incorrect_login_left.classList.add("fade-in-element")
        
        left_form.classList.add("form-hide");
        incorrect_login_left.classList.remove("cover-hide")
        incorrect_login_right.classList.remove("form-hide")
        right_cover.classList.add("cover-hide");
    }
    else {
        document.getElementById("loggedInUser").innerHTML = username
        right_form.classList.add("fade-in-element");
        left_cover.classList.add("fade-in-element");

        left_form.classList.add("form-hide");
        left_cover.classList.remove("cover-hide");
        right_form.classList.remove("form-hide");
        right_cover.classList.add("cover-hide");
    }
}
</script>
<body>
    
    <section class="left-section">
        <div id="left-cover" class="cover cover-hide">
            <img src="img/cover.png" alt="">
            <h1>Welcome !</h1>
            <h3 id="loggedInUser"></h3>
            <button type="button" class="switch-btn" onclick="location.reload()">Logout</button>
        </div>
        <div id="left-form" class="form fade-in-element">
            <h1>Login</h1>
            <form action="" method="post">
                <input type="text" name="user-name" class="input-box" placeholder="User Name" id="login-username">
                <input type="password" name="user-pass" class="input-box" placeholder="Password" id="login-password">
                <input type="button" name="login-btn" class="btn" onclick="login()" value="Login">
            </form>
        </div>
    </section>

    <section class="right-section">
        <div id="right-cover" class="cover fade-in-element">
            <img src="img/cover.png" alt="">
        </div>
        <div id="right-form" class="form form-hide">
            <form action="" method="post">
            </form>
        </div>
    </section>

    <section class="left-section">
        <div id="incorrect-login-left-cover" class="cover cover-hide">
            <img src="img/cover.png" alt="">
            <h3>Incorrect UserName or Password</h3>
            <button type="button" class="switch-btn" onclick="location.reload()">Retry Login</button>
        </div>
    </section>

    <section class="right-section">
        <div id="incorrect-login-right-form" class="form form-hide">
        </div>
    </section>

</body>
</html>
"""


def application(environ, start_response):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'],
                            environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
