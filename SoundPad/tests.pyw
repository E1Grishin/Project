def read_saves(dict,file_path):
    s = open(file_path)

    for i in range(1,15):
        a = str(i)
        dict[a] = s.readline().replace('\n','')
    s.close()
    return dict
def write_saves(dict, file_path ):
    s = open(file_path,'r+')
    n = ''
    for i in range(1,15):
        a = str(i)
        n += dict[a] + '\n'
    s.write(n)
    s.close()
sounds = {"1":'',"2":'',"3":'',"4":'',"5":'',"6":'',"7":'',"8":'',"9":'',
         "10":'',"11":'',"12":'',"13":'',"14":''}
binds = {"1":'',"2":'',"3":'',"4":'',"5":'',"6":'',"7":'',"8":'',"9":'',
         "10":'',"11":'',"12":'',"13":'',"14":''}
read_saves(binds,"Content/Binds.txt")
read_saves(sounds,"Content/Sounds.txt")
binds['1']='лупа'
sounds['1'] = 'ггг'
write_saves(binds,"Content/Binds.txt")
write_saves(sounds,"Content/Sounds.txt")
