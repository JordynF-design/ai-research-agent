from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)


from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import datetime
import re


def add_page_number(canvas, document):

    canvas.saveState()

    canvas.setFont("Helvetica", 9)

    page_number = canvas.getPageNumber()

    canvas.drawCentredString(
        4.25 * inch,
        0.5 * inch,
        f"Page {page_number}"
    )

    canvas.restoreState()


def create_pdf(topic, articles, summary):

    safe_topic = re.sub(r'[^a-zA-Z0-9]+', '_', topic).strip('_').lower()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"research_report_{safe_topic}_{timestamp}.pdf"

    document = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph("AI RESEARCH AGENT REPORT", styles["Title"])
    )

    content.append(Spacer(1, 0.3 * inch))

    content.append(
        Paragraph(f"Research Topic: {topic}", styles["Heading2"])
    )

    content.append(
        Paragraph(
            f"Date Generated: {datetime.now().strftime('%B %d, %Y')}",
            styles["Normal"]
        )
    )


    content.append(Spacer(1, 0.5 * inch))

    content.append(
        Paragraph(
            "Prepared by AI Research Agent",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "Research findings, source references, and analysis",
            styles["Normal"]
        )
    )

    content.append(PageBreak())


    content.append(Spacer(1, 0.3 * inch))

    content.append(
        Paragraph("Research Findings", styles["Heading1"])
    )

    for number, article in enumerate(articles, start=1):

        content.append(
            Paragraph(
                f"{number}. {article['title']}",
                styles["Heading3"]
            )
        )

        content.append(
            Paragraph(article["snippet"], styles["BodyText"])
        )

        content.append(
        Paragraph(
            f'Source: <link href="{article["url"]}" color="blue">Open source</link>',
            styles["BodyText"]
        )
    )


        content.append(Spacer(1, 0.2 * inch))

    content.append(PageBreak())

    content.append(
        Paragraph("Research Summary", styles["Heading1"])
    )

    for line in summary.split("\n"):
        if line.strip():
            content.append(
                Paragraph(line, styles["BodyText"])
            )
            content.append(Spacer(1, 0.1 * inch))

    document.build(
    content,
    onFirstPage=add_page_number,
    onLaterPages=add_page_number
)

    print(f"\nPDF report created: {filename}")