import importlib
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import argparse # For parsing command line arguments
import yoda as yd
import os
import sys
from rivet.plotting.make_plots import assemble_plotting_data
from yoda.plotting import script_generator
import numpy as np


parser = argparse.ArgumentParser(usage=__doc__)
parser.add_argument("YODAFILES", nargs="+", help="data files to compare")
parser.add_argument("-o", "--outputdir", dest="OUTPUTDIR",
                    default="./rivet-plots", help="directory for Web page output")
parser.add_argument("-c", "--config", dest="CONFIGFILES", action="append", default=['~/.make-plots'],
                    help="plot config file(s) to be used with rivet-cmphistos")
parser.add_argument("--ignore-missing", dest="IGNORE_MISSING", action="store_true",
                    default=False, help="ignore missing YODA files")
parser.add_argument("-i", "--ignore-unvalidated", dest="IGNORE_UNVALIDATED", action="store_true",
                    default=False, help="ignore unvalidated analyses")
# parser.add_argument("--ref", "--refid", dest="REF_ID",
#                   default=None, help="ID of reference data set (file path for non-REF data)")
parser.add_argument("--no-rivet-refs", dest="RIVETREFS", action="store_false",
                        default=True, help="don't use Rivet reference data files")
parser.add_argument("--dry-run", help="don't actually do any plotting or HTML building", dest="DRY_RUN",
                    action="store_true", default=False)
parser.add_argument("--pwd", dest="PATH_PWD", action="store_true", default=False,
                    help="append the current directory (pwd) to the analysis/data search paths (cf. $RIVET_ANALYSIS_PATH)")
parser.add_argument("--style", dest="STYLE", help="Choose the plotting style", default='default')

stygroup = parser.add_argument_group("Style options")
stygroup.add_argument("-t", "--title", dest="TITLE",
                      default="Plots from Rivet analyses", help="title to be displayed on the main web page")
stygroup.add_argument("--reflabel", dest="REFLABEL",
                      default="Data", help="legend entry for reference data")
stygroup.add_argument("--ratiolabel", dest="RATIOPLOTLABEL",
                      default=None, help="label on ratio panel")
stygroup.add_argument("--deviation", dest="DEVIATION", action="store_true",
                      default=False, help="rescale ratio panel to standard deviation (bin by bin)")
#stygroup.add_argument("--no-plottitle", dest="NOPLOTTITLE", action="store_true",
#                      default=False, help="don't show the plot title on the plot "
#                      "(useful when the plot description should only be given in a caption)")
stygroup.add_argument("-s", "--single", dest="SINGLE", action="store_true",
                      default=False, help="display plots on single webpage.")
stygroup.add_argument("--no-ratio", dest="SHOW_RATIO", action="store_false",
                     default=True, help="don't draw a ratio plot under each main plot.")
stygroup.add_argument("--no-errs", "--no-mcerrs", "--no-mc-errs", dest="MC_ERRS", action="store_false",
                      default=True, help="plot error bars.")
stygroup.add_argument("--canvastext", dest="CANVASTEXT", default=None,
                      help="Additional text to draw on the canvas")
stygroup.add_argument("--nRatioTicks", dest="NRATIOTICKS", default=1,
                      help="Modify number of minor ticks between major ticks on ratio plot.")
stygroup.add_argument("--offline", dest="OFFLINE", action="store_true",
                      default=False, help="generate HTML that does not use external URLs.")
stygroup.add_argument("-f", "--format", action="append", dest="FORMATS", default=["PDF", "PNG"],
                    help="output format string consisting of desired output formats separated by commas [default=PDF,PNG]")
stygroup.add_argument("--booklet", dest="BOOKLET", action="store_true",
                      default=False, help="create booklet (currently only available for PDF with pdftk or pdfmerge).")
stygroup.add_argument("--rmopts", "--remove-options", dest="REMOVE_OPTIONS", action="store_true", default=False,
                      help="remove options label from legend")

selgroup = parser.add_argument_group("Selective plotting")
selgroup.add_argument("-m", "--match", action="append", dest="PATHPATTERNS", default=[],
                      help="only write out histograms whose $path/$name string matches any of these regexes")
selgroup.add_argument("-M", "--unmatch", action="append", dest="PATHUNPATTERNS", default=[],
                      help="exclude histograms whose $path/$name string matches any of these regexes")
selgroup.add_argument("--ana-match", action="append", dest="ANAPATTERNS", default=[],
                      help="only write out histograms from analyses whose name matches any of these regexes (same as --match)")
selgroup.add_argument("--ana-unmatch", action="append", dest="ANAUNPATTERNS", default=[],
                      help="exclude histograms from analyses whose name matches any of these regexes (same as --unmatch)")
selgroup.add_argument("--no-weights", "--skip-weights", help="prevent multiweights from being plotted", dest="SKIP_WEIGHTS",
                    action="store_true", default=False)

vrbgroup = parser.add_argument_group("Verbosity control")
vrbgroup.add_argument("-v", "--verbose", help="add extra debug messages", dest="VERBOSE",
                      action="store_true", default=False)


pargs = parser.parse_args()

names = []
for f in pargs.YODAFILES:
    for k,_ in yd.read(f).items():
        if "[" not in k:
            names.append(k)

print(names)


# Sample data: dictionary mapping names to image paths

class ImageSelectorApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Image Selector')

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side='right', fill='both', expand=True)

        self.dropdown_var = tk.StringVar(master)
        self.dropdown_var.set(names[0])  # Set default selection
        self.dropdown_var.trace('w', self.update_image)

        self.dropdown = tk.OptionMenu(self.master, self.dropdown_var, *names)
        self.dropdown.pack(side='left', fill='x')

        self.update_image()

    def update_image(self, *args):

        tstart = time.time()
        selected_image_name = self.dropdown_var.get()
        name = selected_image_name

        # Clear previous image
        self.ax.clear()

        OUTPUTDIR=pargs.OUTPUTDIR
        if not os.path.exists(OUTPUTDIR):
            os.makedirs(OUTPUTDIR)
        # track time
        start = time.time()
        plotContents, hasVars = assemble_plotting_data(pargs.YODAFILES, pargs.PATH_PWD,pargs.RIVETREFS,name)
        stop = time.time()
        print("Time to assemble plotting data: ", stop-start, "s")
        analyses = list(set([p.split("/")[1] for p in plotContents.keys()]))
        for analysis in analyses:
            if name.startswith("/"+analysis):
                anapath = os.path.join(OUTPUTDIR, analysis)
                if os.path.exists(anapath):  continue
                os.makedirs(anapath)
        for i, (plotName, singlePlotContent) in enumerate(plotContents.items()):
            if plotName == name:
                script = OUTPUTDIR +"/"+ plotName + ".py"
                data = OUTPUTDIR +"/"+ plotName + "__data.py"
                # delete script
                for f in [script, data]:
                    if os.path.exists(f):
                        os.remove(f)
                start = time.time()
                script_generator.process(singlePlotContent, plotName, OUTPUTDIR, ["PDF"])
                stop = time.time()
                print("Time to generate scripts: ", stop-start, "s")
                # remove line "plt.close(fig)" from script file

                with open(script, "r") as f:
                    lines = f.readlines()
                with open(script, "w") as f:
                    for line in lines:
                        if "plt.close(fig)" in line:
                            continue
                        if "import" in line:
                            continue
                        #if "plt.savefig" in line:
                        #    continue
                        f.write(line)

                try:
                    # load shared imports
                    mpl = importlib.import_module("matplotlib")
                    np  = importlib.import_module("numpy")
                    sys_lib = importlib.import_module("sys")
                    os_lib  = importlib.import_module("os")
                    plt  = importlib.import_module("matplotlib.pyplot")

                    # pass imports to globals, including plot directory
                    script_globals = {'mpl': mpl, 'np': np, 'sys' : sys_lib,
                                    'plt' : plt,
                                      'os' : os_lib, '__file__': script}

                    start = time.time()
                    exec(open(script).read(), script_globals)
                    stop = time.time()
                    print("Time to execute script: ", stop-start, "s")
                except Exception as ex:
                    print("Unexpected error when executing ", script)
                    print(ex)

        
        #import io
        #import fitz
        #from PIL import Image

        #file = OUTPUTDIR +"/"+ name + ".pdf"
        #pdf_file = fitz.open(file)
        #page = pdf_file[0]
        #rgb = page.get_pixmap(dpi=300)
        #pil_image = Image.open(io.BytesIO(rgb.tobytes()))
        #plt.imshow(pil_image.convert('RGB'))
        # Copy the plot onto the new axis
        #self.ax = script_globals['ax']

        #print(script_globals['fig'])
        #script_globals['fig'].savefig("ok.pdf")
        #self.ax = script_globals['ax']
        new_fig = script_globals['fig']
        new_canvas = FigureCanvasTkAgg(new_fig, master=self.master)
        new_canvas.get_tk_widget().pack(side='right', fill='both', expand=True)
        
        # Optionally, you can delete the previous canvas
        self.canvas.get_tk_widget().pack_forget()
        self.canvas.get_tk_widget().destroy()
        self.canvas = new_canvas
        #self.canvas.fig.show()


        # Refresh canvas
        self.canvas.draw()
        tstop = time.time()
        print("Time to update image: ", tstop-tstart, "s")

def main():
    root = tk.Tk()
    app = ImageSelectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()