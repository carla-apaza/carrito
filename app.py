from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "8350e5a3e24c153df2275c9f80692773"


@app.route("/verproducto")
def home():
    carrito = session.get("carrito", [])
    total_total = 0
    for p in carrito:
        total_total += p["total"]
    return render_template("index.html", carrito=carrito, total_total=total_total)


@app.route("/agregar", methods=["POST"])
def agregar():
    producto = request.form["producto"]
    cantidad = int(request.form["cantidad"])
    precio = {
        "arroz": 10,
        "frijoles": 12,
        "azucar": 15,
        "lentejas": 11,
        "leche": 8,
        "miel": 5,
    }
    precio_producto = precio[producto]
    total = precio_producto * cantidad

    if "carrito" not in session:
        session["carrito"] = []

    carrito = session["carrito"]
    carrito.append(
        {
            "producto": producto,
            "precio": precio_producto,
            "cantidad": int(cantidad),
            "total": total,
        }
    )

    session["carrito"] = carrito
    return redirect("/verproducto")


@app.route("/vaciar")
def vaciar():
    session["carrito"] = []
    return redirect("/verproducto")


if __name__ == "__main__":
    app.run(debug=True)
