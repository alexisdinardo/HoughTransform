
import numpy as np
import cv2 
import A05


def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))

   return mse

def mse2(img1, img2):
   h, w , l = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w*l))

   return mse


def test01() :  #detect_circles
   
   tolerance=1e-3
   img = cv2.imread('images/jupiter.jpg')#.astype(np.float32)
   threshold = 0.05

   edges = A05.detect_edges(img,threshold, False)
   
   center=A05.detect_circles(img, edges, 10, 1,False) # un mundo

   correct_center = np.loadtxt('autograd/jupyter_center01.txt')

   return  (abs(center-correct_center)).sum() < tolerance


def test02() :  #detect_circles
   
   tolerance=1e-3
   img = cv2.imread('images/jupiter.jpg')#.astype(np.float32)
   threshold = 0.05

   edges = A05.detect_edges(img,threshold, False)
   
   center=A05.detect_circles(img, edges, 32, 1,False) # un mundo

   correct_center = np.loadtxt('autograd/jupyter_center02.txt')

   return  (abs(center-correct_center)).sum() < tolerance



def test03() :  #detect_circles
   
   tolerance=1e-3
   img = cv2.imread('images/jupiter.jpg')#.astype(np.float32)
   threshold = 0.05

   edges = A05.detect_edges(img,threshold, False)
   
   center=A05.detect_circles(img, edges, 52, 1,False) # un mundo

   correct_center = np.loadtxt('autograd/jupyter_center03.txt')

   return  (abs(center-correct_center)).sum() < tolerance



def test04() :  #detect_circles
   
   tolerance=1e-3
   img = cv2.imread('images/jupiter.jpg')#.astype(np.float32)
   threshold = 0.05

   edges = A05.detect_edges(img,threshold, False)
   
   center=A05.detect_circles(img, edges, 100, 1,False) # un mundo

   correct_center = np.loadtxt('autograd/jupyter_center04.txt')

   return  (abs(center-correct_center)).sum() < tolerance


def test05() :  #quantize_RGB

   tolerance=1e-3
   img = cv2.imread('images/fish.jpg')
   k=2
   quant_img_rgb, mean_colors, cluster_ids_rgb = A05.quantize_RGB(img, k)

   img_out=cv2.imread('autograd/fish_quantize01.png' )
   mean_out=np.loadtxt('autograd/fish_mean_colors01.txt')
   cluster_ids=np.loadtxt('autograd/fish_cluster_ids01.txt')

   flag=True
   flag &= (mse2(quant_img_rgb,img_out) < tolerance)
   flag &= ((abs(mean_colors-mean_out) ).sum()<tolerance )
   flag &= ((abs(cluster_ids_rgb-cluster_ids) ).sum()<tolerance )

   assert flag


def test06() :  #quantize_RGB

   tolerance=1e-3
   img = cv2.imread('images/fish.jpg')
   k=5
   quant_img_rgb, mean_colors, cluster_ids_rgb = A05.quantize_RGB(img, k)


   img_out=cv2.imread('autograd/fish_quantize02.png' )
   mean_out=np.loadtxt('autograd/fish_mean_colors02.txt')
   cluster_ids=np.loadtxt('autograd/fish_cluster_ids02.txt')

   flag=True
   flag &= (mse2(quant_img_rgb,img_out) < tolerance)
   flag &= ((abs(mean_colors-mean_out) ).sum()<tolerance )
   flag &= ((abs(cluster_ids_rgb-cluster_ids) ).sum()<tolerance )

   assert flag

def test07() :  #quantize_RGB

   tolerance=1e-3
   img = cv2.imread('images/fish.jpg')
   k=10
   quant_img_rgb, mean_colors, cluster_ids_rgb = A05.quantize_RGB(img, k)

   img_out=cv2.imread('autograd/fish_quantize03.png' )
   mean_out=np.loadtxt('autograd/fish_mean_colors03.txt')
   cluster_ids=np.loadtxt('autograd/fish_cluster_ids03.txt')

   flag=True
   flag &= (mse2(quant_img_rgb,img_out) < tolerance)
   flag &= ((abs(mean_colors-mean_out) ).sum()<tolerance )
   flag &= ((abs(cluster_ids_rgb-cluster_ids) ).sum()<tolerance )

   assert flag