import argparse
import cv2
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ki", help = "Relative location of kitti images directory", required=True)
    parser.add_argument("--kl", help = "Relative location of kitti labels directory", required=True)
    parser.add_argument("--out", help = "Relative location of output txt files directory", default="out")
    args = parser.parse_args()

    dic = ['Car', 'Van', 'Truck', 'Pedestrian', 'Person_sitting', 'Cyclist', 'Tram', 'Misc', 'DontCare']
    
    img_path = args.ki
    label_path_in = args.kl
    label_path_out = args.out
    
    label_files= os.listdir(label_path_in) # Get all files in label directory

    for label_file in label_files: 
        
        fin = open(label_path_in + label_file, 'r')
        fout = open(label_path_out + label_file, 'w')

        img = cv2.imread(img_path + label_file.split('.')[0] + '.png')
        
        dh = 1 / img.shape[0]
        dw = 1 / img.shape[1]

        for line in fin.readlines():
            
            obj = line.split()

            cls = dic.index(obj[0])

            x_min = float(obj[4])
            y_min = float(obj[5])
            x_max = float(obj[6])
            y_max = float(obj[7])

            x_center = (x_min + x_max) / 2 * dw
            y_center = (y_min + y_max) / 2 * dh
            width = (x_max - x_min) * dw
            height = (y_max - y_min) * dh

            fout.write("%d %f %f %f %f\n" % (cls, x_center, y_center, width, height))

        fin.close()
        fout.close()