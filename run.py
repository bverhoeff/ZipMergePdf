import os
from pypdf import PdfReader, PdfWriter

def merge_pdfs(odd_file, even_file, output_file):
    """Merges two pdf files. The odd_file contains odd pages only whereas the
    even_file contains even pages in reversed order. These two files result from
    scanning a two sided paper document when first the front side of all pages
    is scanned, followed by scanning of all back sides. This way of scanning
    can be more practical for large documents.

    Args:
        odd_file (str): path of file with odd pages
        even_file (str): path of file with even pages
        output_file (str): path of resulting merged file
    """
    # Open the PDF files
    odd_pages = PdfReader(odd_file, 'rb')
    even_pages = PdfReader(even_file, 'rb')

    # determine number of pages
    num_pages = len(odd_pages.pages)

    print(f"\nMerging pages of pdf-files '{odd_file}' and '{even_file}' with each {num_pages} pages.")

    # merge pdf pages, adding odd and even pages in turn, reversing order of even pages
    merger = PdfWriter()
    for i in range(num_pages):
        merger.merge(position=i*2, fileobj=odd_pages, pages=(i, i+1))
        merger.merge(position=i*2+1, fileobj=even_pages, pages=(num_pages - i - 1, num_pages - i))

    # determine final number of pages
    final_num_pages = len(merger.pages)

    # Write to an output PDF document
    with open(output_file, "wb") as o:
        merger.write(o)

    print(f"New merged PDF file with {final_num_pages} pages saved at: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    merge_pdfs("input_odd.pdf", "input_even.pdf", "merged.pdf")