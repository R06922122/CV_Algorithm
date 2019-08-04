from PIL import Image, ImageDraw
import numpy as np

if __name__ == '__main__':
    
    block_size = 31
    window_size = 20
    
    ima = Image.open("trucka.bmp")
    draw = ImageDraw.Draw(ima)
    imb = Image.open("truckb.bmp")
    print(ima.format, ima.size, ima.mode)
    ima_pix = list(ima.getdata())
    ima_pix = np.array(ima_pix)
    ima_pix = np.reshape(ima_pix, (386, 386))
    imb_pix = list(imb.getdata())
    imb_pix = np.array(imb_pix)
    imb_pix = np.reshape(imb_pix, (386, 386))

    block_num = 386 // block_size
    for i in range(block_num):
        for j in range(block_num):
            start_x = block_size*i
            init_x = start_x
            start_y = block_size*j
            init_y = start_y
            step_size = 8
            
            while step_size >= 1:
                left_x, left_y = start_x, (start_y - step_size)
                right_x, right_y = start_x, (start_y + step_size)
                top_x, top_y = (start_x - step_size), start_y
                down_x, down_y = (start_x + step_size), start_y
                left_sum, right_sum, top_sum, down_sum = 999999, 999999, 999999, 999999
                min = 999999

                x1, y1, x2, y2, x3, y3, x4, y4 = start_x-step_size//2, start_y-step_size//2, start_x-step_size//2, start_y+step_size//2, start_x+step_size//2, start_y+step_size//2, start_x+step_size//2, start_y-step_size//2
                x1_sum, x2_sum, x3_sum, x4_sum = 999999, 999999, 999999, 999999
                
                
                
                start_sum = 0
                for x in range(block_size):
                    for y in range(block_size):
                        start_sum = start_sum + abs(imb_pix[start_x+x, start_y+y] - ima_pix[start_x+x, start_y+y])
                if start_sum < min:
                    min = start_sum
                    start_x, start_y = start_x, start_y
                
                if left_y >= 0:
                    left_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            left_sum = left_sum + abs(imb_pix[left_x+x, left_y+y] - ima_pix[start_x+x, start_y+y])
                if left_sum < min:
                    min = left_sum
                    start_x, start_y = left_x, left_y
                    
                if right_y+block_size-1 < 386:
                    right_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            right_sum = right_sum + abs(imb_pix[right_x+x, right_y+y] - ima_pix[start_x+x, start_y+y])
                if right_sum < min:
                    min = right_sum
                    start_x, start_y = right_x, right_y
                    
                if top_x >= 0:
                    top_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            top_sum = top_sum + abs(imb_pix[top_x+x, top_y+y] - ima_pix[start_x+x, start_y+y])
                if top_sum < min:
                    min = top_sum
                    start_x, start_y = top_x, top_y
                    
                if down_x+block_size-1 < 386:
                    down_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            down_sum = down_sum + abs(imb_pix[down_x+x, down_y+y] - ima_pix[start_x+x, start_y+y])
                if down_sum < min:
                    min = down_sum
                    start_x, start_y = down_x, down_y
                    
                    
                    
                    
                    
                
                if x1>=0 and y1>=0:
                    x1_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            x1_sum = x1_sum + abs(imb_pix[x1+x, y1+y] - ima_pix[start_x+x, start_y+y])
                if x1_sum < min:
                    min = x1_sum
                    start_x, start_y = x1, y1
                    
                if x2>=0 and y2+block_size-1<386:
                    x2_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            x2_sum = x2_sum + abs(imb_pix[x2+x, y2+y] - ima_pix[start_x+x, start_y+y])
                if x2_sum < min:
                    min = x2_sum
                    start_x, start_y = x2, y2
                    
                if x3+block_size-1<386 and y3+block_size-1<386:
                    x3_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            x3_sum = x3_sum + abs(imb_pix[x3+x, y3+y] - ima_pix[start_x+x, start_y+y])
                if x3_sum < min:
                    min = x3_sum
                    start_x, start_y = x3, y3
                    
                if x4+block_size-1<386 and y4>=0:
                    x4_sum = 0
                    for x in range(block_size):
                        for y in range(block_size):
                            x4_sum = x4_sum + abs(imb_pix[x4+x, y4+y] - ima_pix[start_x+x, start_y+y])
                if x4_sum < min:
                    min = x4_sum
                    start_x, start_y = x4, y4
                
                
                    
                    
                step_size = step_size // 2
                #print(i,j,init_x, init_y,start_x, start_y)
            #print(i,j,init_x, init_y,start_x, start_y)
            draw.line([(init_x+block_size//2, init_y+block_size//2),(start_x+block_size//2, start_y+block_size//2)])
    ima.save('sample_31.bmp')            
                
                
                
                
                
            
