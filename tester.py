import docx
 
# open connection to Word Document
doc = docx.Document("Quickstart.docx")
 
# read in each paragraph in file
result = [p.text for p in doc.paragraphs]