#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pickletools import read_string4
import sys
import os
import statistics


if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        print("ログを保存したディレクトリを指定してください。")
        sys.exit(1)

    logdir = sys.argv[1]

    if os.path.exists(logdir):
        logbase = os.path.basename(logdir)
        dirname_sp = logbase.split("_")
        if len(dirname_sp) == 5:
            address = dirname_sp[1]
            minsize = dirname_sp[2]
            maxsize = dirname_sp[3]
            stepsize = dirname_sp[4]

            filelist = os.listdir(path=logdir)
            resultlist = {}
            for fname in filelist:
                fname_sp = fname.split("_")
                if len(fname_sp) == 6:
                    #address = fname_sp[1]
                    #minsize = fname_sp[2]
                    #maxsize = fname_sp[3]
                    #stepsize = fname_sp[4]
                    datasize = int(fname_sp[5].split(".")[0])

                    jitterlist = []
                    max_jitter = -10000000.0
                    min_jitter = 10000000.0

                    with open(os.path.join(logdir, fname), encoding='utf16') as fr:
                        slist = fr.readlines()
                        for s in slist:
                            if "ms TTL=" in s:
                                s1 = s.split("ms TTL=")[0]
                                jitter = float(s1.split("=")[-1])
                                if jitter > max_jitter:
                                    max_jitter = jitter
                                if jitter < min_jitter:
                                    min_jitter = jitter
                                jitterlist.append(jitter)

                    mean = statistics.mean(jitterlist)

                    resultlist[datasize] = {
                        "max": max_jitter, "min": min_jitter, "mean": mean, "list": jitterlist}

            result_file = "result_"+address+"_"+maxsize+"_"+stepsize+".txt"

            jitterlistsize = 10000000
            with open(result_file, mode='w') as fw:
                fw.write("DATASIZE, MAX, MIN, MEAN\n")
                for datasize, data in sorted(resultlist.items()):
                    max_jitter = data["max"]
                    min_jitter = data["min"]
                    mean_jitter = data["mean"]

                    fw.write(str(datasize)+", "+str(max_jitter) +
                             ", "+str(min_jitter)+", "+str(mean_jitter)+"\n")

                    jitterlist = data["list"]

                    if jitterlistsize > len(jitterlist):
                        jitterlistsize = len(jitterlist)

                        #print(k, i)

            data_file = "result_"+address+"_"+maxsize + \
                        "_"+stepsize+"_datalist"+".txt"
            with open(data_file, mode='w') as fw_data:
                fw_data.write(" , ")
                for datasize, data in sorted(resultlist.items()):
                    fw_data.write(str(datasize)+", ")
                fw_data.write("\n")
                for i in range(0, jitterlistsize):
                    for datasize, data in sorted(resultlist.items()):
                        fw_data.write(str(jitterlist[i])+", ")

                    fw_data.write("\n")

                print(result_file+" に出力しました")

        else:
            print(logbase+" のフォルダ名は不正です")

    else:
        print(logdir+" は存在しません")
        sys.exit(1)
