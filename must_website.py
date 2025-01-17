
from flask import Flask, render_template_string

app = Flask(__name__)

web_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MUST - Mi Sueño</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
        }
        header {
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        header img {
            max-width: 150px;
            margin: 10px 0;
        }
        main {
            padding: 20px;
        }
        h1 {
            color: #555;
        }
        .intro {
            margin-bottom: 30px;
            font-size: 18px;
        }
        .product {
            margin: 20px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <header>
        <img src="logo.png" alt="MUST Logo">
    </header>
    <main>
        <h1>Bienvenido a MUST</h1>
        <p class="intro">Soy un chico con un sueño de crear mi propia marca de ropa. Aquí estoy, dando mis primeros pasos. ¡Gracias por apoyarme!</p>
        <div class="product">
            <h2>Sudaderas Exclusivas</h2>
            <p>Pronto disponibles.</p>
        </div>
    </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(web_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
