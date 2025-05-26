import PyPDF2 as pdf

files = ["Python-Projects/sample1.pdf", "Python-Projects/sample2.pdf", "Python-Projects/sample3.pdf"]  # List of PDF files to merge
merger = pdf.PdfMerger()

for file in files:
    with open(file, 'rb') as pdfFile:  # Use 'with' to ensure the file is closed after reading
        pdfReader = pdf.PdfReader(pdfFile)  # Create a PDF reader object
        merger.append(pdfReader) 
merger.write("Python-Projects/merged.pdf")  # Write the merged PDF to a new file
merger.close()  # Close the merger object