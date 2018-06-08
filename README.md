# ImageTool
影像處理工具



Binarization(self,im,th = None)
圖形二值化 
th : 閾值 預設為灰階值平均
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