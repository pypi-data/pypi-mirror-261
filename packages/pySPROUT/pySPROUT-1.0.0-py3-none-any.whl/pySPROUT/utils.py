import numpy as np
########## preprocessing ###################
def pear(D,D_re):
    tmp = np.corrcoef(D.flatten(order='C'), D_re.flatten(order='C'))
    return tmp[0,1] 

def check_weight_sum_to_one(matrix):
    # check if the gene sum is
    check = False
    row = matrix.shape[0]
    if np.sum(np.sum(matrix,axis = 1)) == row:
        check = True
    return check

def check_st_coord(st_coord,st_exp):
    if st_coord.shape[1] >2:
        raise ValueError(
            f'Spatial coordinates expected two dimensional, got {st_coord.shape[1]}.')
    else:
        st_coord.columns = ['x','y']
    if st_coord.shape[0] != st_exp.shape[0]:
        raise ValueError(
            f'Accoding to spatial epxression data, spatial coordinates expected {st_exp.shape[0]} spots, got {st_coord.shape[0]}.')
    return st_coord

def check_st_sc_pair(st_exp, sc_exp):
    if len(set(st_exp.columns).intersection(set(sc_exp.columns)))<100:
        # st_exp.columns = map(lambda x: str(x).upper(), st_exp.columns)
        # sc_exp.columns = map(lambda x: str(x).upper(), sc_exp.columns)
        raise ValueError(
            f'The shared gene of ST and SC expression data is less than 1000, check if they are the same species.')
    return st_exp, sc_exp

def check_decon_type(weight, meta_df, cell_type_key):
    if len(set(weight.columns).intersection(set(meta_df[cell_type_key]))) != len(set(weight.columns)):
        raise ValueError(
            f'Cell type in weight matrix is different from single-cell meta file.')

def check_spots_match(weight, st_exp, st_coord):
    # check and adjust
    if len(set(weight.index)) != len(set(st_exp.index)):
        shared_idx = set(weight.index).intersection(set(st_exp.index))
        shared_idx = shared_idx.intersection(set(st_coord.index))
        st_coord = st_coord.loc[shared_idx]
        weight = weight.loc[shared_idx]
        st_exp = st_exp.loc[shared_idx]
        print(f'Spot index in weight matrix is different from ST expression\'s.\n Adjusted to {len(shared_idx)} shared spots.')
    return weight, st_exp, st_coord
