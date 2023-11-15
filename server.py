from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

compra = [
        {
        "nombre":"michael",
        "apellido":"choi",
        "manzanas":"2",
        "frutillas":"2",
        "frezas":"2",
        "id":"123-456-7890"
        }
    ]

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    nueva_compra = {
        "nombre":request.form["first_name"],
        "apellido":request.form["last_name"],
        "manzanas":request.form["apple"],
        "frutillas":request.form["strawberry"],
        "frezas":request.form["raspberry"],
        "id":request.form["student_id"]
    }         
    compra[0]=nueva_compra
    print("cobrando a "+ request.form["first_name"]+" por " + f'{int(request.form["apple"]) + int(request.form["strawberry"]) + int(request.form["raspberry"])}')
    return redirect('/checkout1')

@app.route('/checkout1')
def lista_de_compra():

    return render_template("checkout.html", compra = compra)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    


    