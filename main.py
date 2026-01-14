from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        n1 = float(request.form.get('n1'))
        n2 = float(request.form.get('n2'))
        n3 = float(request.form.get('n3'))
        asistencia = int(request.form.get('asistencia'))

        promedio = round((n1 + n2 + n3) / 3, 1)
        estado = "APROBADO" if promedio >= 4.0 and asistencia >= 75 else "REPROBADO"
        color = "#34a853" if estado == "APROBADO" else "#ea4335"

        # El estilo 'flex' en el div asegura que el contenido esté al centro
        return f"""
        <div style="display:flex; justify-content:center; align-items:center; height:100vh; font-family:Arial; background-color:#f0f2f5;">
            <div style="background:white; padding:40px; border-radius:15px; border:3px solid {color}; text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
                <h1 style="color:{color};">{estado}</h1>
                <p>Promedio: <strong>{promedio}</strong></p>
                <p>Asistencia: <strong>{asistencia}%</strong></p>
                <br><a href="/ejercicio1" style="text-decoration:none; color:#1a73e8;">Volver</a>
            </div>
        </div>
        """
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nom1 = request.form.get('nombre1')
        nom2 = request.form.get('nombre2')
        nom3 = request.form.get('nombre3')
        lista = [nom1, nom2, nom3]

        largo_maximo = max(len(nom) for nom in lista)
        ganadores = [nom for nom in lista if len(nom) == largo_maximo]

        mensaje = "Los nombres más largos son" if len(ganadores) > 1 else "El nombre más largo es"
        nombres_finales = ", ".join(ganadores)

        return f"""
        <div style="display:flex; justify-content:center; align-items:center; height:100vh; font-family:Arial; background-color:#f0f2f5;">
            <div style="background:white; padding:40px; border-radius:15px; border:3px solid #34a853; text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
                <h2 style="color:#2d8e47;">Resultado de Nombres</h2>
                <p>{mensaje}: <strong>{nombres_finales}</strong></p>
                <p>Cantidad de caracteres: <strong>{largo_maximo}</strong></p>
                <br><a href="/ejercicio2" style="text-decoration:none; color:#1a73e8;">Volver</a>
            </div>
        </div>
        """
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)