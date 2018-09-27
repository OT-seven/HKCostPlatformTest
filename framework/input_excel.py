# _*_ coding: utf -8 _*_
import xlrd, xlwt

class Update_Excel(object):

    def update_hkcost_sysbill(self, file, value, outputfile):
        self.data = xlrd.open_workbook(file)
        self.table = self.data.sheet_by_index(0)
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
        ctype = 2
        xf = 0
        self.table.put_cell(1, 1, ctype, value, xf)
        self.table.put_cell(2, 1, ctype, value, xf)
        self.wbook = xlwt.Workbook()
        self.wsheet = self.wbook.add_sheet(self.table.name)
        style = xlwt.XFStyle()
        fnt = xlwt.Font()
        for r in range(self.nrows):
            for c in range(self.ncols):

                fnt.name = u'文本'
                fnt.bold = False
                style.font = fnt
                self.wsheet.write(r, c, self.table.cell_value(r, c), style)
        self.wbook.save(outputfile)

# uhs = Update_Excel()
# uhs.update_hkcost_sysbill('账单信息导入模板.xlsx', '5001013', 'output.xls')