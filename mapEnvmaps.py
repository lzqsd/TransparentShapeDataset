import glob
import os.path as osp
import cv2
import pickle
import os


src = 'IndoorHDRDataset2018'
dst = 'Envmaps'
os.system('mkdir -p %s' % osp.join(dst, 'train') )
os.system('mkdir -p %s' % osp.join(dst, 'test') )

with open('infoList.dat', 'rb') as fIn:
    infoList = pickle.load(fIn )


imNames = glob.glob(osp.join(src, '*.exr') )
cnt = 0
for imName in imNames:
    imId = imName.split('/')[-1]
    if imId in infoList:
        cnt += 1
        print('%d %s' % (cnt, imId ) )
        im = cv2.imread(imName, -1 )
        im = cv2.resize(im, (1024, 512), interpolation = cv2.INTER_AREA )

        mode = infoList[imId ]['mode']
        name = infoList[imId ]['imId' ]
        scale = infoList[imId ]['scale' ]

        im = im * scale
        imNewName = osp.join(dst, mode, name )
        cv2.imwrite(imNewName, im )
