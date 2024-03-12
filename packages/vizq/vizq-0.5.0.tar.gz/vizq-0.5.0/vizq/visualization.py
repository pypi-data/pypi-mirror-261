import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import argparse
import matplotlib.ticker as plticker
from matplotlib.ticker import MultipleLocator


def kb2mb(df):
    df["use"] = df["use"].apply(lambda x: x // 1024)


def mb2gb(df):
    df["use"] = df["use"].apply(lambda x: x // 1024)


def clean_string(x, suffix: str = "kb"):
    if isinstance(x, str):
        x = x.lower()
        if x.endswith(suffix):
            return float(x[:-2])
    return float(x)


def reset_time(df):
    df.reset_index(inplace=True, drop=True)
    t0 = int(df['time'].iloc[0])
    df['time'] = df['time'].apply(lambda x: (int(x) - t0))


def process_log(file_path, output_memory_unit, memory):
    df = pd.read_csv(file_path, sep=" ", usecols=[0, 1], names=['time', 'use'], engine='python', on_bad_lines='skip',
                     header=None)
    df = df[pd.to_numeric(df['time'], errors='coerce').notnull()]
    df = df[pd.to_numeric(df['use'], errors='coerce').notnull()]

    print("resetting df time...")
    reset_time(df)

    # After this values are clean and float
    df["use"] = df["use"].apply(clean_string)

    if output_memory_unit == "kb":
        print("assuming default unit is kb, so won't do a conversion")
    elif output_memory_unit == "mb":
        print("converting kb to mb...")
        kb2mb(df)
    elif output_memory_unit == "gb":
        print("converting kb to gb...")
        kb2mb(df)
        mb2gb(df)

    if memory is not None:
        df['use'] = df['use'].apply(lambda x: x * memory / 100)

    return df


parser = argparse.ArgumentParser()
# Graficar por archivo
parser.add_argument('-f', '--file', dest='files', action='append', type=str,
                    help='File or files to process. Can specify multiple with: "-f file1.log -f file2.log"',
                    required=False, default=None)
parser.add_argument('-m', '--memory', dest='memory', type=int,
                    help='Total memory size, expected when values are percentages.', required=False, default=None)
parser.add_argument('-o', '--output', dest='output', type=str, help='Path of output files.', required=False,
                    default=None)

parser.add_argument('-t', '--title', dest='title', type=str,
                    help='Title to use in the plot', required=False,
                    default="")
parser.add_argument('-x', '--xlabel', dest='x_label', type=str,
                    help='X axis label to use in the plot', required=False,
                    default="")

parser.add_argument('-y', '--ylabel', dest='y_label', type=str,
                    help='Y axis label to use in the plot', required=False,
                    default="")

parser.add_argument('-of', '--offset', dest='offset', type=int,
                    help='Offset line to draw on the chart', required=False,
                    default=100)

parser.add_argument('--x-range', dest="x_range", type=int, nargs=2, required=False,
                    help='Start and end of the x axis range to plot')

parser.add_argument('-omu', '--output-memory-unit', dest='output_memory_unit', choices=['kb', 'mb', 'gb'],
                    help='memory unit to use between [kb, mb, gb], default is mb. Assume unit is KB by default.',
                    required=False, default="kb")

parser.add_argument('-xt', '--xtick', dest='x_tick', type=int,
                    help='will add a tick on the X axis every n values. Should pass an Integer value',
                    required=False, default=100)

args = parser.parse_args()
plot_title = args.title
x_label = args.x_label
y_label = args.y_label

# offset used to draw horizontal line
offset = args.offset

# X range to plot, this should be a sub range of the total X axis
x_range = args.x_range

# memory unit to use, this defines which function to call and do the casting
output_memory_unit = args.output_memory_unit

# total memory size
memory = args.memory

# value used to add a tick every n number of values
x_tick = args.x_tick

print(f"received args: {args}")

##############################
# Some hardcoded design params
# time interval between marks in the x axis
secs_per_tick = 120
# size of generated graph.
# number means "5 inches for every 200 seconds"
figure_width = 5 / 200
# Alternative to scale both dimentions
# number means 1 inch for every 200 seconds
figure_size = 1 / 200
##############################
# vertical line interval
v_line_int = 120
# number of horizontal lines
h_lines = 10
###############################
# Colors list. Iterates through them in order
colors_1 = ['b', 'r', 'k', 'y', 'g', 'c', 'm']
colors_2 = ['#377eb8', '#ff7f00', '#f781bf', '#999999', '#e41a1c', '#dede00', '#4daf4a', '#a65628', '#984ea3']
##############################


#####################
# If 'file'
#####################

if args.files is not None:
    print(f"files argunment received: {args.files}")
    print("---------------------------- Start colorblind timeline ----------------------------")
    ############
    # Colorblind Timeline
    ############
    print(f"starting colorblind plot...")
    stats = dict()
    f_names = []
    # Adjusting the figure size
    fig, ax = plt.subplots(figsize=(16, 5))
    # M will be the max value on the graph. We use it for framing purposes
    M = 0
    # tf is the farthest point in time. Used for figure size
    tf = 0
    for f, c in zip(args.files, colors_2):
        print(f"doing plot for file:{f} and color:{c}")
        # Name and path of file to read
        f_name = os.path.basename(f)
        f_path = f.removesuffix(f_name)
        f_name = os.path.splitext(f_name)[0]
        f_names.append(f_name)

        print(f"starting to process log: {f}...")
        df = process_log(f, output_memory_unit=output_memory_unit, memory=memory)
        csv_file_name = os.path.join(f_path, f_name + '.csv')
        print(f"saving csv file: {csv_file_name}")
        df.to_csv(csv_file_name, header=False, index=False)
        M = max(M, max(df['use']))
        print(f"max value on the graph: {M}")
        tf = max(tf, max(df['time']))
        print(f"farthest point in time: {tf}")

        ax.plot(df['time'], df['use'], c, label=f_name, linestyle=':', marker='.')

        stats.update({f: {'average': int(df['use'].mean()), 'max_value': int(max(df['use']))}})

    plt.title(plot_title, fontsize=35)
    ax.set_xlabel(x_label, fontdict={"fontsize": 22})
    ax.set_ylabel(y_label, fontdict={"fontsize": 22})

    # We resize image proportionally to the time lenght. 'tf' is total time, 'figure_width' is how long we make it
    # fig.set_figwidth(tf * figure_width)
    #######
    # there is a max size of image = 65536
    ####
    x_size = min(655, (16 * tf * figure_size))
    y_size = min(655, (5 * tf * figure_size))
    fig.set_size_inches(x_size, y_size)

    # Places a mark 'every secs_per_tick' seconds
    loc = plticker.MultipleLocator(base=secs_per_tick)
    ax.xaxis.set_major_locator(loc)
    plt.xticks(np.array([i for i in range(0, int(1.01 * tf), x_tick)]))
    plt.xlim([0, 1.01 * tf])
    plt.ylim([-0.1 * M, 1.1 * M])

    # Aux lines
    # Horizontal
    ax.legend(title='Resources usage')

    if f_name.startswith('cpu'):
        plt.hlines(y=range(0, round(1.1 * M), 50), xmin=0, xmax=1.01 * tf, color='gray', linestyle='dotted')
        plt.axhline(y=offset, color='gray', linestyle='dotted')
    else:
        plt.hlines(y=range(0, round(1.1 * M), round(((1.1 * M) / h_lines))), xmin=0, xmax=1.01 * tf, color='gray',
                   linestyle='dotted')
        plt.axhline(y=offset, color='gray', linestyle='dotted')

    # Vertical
    plt.vlines(x=range(0, tf, v_line_int), ymin=-0.1 * M, ymax=1.1 * M, color='gray', linestyle='dotted')

    if args.output is not None:
        file_path = os.path.join(args.output, 'graphs')
    else:
        file_path = 'graphs'
    file_name = 'colorblind_timeline-' + '-'.join(f_names)
    if not os.path.exists(file_path):
        print(f"creating directory:{file_path}")
        os.makedirs(file_path)

    if x_range:  # plot sub range of the X axis
        plt.xlim(x_range[0], x_range[1])

    save_config_path = os.path.join(file_path, file_name)
    print(f"saving config path to: {save_config_path}")
    fig.savefig(save_config_path, bbox_inches="tight")
    plt.close()
    print("---------------------------- Finish colorblind timeline ----------------------------")

    ############
    # RBK Timeline
    ############
    print("---------------------------- Start RBK timeline ----------------------------")
    stats = dict()
    f_names = []
    # Adjusting the figure size
    fig, ax = plt.subplots(figsize=(16, 5))
    # M will be the max value on the graph. We use it for framing purposes
    M = 0
    # tf is the farthest point in time. Used for figure size
    tf = 0
    for f, c in zip(args.files, colors_1):
        print(f"doing plot for file:{f} and color:{c}")
        # Name and path of file to read
        f_name = os.path.basename(f)
        f_path = f.removesuffix(f_name)
        f_name = os.path.splitext(f_name)[0]
        f_names.append(f_name)

        print(f"starting to process log: {f}...")
        df = process_log(f, output_memory_unit=output_memory_unit, memory=memory)
        csv_file_name = os.path.join(f_path, f_name + '.csv')
        print(f"saving csv file: {csv_file_name}")
        df.to_csv(csv_file_name, header=False, index=False)
        M = max(M, max(df['use']))
        print(f"max value on the graph: {M}")
        tf = max(tf, max(df['time']))
        print(f"farthest point in time: {tf}")

        ax.plot(df['time'], df['use'], c, label=f_name, linestyle=':', marker='.')

        stats.update({f: {'average': int(df['use'].mean()), 'max_value': int(max(df['use']))}})
        print(f"new stat collected: {stats}")

    plt.title(plot_title, fontsize=35)
    ax.set_xlabel(x_label, fontdict={"fontsize": 22})
    ax.set_ylabel(y_label, fontdict={"fontsize": 22})

    # We resize image proportionally to the time lenght. 'tf' is total time, 'figure_width' is how long we make it
    # fig.set_figwidth(tf * figure_width)
    #######
    # there is a max size of image = 65536
    ####
    x_size = min(655, (16 * tf * figure_size))
    y_size = min(655, (5 * tf * figure_size))
    fig.set_size_inches(x_size, y_size)

    # Places a mark 'every secs_per_tick' seconds
    loc = plticker.MultipleLocator(base=secs_per_tick)
    ax.xaxis.set_major_locator(loc)
    plt.xticks(rotation=30, fontsize=15)
    plt.xticks(np.array([i for i in range(0, int(1.01 * tf), x_tick)]))
    plt.xlim([0, 1.01 * tf])
    plt.ylim([-0.1 * M, 1.1 * M])

    # Aux lines
    # Horizontal
    ax.legend(title='Resources usage')

    if f_name.startswith('cpu'):
        plt.hlines(y=range(0, round(1.1 * M), 50), xmin=0, xmax=1.01 * tf, color='gray', linestyle='dotted')
        plt.axhline(y=offset, color='gray', linestyle='dotted')
    else:
        plt.hlines(y=range(0, round(1.1 * M), round(((1.1 * M) / h_lines))), xmin=0, xmax=1.01 * tf, color='gray',
                   linestyle='dotted')
        plt.axhline(y=offset, color='gray', linestyle='dotted')
    # Vertical
    plt.vlines(x=range(0, tf, v_line_int), ymin=-0.1 * M, ymax=1.1 * M, color='gray', linestyle='dotted')

    if args.output is not None:
        file_path = os.path.join(args.output, 'graphs')
    else:
        file_path = 'graphs'
    file_name = 'rbk_timeline-' + '-'.join(f_names)
    if not os.path.exists(file_path):
        print(f"creating directory:{file_path}")
        os.makedirs(file_path)

    if x_range:  # plot sub range of the X axis
        plt.xlim(x_range[0], x_range[1])

    fig.savefig(os.path.join(file_path, file_name), bbox_inches="tight")
    plt.close()
    print("---------------------------- Finish RBK timeline ----------------------------")

    ###########
    # Bar Graph
    ###########

    print("---------------------------- Bar graph ----------------------------")
    avg = []
    max_val = []
    for file in stats:
        avg.append(stats[file]['average'])
        max_val.append(stats[file]['max_value'])

    X_axis = np.arange(len(stats.keys()))

    p = plt.bar(X_axis - 0.2, avg, 0.4, label='Average')  # , color='green')

    plt.bar_label(p, label_type='edge')

    p = plt.bar(X_axis + 0.2, max_val, 0.4, label='Max Value')  # , color='red')

    plt.bar_label(p, label_type='edge')

    plt.xticks(X_axis, f_names)
    plt.xlabel('Experiment')
    plt.ylabel('Usage')
    plt.title('Usage statistics')
    plt.legend()

    if args.output is not None:
        file_path = os.path.join(args.output, 'graphs')
    else:
        file_path = 'graphs'
    file_name = 'bars-' + '-'.join(f_names)
    if not os.path.exists(file_path):
        print(f"creating directory:{file_path}")
        os.makedirs(file_path)
    plt.savefig(os.path.join(file_path, file_name), bbox_inches="tight")
    plt.close()
    print("---------------------------- Finish Bar graph ----------------------------")

else:
    print("No input files given. Skipping individual file processing...")

print(f"All files are created under: \x1b[6;30;42m graphs/ \x1b[0m directory")

#####################
# If 'path'
#####################
"""
if args.path is not None:
    print("------------------------------args.path given------------------------------------------")
    fields = ['gpu', 'cpu', 'rss']
    experiments = [x for x in os.walk(args.path)][0][1]
    if 'graphs' in experiments: experiments.remove('graphs')
    files = dict()
    for exp in experiments:
        # This condition is so complex because it is customized to a specific folder structure. Change it as needed
        files[exp] = [x for x in [x[2] for x in os.walk(os.path.join(args.path, exp))][0] if
                      x.startswith(tuple(fields)) and any(char.isdigit() for char in x) and x.endswith('log')]

    stats = dict()

    ##########
    # Timeline
    ##########

    for field in fields:

        stats[field] = dict()

        # Adjusting the figure size
        fig, ax = plt.subplots(figsize=(16, 5))
        # M will be the max value on the graph. We use it for framing purposes
        M = 0
        # tf is the farthest point in time. Used for figure size
        tf = 0
        for key in files:
            file = os.path.join(args.path, key, [x for x in files[key] if x.startswith(field)][0])
            df = process_log(file, args)
            df.to_csv(file[:-4] + '.csv', header=False, index=False)
            M = max(M, max(df['use']))
            tf = max(tf, max(df['time']))

            ax.plot(df['time'], df['use'], label=key, linestyle=':', marker='.')

            stats[field].update({key: {'average': int(df['use'].mean()),
                                       'max_value': int(max(df['use']))}})
            # Save .csv
            f_name = os.path.splitext(file)[0]

        plt.title(field.upper(), fontsize=20)

        plt.xlabel('Time - seconds', fontsize=15)
        if field == 'cpu':
            plt.ylabel(field.upper() + ' usage %', fontsize=15)
        else:
            plt.ylabel(field.upper() + ' usage MB', fontsize=15)

        # We resize image proportionally to the time lenght. 'tf' is total time, 'figure_width' is how long we make it
        fig.set_figwidth(tf * figure_width)
        # Places a mark 'every secs_per_tick' seconds
        loc = plticker.MultipleLocator(base=secs_per_tick)
        ax.xaxis.set_major_locator(loc)
        plt.xticks(rotation=30, fontsize=15)
        plt.ylim([0, 1.1 * M])
        plt.xlim([-10, 1.01 * tf])

        ax.legend(title=field.upper() + ' usage')
        if field == 'cpu':
            plt.axhline(y=50, color='gray', linestyle='dotted')
            plt.axhline(y=100, color='gray', linestyle='dotted')
            plt.axhline(y=150, color='gray', linestyle='dotted')

        file_name = field.upper() + '_comparison_' + '_'.join(experiments)
        file_path = os.path.join(args.path, 'graphs')
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        fig.savefig(os.path.join(file_path, file_name), bbox_inches="tight")
        plt.close()

    ############
    # Bar Graphs
    ############

    for field in stats:
        avg = []
        max_val = []

        for experiment in stats[field]:
            avg.append(stats[field][experiment]['average'])
            max_val.append(stats[field][experiment]['max_value'])

        X_axis = np.arange(len(stats.keys()))

        p = plt.bar(X_axis - 0.2, avg, 0.4, label='Average')  # , color='green')

        plt.bar_label(p, label_type='edge')

        p = plt.bar(X_axis + 0.2, max_val, 0.4, label='Max Value')  # , color='red')

        plt.bar_label(p, label_type='edge')

        plt.xticks(X_axis, stats[field].keys())
        plt.xlabel('Experiment')
        plt.ylabel(field.upper() + ' usage')
        plt.title(field.upper() + ' usage per experiment')
        plt.legend()

        file_name = field.upper() + '_stats_' + '_'.join(experiments)
        file_path = os.path.join(args.path, 'graphs')
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        plt.savefig(os.path.join(file_path, file_name), bbox_inches="tight")
        plt.close()

else:
    print("No input path given. skipping folder processing...")
"""
