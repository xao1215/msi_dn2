from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

def give_count():
    return redis.get("counter")


@app.route("/")
def hello():
    redis.incr("counter")
    lol = redis.get("counter").decode("utf8")
    # lol = lol.decode("utf8")
    return render_template( "index.html" , message=lol)
    # return 'Hello World{}" ..." )
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)