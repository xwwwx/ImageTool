# ImageTool
影像處理工具

Binarization(self,im)
圖形二值化 閾值為平均灰階值
im : 圖形灰階值二維ndarray
return ndarray

Binarization(self,im,th)
圖形二值化 
th : 閾值
im : 圖形灰階值二維ndarray
return ndarray

ImageSave(self,fp,im)
圖形儲存
fp : filepath
im : 圖形ndarray

Sobel(self,im)
Sobel演算法邊緣檢測
im : 圖形灰階值二維ndarray
return ndarray