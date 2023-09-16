import itk
import SimpleITK as sitk

def rescale_image(image_path, x_factor, y_factor, primero):
    reader = itk.ImageFileReader.New(FileName=image_path)
    try:
        reader.Update()
    except itk.ExceptionObject as err:
        print("Error: " + str(err))
        return

    img = reader.GetOutput()
    inputSize = img.GetLargestPossibleRegion().GetSize()

    outputSize = itk.Size[2]()
    outputSize[0] = int(inputSize[0] * float(x_factor))
    outputSize[1] = int(inputSize[1] * float(y_factor))

    outputSpacing = itk.Vector[itk.D, 2]()
    outputSpacing[0] = img.GetSpacing()[0] * (float(inputSize[0]) / float(outputSize[0]))
    outputSpacing[1] = img.GetSpacing()[1] * (float(inputSize[1]) / float(outputSize[1]))

    resampleFilter = itk.ResampleImageFilter.New(Input=img)
    resampleFilter.SetSize(outputSize)
    resampleFilter.SetOutputSpacing(outputSpacing)
    resampleFilter.UpdateLargestPossibleRegion()

    basename = image_path.split('.')[0]
    if "R" in basename:
        channel = "sR"
    elif "G" in basename:
        channel = "sG"
    elif "B" in basename:
        channel = "sB"
    else:
        channel = "scaled"

    if primero:
        writer = itk.ImageFileWriter.New(Input=resampleFilter.GetOutput(),
                                         FileName="out_itk/color_wheel" + "_" + channel + ".png")
    else:
        writer = itk.ImageFileWriter.New(Input=resampleFilter.GetOutput(),
                                         FileName="out_itk/color_wheel" + "_s" + channel + ".png")

    try:
        writer.Update()
    except itk.ExceptionObject as err:
        print("Error: " + str(err))
        return


# end def


image = itk.imread("color_wheel.jpg")

red_filter = itk.VectorIndexSelectionCastImageFilter.New(image,
                                                         Index=0)  # Crea un filtro para seleccionar el canal rojo de la imagen
green_filter = itk.VectorIndexSelectionCastImageFilter.New(image,
                                                           Index=1)  # Crea un filtro para seleccionar el canal verde de la imagen
blue_filter = itk.VectorIndexSelectionCastImageFilter.New(image,
                                                          Index=2)  # Crea un filtro para seleccionar el canal azul de la imagen

red = red_filter.GetOutput()  # Obtiene el canal rojo de la imagen utilizando el filtro
green = green_filter.GetOutput()  # Obtiene el canal verde de la imagen utilizando el filtro
blue = blue_filter.GetOutput()  # Obtiene el canal azul de la imagen utilizando el filtro

itk.imwrite(red, "out_itk/color_wheel_R.png")
itk.imwrite(green, "out_itk/color_wheel_G.png")
itk.imwrite(blue, "out_itk/color_wheel_B.png")

rescale_image("out_itk/color_wheel_R.png", 0.75, 0.75, True)
rescale_image("out_itk/color_wheel_G.png", 0.5, 0.5, True)
rescale_image("out_itk/color_wheel_B.png", 0.25, 0.25, True)

# Reedimensionar imágenes al tamaño de la imagen original
rescale_image("out_itk/color_wheel_sR.png", 2000 / 1500, 2000 / 1500, False)
rescale_image("out_itk/color_wheel_sG.png", 2.0, 2.0, False)
rescale_image("out_itk/color_wheel_sB.png", 4.0, 4.0, False)

red_rescaled = itk.imread("out_itk/color_wheel_ssR.png")
green_rescaled = itk.imread("out_itk/color_wheel_ssG.png")
blue_rescaled = itk.imread("out_itk/color_wheel_ssB.png")

rgb = itk.ComposeImageFilter.New(red_rescaled, green_rescaled, blue_rescaled)
itk.imwrite(rgb, "out_itk/color_wheel_rRGB.png")


# Diferencia entre imágenes
image1 = itk.imread("color_wheel.jpg", itk.UC)# Lee una imagen llamada "color_wheel.jpg" y la almacena en una variable
image2 = itk.imread("out_itk/color_wheel_rRGB.png", itk.UC)# Lee una imagen llamada "color_wheel_rRGB" y la almacena en una variable
image2.SetSpacing(image1.GetSpacing())#Igualar el espacion entre pixeles de la segunda imagen a la primera
subtract = itk.SubtractImageFilter(image1, image2)#Realizar la diferencia
itk.imwrite(subtract, "out_itk/color_wheel_diff.png")# Escribe la diferencia en un archivo de salida

"""
# Diferencia entre imágenes con SimpleITK
image1 = sitk.ReadImage("color_wheel.jpg")
image2 = sitk.ReadImage("out_itk/color_wheel_rRGB.png")
image2.SetSpacing(image1.GetSpacing())
subtracted_image = sitk.Subtract(image1, image2)
sitk.WriteImage(subtracted_image, "out_itk/color_wheel_diff_sitk.png")"""
