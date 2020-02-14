import xlsxwriter


def segitigaExcel(kata) :
    syarat = [1]
    awal = 1
    inisiasi = 0
    kata = kata.replace(' ', '')
    for i in range(2, len(kata)):
        awal = awal + i
        syarat.append(awal)
    if len(kata) in syarat :
        book = xlsxwriter.Workbook("soal2.xlsx")
        sheet = book.add_worksheet("jawaban")
        for i in range(syarat.index(len(kata))+2):
            for j in range(i) :
                sheet.write(i-1,j,kata[inisiasi])
                inisiasi += 1
        book.close()
    else :
        print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola")

# segitigaExcel('Purwadhika')
# segitigaExcel('Purwadhika Startup and Coding School @BSD')
# segitigaExcel('kode')
# segitigaExcel('kode python')
# segitigaExcel('Lintang')