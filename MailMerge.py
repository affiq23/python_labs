import xlrd
import csv
import docx
import pathlib

page = """
Sales Promotion letter on shoes
(Circular letter) 

Frisco Shoes
1234 Awesome Dr.
Frisco, TX 7654

<DATE>

<NAME>
<ADDRESS>
<CITY> , <STATE> <ZIPCODE>

Dear  <NAME> 

We do not remember the names and faces of our customers. It is so because they are satisfied. Moreover ones they purchase our shoes they do not need the others for the next two years.

Road master shoes are manufactured by us are durable, soft, and comfortable. Wear them throughout the day but never feel fatigued. So soft and comfortable! Road master are also so light that you may walk along with for miles untiringly.

Road master shoes are available in several varieties, qualities, sizes and colors. Pure leather, artificial leather, and rubber shoes at reasonable prices are always in our stock.

Purchase your favorite shoes now for yourself, wife and kids and look more smart in Road Master   

	
Yours truly,


<YOURNAME>
Manager


"""

with xlrd.open_workbook('Address.xlsx') as wb:
    sh = wb.sheet_by_index(0)  # wb.sheet_by_name('sheet_name')
    with open('Address.csv', 'w', newline="") as f:
        col = csv.writer(f)
        for row in range(sh.nrows):
            col.writerow(sh.row_values(row))
            
            
with xlrd.open_workbook('Address.xlsx') as wb:
    sh = wb.sheet_by_index(0)  # wb.sheet_by_name('sheet_name')
    count = 0
    for row in range(sh.nrows):
        work_page = page
        firstName = sh.row_values(row)[0]
        lastName = sh.row_values(row)[1]
        address = sh.row_values(row)[2]
        city = sh.row_values(row)[3]
        state = sh.row_values(row)[4]
        zipcode = sh.row_values(row)[5]
        work_page = work_page.replace("<DATE>",'4-25-2021')
        work_page = work_page.replace("<YOURNAME>",'Affiq Mohammed')
        work_page = work_page.replace("<NAME>",firstName + " " + lastName)
        work_page = work_page.replace("<ADDRESS>",address)
        work_page = work_page.replace("<CITY>",city)
        work_page = work_page.replace("<STATE>",state)

        print(work_page)
            