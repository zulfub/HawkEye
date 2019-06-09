import pyodbc

def sql_conn(licPlate) :
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=SKULD\ELGINDB;"
                            "Database=db_Graduation;"
                            "uid=sa;"
                            "pwd=1234")
    cursor = cnxn.cursor()
    #all_files = os.listdir("C:/Users/dell/Desktop/deneme/test1")
    #all_captures = os.listdir("C:/Users/dell/Desktop/deneme/photos")
    #a = 0
    #for x in all_captures :
    #    os.system("cd C:/Users/dell/Desktop/deneme/photos ")
    #    os.system("tesseract.exe " + x + " test" + str(a))
    #    a+= 1

    #for n in all_files:
    #    fo = open("C:/Users/dell/Desktop/test/test1/" + n, "r")
    #for n in range(0,16):
    #    im = Image.open("test" + str(n) + ".JPG")
    #    text = image_to_string(im)
    #    data = text.split()
    #    if (len(data) >2 & len(data)<4):

    #       sehir = data[0]
    #        harf = data[1]
    #        num = data[2]
    cursor.execute("INSERT INTO tbl_Plate (Plaka) values(?);", (licPlate))
    cursor.commit()
    #    else :
    #        break


    print ('=====output=======\n')
    cursor.execute('SELECT * FROM tbl_Plate')
    for row in cursor:
        print('row = %r' % (row))