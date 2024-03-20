def beolvasas():
    with open("info.txt", "r", encoding="UTF-8") as fm:
            szoveg=fm.read()
            szoveg.strip
    szavak=szoveg.split(" ")
    return szavak

def kiir(fi, szsz, fl, lh_sz, mgh_szam, msh_szam, mgh_szam_sz):            
    print(fi)     
    print(f"A szöveg {szsz} szóból áll.")  
    print(f"A szöveg visszafelé: {fl}")
    print(f"A leghosszabb szó a: {lh_sz}.({len(lh_sz)} betűből áll.)")
    print(f"A teljes szövegre:\n Magánhangzók száma: {mgh_szam}\n Mássalhangzók száma: {msh_szam} ")
    print(f"Szavanként: \n Magánhangzók száma: {mgh_szam_sz} ")
    
def forditva_kiir(l):
    rl=([elem for elem in reversed(l)])       
    return rl

def leghosszabb_szo(l):
    lhsz=l[0]
    for szo in l:
        if len(szo)>len(lhsz):
            lhsz=szo
    return lhsz
        
def maganhangzok_szama(l):
    mgh=["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
    mgh_szam=0
    for szo in l:
        for karakter in szo:
            if karakter in mgh:
                mgh_szam+=1
    return mgh_szam

def massalhangzok_szama(l):
    mgh=["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
    msh_szam=0
    for szo in l:
        for karakter in szo:
            if karakter not in mgh:
                msh_szam+=1
    return msh_szam

def mgh_szama_szavak(l):
    mgh=["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
    i=0
    mgh_szam=0
    szo=l[i]
    for szo in l:
        for karakter in szo:
            if karakter in mgh:
                mgh_szam+=1
                i+=1
            else:
                i+=1
    return szo, mgh_szam

file_beolvas=beolvasas()
mondat=beolvasas()
szo_szam=len(mondat)
forditott_lista=forditva_kiir(mondat)
leghosszabb=leghosszabb_szo(mondat)
mgh_szama=maganhangzok_szama(mondat)
msh_szama=massalhangzok_szama(mondat)
mgh_szama_szavankent=mgh_szama_szavak(mondat)

kiir(file_beolvas, szo_szam, forditott_lista, leghosszabb, mgh_szama, msh_szama, mgh_szama_szavankent)