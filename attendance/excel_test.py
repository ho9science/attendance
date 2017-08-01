import openpyxl
from attend import Attend

# 엑셀파일 열기
wb = openpyxl.load_workbook('attendance.xlsx')

# 현재 Active Sheet 얻기
ws = wb.active
# ws = wb.get_sheet_by_name("Sheet1")


#cell 정보 읽기
for r in ws.rows:
    absent = 0
    day = []
    row_index = r[0].row  # 행 인덱스

    if row_index > 5 and row_index < 25:
        print("row index : " + str(row_index))
        name = r[4].value

        day.append(r[6].value)
        day.append(r[7].value)
        day.append(r[8].value)
        day.append(r[9].value)
        day.append(r[10].value)
        day.append(r[11].value)
        for d in day:

            if d == -20:
                absent = absent + 1;

        attendance = (len(day) - absent) / len(day) * 100
        member = Attend(name, attendance)
        member.print()
    # 합계 쓰기
    #ws.cell(row=row_index, column=5).value = sum


# 엑셀 파일 저장
#wb.save("score2.xlsx")
wb.close()