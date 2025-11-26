from reportlab.pdfgen import canvas
from io import BytesIO

def generar_pdf(alumno):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(100, 800, f"Alumno: {alumno.nombre}")
    p.drawString(100, 780, f"DNI: {alumno.dni}")
    p.drawString(100, 760, f"Curso: {alumno.curso}")

    p.save()
    buffer.seek(0)
    return buffer
