from PyPDF2 import PdfFileWriter, PdfFileReader

f = open("recap.pdf", "br")
reader = PdfFileReader(f)

page0 = reader.getPage(0)
texte = page0.extractText()
f.close()

print(texte)


