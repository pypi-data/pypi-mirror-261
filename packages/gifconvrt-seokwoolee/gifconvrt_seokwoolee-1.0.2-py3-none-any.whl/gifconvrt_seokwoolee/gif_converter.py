import glob
from PIL import Image

class GifConvertor:
    def __init__(self, path_in=None, path_out=None, resize=(320,240)):
        '''
        path_in : original images path (ex. images/*.png)
        path_out : result iamge path (ex. output/{filename}.gif)
        resize : resizing image size (default : 320 X 240)
        '''
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize

    def convert_gif(self):
        '''
        Execute to generate gif image file
        '''
        print(self.path_in, self.path_out, self.resize)

        image, *images = \
        [Image.open(img).resize(self.resize, Image.Resampling.LANCZOS).convert("P") for img in sorted(glob.glob(self.path_in))]

        try:
            # Save GIF
            image.save(
                fp=self.path_out, # 저장할 gif file pointer
                format='GIF', # 파일 포맷 형식
                append_images=images, # 첫번쨰 이미지 이후, append 시킬 이미지들
                save_all=True, # 모두 저장
                duration=200, # 멀티프레임 gif의 각 프레임의 표시 기간(밀리초)
                loop=0 # GIF가 루프해야 하는 정수 횟수입니다. 0은 GIF가 영원히 루프한다는 것을 의미
            )
        except IOError:
            print('Cannot Convert!', image)

if __name__ == '__main__':
    # 클래스
    c = GifConvertor('./project/images/*.png', './project/image_out/result.gif', (320, 240))

    # 변환
    c.convert_gif()