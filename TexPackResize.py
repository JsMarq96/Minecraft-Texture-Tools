from PIL import Image
from DirectoryTransversal import file_search
import shutil
import png

IMAGE_TYPES = ('.png', '.jpg')

class TexPackResize:
    '''
        Texture pack resize utility by Juan S. Marquerie
        Using the PIL library, apply bicubic interpolation in order to escale,
        or downscale the directory
    '''

    def __init__(self, new_scale):
        self.scale = new_scale
    
    def change_scale(self, new_scale):
        self.scale = new_scale

    '''
        Function to scale a single image, and save it
    '''
    def image_scale(self, img_adress, result_img_adress, new_size):
        img = Image.open(img_adress).convert('RGB')
        img.resize(new_size, Image.BICUBIC).save(result_img_adress)

    '''
        Function to clone a full folder directory, in order to scale it
    '''
    def directory_clone(self, directory):
        new_dir_name =  directory + '_' + str(self.scale)
        shutil.copytree(directory, new_dir_name)
        
        return new_dir_name

    '''
        Iterate throught a directory, and scale all the images
        to the selected size
    '''
    def scale_directory(self, directory):
        images_in_directory = file_search(IMAGE_TYPES, directory)

        print('Scalling ' + str(len(images_in_directory)) + ' images...')
        for image in images_in_directory:
            print('Scalling image: ' + image)
            self.image_scale(image, image, self.scale)

    '''
        (Main function)
        Duplicates a directory and then scales it
    '''
    def resize_directory(self, directory):
        new_dir = self.directory_clone(directory)
        self.scale_directory(new_dir)


'''
    Command interface
'''
if __name__ == '__main__':
    directory = input('Enter Texpack direcction: ')
    new_dim_raw = input('Enter the new texture dimensions with format "W,H: "')

    w = int(new_dim_raw.split(',')[0])
    h = int(new_dim_raw.split(',')[1])

    scaler = TexPackResize((w,h))

    scaler.resize_directory(directory)