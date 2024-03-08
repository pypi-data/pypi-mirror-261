import os
import argparse
import pandas as pd
import multiprocessing as mp


def subset_df(file_in, rows_to_keep, cols_to_keep, sep_symbol, row_name_pos, column_name_pos, file_out):

    df = pd.read_csv(file_in, sep=sep_symbol, header=column_name_pos, index_col=row_name_pos)

    if len(rows_to_keep) == 0:
        if len(cols_to_keep) == 0:
            subset_df = df.loc[:, :]
        else:
            subset_df = df.loc[:, cols_to_keep]
    else:
        if len(cols_to_keep) == 0:
            subset_df = df.loc[rows_to_keep, :]
        else:
            subset_df = df.loc[rows_to_keep, cols_to_keep]

    subset_df.to_csv(file_out, sep=sep_symbol)


PhyloBiAssoc_usage = '''
=========================== PhyloBiAssoc example commands ===========================

BioSAK PhyloBiAssoc -i demo.tre -d demo.txt -o op_dir -t 10 -f

# Note, header for the first two columns in -d has to be "ID" and "cate"!!!

# It will perform:
# 1) binaryPGLMM test if phylosig p-value <= 0.05 (significant phylogenetic signal)
# 2) chi-squared test if phylosig p-value > 0.05  (no phylogenetic signal)
# 3) do nothing if phylosig returns NaN (might due to the same value across all genomes)

# https://www.rdocumentation.org/packages/ape/versions/5.7-1/topics/binaryPGLMM

=====================================================================================
'''


def PhyloBiAssoc(args):

    tree_file           = args['i']
    data_file           = args['d']
    op_dir              = args['o']
    num_threads         = args['t']
    force_create_op_dir = args['f']

    pwd_current_script  = os.path.realpath(__file__)
    current_script_path = '/'.join(pwd_current_script.split('/')[:-1])
    PhyloBiAssoc_R      = '%s/PhyloBiAssoc.R' % current_script_path

    cmd_txt             = '%s/cmds.txt'             % op_dir
    df_subset_dir       = '%s/df_subset'            % op_dir
    stats_op_dir        = '%s/stats_results'        % op_dir
    combined_stats_txt  = '%s/stats_results.txt'    % op_dir

    # create op_dir
    if os.path.isdir(op_dir) is True:
        if force_create_op_dir is True:
            os.system('rm -r %s' % op_dir)
        else:
            print('output directory exist, program exited!')
            exit()
    os.system('mkdir %s' % op_dir)
    os.system('mkdir %s' % df_subset_dir)
    os.system('mkdir %s' % stats_op_dir)

    # read in dataframe
    df = pd.read_csv(data_file, sep='\t', header=0, index_col=0)
    col_header_list = list(df.columns.values)

    subset_dict = dict()
    for each_col in col_header_list[1:]:
        subset_dict[each_col] = ['cate', each_col]

    # subset dataframe
    cmd_txt_handle = open(cmd_txt, 'w')
    stats_cmd_list = []
    op_stats_txt_set = set()
    for each_subset in subset_dict:
        cols_to_keep   = subset_dict[each_subset]
        df_subset_file = '%s/%s.txt' % (df_subset_dir, each_subset)
        stats_out_txt  = '%s/%s_stats.txt' % (stats_op_dir, each_subset)
        subset_df(data_file, set(), cols_to_keep, '\t', 0, 0, df_subset_file)
        stats_cmd = 'Rscript %s -t %s -d %s > %s' % (PhyloBiAssoc_R, tree_file, df_subset_file, stats_out_txt)
        cmd_txt_handle.write(stats_cmd + '\n')
        stats_cmd_list.append(stats_cmd)
        op_stats_txt_set.add(stats_out_txt)
    cmd_txt_handle.close()

    print('Processing %s objects with %s cores' % (len(stats_cmd_list), num_threads))
    pool = mp.Pool(processes=num_threads)
    pool.map(os.system, stats_cmd_list)
    pool.close()
    pool.join()

    # combine stats results
    combined_stats_txt_handle = open(combined_stats_txt, 'w')
    combined_stats_txt_handle.write('ID	phylosig	binaryPGLMM	chisq.test	coefficient	significance\n')
    for each_file in sorted(list(op_stats_txt_set)):
        for each_line in open(each_file):
            if not each_line.startswith('ID\tphylosig\tbinaryPGLMM\tchisq.test\tcoefficient\tsignificance'):
                combined_stats_txt_handle.write(each_line)
    combined_stats_txt_handle.close()

    # Final report
    print('Results exported to %s' % combined_stats_txt)
    print('Done')


if __name__ == "__main__":

    PhyloBiAssoc_parser = argparse.ArgumentParser(usage=PhyloBiAssoc_usage)
    PhyloBiAssoc_parser.add_argument('-i', required=True,                       help='tree file')
    PhyloBiAssoc_parser.add_argument('-d', required=True,                       help='data file')
    PhyloBiAssoc_parser.add_argument('-o', required=True,                       help='output directory')
    PhyloBiAssoc_parser.add_argument('-t', required=False, type=int, default=1, help='number of threads, default: 1')
    PhyloBiAssoc_parser.add_argument('-f', required=False, action="store_true", help='force overwrite')
    args = vars(PhyloBiAssoc_parser.parse_args())
    PhyloBiAssoc(args)
