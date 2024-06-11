from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, PageBreak
from reportlab.pdfgen.canvas import Canvas


class ESKD:
    def __init__(self, filename):
        page_size = A4
        portrait_frame_page = Frame(0, 0, page_size[0], page_size[1])
        pagetemplate = [
            PageTemplate(id='portrait', frames=portrait_frame_page, onPage=self.on_portrait_page)
        ]
        self.__report = BaseDocTemplate(filename=filename, pageTemplates=pagetemplate)
        self.__flowables = [Paragraph('test'), PageBreak(), Paragraph('test')]

    def on_portrait_page(self, canvas: Canvas, doc):
        canvas.setLineWidth(1.5)
        canvas.line(20 * mm, 5 * mm, A4[0] - 5 * mm, 5 * mm)
        canvas.line(20 * mm, A4[1] - 5 * mm, A4[0] - 5 * mm, A4[1] - 5 * mm)

        canvas.line(20 * mm, 5 * mm, 20 * mm, A4[1] - 5 * mm)
        canvas.line(A4[0] - 5 * mm, 5 * mm, A4[0] - 5 * mm, A4[1] - 5 * mm)

        # left stamp
        canvas.line(13 * mm, 5 * mm, 13 * mm, 150 * mm)
        canvas.line(8 * mm, 5 * mm, 8 * mm, 150 * mm)

        canvas.line(8 * mm, 5 * mm, 20 * mm, 5 * mm)
        canvas.line(8 * mm, 30 * mm, 20 * mm, 30 * mm)
        canvas.line(8 * mm, 65 * mm, 20 * mm, 65 * mm)
        canvas.line(8 * mm, 90 * mm, 20 * mm, 90 * mm)
        canvas.line(8 * mm, 115 * mm, 20 * mm, 115 * mm)
        canvas.line(8 * mm, 150 * mm, 20 * mm, 150 * mm)

        if doc.page == 2:
            canvas.line(A4[0] - 190 * mm, 45 * mm, A4[0] - 5 * mm, 45 * mm)
            canvas.line(A4[0] - 190 * mm, 35 * mm, A4[0] - 5 * mm, 35 * mm)

            canvas.line(A4[0] - 50 * mm, 5 * mm, A4[0] - 50 * mm, 35 * mm)
            canvas.line(A4[0] - 125 * mm, 5 * mm, A4[0] - 125 * mm, 35 * mm)
            canvas.line(A4[0] - 135 * mm, 5 * mm, A4[0] - 135 * mm, 35 * mm)
            canvas.line(A4[0] - 150 * mm, 5 * mm, A4[0] - 150 * mm, 35 * mm)
            canvas.line(A4[0] - 173 * mm, 5 * mm, A4[0] - 173 * mm, 35 * mm)

            canvas.line(A4[0] - 183 * mm, 35 * mm, A4[0] - 183 * mm, 45 * mm)
        else:
            canvas.line(A4[0] - 190 * mm, 20 * mm, A4[0] - 5 * mm, 20 * mm)
            canvas.line(A4[0] - 15 * mm, 5 * mm, A4[0] - 15 * mm, 20 * mm)

            canvas.drawString(A4[0] - 15 * mm, 15+8, 'Лист')

    def save(self):
        self.__report.build(self.__flowables)


if __name__ == "__main__":
    eskd = ESKD("test.pdf")
    eskd.save()
