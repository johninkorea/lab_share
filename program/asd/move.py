def mv2bottom(ma):
    import numpy as np
    from pymatgen.core.structure import Structure
    import re


    # 좌표 읽기
    asd=np.array(ma)
    asd=str(asd).split("PeriodicSite: ")
    del asd[0]

    # 좌표들 정리
    data=[]
    z=0
    while z<len(asd):
        qwe = re.findall(r'-?\d+\.?\d*', asd[z])
        data.append(qwe)
        z+=1
    data=np.array(data,dtype=float)

    # 평행 이동
    data[:,5]=data[:,5]-np.min(data[:,5])

    # 새로운 구조 생성
    new=Structure(lattice=ma.lattice, species=ma.species, coords=data[:,3:])
    return new