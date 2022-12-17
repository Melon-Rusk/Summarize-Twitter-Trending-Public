import math
import cv2
import numpy as np

def get_image_file(heading,text, file_name, folder):
    split_text = text.split(" ")
    lines = []
    len_text =int(len(text)*5/25) 
    # no_line = math.ceil(len(text)/len_text)
    len_line = 50
    s= 0
    line = ''
    temp_text = split_text
    for t1 in temp_text:
        print(t1)
        s = s +1
        if len(line)+len(t1)<len_line and s < len(split_text):
            line = line+" "+t1
        elif len(line)+len(t1)<len_line and s == len(split_text):
            line = line+" "+t1
            lines.append(line)
        elif len(line)+len(t1)>=len_line and s == len(split_text):
            lines.append(t1)
            pass
        else:
            lines.append(line)
            print(lines)
            line = t1
        # s = s +1
    # print(i)
    lines[0] = lines[0][1:]
    lines = [line.center(len(line)) for line in lines]
    max_len = max([len(line) for line in lines])
    heading = heading[:25].title()+"..."
    # Create an image with a white background and black text
    image = np.zeros((900, 1600, 3), dtype="uint8")
    image[:,:] = (248, 196, 113)  # orange background
    head_color = (61, 153, 112)  
    # text_color = (75, 86, 210) # white text
    text_color = (236, 112, 99)
    line_color = (0,0,0)
    # Add the text to the image using middle and center alignment
    cv2.putText(image, heading, (200, 55), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, head_color, 2, cv2.LINE_AA)
    cv2.putText(image, '-'*10, (200, 75), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, line_color, 2, cv2.LINE_AA)
    for i, line in enumerate(lines):
        cv2.putText(image, line, (25, (i * 30)+120), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, text_color, 1, cv2.LINE_AA)

    # Save the image file
    image_path = f"{folder}/image_files/image_{file_name}.png"
    cv2.imwrite(image_path, image)
    return image_path

if __name__ == "__main__":
    heading = "test text"
    text = "test code, to test the complete process of audio video creation using python"
    file_name  = 'delete'
    folder = 'store_data'
    get_image_file(heading,text, file_name, folder)
