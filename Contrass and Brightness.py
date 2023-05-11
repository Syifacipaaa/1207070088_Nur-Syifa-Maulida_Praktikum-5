import numpy as np#memanggil library numpy untuk mengolah array
import cv2 #memanggil library cv2
import matplotlib.pyplot as plt #memanggil library matplotlib
img = cv2.imread('aurora.jpg')#membaca gambar dengan nama aurora.jpg dan menyimpannya ke dalam variable img

#define reso dan tipe gambar
img_height = img.shape[0] #membuat variable tinggi gambar
img_width = img.shape[1] #membuat variable lebar gambar
img_channel = img.shape[2] #membuat variable channel gambar
img_type = img.dtype #membuat variable tipe gambar

#Percobaan 1 Mengatur Brightness untuk Gambar Gray Scale

img_brightness = np.zeros(img.shape, dtype=np.uint8)#membuat array numpy dengan nilai nol yang ukurannya sama dengan gambar img dan tipe data unsigned integer 8-bit (uint8).


def brighter(nilai) :#narasi fungsi Python yang akan menambahkan kecerahan pada gambar. Fungsi ini akan menerima satu argumen yaitu nilai, yang akan menentukan seberapa banyak kecerahan yang akan ditambahkan pada gambar.
    for y in range(0, img_height):#loop untuk mengiterasi setiap baris pada gambar dengan tinggi sebesar img_height.
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]#mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]#mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]#mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red)+int(green)+int(blue))/3#Hitung rata-rata nilai piksel pada titik (y,x)
            gray += nilai #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if gray > 255:#jika nilai gray lebih besar dari 255 maka nilai gray diset menjadi 255
                gray = 255
            if gray < 0:# jika nilai gray kurang dari 0 maka nilai gray diset menjadi 0
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)#untuk mengatur nilai piksel pada koordinat (x,y) pada gambar dengan nilai keabuan (grayscale) yang sama pada ketiga saluran warna (R,G,B) sehingga menghasilkan gambar dengan skala keabuan (grayscale).

fig, axes = plt.subplots(ncols=2)#untuk membuat objek figure dan objek axes untuk menampilkan dua gambar secara horizontal (dalam satu baris) menggunakan library Matplotlib.
ax = axes.ravel()#menyusun plot ke dalam bentuk array
brighter(-100)#mengatur  kecerahan dengan nilai -100
ax[0].imshow(img_brightness)#menampilkan gambar
ax[0].set_title("Kecerahan -100")#Title pada plot
brighter(50)#mengatur kecerahan dengan nilai 50
ax[1].imshow(img_brightness)#menampilkan gambar
ax[1].set_title("Kecerahan 50")#Title  pada plot
fig.tight_layout()#untuk memperbaiki tata letak (layout) dari objek figure pada library Matplotlib.
plt.show()#menampilkan semua plot

#brightness RGB
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)#membuat array numpy dengan nilai nol yang ukurannya sama dengan gambar img dan tipe data unsigned integer 8-bit (uint8)

#Fungsi untuk brightness RGB dengan nilai parameter
def rgbbrighter(nilai):#narasi fungsi Python yang akan menambahkan kecerahan pada gambar. Fungsi ini akan menerima satu argumen yaitu nilai, yang akan menentukan seberapa banyak kecerahan yang akan ditambahkan pada gambar.
    for y in range(0, img_height):#loop untuk mengiterasi setiap baris pada gambar dengan tinggi sebesar img_height.
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]#mengambil nilai piksel red pada titik (y,x)
            red += nilai#menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if red > 255:#jika nilai red lebih besar dari 255 maka nilai red diset menjadi 255
                red = 255
            if red < 0:#jika nilai red kurang dari dari 0 maka nilai red diset menjadi 0
                red = 0
            green = img[y][x][1]#mengambil nilai piksel green pada titik (y,x)
            green += nilai#menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if green > 255:#jika nilai green lebih besar dari 255 maka nilai green diset menjadi 255
                green = 255
            if green < 0:#jika nilai green kurang dari dari 0 maka nilai green diset menjadi 0
                green = 0
            blue = img[y][x][2]#mengambil nilai piksel blue pada titik (y,x)
            blue += nilai#menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if blue > 255:#jika nilai blue lebih besar dari 255 maka nilai blue diset menjadi 255
                blue = 255
            if blue < 0:#jika nilai blue kurang dari dari 0 maka nilai blue diset menjadi 0
                blue = 0
            img_brightness[y][x] = (red, green, blue)#muntuk menentukan nilai pixel baru pada koordinat (x, y) pada gambar yang sudah diubah kecerahannya.
fig, axes = plt.subplots(ncols=2)#untuk membuat objek figure dan objek axes untuk menampilkan dua gambar secara horizontal (dalam satu baris) menggunakan library Matplotlib.
ax = axes.ravel()#menyusun plot ke dalam bentuk array
rgbbrighter(-100)#mengatur  rgbbrighter dengan nilai -100
ax[0].imshow(img_brightness)#menampilkan gambar
ax[0].set_title("Brighness -100")#Title pada plot
rgbbrighter(100)#mengatur  rgbbrighter dengan nilai 100
ax[1].imshow(img_brightness)#menampilkan gambar
ax[1].set_title("Brighness 100")#Title pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

#contrast
img_contrass = np.zeros(img.shape, dtype=np.uint8)#membuat array numpy dengan nilai nol yang ukurannya sama dengan gambar img dan tipe data unsigned integer 8-bit (uint8)

def contrass(nilai):#implementasi fungsi contrass yang dapat meningkatkan kontras pada gambar RGB menggunakan NumPy:
    for y in range(0, img_height):#loop untuk mengiterasi setiap baris pada gambar dengan tinggi sebesar img_height.
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  #mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  #mengambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  #mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  #menghitung rata-rata nilai piksel pada titik (y,x)
            gray += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if gray > 255:  #jika nilai gray lebih besar dari 255 maka nilai gray diset menjadi 255
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_contrass

fig, axes = plt.subplots(ncols=2)#untuk membuat objek figure dan objek axes untuk menampilkan dua gambar secara horizontal (dalam satu baris) menggunakan library Matplotlib.
ax = axes.ravel()#menyusun plot ke dalam bentuk array
contrass(50)#mengatur  contrass dengan nilai 50
ax[0].imshow(img_contrass)#menampilkan gambar
ax[0].set_title("Contrass 50")#Title pada plot
contrass(100)#mengatur  contrass dengan nilai 100
ax[1].imshow(img_contrass)#menampilkan gambar
ax[1].set_title("Contrass 100")#Title pada plot
fig.tight_layout()#untuk memperbaiki tata letak (layout) dari objek figure pada library Matplotlib.
plt.show()#menampilkan semua subplot


#Brightness Contrass RGB
img_rgbcontrass = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

#Fungsi untuk brightness RGB dengan nilai parameter
def rgbcontrass(nilai):# meningkatkan kontras pada gambar RGB menggunakan NumPy:
    for y in range(0, img_height):#loop untuk mengiterasi setiap baris pada gambar dengan tinggi sebesar img_height.
        for x in range(0, img_width):#melakukan perulangan pada setiap piksel pada sumbu x untuk variable img_width
            red = img[y][x][0]  #mengambil nilai piksel red pada titik (y,x)
            red += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if red > 255:  #jika nilai red lebih besar dari 255 maka nilai red diset menjadi 255
                red = 255
            green = img[y][x][1]  #mengambil nilai piksel green pada titik (y,x)
            green += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if green > 255:  #jika nilai green lebih besar dari 255 maka nilai green diset menjadi 255
                green = 255
            blue = img[y][x][2]  #mengambil nilai piksel blue pada titik (y,x)
            blue += nilai  #menambahkan nilai 1 setiap parameter pada nilai rata-rata piksel
            if blue > 255:  #jika nilai blue lebih besar dari 255 maka nilai blue diset menjadi 255
                blue = 255
            img_rgbcontrass[y][x] = (red, green, blue)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_rgbcontrass
fig, axes = plt.subplots(ncols=2)#untuk membuat objek figure dan objek axes untuk menampilkan dua gambar secara horizontal (dalam satu baris) menggunakan library Matplotlib.
ax = axes.ravel()#menyusun plot ke dalam bentuk array
rgbcontrass(50)#mengatur  rgbcontrass dengan nilai 50
ax[0].imshow(img_rgbcontrass)#menampilkan gambar
ax[0].set_title("Contrass 50")#Title pada plot
rgbcontrass(100)#mengatur fungsi rgbcontrass dengan nilai 100
ax[1].imshow(img_rgbcontrass)#menampilkan gambar
ax[1].set_title("Contrass 100")#memberikan judul pada plot
fig.tight_layout()#untuk memperbaiki tata letak (layout) dari objek figure pada library Matplotlib.
plt.show()#menampilkan semua subplot

#Contrass Auto Level
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)#membuat array Numpy dengan elemen yang diinisialisasi ke nilai nol dengan unsigned integer dengan panjang 8 bit

def autocontrass():#dapat secara otomatis meningkatkan kontras pada gambar menggunakan NumPy:
    #Inisialisasi variabel xmax, xmin, dan d dengan nilai awal.
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):  #loop untuk mengiterasi setiap baris pada gambar dengan tinggi sebesar img_height.
        for x in range(0, img_width):  #loop untuk mengiterasi setiap baris pada gambar dengan x sebesar img_widht.
            red = img[y][x][0]  #mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # engambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  #mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  #menghitung rata-rata nilai piksel pada titik (y,x)
            if gray < xmax:#jika nilai gray lebih besar dari xmax maka nilai gray diset menjadi xmax
                xmax = gray
            if gray > xmin:#jika nilai gray lebih besar dari xmin maka nilai gray diset menjadi xmin
                xmin = gray
    d = xmin-xmax #mengurangkan parameter xmin dengan xmax
    for y in range(0, img_height):  #loop untuk mengiterasi setiap baris pada gambar dengan tinggi sebesar img_height.
        for x in range(0, img_width):  # oop untuk mengiterasi setiap baris pada gambar dengan sumbu x untuk variable img_width
            red = img[y][x][0]  # mengambil nilai piksel red pada titik (y,x)
            green = img[y][x][1]  # engambil nilai piksel green pada titik (y,x)
            blue = img[y][x][2]  # mengambil nilai piksel blue pada titik (y,x)
            gray = (int(red) + int(green) + int(blue)) / 3  # menghitung rata-rata nilai piksel pada titik (y,x)
            gray = int(float(255/d) * (gray-xmax))#melakukan perhitungan di setiap parameter untuk mendapatkan hasil desimal
            img_autocontrass[y][x] = (gray, gray, gray)#menyimpan nilai piksel yang sudah diatur sebelumnya pada variabel img_autocontrass
autocontrass()#Memanggil fungsi autocontrass() untuk mengaplikasikan proses "auto level" pada gambar.
plt.imshow(img_autocontrass)#menampilkan gambar
plt.title("Contrass Autolevel")#Title pada plot
plt.show()#menampilkan semua plot