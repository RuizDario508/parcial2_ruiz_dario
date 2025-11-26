from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Alumno
from .forms import AlumnoForm
import tempfile


@login_required
def alumno_list(request):
    alumnos = Alumno.objects.filter(usuario=request.user)
    return render(request, "alumnos/alumno_list.html", {"alumnos": alumnos})


@login_required
def alumno_detail(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    return render(request, "alumnos/alumno_detail.html", {"alumno": alumno})


@login_required
def alumno_create(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.usuario = request.user
            alumno.save()
            return redirect("alumno_list")
    else:
        form = AlumnoForm()

    return render(request, "alumnos/alumno_form.html", {"form": form})


@login_required
def alumno_update(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)

    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect("alumno_detail", pk=pk)

    else:
        form = AlumnoForm(instance=alumno)

    return render(request, "alumnos/alumno_form.html", {"form": form})


@login_required
def alumno_delete(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)

    if request.method == "POST":
        alumno.delete()
        return redirect("alumno_list")

    return render(request, "alumnos/alumno_confirm_delete.html", {"alumno": alumno})


# -------------------------------
# PDF + Envío por email
# -------------------------------
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io


@login_required
def alumno_pdf(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    # Contenido del PDF
    p.setFont("Helvetica-Bold", 18)
    p.drawString(100, 800, f"Ficha del alumno: {alumno.nombre}")

    p.setFont("Helvetica", 14)
    p.drawString(100, 760, f"Edad: {alumno.edad}")
    p.drawString(100, 740, f"Curso: {alumno.curso}")
    p.drawString(100, 720, f"Creado: {alumno.created_at.strftime('%d/%m/%Y')}")

    p.showPage()
    p.save()

    buffer.seek(0)
    pdf_content = buffer.getvalue()

    # Enviar el PDF por correo
    email = EmailMessage(
        subject=f"Ficha del alumno {alumno.nombre}",
        body="Adjunto encontrarás el PDF con los datos del alumno.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[request.user.email],
    )
    email.attach(f"{alumno.nombre}.pdf", pdf_content, "application/pdf")
    email.send()

    return HttpResponse("PDF enviado correctamente ✔")
