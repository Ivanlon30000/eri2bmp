import os
import time
from concurrent.futures import ThreadPoolExecutor, wait


class Eri2Bmp:
    def __init__(self, cvter, log=None):
        if os.path.isdir(cvter):
            cvter = os.path.join(cvter, "ericvt.exe")
        if os.path.exists(cvter):
            self.cvter = cvter
        else:
            raise ValueError("Can't find 'ericvt.exe' file. Please check your path.\nDon't have 'ericvt.exe'? Download"
                             " at http://www.entis.jp/eridev/download/index.html")

        if log is None:
            self.log = "Eri2Bmp_{}.log".format(time.strftime("%Y_%m_%d_%H_%M_%S"))
        else:
            self.log = log

    @staticmethod
    def _is_eri(dir, name):
        return name[name.rindex('.') + 1:] == 'eri' and os.path.isfile(os.path.join(dir, name))

    def _wl(self, s):
        print(s)
        with open(self.log, 'a', encoding='utf8') as lf:
            lf.write(s+'\n')

    def eri2bmp(self, src, dst):
        self._wl("{} -> {}".format(src, dst))
        os.system('{} "{}" "{}"'.format(self.cvter, src, dst))

    def _eris2bmps(self, src, dst):
        for eri in os.listdir(src):
            if Eri2Bmp._is_eri(src, eri):
                self.eri2bmp(os.path.join(src, eri),
                             os.path.join(dst, "{}.bmp".format(eri[:eri.rindex('.')])))

    def eris2bmps(self, src, dst, workers=1):
        if workers > 0:
            if not os.path.exists(dst):
                os.makedirs(dst)

            if workers == 1:
                self._wl("normal mode:\n\t{} -> {}".format(src, dst))
                self._eris2bmps(src, dst)
            elif workers > 1:
                self._wl("multi-workers mode:\n\t{} workers running\n\t{} -> {}".format(workers, src, dst))
                futures = []
                pool = ThreadPoolExecutor(max_workers=workers)
                for eri in os.listdir(src):
                    if Eri2Bmp._is_eri(src, eri):
                        futures.append(pool.submit(self.eri2bmp,
                                                   *(os.path.join(src, eri),
                                                    os.path.join(dst, "{}.bmp".format(eri[:eri.rindex('.')])))))
                wait(futures)
            self._wl("done.")
        else:
            raise ValueError("param 'workers' should be greater than 0")


if __name__ == '__main__':
    src_folder = r"D:\Downloads\ev"
    dst_folder = r"D:\output\4"
    cvter = r"D:\Downloads\ericvt\ericvt.exe"

    st = time.time()
    e2b = Eri2Bmp(cvter)
    e2b.eris2bmps(src_folder, dst_folder, 4)
    et = time.time()
    print("{}s taken.".format(et-st))
