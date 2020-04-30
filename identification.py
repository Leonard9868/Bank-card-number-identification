# 查看数据集样本及其对应标签情况
%matplotlib inline

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig = plt.gcf()
fig.set_size_inches(4 * 4, 4 * 4)

for i,imgpath in enumerate(
    [os.path.join(base_dir, fname)
               for fname in base_data_fnames[:16]]
):
    sp = plt.subplot(4, 4, i+1)
    sp.axis('Off')
    img = mpimg.imread(imgpath)
    plt.title(base_data_fnames[i])
    plt.imshow(img)
