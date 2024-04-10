import PyPDF2

with open('twopage.pdf','rb') as file:
  reader = PyPDF2.PdfReader(file)
  for i in range(len(reader.pages)):
    page = reader.pages[i].extract_text()
    pagerotate = reader.pages[i].rotate(90)
    print(page)
    print(pagerotate)
    writer = PyPDF2.PdfWriter()
    writer.add_page(pagerotate)
    with open('rotatedpage.pdf', 'wb') as new_file:
      writer.write(new_file)

  # just a comment
  



  