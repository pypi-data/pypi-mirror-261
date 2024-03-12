# VizQ

## Description
Tool to create plots based on CPU, GPU and memory usage.

## Installation
```
pip install -U vizq
```

## Usage
You can see the options of this project by doing `python -m vizq --help`

```
usage: __main__.py [-h] [-f FILES] [-m MEMORY] [-o OUTPUT] [-t TITLE] [-x X_LABEL] [-y Y_LABEL] [-of OFFSET] [--x-range X_RANGE X_RANGE] [-omu {kb,mb,gb}] [-xt X_TICK]

optional arguments:
  -h, --help            show this help message and exit
  -f FILES, --file FILES
                        File or files to process. Can specify multiple with: "-f file1.log -f file2.log"
  -m MEMORY, --memory MEMORY
                        Total memory size, expected when values are percentages.
  -o OUTPUT, --output OUTPUT
                        Path of output files.
  -t TITLE, --title TITLE
                        Title to use in the plot
  -x X_LABEL, --xlabel X_LABEL
                        X axis label to use in the plot
  -y Y_LABEL, --ylabel Y_LABEL
                        Y axis label to use in the plot
  -of OFFSET, --offset OFFSET
                        Offset line to draw on the chart
  --x-range X_RANGE X_RANGE
                        Start and end of the x axis range to plot
  -omu {kb,mb,gb}, --output-memory-unit {kb,mb,gb}
                        memory unit to use between [kb, mb, gb], default is mb. Assume unit is KB by default.
  -xt X_TICK, --xtick X_TICK
                        will add a tick on the X axis every n values. Should pass an Integer value

```

## Examples

Plot specifying chart title and axis title.
```
python -m vizq.visualization -f device2/211/cpu_use_20231019-123121.log \
--title "CPU Timeline title" \
--xlabel "new X axis label" \
--ylabel "new Y axis label"
```

Use the offset, X axis range and memory unit example.
--offset draws an horizontal line at the specified value, would be a fixed line at offset value, not a percentage.
--x-range will just save the portion of the plot for the range [x1, x2]
--output-memory-unit could be one of [kb, mb, gb] and will convert the values in the chart to one of those units. 
Default value is kb.
--xtick is drawing a tick on the X axis, so if `--xtick 10` is passed, a mark every 10 values in x will be drawned.
```
python -m vizq.visualization -f device2/211/rss_mem_20231019-123119.log --offset 90 --x-range 50 150 --output-memory-unit mb --xtick 10
```


## Contributing
Instructions on how to contribute to the project

## References
Link to references used in the project (Books, posts, videos, courses, repos, etc.)
