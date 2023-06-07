from PyPDF2 import PdfFileWriter, PdfFileReader

continu_sortie = PdfFileWriter()

fichier_pdf_presentation = open("presentation.pdf", "rb")
fichier_pdf_recap =  open("recap.pdf", "rb")

reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

print("Nombre de page : " + str(reader_recap.getNumPages()))

continu_sortie.addPage(reader_presentation.getPage(0))
for i in range(reader_presentation.getNumPages()):
    continu_sortie.addPage(reader_recap.getPage(i))


fichier_sortie = open("fichier_sortie.pdf", "wb")
continu_sortie.write(fichier_sortie)

fichier_sortie.close()
fichier_pdf_presentation.close()
fichier_pdf_recap.close()