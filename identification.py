# 分割原始数据样本为单数字图片并存放到相应目录
from PIL import Image
IdentificationImages_dir = './第八届中国软件杯/IdentificationImages'
for j in range(len(base_data_fnames)):
    img = Image.open(os.path.join(base_dir, base_data_fnames[j]))
    img_size = img.size
    x = 0 y = 0 w = 30 h = 46
    region1 = img.crop((x, y, w, h))
    crop1 = str(base_data_fnames[j][0]+base_data_fnames[j][4]+base_data_fnames[j][5]+
    base_data_fnames[j][6]+'0'+'_'+('%04d'% j)+base_data_fnames[j][7]+base_data_fnames[j][8]
         +base_data_fnames[j][9]+base_data_fnames[j][10])
    region1.save(os.path.join(IdentificationImages_dir,crop1))
    region2 = img.crop((x+w, y, x+2*w, h))
    crop2 = str(base_data_fnames[j][1]+base_data_fnames[j][4]+base_data_fnames[j][5]+
    base_data_fnames[j][6]+'1'+'_'+('%04d'% j)+base_data_fnames[j][7]+base_data_fnames[j][8]
         +base_data_fnames[j][9]+base_data_fnames[j][10])
    region2.save(os.path.join(IdentificationImages_dir,crop2))
    region3 = img.crop((x+2*w, y, x+3*w, h))
    crop3 = str(base_data_fnames[j][2]+base_data_fnames[j][4]+base_data_fnames[j][5]+
    base_data_fnames[j][6]+'2'+'_'+('%04d'% j)+base_data_fnames[j][7]+base_data_fnames[j][8]
         +base_data_fnames[j][9]+base_data_fnames[j][10])
    region3.save(os.path.join(IdentificationImages_dir,crop3))
    region4 = img.crop((x+3*w, y, x+4*w, h))
    crop4 = str(base_data_fnames[j][3]+base_data_fnames[j][4]+base_data_fnames[j][5]+
    base_data_fnames[j][6]+'3'+'_'+('%04d'% j)+base_data_fnames[j][7]+base_data_fnames[j][8]
         +base_data_fnames[j][9]+base_data_fnames[j][10])
    region4.save(os.path.join(IdentificationImages_dir,crop4))
