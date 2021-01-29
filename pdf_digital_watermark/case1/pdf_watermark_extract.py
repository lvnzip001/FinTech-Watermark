import PyPDF2
import sys


def extract_watermark(file_watermarked):
    # Input file
    pdf_input = PyPDF2.PdfFileReader(open(file_watermarked, 'rb'))
    pageNum = pdf_input.getNumPages()
    extractedText = pdf_input.getPage(pageNum - 1).extractText()
    watermarkInfo = extractedText.split()[-1]
    result = watermarkInfo.split("-", 3)     # split into 3 variables if we have a resource ID 
    print("Extract watermaker mark from",file_watermarked)
    print("Resource owner_email:",result[0], "  current user_email:",result[1] , "  ResourceID:",result[2] )


if __name__ == '__main__':
    file_watermarked = "./out.pdf"
    #file_watermarked = sys.argv[1]    # for CLI
    extract_watermark(file_watermarked)


