
"""
# Feature detection in a image with:
- a convolution kernel,
- a threshold and
- image
as input. The convolution kernel is a square K x K real matrix denoted by k(i,j),
the threshold is a real number, and the image is given as an RxC real matrix with
elements between 0 and 1, with the pixel in row r and column c given by p(r,c)
where r in [0,R) and c in [0,C). We say theat there is a feature at position (r,c)
if SUM (k(i,j) p(r+i, c+j)) > T

However, the kernel is only valid if it is not overflowing the image, therefore,
if the kernel is overflowing the image, we do not want to detect a feature.

Input:
2 0.65 3 4   # K, T, R and C where all are integers except T which is a real number
-1.0 1.0  # kernel values (KxK)
1.0 0.0
0.0 0.1 0.2 0.3  # image values (RxC)
0.4 0.5 0.6 0.7
0.8 0.9 0.0 0.1
Output:
0 2  # the positions of the detected features (r, c), one per line
1 0
1 1
"""

def detect_features_with_convolution_kernel_and_threshold():#kernel, T, R, C):
  K,T,R,C  = str(raw_input()).strip().split()
  K = int(K)
  T = float(T)
  R = int(R)
  C = int(C)
  #print "K,T,R,C : ",K,T,R,C

  kernel = []
  # read kernel
  for kernel_row in range(K):
    kernel_row = []
    for value in (raw_input()).split():#strip().split()
    	kernel_row.append(float(value))
    kernel.append(kernel_row)
  #print "Kernel: \n",kernel

  # read image
  img = []
  for image_row in range(R):
    image_row = []
    for value in (raw_input()).split():#strip().split()
  		image_row.append(float(value))
    img.append(image_row)
  #print "Image: \n",img

  features = []
  for r in range(R):
    for c in range(C): #while kernel_start_r < (R-K) and kernel_start_c  < (C-K):
      if feature_is_present_in_pos(kernel, img, r, c, K, T, R, C):
        features.append((r, c))
  print_features(features)


def feature_is_present_in_pos(kernel, img, r, c, K, T, R, C):
  suma = 0
  if not kernel_overflows_img(r, c, K, R, C):
    for i in range(K):
      for j in range(K):
        partial_sum = kernel[i][j] * img[r+i][c+j]
        suma += partial_sum
    if suma > T:
      #print "feature_is_present in (r,c): ", r,c
      return True
  return False

def kernel_overflows_img(r, c, K, R, C):
  if (r+K) > R or (c+K)> C:
      return True
  return False

def print_features(features):
  for (r,c) in features:
    print r, " ", c

detect_features_with_convolution_kernel_and_threshold()
