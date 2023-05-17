import PyPDF2
pdffiles=["p1.pdf","p2.pdf","p3.pdf"]

merger=PyPDF2.PdfMerger()

for filename in pdffiles:
    pdffiles=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdffiles)
    merger.append(pdfReader)
pdffiles.close()
merger.write('merge.pdf')

