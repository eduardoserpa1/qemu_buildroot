#include <stdio.h>
#include <stdlib.h>

int main(){
	system("make clean -C modules/sstf-iosched-skeleton-master");
	system("make -C modules/sstf-iosched-skeleton-master");
	system("make");
	system("qemu-system-i386 --kernel output/images/bzImage --hda output/images/rootfs.ext2 --hdb sdb.bin --nographic --append 'console=ttyS0 root=/dev/sda'");
}
