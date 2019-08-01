import xlwt
import time
# 开始
start = time.perf_counter()
# 编码
work_excel = xlwt.Workbook(encoding = 'utf-8')
# 字体加粗
style = xlwt.easyxf('font: bold on')
# sheet1名称
sheet = work_excel.add_sheet('自动化1')
# 行
sheet.write(0,0,"账号",style)
sheet.write(0,1,"密码",style)
# 列宽
sheet.col(0).width = 256*20
sheet.col(1).width = 256*20
# 居中对齐
jz = xlwt.Alignment()
jz.horz = 0x02
jz.vert = 0x01
style2 = xlwt.XFStyle()
style2.alignment = jz
# 创建一个循环
for l in range(1,1001):
    s = l + 8451252630000
    sheet.write(l,0,s,style2)
    sheet.write(l,1,"Faxuan.%1234",style2)
# sheet2名称
sheet2 = work_excel.add_sheet('自动化2')
# 行
sheet2.write(0,0,"平均值",style)
sheet2.col(0).width = 256*20
sheet2.col(1).width = 256*20
# 创建循环
sum = 0
for a in range(8451252630001,8451252631001):
    sum += a
sheet2.write(1,0,sum/1000,style2)
# 保存
work_excel.save('D:/2019-08-01.xls')
# 结束
end = time.perf_counter()
print(end-start,'s')

