# document_converter.py (doc => docx)
import os
from doc2docx import convert

def process_documents(documentList):
    # Get the absolute path of the parent directory where the program is running
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    print(f"Processing {len(documentList)} documents in doc to docX converter")

    # Check if document is doc or docx and if so, converts
    for index, document in enumerate(documentList):

        if document.endswith(".doc"):
            new_document_x = document[:-4] + ".docx"
            convert(document, new_document_x)
            print(f"Converted {document} to {new_document_x}")
            documentList[index] = new_document_x
        # else:
        # print(f"Skipping {document}: Not a .doc file")

    # print(f"List of documents checked: {documentList}")
    return documentList

if __name__ == "__main__":
    print("Running Test")

