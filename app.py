
from flask import Flask, render_template, request, redirect, url_for,flash
from conexion import conexion

app = Flask(__name__)
bd = conexion(app)
app.secret_key = 'Mi_llave_secreta'

@app.route('/')
def index():
    data = bd.get_contacts()
    return render_template('index.html', contacts=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        bd.add_contact(fullname, phone, email)
        flash('Contact added succesfully') #Para mandar mensajes del servidor al cliente
        return redirect(url_for('index'))
    return 'no added'


@app.route('/edit/<id>')
def edit_contact(id):
    data = bd.get_contact(id)
    return render_template('edit_contact.html', contact = data)

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    bd.update_contact(id, fullname, phone, email)
    flash('Contact updated succefully')
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    bd.delete_contact(id)
    flash('Contact delete succefully')
    return redirect(url_for('index'))

    

if __name__ == '__main__':
    app.run(debug=True)



    



