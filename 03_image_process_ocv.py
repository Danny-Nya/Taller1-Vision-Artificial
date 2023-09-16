import cv2  # Importa la librería OpenCV para procesamiento de imágenes

image = cv2.imread("color_wheel.jpg")  # Lee una imagen llamada "color_wheel.jpg" y la almacena en una variable
# llamada `image`

blue, green, red = cv2.split(image)  # Separa la `image` en sus canales de color azul, verde y rojo y los almacena en
# las variables `blue`, `green` y `red`, respectivamente
cv2.imwrite("out_ocv/color_wheel_B.png", blue)  # Escribe el canal azul de la imagen en un archivo llamado
# "color_wheel_B.png"
cv2.imwrite("out_ocv/color_wheel_G.png", green)  # Escribe el canal verde de la imagen en un archivo llamado
# "color_wheel_G.png"
cv2.imwrite("out_ocv/color_wheel_R.png",
            red)  # Escribe el canal rojo de la imagen en un archivo llamado "color_wheel_R.png"

b_w = int(blue.shape[1] / 4)  # Calcula el ancho del canal azul dividiendo su ancho por 4 y lo almacena en una variable
# llamada `b_w`
b_h = int(blue.shape[0] / 4)  # Calcula el alto del canal azul dividiendo su alto por 4 y lo almacena en una variable
# llamada `b_h`
blue_bgr = cv2.resize(blue, (b_w, b_h))  # Redimensiona el canal azul para t
# ener un ancho de `b_w` y un alto de `b_h` y
# lo almacena en una variable llamada `blue_bgr`

g_w = int(green.shape[1] / 2)  # Calcula el ancho del canal verde dividiendo su ancho por 2 y lo almacena en una
# variable llamada `g_w`
g_h = int(green.shape[0] / 2)  # Calcula el alto del canal verde dividiendo su alto por 2 y lo almacena en una variable
# llamada `g_h`
green_bgr = cv2.resize(green, (g_w, g_h))  # Redimensiona el canal verde para tener un ancho de `g_w` y un alto de
# `g_h` y lo almacena en una variable llamada `green_bgr`

r_w = int(red.shape[
              1] / 0.75)  # Calcula el ancho del canal rojo dividiendo su ancho por 0.75 y lo almacena en una
# variable llamada `r_w`
r_h = int(red.shape[
              0] / 0.75)  # Calcula el alto del canal rojo dividiendo su alto por 0.75 y lo almacena en una variable
# llamada `r_h`
red_bgr = cv2.resize(red, (r_w,
                           r_h))  # Redimensiona el canal rojo para tener un ancho de `r_w` y un alto de `r_h` y lo
# almacena en una variable llamada `red_bgr`

cv2.imwrite("out_ocv/color_wheel_sB.png",
            blue_bgr)  # Escribe el canal azul redimensionado en un archivo llamado "color_wheel_sB.png"
cv2.imwrite("out_ocv/color_wheel_sG.png",
            green_bgr)  # Escribe el canal verde redimensionado en un archivo llamado "color_wheel_sG.png"
cv2.imwrite("out_ocv/color_wheel_sR.png",
            red_bgr)  # Escribe el canal rojo redimensionado en un archivo llamado "color_wheel_sR.png"

# Redimensionar imágenes al tamaño de la imagen original
gray_blue = cv2.resize(blue_bgr, (image.shape[1], image.shape[0]))
gray_green = cv2.resize(green_bgr, (image.shape[1], image.shape[0]))
gray_red = cv2.resize(red_bgr, (image.shape[1], image.shape[0]))

# Escribe cada canal de color redimensionado a su tamaño original en archivos separados
cv2.imwrite("out_ocv/color_wheel_ssB.png", gray_blue)
cv2.imwrite("out_ocv/color_wheel_ssG.png", gray_green)
cv2.imwrite("out_ocv/color_wheel_ssR.png", gray_red)

# Unir las imágenes
gray = cv2.merge([gray_blue, gray_green, gray_red])  # Combina los tres canales de color en una sola imagen
cv2.imwrite("out_ocv/color_wheel_rRGB.png", gray)  # Escribe la imagen combinada en un archivo

# Diferencia entre imágenes
diff = cv2.subtract(image, gray)  # Calcula la diferencia entre la imagen original y la imagen combinada
cv2.imwrite("out_ocv/color_wheel_diff.png", diff)  # Escribe la diferencia en un archivo de salida