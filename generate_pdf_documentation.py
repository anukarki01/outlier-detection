from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class PDFDocumentGenerator:
    def __init__(self, filename):
        self.filename = filename

    def generate_complete_document(self):
        c = canvas.Canvas(self.filename, pagesize=A4)
        width, height = A4

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "Outlier Detection System")

        c.setFont("Helvetica", 11)
        text = c.beginText(50, height - 90)
        text.textLine("Project Documentation")
        text.textLine("")
        text.textLine("This document describes an Outlier Detection System")
        text.textLine("implemented using multiple algorithms:")
        text.textLine("")
        text.textLine("• K-Nearest Neighbors (KNN)")
        text.textLine("• Local Outlier Factor (LOF)")
        text.textLine("• Isolation Forest")
        text.textLine("")
        text.textLine("Key features:")
        text.textLine("• CSV dataset upload")
        text.textLine("• Algorithm comparison")
        text.textLine("• Visualization of detected outliers")
        text.textLine("• Performance evaluation metrics")
        text.textLine("")
        text.textLine("This system is designed for academic and research purposes.")

        c.drawText(text)
        c.showPage()
        c.save()
