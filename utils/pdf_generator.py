from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def generate_pdf(report_text, filename="research_report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    elements = []

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    paragraphs = report_text.split("\n")

    title_style = styles["Heading1"]

    elements.append(Paragraph("AI Research Report", title_style))
    elements.append(Spacer(1, 0.5 * inch))

    for para in paragraphs:
        elements.append(Paragraph(para, normal_style))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)

    print(f"PDF generated successfully: {filename}")