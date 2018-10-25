from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


def create_watermark(f_jpg):
    f_pdf = 'mark.pdf'
    w_pdf = 20 * cm
    h_pdf = 20 * cm

    c = canvas.Canvas(f_pdf, pagesize=(w_pdf, h_pdf))
    c.setFillAlpha(0.3)  # 设置透明度
    print
    c.drawImage(f_jpg, 7 * cm, 7 * cm, 6 * cm, 6 * cm)  # 这里的单位是物理尺寸
    c.save()


# create_watermark('tmp.png')



from PyPDF2 import PdfFileWriter, PdfFileReader
output = PdfFileWriter()

ipdf = PdfFileReader(open('source.pdf', 'rb'))
wpdf = PdfFileReader(open('mark.pdf', 'rb'))
watermark = wpdf.getPage(0)

for i in range(0, ipdf.getNumPages()):
    page = ipdf.getPage(i)
    page.mergePage(watermark)
    output.addPage(page)

with open('newfile.pdf', 'wb') as f:
   output.write(f)


# # encoding=utf-8
# # author: walker
# # date: 2014-03-18
# # function:给pdf添加水印
# from PyPDF2 import PdfFileWriter, PdfFileReader
# from reportlab.pdfgen import canvas
#
#
# # 所有路径为绝对路径
# def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
#     pdf_output = PdfFileWriter()
#     input_stream = file(pdf_file_in, 'rb')
#     pdf_input = PdfFileReader(input_stream)
#
#     # PDF文件被加密了
#     if pdf_input.getIsEncrypted():
#         print('该PDF文件被加密了.')
#         # 尝试用空密码解密
#         try:
#             pdf_input.decrypt('')
#         except Exception, e:
#             print('尝试用空密码解密失败.')
#             return False
#         else:
#             print
#             '用空密码解密成功.'
#     # 获取PDF文件的页数
#     pageNum = pdf_input.getNumPages()
#     # 读入水印pdf文件
#     pdf_watermark = PdfFileReader(file(pdf_file_mark, 'rb'))
#     # 给每一页打水印
#     for i in range(pageNum):
#         page = pdf_input.getPage(i)
#         page.mergePage(pdf_watermark.getPage(0))
#         page.compressContentStreams()  # 压缩内容
#         pdf_output.addPage(page)
