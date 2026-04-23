<!-- frontend/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>AI Agent Chat</title>
</head>
<body>
    <h2>AI Agent</h2>

    <input id="input" placeholder="Type your task..." />
    <button onclick="send()">Send</button>

    <pre id="output"></pre>

    <script>
        async function send() {
            let text = document.getElementById("input").value;

            let res = await fetch("http://127.0.0.1:8000/run", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({task: text})
            });

            let data = await res.json();
            document.getElementById("output").innerText = data.result;
        }
    </script>
</body>
</html>



# api/main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



<div id="chat"></div>

<script>
async function send() {
    let text = document.getElementById("input").value;

    document.getElementById("chat").innerHTML += "<p>🧑‍💻 " + text + "</p>";

    let res = await fetch("http://127.0.0.1:8000/run", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({task: text})
    });

    let data = await res.json();

    document.getElementById("chat").innerHTML += "<p>🤖 " + data.result + "</p>";
}
</script>