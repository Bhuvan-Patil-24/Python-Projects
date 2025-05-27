import PyPDF2 as pdf

files = ["Python-Projects/PDF_Merger/sample1.pdf", "Python-Projects/PDF_Merger/sample2.pdf", "Python-Projects/PDF_Merger/sample3.pdf"]  # List of PDF files to merge
merger = pdf.PdfMerger()

print(f"Merging {len(files)} PDF files...")  # Print the number of files being merged
for file in files:
    with open(file, 'rb') as pdfFile:  # Use 'with' to ensure the file is closed after reading
        pdfReader = pdf.PdfReader(pdfFile)  # Create a PDF reader object
        merger.append(pdfReader) 
print("Files merged successfully!")  
merger.write("Python-Projects/PDF_Merger/merged.pdf")  # Write the merged PDF to a new file
merger.close()  # Close the merger object