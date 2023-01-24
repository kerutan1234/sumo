#! /usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw, ImageFont
import json
import textwrap



json_open = open('./data.json', 'r')
json_load=json.load(json_open)
bc_lists=json_load


def get_concat_h_blank(im1,bc_list, color=(255, 255, 255)):
    dst = Image.new('RGB', (im1.width + 300, max(im1.height, 300)), color)
    dst.paste(im1, (300, 0))
    draw = ImageDraw.Draw(dst)
    font=ImageFont.truetype('C:/Windows/Fonts/msgothic.ttc', 30)
    font2=ImageFont.truetype('C:/Windows/Fonts/msgothic.ttc', 25)
    line_counter = 0
    wrap_list_address = textwrap.wrap(bc_list["住所"], 8)
    print(bc_list)
    for line in wrap_list_address:
        y=line_counter*35+20
        draw.multiline_text((10, y),line, fill=(0,0,0), font=font)
        line_counter = line_counter +1  # 行数のカウンターに1
    line_counter = 0
    split_fee=bc_list["価格（月額のローン支払い）"].split("円")
    del split_fee[-1]
    for line in split_fee:
        y=line_counter*35+225
        draw.multiline_text((10, y),line+"円", fill=(0,0,0), font=font2)
        line_counter = line_counter +1  # 行数のカウンターに1
    line_counter = 0
    wrap_list_time = textwrap.wrap(bc_list["築年数・入居時期"], 8)
    for line in wrap_list_time:
        y=line_counter*35+350
        draw.multiline_text((10, y),"築年数:"+line, fill=(0,0,0), font=font2)
        line_counter = line_counter +1  # 行数のカウンターに1
    line_counter = 0
    split_madori=bc_list["間取り/面積/総戸数"].split("間取り")
    for line in split_madori:
        y=line_counter*35+400
        if line_counter==1:
            draw.multiline_text((10, y),"間取り"+line, fill=(0,0,0), font=font2)
        else:
            draw.multiline_text((10, y),line, fill=(0,0,0), font=font2)
        line_counter = line_counter +1  # 行数のカウンターに1

    return dst

def get_concat_v_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
for bc_list in bc_lists:
    #print(bc_list)
    play_path = "./drawing/"+bc_list["bcid"]+".jpg"
    im1 = Image.open(play_path).copy()
    get_concat_h_blank(im1,bc_list).save('data/'+bc_list["bcid"]+'.jpg')


#get_concat_v_blank(im1, im2, (0, 64, 128)).save('data/dst/pillow_concat_v_blank.jpg')
#VISON解像度　1920:1080