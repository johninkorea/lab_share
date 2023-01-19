def slabgen(ma, miller_index, min_slab_size, min_vacuum_size):
    from pymatgen.core.surface import SlabGenerator
    # ma.add_oxidation_state_by_element({'Cu':2, 'Si':2, 'O':-2})
    slabgen=SlabGenerator(ma,
                        miller_index=miller_index,
                        min_slab_size=min_slab_size,
                        min_vacuum_size=min_vacuum_size,
                        center_slab=1,
                        lll_reduce=1 # 직교를 만들어줌
                        )
    slabs=slabgen.get_slabs()
    print("# of generated structure: ",len(slabs))
    print("# of structure\t\tpolar\t\tsysmmetric")
    print("-"*50)
    for n, slab in enumerate(slabs):
        print(f"        {n}               {slab.is_polar()}             {slab.is_symmetric()}")
        print("-"*50)

    ## choose cell if ther have many results
    if len(slabs)==1:
        qwe=[0]
    else:
        qwe=list(map(int,input("choose structures: ").split( )))
    return slabs, qwe