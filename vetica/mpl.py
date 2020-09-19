import matplotlib
import shutil
import pkg_resources

fonts_dir = os.path.join(matplotlib.rcParams['datapath'], 'fonts/ttf')

helvetica_filename = 'Helvetica_33244fbeea10f093ae87de7a994c3697.ttf'
helvetica_dest_filename = os.path.join(fonts_dir, helvetica_filename)
helvetica_src_filename = pkg_resources.resource_filename('vetica', 'data/'+helvetica_filename)

if not os.path.exists(helvetica_dest_filename):
    shutil.copyfile(helvetica_src_filename, helvetica_dest_filename)
    matplotlib.font_manager._rebuild()

prop = matplotlib.font_manager.FontProperties(fname=helvetica_dest_filename)

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'Helvetica'

