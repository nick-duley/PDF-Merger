from PyPDF2 import PdfFileMerger
import os

#The merged PDF file will be saved to this directory
folder_path = "your file path (e.g. users/Username/Desktop/Folder)"

'''This list contains the PDF files that will be merged, the file at the first
index will be at the start'''
pdf_files = ['PDF1.pdf', 'PDF2.pdf']

#Declares the merger object
merger = PdfFileMerger()

'''For every file in the 'pdf_files' list, merge the files together
   and store the result in the specified folder'''
for files in pdf_files:
    merger.append(folder_path+files)

#If the directory doesn't exist, create a folder and store the file there
if not os.path.exists(folder_path+'merged.pdf'):
    merger.write(folder_path + 'merged.pdf')

#Close the merger object
merger.close()
