import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import nametofont
import matplotlib
#matplotlib.use('TkAgg')
matplotlib.use('Agg')
import ctypes
import ast
import matplotlib.pyplot as plt
import sys
import io
import traceback
import spacr

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except AttributeError:
    pass

from .logger import log_function_call

def safe_literal_eval(value):
    try:
        # First, try to evaluate as a literal
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        # If it fails, return the value as it is (a string)
        return value

def disable_interactivity(fig):
    if hasattr(fig.canvas, 'toolbar'):
        fig.canvas.toolbar.pack_forget()

    event_handlers = fig.canvas.callbacks.callbacks
    for event, handlers in list(event_handlers.items()):
        for handler_id in list(handlers.keys()):
            fig.canvas.mpl_disconnect(handler_id)

def set_default_font(app, font_name="Arial Bold", size=10):
    default_font = nametofont("TkDefaultFont")
    text_font = nametofont("TkTextFont")
    fixed_font = nametofont("TkFixedFont")
    
    # Set the family to Open Sans and size as desired
    for font in (default_font, text_font, fixed_font):
        font.config(family=font_name, size=size)

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, bg='#333333', **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(style='TFrame')  # Ensure this uses the styled frame from dark mode
        
        canvas = tk.Canvas(self, bg=bg)  # Set canvas background to match dark mode
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        
        self.scrollable_frame = ttk.Frame(canvas, style='TFrame')  # Ensure it uses the styled frame
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

def check_mask_gui_settings(vars_dict):
    settings = {}
    for key, var in vars_dict.items():
        value = var.get()
        
        # Handle conversion for specific types if necessary
        if key in ['channels', 'timelapse_frame_limits']:  # Assuming these should be lists
            try:
                # Convert string representation of a list into an actual list
                settings[key] = eval(value)
            except:
                messagebox.showerror("Error", f"Invalid format for {key}. Please enter a valid list.")
                return
        elif key in ['nucleus_channel', 'cell_channel', 'pathogen_channel', 'examples_to_plot', 'batch_size', 'timelapse_memory', 'workers', 'fps', 'magnification']:  # Assuming these should be integers
            try:
                settings[key] = int(value) if value else None
            except ValueError:
                messagebox.showerror("Error", f"Invalid number for {key}.")
                return
        elif key in ['nucleus_background', 'cell_background', 'pathogen_background', 'nucleus_Signal_to_noise', 'cell_Signal_to_noise', 'pathogen_Signal_to_noise', 'nucleus_CP_prob', 'cell_CP_prob', 'pathogen_CP_prob', 'lower_quantile']:  # Assuming these should be floats
            try:
                settings[key] = float(value) if value else None
            except ValueError:
                messagebox.showerror("Error", f"Invalid number for {key}.")
                return
        else:
            settings[key] = value
    return settings

def check_measure_gui_settings_v1(vars_dict):
    settings = {}
    for key, var in vars_dict.items():
        value = var.get()  # This retrieves the string representation for entries or the actual value for checkboxes and combos

        try:
            # Special handling for 'channels' to convert into a list of integers
            if key == 'channels':
                settings[key] = [int(chan) for chan in eval(value)] if value else []
                
            elif key == 'png_size':
                temp_val = ast.literal_eval(value) if value else []
                settings[key] = [list(map(int, dim)) for dim in temp_val] if temp_val else None

            elif key in ['cell_loc', 'pathogen_loc', 'treatment_loc']:
                settings[key] = ast.literal_eval(value) if value else None

            elif key == 'dialate_png_ratios':
                settings[key] = [float(num) for num in eval(value)] if value else None

            elif key in ['pathogens', 'treatments', 'cells', 'crop_mode']:
                settings[key] = eval(value) if value else None

            elif key == 'timelapse_objects':
                # Ensure it's a list of strings
                settings[key] = eval(value) if value else []

            # Handling for keys that should be treated as strings directly
            elif key in ['normalize_by', 'experiment', 'measurement']:
                settings[key] = str(value) if value else None

            # Handling for single values that are not strings (int, float, bool)
            elif key in ['cell_mask_dim', 'cell_min_size', 'nucleus_mask_dim', 'nucleus_min_size', 'pathogen_mask_dim', 'pathogen_min_size', 'cytoplasm_min_size', 'max_workers', 'channel_of_interest', 'nr_imgs']:
                settings[key] = int(value) if value else None

            elif key == 'um_per_pixel':
                settings[key] = float(value) if value else None

            # Direct handling of boolean values based on checkboxes
            elif key in ['save_png', 'use_bounding_box', 'save_measurements', 'plot', 'plot_filtration', 'include_uninfected', 'dialate_pngs', 'timelapse', 'representative_images']:
                settings[key] = bool(value)

            else:
                settings[key] = value

        except SyntaxError as e:
            messagebox.showerror("Error", f"Syntax error processing {key}: {str(e)}")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Error processing {key}: {str(e)}")
            return None

    return settings

def check_measure_gui_settings(vars_dict):
    settings = {}
    for key, var in vars_dict.items():
        value = var.get()  # This retrieves the string representation for entries or the actual value for checkboxes and combos

        try:
            if key == 'channels' or key == 'png_dims':
                # Converts string representation to a list of integers
                settings[key] = [int(chan) for chan in ast.literal_eval(value)] if value else []
                
            elif key in ['cell_loc', 'pathogen_loc', 'treatment_loc']:
                settings[key] = ast.literal_eval(value) if value else None
                
            elif key == 'dialate_png_ratios':
                settings[key] = [float(num) for num in eval(value)] if value else None

            elif key == 'normalize':
                # Converts 'normalize' into a list of two integers
                settings[key] = [int(num) for num in ast.literal_eval(value)] if value else None

            elif key == 'normalize_by':
                # 'normalize_by' is a string, so directly assign the value
                settings[key] = value

            elif key == 'png_size':
                # Converts string representation into a list of lists of integers
                temp_val = ast.literal_eval(value) if value else []
                settings[key] = [list(map(int, dim)) for dim in temp_val] if temp_val else None

            # Handling for other keys as in your original function...
            
            elif key in ['pathogens', 'treatments', 'cells', 'crop_mode', 'timelapse_objects']:
                # Ensuring these are evaluated correctly as lists or other structures
                settings[key] = ast.literal_eval(value) if value else None

            elif key == 'timelapse_objects':
                # Ensure it's a list of strings
                settings[key] = eval(value) if value else []

            # Handling for keys that should be treated as strings directly
            elif key in ['normalize_by', 'experiment', 'measurement', 'input_folder']:
                settings[key] = str(value) if value else None

            # Handling for single values that are not strings (int, float, bool)
            elif key in ['cell_mask_dim', 'cell_min_size', 'nucleus_mask_dim', 'nucleus_min_size', 'pathogen_mask_dim', 'pathogen_min_size', 'cytoplasm_min_size', 'max_workers', 'channel_of_interest', 'nr_imgs']:
                settings[key] = int(value) if value else None

            elif key == 'um_per_pixel':
                settings[key] = float(value) if value else None

            # Direct handling of boolean values based on checkboxes
            elif key in ['save_png', 'use_bounding_box', 'save_measurements', 'plot', 'plot_filtration', 'include_uninfected', 'dialate_pngs', 'timelapse', 'representative_images']:
                settings[key] = bool(value)

        except SyntaxError as e:
            messagebox.showerror("Error", f"Syntax error processing {key}: {str(e)}")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Error processing {key}: {str(e)}")
            return None

    return settings

def measure_variables():
    variables = {
        'input_folder':('entry', None, '/mnt/data/CellVoyager/40x/einar/mitotrackerHeLaToxoDsRed_20240224_123156/test_gui/merged'),
        'channels': ('combo', ['[0,1,2,3]','[0,1,2]','[0,1]','[0]'], '[0,1,2,3]'),
        'cell_mask_dim':('entry', None, 4),
        'cell_min_size':('entry', None, 0),
        'nucleus_mask_dim':('entry', None, 5),
        'nucleus_min_size':('entry', None, 0),
        'pathogen_mask_dim':('entry', None, 6),
        'pathogen_min_size':('entry', None, 0),
        'cytoplasm_min_size':('entry', None, 0),
        'save_png':('check', None, True),
        'crop_mode':('entry', None, '["cell"]'),
        'use_bounding_box':('check', None, True),
        'png_size': ('entry', None, '[[224,224]]'), 
        'normalize':('entry', None, '[2,98]'),
        'png_dims':('entry', None, '[1,2,3]'),
        'normalize_by':('combo', ['fov', 'png'], 'png'),
        'save_measurements':('check', None, True),
        'representative_images':('check', None, True),
        'plot':('check', None, True),
        'plot_filtration':('check', None, True),
        'include_uninfected':('check', None, True),
        'dialate_pngs':('check', None, False),
        'dialate_png_ratios':('entry', None, '[0.2]'),
        'timelapse':('check', None, False),
        'timelapse_objects':('combo', ['["cell"]', '["nucleus"]', '["pathogen"]', '["cytoplasm"]'], '["cell"]'),
        'max_workers':('entry', None, 30),
        'experiment':('entry', None, 'experiment name'),
        'cells':('entry', None, ['HeLa']),
        'cell_loc': ('entry', None, '[["c1","c2"], ["c3","c4"]]'),
        'pathogens':('entry', None, '["wt","mutant"]'),
        'pathogen_loc': ('entry', None, '[["c1","c2"], ["c3","c4"]]'),
        'treatments': ('entry', None, '["cm","lovastatin_20uM"]'),
        'treatment_loc': ('entry', None, '[["c1","c2"], ["c3","c4"]]'),
        'channel_of_interest':('entry', None, 3),
        'measurement':('entry', None, 'mean_intensity'),
        'nr_imgs':('entry', None, 32),
        'um_per_pixel':('entry', None, 0.1)
    }
    return variables
    

@log_function_call
def create_input_field(frame, label_text, row, var_type='entry', options=None, default_value=None):
    label = ttk.Label(frame, text=label_text, style='TLabel')  # Assuming you have a dark mode style for labels too
    label.grid(column=0, row=row, sticky=tk.W, padx=5, pady=5)
    
    if var_type == 'entry':
        var = tk.StringVar(value=default_value)  # Set default value
        entry = ttk.Entry(frame, textvariable=var, style='TEntry')  # Assuming you have a dark mode style for entries
        entry.grid(column=1, row=row, sticky=tk.EW, padx=5)
    elif var_type == 'check':
        var = tk.BooleanVar(value=default_value)  # Set default value (True/False)
        # Use the custom style for Checkbutton
        check = ttk.Checkbutton(frame, variable=var, style='Dark.TCheckbutton')
        check.grid(column=1, row=row, sticky=tk.W, padx=5)
    elif var_type == 'combo':
        var = tk.StringVar(value=default_value)  # Set default value
        combo = ttk.Combobox(frame, textvariable=var, values=options, style='TCombobox')  # Assuming you have a dark mode style for comboboxes
        combo.grid(column=1, row=row, sticky=tk.EW, padx=5)
        if default_value:
            combo.set(default_value)
    else:
        var = None  # Placeholder in case of an undefined var_type
    
    return var

def add_measure_gui_defaults(settings):
    settings['compartments'] = ['pathogen', 'cytoplasm']
    return settings
    
def mask_variables():
    variables = {
        'src': ('entry', None, '/mnt/data/CellVoyager/40x/einar/mitotrackerHeLaToxoDsRed_20240224_123156/test_gui'),
        'metadata_type': ('combo', ['cellvoyager', 'cq1', 'nikon', 'zeis', 'custom'], 'cellvoyager'),
        'custom_regex': ('entry', None, None),
        'experiment': ('entry', None, 'exp'),
        'channels': ('combo', ['[0,1,2,3]','[0,1,2]','[0,1]','[0]'], '[0,1,2,3]'),
        'magnification': ('combo', [20, 40, 60,], 40),
        'nucleus_channel': ('combo', [0,1,2,3, None], 0),
        'nucleus_background': ('entry', None, 100),
        'nucleus_Signal_to_noise': ('entry', None, 5),
        'nucleus_CP_prob': ('entry', None, 0),
        'cell_channel': ('combo', [0,1,2,3, None], 3),
        'cell_background': ('entry', None, 100),
        'cell_Signal_to_noise': ('entry', None, 5),
        'cell_CP_prob': ('entry', None, 0),
        'pathogen_channel': ('combo', [0,1,2,3, None], 2),
        'pathogen_background': ('entry', None, 100),
        'pathogen_Signal_to_noise': ('entry', None, 3),
        'pathogen_CP_prob': ('entry', None, 0),
        #'preprocess': ('check', None, True),
        #'masks': ('check', None, True),
        #'examples_to_plot': ('entry', None, 1),
        #'randomize': ('check', None, True),
        'batch_size': ('entry', None, 50),
        'timelapse': ('check', None, False),
        'timelapse_displacement': ('entry', None, None),
        'timelapse_memory': ('entry', None, 0),
        'timelapse_frame_limits': ('entry', None, '[0,1000]'),
        'timelapse_remove_transient': ('check', None, True),
        'timelapse_mode': ('combo',  ['trackpy', 'btrack'], 'trackpy'),
        'timelapse_objects': ('combo', ['cell','nucleus','pathogen','cytoplasm', None], None),
        #'fps': ('entry', None, 2),
        #'remove_background': ('check', None, True),
        'lower_quantile': ('entry', None, 0.01),
        #'merge': ('check', None, False),
        #'normalize_plots': ('check', None, True),
        #'all_to_mip': ('check', None, False),
        #'pick_slice': ('check', None, False),
        #'skip_mode': ('entry', None, None),
        'save': ('check', None, True),
        'plot': ('check', None, True),
        'workers': ('entry', None, 30),
        'verbose': ('check', None, True),
    }
    return variables

def add_mask_gui_defaults(settings):
    settings['remove_background'] = True
    settings['fps'] = 2
    settings['all_to_mip'] = False
    settings['pick_slice'] = False
    settings['merge'] = False
    settings['skip_mode'] = ''
    settings['verbose'] = False
    settings['normalize_plots'] = True
    settings['randomize'] = True
    settings['preprocess'] = True
    settings['masks'] = True
    settings['examples_to_plot'] = 1
    return settings

def generate_fields(variables, scrollable_frame):
    vars_dict = {}
    row = 0
    for key, (var_type, options, default_value) in variables.items():
        vars_dict[key] = create_input_field(scrollable_frame.scrollable_frame, key, row, var_type, options, default_value)
        row += 1
    return vars_dict
    
class TextRedirector(object):
    def __init__(self, widget, queue):
        self.widget = widget
        self.queue = queue

    def write(self, str):
        self.queue.put(str)

    def flush(self):
        pass

def create_dark_mode(root, style, console_output):
    dark_bg = '#333333'
    light_text = 'white'
    dark_text = 'black'
    input_bg = '#555555'  # Slightly lighter background for input fields
    
    # Configure ttkcompartments('TFrame', background=dark_bg)
    style.configure('TLabel', background=dark_bg, foreground=light_text)
    style.configure('TEntry', fieldbackground=input_bg, foreground=dark_text, background=dark_bg)
    style.configure('TButton', background=dark_bg, foreground=dark_text)
    style.map('TButton', background=[('active', dark_bg)], foreground=[('active', dark_text)])
    style.configure('Dark.TCheckbutton', background=dark_bg, foreground=dark_text)
    style.map('Dark.TCheckbutton', background=[('active', dark_bg)], foreground=[('active', dark_text)])
    style.configure('TCombobox', fieldbackground=input_bg, foreground=dark_text, background=dark_bg, selectbackground=input_bg, selectforeground=dark_text)
    style.map('TCombobox', fieldbackground=[('readonly', input_bg)], selectbackground=[('readonly', input_bg)], foreground=[('readonly', dark_text)])
    
    if console_output != None:
        console_output.config(bg=dark_bg, fg=light_text, insertbackground=light_text) #, font=("Arial", 12)
    root.configure(bg=dark_bg)
    
def set_dark_style(style):
    style.configure('TFrame', background='#333333')
    style.configure('TLabel', background='#333333', foreground='white')
    style.configure('TEntry', background='#333333', foreground='white')
    style.configure('TCheckbutton', background='#333333', foreground='white')



@log_function_call   
def main_thread_update_function(root, q, fig_queue, canvas_widget, progress_label):
    try:
        while not q.empty():
            message = q.get_nowait()
            if message.startswith("Progress"):
                progress_label.config(text=message)
            elif message == "" or message == "\r":
                pass
            else:
                print(message)  # Or handle other messages differently
                # For non-progress messages, you can still print them to the console or handle them as needed.

        while not fig_queue.empty():
            fig = fig_queue.get_nowait()
            clear_canvas(canvas_widget)
    except Exception as e:
        print(f"Error updating GUI: {e}")
    finally:
        root.after(100, lambda: main_thread_update_function(root, q, fig_queue, canvas_widget, progress_label))
        
def process_stdout_stderr(q):
    """
    Redirect stdout and stderr to the queue q.
    """
    sys.stdout = WriteToQueue(q)
    sys.stderr = WriteToQueue(q)

class WriteToQueue(io.TextIOBase):
    """
    A custom file-like class that writes any output to a given queue.
    This can be used to redirect stdout and stderr.
    """
    def __init__(self, q):
        self.q = q

    def write(self, msg):
        self.q.put(msg)

    def flush(self):
        pass

def clear_canvas(canvas):
    # Clear each plot (axes) in the figure
    for ax in canvas.figure.get_axes():
        ax.clear()

    # Redraw the now empty canvas without changing its size
    canvas.draw_idle()
    
@log_function_call
def measure_crop_wrapper(settings, q, fig_queue):
    """
    Wraps the measure_crop function to integrate with GUI processes.
    
    Parameters:
    - settings: dict, The settings for the measure_crop function.
    - q: multiprocessing.Queue, Queue for logging messages to the GUI.
    - fig_queue: multiprocessing.Queue, Queue for sending figures to the GUI.
    """
    
    def my_show():
        """
        Replacement for plt.show() that queues figures instead of displaying them.
        """
        fig = plt.gcf()
        fig_queue.put(fig)  # Queue the figure for GUI display
        plt.close(fig)  # Prevent the figure from being shown by plt.show()

    # Temporarily override plt.show
    original_show = plt.show
    plt.show = my_show

    try:
        # Assuming spacr.measure.measure_crop is your function that potentially generates matplotlib figures
        # Pass settings as a named argument, along with any other needed arguments
        spacr.measure.measure_crop(settings=settings, annotation_settings={}, advanced_settings={})
    except Exception as e:
        errorMessage = f"Error during processing: {e}"
        q.put(errorMessage)  # Send the error message to the GUI via the queue
        traceback.print_exc()
    finally:
        plt.show = original_show  # Restore the original plt.show function