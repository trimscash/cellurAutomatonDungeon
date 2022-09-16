# 図形の描画
import pygame as pg
import sys, time

pg.init()
GAMEN = pg.display.set_mode((400, 300))
pg.display.set_caption('Hello World!')
GAMEN.fill((0, 120, 120))

pg.draw.rect(GAMEN, (255, 0, 0), (150, 50, 100, 50))
pg.draw.polygon(GAMEN, (255, 255, 0), ((0, 0), (100, 20), (30, 30), (40, 20)))
pg.draw.line(GAMEN, (255, 0, 255), (0, 50), (100, 100), 5)
pg.draw.circle(GAMEN, (0, 255, 0), (200, 200), 50, 5)
pg.draw.ellipse(GAMEN, (0, 255, 255), (300, 100, 50, 150), 3)
pixObj = pg.PixelArray(GAMEN)
for i in range(0, 100, 4):
    pixObj[100][150+i] = (255, 255, 255)
del pixObj

pg.display.update()
time.sleep(5)
pg.quit()
sys.exit()
