# drawing_polygons.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_shapes():
    my_canvas = canvas.Canvas("drawing_polygons.pdf")
    my_canvas.setStrokeColorRGB(0.2, 0.5, 0.3)
    my_canvas.rect(10, 740, 100, 80, stroke=1, fill=0)
    my_canvas.ellipse(10, 680, 100, 630, stroke=1, fill=1)
    my_canvas.wedge(10, 600, 100, 550, 45, 90, stroke=1, fill=0)
    my_canvas.circle(300, 600, 50)
    my_canvas.save()

if __name__ == '__main__':
    draw_shapes()