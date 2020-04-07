import os

count = 2
for i in range(count):
    print("we are in mounting step" + str(i))
    os.system('rbd create data' + str(i) + ' --size 1024 --pool test1 --image-feature layering')
    os.system('rbd map data' + str(i) + ' --pool test1 --id admin')
    os.system('mkdir /mnt/rbd' + str(i))
    os.system('mkfs.xfs /dev/rbd' + str(i))
    os.system('mount -o noatime /dev/rbd' + str(i) + ' /mnt/rbd' + str(i))

'''for i in range(count):
    os.system('rbd map data' + str(i) + ' --pool test1 --id admin')

for i in range(count):
    os.system('mkdir /mnt/rbd' + str(i))

for i in range(count):
    os.system('mkfs.xfs /dev/rbd' + str(i))

for i in range(count):
    os.system('mount -o noatime /dev/rbd'+ str(i) +' /mnt/rbd' + str(i))
'''

for i in range(count):
    print("we are in unmounting step" + str(i))
    os.system('umount /mnt/rbd' + str(i))
    os.system('rbd unmap /dev/rbd' + str(i))
    os.system('rbd rm data' + str(i) + ' -p test1')
    os.system('rmdir /mnt/rbd' + str(i))
''' 
for i in range(count):
    os.system('rbd unmap /dev/rbd' + str(i))

for i in range(count):
    os.system('rbd rm data' + str(i) + ' -p test1')

for i in range(count):
    print("we are in step" + str(i))
    os.system('rmdir /mnt/rbd' + str(i))

'''
