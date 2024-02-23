import Image_Cropping
import Marging_Adding
import Pdf_Creation
import cv2
import os
import sys
def main() :
    args = sys.argv
    image = args[1]
    image_cropped_path="cropped" + image 
    pdf_path =  image[0:image.find('.')]   +   "pdf.pdf"
    cropped_image = Image_Cropping.crop_document(image)
    cropped_image_margin=Marging_Adding.add_margin_to_photo_frame(cropped_image)
    cv2.imwrite(image_cropped_path, cropped_image_margin)
    Pdf_Creation.create_pdf(image_cropped_path, pdf_path)
    os.remove(image_cropped_path)

main()