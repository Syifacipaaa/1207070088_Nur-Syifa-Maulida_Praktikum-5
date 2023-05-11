import matplotlib.pyplot as plt #memanggil library matplotlib untuk menampilkan gambar dengan nama plt
import numpy as np#memanggil library numpy untuk mengolah array
import cv2#memanggil library cv2 untuk mengolah gambar

#Percobaan 1 - Cropping Image
# membaca gambar
image = cv2.imread('Bunga.jpeg')#membaca gambar dengan nama Bunga.jpg dan menyimpannya ke dalam variable image
image1 = cv2.imread('aljabar.jpg')#membaca gambar dengan nama aljabar.jpg dan menyimpannya ke dalam variable image1

#memotong gambar
crop = image[60:60+100, 60:60+100]
crop2 = image1[60:60+100, 60:60+100]

#menampilkan gambar yang telah dipotong
fig, axes = plt.subplots(ncols=2, nrows=2)#untuk membuat subplot dengan 2 kolom dan 2 baris di Matplotlib.
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(image)#menampilkan gambar
ax[0].set_title("Citra Asli")#Title pada plot
ax[1].imshow(crop)#menampilkan gambar yang telah disetting cropped
ax[1].set_title("Crop 1")#Title pada plot
ax[2].imshow(image1)#menampilkan gambar image1
ax[2].set_title("Citra Asli 2")#Title epada plot
ax[3].imshow(crop2)#menampilkan  gambar yang telah disetting cropped
ax[3].set_title("Crop 2")#Title pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

#Percobaan 2 - Citra Negative
inv = 255 - crop2 #rumus untuk mengkonversi gambar menjadi citra negatif
print('Shape Input : ', crop.shape)#menampilkan hasil gambar crop dengan Title Share input
print('Shape Output : ',inv.shape)#menampilkan hasil gambar crop dengan Title Share output

fig, axes = plt.subplots(ncols=2, nrows=2)#untuk membuat subplot dengan 2 kolom dan 2 baris di Matplotlib.
ax = axes.ravel()#untuk meratakan (flatten) sebuah array multidimensi menjadi array 1 dimensi.

ax[0].imshow(crop)#menampilkan gambar
ax[0].set_title("Citra Input")#Title pada plot
ax[1].hist(crop.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[1].set_title('Histogram Input')#Title pada plot
ax[2].imshow(inv)#menampilkan gambar
ax[2].set_title('Citra Output (Inverted Image)')#Title pada plot
ax[3].hist(inv.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[3].set_title('Histogram Output')#Title pada plot
fig.tight_layout()#untuk secara otomatis menyesuaikan jarak antar subplot dan label dalam sebuah gambar.
plt.show()#menampilkan semua plot

gambar2=crop2.copy().astype(float)#m: melakukan operasi copy (menggandakan) array cropped2, sehingga kita mendapatkan array yang sama persis dengan cropped2,mengonversi tipe data array tersebut dari uint8 menjadi float.
m1, n1 = gambar2.shape#ukuran array pada masing2 dimensi(baris dan kolom)
output1 = np.empty([m1, n1])#untuk membuat array kosong dengan alokasi memori yang cukup untuk menampung elemen array yang diinginkan.

for baris in range(0, m1 - 1):#untuk melakukan iterasi atau perulangan pada sebuah urutan data, yang dalam hal ini adalah sebuah urutan angka dari 0 hingga m1-2.
    for kolom in range(0, n1 - 1):#perulangan untuk mengintegrasikan setiap baris pada gambar untuk kolom
        a1 = baris#menyimpan nilai baris kedalam variable a1
        b1 = kolom#menyimpan nilai kolom kedalam variable b1
        output1[a1, b1] = gambar2[baris, kolom] + 100#menambahkan nilai 100 pada piksel baris dan kolom pada output untuk citra hasil informasi

fig, axes = plt.subplots(ncols=2, nrows=2)#untuk membuat subplot dengan 2 kolom dan 2 baris di Matplotlib.
ax = axes.ravel()#menyusun plot ke dalam bentuk array

ax[0].imshow(crop2, cmap='gray')#menampilkan gambar kedalam bentuk grayscale
ax[0].set_title("Citra Input")#Title pada plot
ax[1].hist(crop.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[1].set_title('Histogram Input')#Title pada plot
ax[2].imshow(output1, cmap='gray')#menampilkan gambar kedalam bentuk grayscale
ax[2].set_title('Citra Output (Brightnes)')#Title judul pada plot
ax[3].hist(output1.ravel(), bins=256)#untuk membuat histogram dari gambar yang telah di-inversi
ax[3].set_title('Histogram Input')#Title pada plot
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot