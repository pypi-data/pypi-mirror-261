import os
import glob
from statsmodels.stats.multitest import multipletests


def sep_path_basename_ext(file_in):
    f_path, file_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(file_name)
    return f_path, f_base, f_ext


########################################################################################################################

combined_stats_txt          = '/Users/songweizhi/Documents/Research/Sponge/12_PhyloBiAssoc_wd/op_dir/combined_stats_demo.txt'
combined_stats_txt_adjusted = '/Users/songweizhi/Documents/Research/Sponge/12_PhyloBiAssoc_wd/op_dir/combined_stats_demo_adjusted.txt'

########################################################################################################################

file_re = '/Users/songweizhi/Documents/Research/Sponge/12_PhyloBiAssoc_wd/op_dir/stats_results/*.txt'
file_list = glob.glob(file_re)

# combine stats results
sig_list_id = []
sig_list_value = []
combined_stats_txt_handle = open(combined_stats_txt, 'w')
combined_stats_txt_handle.write('ID	phylosig	binaryPGLMM	chisq.test	coefficient	significance\n')
for each_file in sorted(file_list):
    f_path, f_base, f_ext = sep_path_basename_ext(each_file)
    for each_line in open(each_file):
        if not each_line.startswith('ID\tphylosig\tbinaryPGLMM\tchisq.test\tcoefficient'):
            each_line_split = each_line.strip().split('\t')
            significance = each_line_split[5]
            combined_stats_txt_handle.write('%s\t%s\n' % (f_base, '\t'.join(each_line_split[1:])))
            if significance == 'y':
                sig_bi = each_line_split[2]
                sig_chi = each_line_split[3]
                current_sig = ''
                if sig_bi == 'na':
                    current_sig = sig_chi
                elif sig_chi == 'na':
                    current_sig = sig_bi
                sig_list_id.append(f_base)
                sig_list_value.append(float(current_sig))
combined_stats_txt_handle.close()


# perform Bonferroni correction
sig_list_value_adjusted = list(multipletests(sig_list_value, alpha=0.1, method='bonferroni')[1])

# write out adjusted p values
combined_stats_txt_adjusted_handle = open(combined_stats_txt_adjusted, 'w')
combined_stats_txt_adjusted_handle.write('ID\tadjusted_p_value\n')
for (id, adjusted_p) in zip(sig_list_id, sig_list_value_adjusted):
    if adjusted_p <= 0.05:
        combined_stats_txt_adjusted_handle.write('%s\t%s\n' % (id, adjusted_p))
combined_stats_txt_adjusted_handle.close()
