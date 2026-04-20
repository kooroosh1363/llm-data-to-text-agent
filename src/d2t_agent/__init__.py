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