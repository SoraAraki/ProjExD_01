import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img02 = pg.transform.flip(bg_img,True,False) 
    kk_img01 = pg.image.load("ex01/fig/3.png")
    kk_img01 = pg.transform.flip(pg.image.load("ex01/fig/3.png"),True,False)
    kk_img02 = pg.transform.rotozoom(kk_img01,3,1.0)
    kk_img03 = pg.transform.rotozoom(kk_img01,10,1.0) 
    kk_img04 = pg.transform.rotozoom(kk_img01,20,1.0)
    kk_img05 = pg.transform.rotozoom(kk_img01,25,1.0)
    kk_img06 = pg.transform.rotozoom(kk_img01,20,1.0) 
    kk_img07 = pg.transform.rotozoom(kk_img01,10,1.0) 
    kk_img08 = pg.transform.rotozoom(kk_img01,3,1.0)



    kk_imgs = [kk_img01,kk_img02,kk_img03,kk_img04,kk_img05,kk_img06,kk_img07,kk_img08] 
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img,[1600-tmr,0])
        screen.blit(kk_imgs[tmr%400//50],[300,200])

        pg.display.update()
        tmr += 1        
        clock.tick(400)

        if tmr == 3200:
            tmr = 0

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()